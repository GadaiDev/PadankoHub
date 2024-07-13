from flask import Flask, send_file, request
from flask_cors import CORS

from Feature import HiraRnd
from Feature import Example
from Feature import BBS

import KIT

app = Flask(__name__)
app.secret_key = "Zmc4uLKRh_gmwRW2vC1Eo0OuBYEDbPAGhb7NXwbpcslT_Cyreia64aklxahvOsP0C3zMMsaCdFCR-fzXv4pxsvBcoQSPzBZ9b7cJn80v9zwUWmO_jHBOLpEA6uZrQ3ZNllvIJA"
CORS(app)

@app.route("/")
def page_index():
    return KIT.html_read("index")

@app.route("/File/<path:path>")
def ev_file(path):
    return send_file(f"./File/{path}")

@app.errorhandler(404)
def ev_err_404(err):
    return KIT.html_read("error").replace("{{ error }}", str(err).split(":")[0]), 404

@app.errorhandler(500)
def ev_err_500(err):
    return KIT.html_read("error").replace("{{ error }}", str(err).split(":")[0]), 500

HiraRnd.Register(app)
Example.Register(app)
BBS.Register(app)

app.run("::", 80, debug=False)