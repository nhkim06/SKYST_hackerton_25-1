from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/snowwhite')
def snowwhite():
    return render_template('introductionSW.html')

@app.route('/cinderella')
def cinderella():
    return render_template('introductionCinderella.html')

@app.route('/slepingbeauty')
def slepingbeauty():
    return render_template('introductionSB.html')

#これより下に@app.routeしちゃうと動かなくなっちゃう
if __name__ == "__main__":
    app.run(debug=True)
