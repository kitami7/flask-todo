from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def list():
    return render_template("list.html")
@app.route("/edit")
def edit():
    return render_template("edit.html")
    
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
