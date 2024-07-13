from flask import Flask, request, session

from json import load, dump
from random import Random
from datetime import datetime
from string import ascii_letters, digits

from threading import Thread

import KIT

import queue
import time
import re


def post_replace(text: str, name: str):
    text = text.replace(">","&gt;")
    text = text.replace("<","&lt;")
    text = text.replace("\n","\n<br>")
    text = re.sub(r"!Img:\"(.+)\"", r"<img src='\1' class='th_bbs_img'>", text)

    name = name.replace(">","&gt;")
    name = name.replace("<","&lt;")

    return text, name

def Register(app: Flask):
    Queue = queue.Queue()
    
    @app.route("/bbs/")
    def page_BBS_index():
        return KIT.html_read("BBS/index")
    
    @app.route("/bbs/post", methods=["POST"])
    def ev_BBS_post():
        text = request.form.get("text")
        name = request.form.get("name")
        
        text, name = post_replace(text, name)
        
        
        date = f"{datetime.now().year}/{datetime.now().month}/{datetime.now().day} {datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}"
        
        rnds = Random(request.remote_addr + " " + f"{datetime.now().year}/{datetime.now().month}/{datetime.now().day}")
        
        Queue.put(
            item={
                "name": name,
                "text": text,
                "ID": "".join(rnds.choices(ascii_letters + digits, k=8)),
                "date": date
            }
        )        
        
        return "1"
    
    def Queue_Posting():
        while True:
            if not Queue.empty():
                thr = load(open("./File/BBS/thread.json", "r"))
                thr.append(Queue.get())
                dump(thr, open("./File/BBS/thread.json", "w"), indent=4, ensure_ascii=False)
            else:
                time.sleep(0.01)
    
    post_daemon_ = Thread(target=Queue_Posting)
    post_daemon_.setDaemon(True)
    post_daemon_.start()
    