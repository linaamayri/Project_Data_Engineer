from flask import Flask, render_template, redirect, request, url_for, redirect
from textblob import TextBlob
from flask import Flask
from textblob import TextBlob


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("test.html")

@app.route("/text", methods=["POST","GET"])
def text():
    if request.method == "POST":
        text = request.form["nm"]
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity
        if sentiment < 0:
            x=-(blob.sentiment.polarity)*100
            return "Your text is Negative with a negativity of : " + str(x) + " % "
        elif sentiment > 0:
            x=(blob.sentiment.polarity)*100
            return "Your text is Positive with a positivity of : " + str(x) + " % "
        else:
            return("Neutral")

    else:
        return render_template("text.html")

#@app.route("/result")
#def result(yourtext):
    #return {yourtext}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)


    