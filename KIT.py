from flask import Response, request
from hashlib import md5

def f_open(fname: str):
    return open(fname, "r").read()

def html_read(fname: str):
    return f_open("./HTML/"+fname+".html")

def XSS_Replace(text: str):
    return text.replace(">","&gt;").replace("<","&lt;")

def Injection_Replace(text: str):
    return text.replace("/","").replace(".","")

def Password_Check():
    try:
        return md5(request.cookies.get("Password").encode()).hexdigest() == f_open("./Admin/password_md5.txt") # クッキーにあるパスワードをハッシュ化、ハッシュ化済みのパスワードと照合
    except:
        return False
