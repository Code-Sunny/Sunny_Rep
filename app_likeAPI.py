from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbplaylist

''' 좋아요 API (GET) 서버 '''

@app.route('/api/show-like', methods=['GET'])
def song_showLike():
    
    # 클라이언트에게 받은 곡 이름 저장
    title_receive = request.args['title_give']

    # 클라이언트에게 받은 곡 가수 저장
    artist_receive = request.args['artist_give']
    
    # 클라이언트에게 받은 곡 정보를 조회하여 그 곡의 데이터 저장
    song = db.songs.find_one({"title" : title_receive, 'artist' : artist_receive}, {'_id' : False})

    # 클라이언트 측으로 그 곡의 데이터를 보내주기
    return jsonify ({'target_song' : song}) 


''' 좋아요 API (POST) 서버''' 

@app.route('/api/like-btn', methods=['POST'])
def like_btn():
    
    ''' 좋아요 +1 기능 '''
    # 사용자가 버튼을 누른 곡 이름 : title_receive
    title_receive = request.form['title_give']
    
    # 사용자가 버튼을 누른 곡 가수 : artist_receive
    artist_receive = request.form['artist_give']
    
    # 사용자가 어떤 버튼을 눌렀는지 정보 : weather_receive
    weatherBtn_receive = request.form['weatherBtn_give']
      
    # 사용자가 누른 곡의 정보 조회해서 song, artist에 저장
    # 이때, 곡 이름 변수 저장 시 곡 이름이 같고 아티스트가 다른 데이터 있을 수 있으므로 이름과 아티스트 둘 다 체크
    # 이때, 곡 가수 변수 저장 시 아티스트가 같고 곡 이름이 다른 데이터 있을 수 있으므로 이름과 아티스트 둘 다 체크
    song = db.songs.find_one({'title':title_receive, 'artist' : artist_receive})
    artist = db.songs.find_one({'artist':artist_receive, 'title' : title_receive})
    
    # db에 없다면 추가할 default 데이터
    doc = {'title' : title_receive, 'artist' : artist_receive, 'Sunny' : 0, 'Cloudy' : 0, 'Rainy' : 0, 'Snowy' : 0}

    # if) 사용자가 누른 곡 이름이 db에 없다면, db에 default 값으로 추가 후
    # 사용자가 누른 버튼에 맞게 좋아요 수 +1
    if song == None:        
        db.songs.insert_one(doc)
        song = db.songs.find_one({'title':title_receive, 'artist' : artist_receive})
        new_like = song[weatherBtn_receive] +1 
        db.songs.update_one({'title' : title_receive, 'artist' : artist_receive}, {'$set' : {weatherBtn_receive : new_like}})

    # else) 이미 db에 곡 정보가 있다면 가수가 있는지, 없는지 판단
    else:
        # 가수가 없다면 곡 이름만 같은 다른 곡이므로 db에 default 값으로 추가 후
        # 사용자가 누른 버튼에 맞게 좋아요 수 +1
        if artist == None:
            db.songs.insert_one(doc)
            song = db.songs.find_one({'title':title_receive, 'artist' : artist_receive})
            new_like = song[weatherBtn_receive] +1 
            db.songs.update_one({'title' : title_receive, 'artist' : artist_receive}, {'$set' : {weatherBtn_receive : new_like}})
        
        # 가수가 있다면 같은 곡이므로 데이터 추가할 필요 없이 좋야요 수만 +1
        else:    
            new_like = song[weatherBtn_receive] +1 
            db.songs.update_one({'title' : title_receive, 'artist' : artist_receive}, {'$set' : {weatherBtn_receive : new_like}})
            
    
    ''' 좋아요 눌렀을 때 로그인 여부 판단 '''       
          
    # 사용자의 닉네임 정보 : username_receive
    username_receive = request.form['username_give']      
            
    # 사용자의 닉네임 정보를 찾아서 변수에 저장
    username = db.users.find_one({'username' : username_receive})
    print(username)
    
    if username == None:
        return jsonify({'msg' : "로그인을 해주세요!", 'redirect_url' : "/login"})
        
    return jsonify({'msg' : "날씨 버튼 좋아요 +1 완료!"})

''' 로그인 페이지 이동 API '''

@app.route("/login")
def login_home():
    return render_template("login.html")


''' 서버 구동 API '''

@app.route('/')
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)