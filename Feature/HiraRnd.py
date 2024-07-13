from flask import Flask, request
import KIT

from random import Random

txt = list("あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん")
for i in range(ord("𛀂"),ord("𛄜")+1):
    txt.append(chr(i))
def Register(app: Flask):
    @app.route("/HiraganaRandom/")
    def page_HiraRnd_1():
        return KIT.html_read("HiraganaRandom/index").replace("{{ r }}", "")

    @app.route("/HiraganaRandom/Result")
    def post_HiraRnd_ev1(): #PostEvent
        page = request.args.get("ttl","")
        return KIT.html_read("HiraganaRandom/index").replace("{{ r }}","".join(Random(page).choices(txt, k=8192))) 
        
