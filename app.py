import redis
from flask import Flask, render_template, request

r = redis.Redis(host = '127.0.0.1')
app = Flask(__name__,static_url_path = '/static')

@app.route("/post", methods =['POST'])
def write():
    title = request.form['title'].replace(" ","")
    text = request.form['text']
    r.set(title,text)
    return render_template("posted.html", title=title, text=text)

@app.route("/post", methods =['GET'])
def read():    
    return ("Algo hiciste mal")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/postlist")
def getAll():
    allKeys = r.keys("*")
    posts = dict()
    for key in allKeys:
        decodedkey = key.decode("utf-8")
        post = r.get(key).decode("utf-8")
        posts[decodedkey] = post
    
    return render_template("posts.html", posts= posts)
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)





