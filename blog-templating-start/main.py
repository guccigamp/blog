from flask import Flask, render_template
import requests

app = Flask(__name__)

all_posts = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391").json()

@app.route('/')
def home():
    return render_template("index.html", all_posts = all_posts)

@app.route("/post/<int:sn>")
def post(sn):
    return render_template("post.html", blog_post = all_posts[sn-1])

if __name__ == "__main__":
    app.run(debug=True)
