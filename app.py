from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbplaylist

''' 좋아요 API (POST) 서버''' 

@app.route('/api/likeBtn', methods=['POST'])
def like_song():
    # 사용자가 버튼을 누른 곡 이름 : title_receive
    title_receive = request.form['title_give']
    
    # 사용자가 어떤 버튼을 눌렀는지 정보 : weather_receive
    weatherBtn_receive = request.form['weatherBtn_give']
      
    # 사용자가 누른 곡의 정보 조회해서 song에 저장
    song = db.songs.find_one({'title':title_receive})
    
    # if) 사용자가 누른 곡 이름이 db에 없다면, db에 default 값으로 추가 후
    # 사용자가 누른 버튼에 맞게 수 +1
    if (song == None):
        doc = {'title' : title_receive, 'Sunny' : 0, 'Cloudy' : 0, 'Rainy' : 0, 'Snowy' : 0}
        db.songs.insert_one(doc)
        song = db.songs.find_one({'title':title_receive})
        new_like = song[weatherBtn_receive] +1 
        db.songs.update_one({'title' : title_receive}, {'$set' : {weatherBtn_receive : new_like}})
        
    # else) 이미 db에 곡 정보가 있다면 추가할 필요 없이 누른 버튼에 맞게 수 +1
    else:
        new_like = song[weatherBtn_receive] +1 
        db.songs.update_one({'title' : title_receive}, {'$set' : {weatherBtn_receive : new_like}})
    
    return jsonify({'msg' : "날씨 버튼 좋아요 +1 완료!"})


''' 좋아요 API (GET) 서버 '''

@app.route('/api/showLike', methods=['GET'])
def song_showLike():
    # 클라이언트에게 받은 곡 정보 저장

    title_receive = request.args['title_give']
    
    # 클라이언트에게 받은 곡 정보를 조회하여 그 곡의 데이터 저장
    song = db.songs.find_one({"title" : title_receive}, {'_id' : False})

    # 클라이언트 측으로 그 곡의 데이터를 보내주기
    return jsonify ({'target_song' : song}) 



''' 서버 구동 API '''

@app.route('/')
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)