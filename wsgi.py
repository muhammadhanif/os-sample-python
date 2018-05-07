from flask import Flask, render_template
application = Flask(__name__)

@application.route("/")
def hello():
    name = "nolsatu.id"
    link = "https://www.nolsatu.id/"
    return render_template("index.html", name=name, link=link)

if __name__ == "__main__":
    application.run()
