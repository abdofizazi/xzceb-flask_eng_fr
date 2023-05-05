from machinetranslation import translator
from flask import Flask, render_template, request
import json
from  machinetranslation.translator import english_to_french,french_to_english
app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('text')
    text_french=english_to_french(textToTranslate)
    return text_french

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('text')
    text_english = french_to_english(textToTranslate)
    return text_english

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
