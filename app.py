from flask import Flask, render_template, request, jsonify
app = Flask(__name__)



@app.route('/api/likeBtn', methods=['POST'])
def like_song():
    title_receive = request.form['title_give']
    weatherBtn_receive = request.form['weatherBtn_give']
    print(title_receive, weatherBtn_receive)
    return jsonify({'msg' : title_receive + weatherBtn_receive})




@app.route('/')
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)