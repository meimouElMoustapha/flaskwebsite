from flask import Flask ,render_template



app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    juice=['mango','banaa','watermillon']
    return render_template ('about.html',juice=juice)


@app.route("/test")
def test():
    return render_template('test.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),400


@app.errorhandler(404)
def page_not_found1(e):
    return render_template('500.html'),500





if __name__ == "__main__":
    app.run(debug=True)