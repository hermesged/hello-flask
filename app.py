from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/hello', methods=["POST"])
def hello_post():
    name = request.form.get('name', '').strip()
    if name:
        return render_template("hello.html", name=name)
    return render_template('about.html')
    
@app.route('/hello/<string:name>')
def hello_get(name):
    name = name.strip()
    if name:
        return render_template("hello.html", name=name)
    return render_template('about.html')


if __name__== "__main__":
    app.run(debug=True)