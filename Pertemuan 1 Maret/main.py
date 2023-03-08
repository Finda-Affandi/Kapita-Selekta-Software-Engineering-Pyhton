from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index() :
    param = "1"
    return render_template("index.html", param=param)

@app.route("/login", methods=['GET', 'POST'])
def login() :
    error = None
    if request.method == "POST":
        if request.form["username"] != 'admin' or request.form["password"] != 'admin':
            error = "Invalid Credentials, please try again!"
        else:
            return redirect(url_for('index'))
    return render_template("login.html", error=error)


if __name__ == "__main__" :
    app.run(host = "127.0.0.1", port = 5000, debug=True)