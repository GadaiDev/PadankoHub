from flask import Flask, request
import KIT

from random import Random

def Register(app: Flask):
    @app.route("/Example/")
    def page_Example_1():
        return KIT.html_read("Example/index").replace("{{ r }}", "")

    @app.route("/Example/post", methods=["POST"])
    def post_Example_ev(): #PostEvent
        return request.form.get("text","")
        
