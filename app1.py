from cmath import pi
from typing import Any
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client.test

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

cid = "e1e48c01f23740de885eff5fefba4db5"
secret = ""
client_credentials_manager = SpotifyClientCredentials(
    client_id=cid, client_secret=secret
)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# 여기까지는 기본 설정~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
3

info_cate = sp.categories(country=None, locale=None, limit=5, offset=0)
# pprint.pprint(info_cate)

# # 그중에 쩰루 인기있는 카테고리로 픽!
top_id = info_cate["categories"]["items"][0]["id"]


# 카테 안의 플레이리스트의 아이디들을 추출
# cate_info = sp.category( top_id , country=None , locale=None )
cate_list = sp.category_playlists(category_id=top_id, country=None, limit=20, offset=0)
# pprint.pprint(cate_list)

# # 플레이리스트 id들을 담을 리스트 생성! 플레이리스트 아이디 4개
ids = []

# 플레이리스트 id들을 꺼내기 위한 준비, 리스트에 담긴 상태로 놓고
dirty_ids = cate_list["playlists"]["items"]

# 인덱스 하나씩 열어서 플레이리스트 아이디를 ids 리스트에 담기
for i in dirty_ids:
    single_id = i["id"]
    ids.append(single_id)

# 플레이리스트id를 통해 가수 id 추출하기
# 추출한 id는 final 리스트에 담기

final = []
for i in ids:
    tracks = sp.playlist_items(
        i,
        fields=None,
        limit=4,
        offset=0,
        market=None,
        additional_types=("track", "episode"),
    )
    # print(tracks['items'][0]['track']['artists'][0]['id'])
    # print(tracks['items'][1]['track']['artists'][0]['id'])
    final.append(tracks["items"][0]["track"]["artists"][0]["id"])
    final.append(tracks["items"][1]["track"]["artists"][0]["id"])
    final.append(tracks["items"][2]["track"]["artists"][0]["id"])
    final.append(tracks["items"][3]["track"]["artists"][0]["id"])
    # print(tracks)
    # k = tracks['items'][0]['track']['artists'][0]['id']
    # final.append(k)
    # print(k)
    # print('@'*100)


# 추출한 가수 id를 통해서 가수, 가수의 노래들, 노래이미지, 노래 미리듣기 추출
# 클라에 값을 내려줄 리스트 생성
contents_list = []

for i in final:
    name = sp.artist(i)
    real_name = name["name"]
    real_id = name["id"]
    sings = sp.artist_albums(real_id, album_type=None, country=None, limit=2, offset=0)
    sing_name = sings["items"][0]["name"]
    sing_pic = sings["items"][0]["images"][0]["url"]
    sing_id = sings["items"][0]["id"]

    track = sp.album_tracks(sing_id, limit=1, offset=0, market=None)
    sing_pre = track["items"][0]["preview_url"]

    # print(real_name)
    # print(real_id)
    # print(sing_name)
    # print(sing_pic)
    # print(sing_pre)

    j = [real_name, sing_name, sing_pic, sing_pre]
    contents_list.append(j)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@app.route("/")
def home():
    return render_template("index.html")


# @app.route('/review', methods=['POST'])
# def write_orders():
#     # 클라로부터 데이터를 받을 수 있게 요청폼을 만듭니다.
#     name_receive = request.form['name_give']
#     quantity_receive = request.form['quantity_give']
#     adress_receive = request.form['adress_give']
#     phoneNumber_receive = request.form['phoneNumber_give']

#     # 딕셔너리를 만들고 DB에 생성한 딕을 넣어주는 방식입니다!
#     doc = {
#         'name': name_receive,
#         'quantity': quantity_receive,
#         'adress': adress_receive,
#         'phoneNumber': phoneNumber_receive
#     }
#     # Collections의 bookreview를 만들어 넣어줍니다.
#     db.orders.insert_one(doc)

#     # 성공시 클라에게 '저장
#     # 완료!'라는 메세지를 내려 줍니다.
#     return jsonify({'msg': '저장 완료'})


@app.route("/show", methods=["GET"])
def show_contents():
    contents = contents_list
    # orders = list(db.orders.find({}, {'_id': False}))
    return jsonify({"all_contents": contents})


# 다른데서 부르면 실행하지 마라는 뜻이다.
if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
