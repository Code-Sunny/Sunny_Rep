from typing import Any
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint
 
cid = ''
secret = ''
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
 
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# 여기까지는 기본 설정~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# spotify안에 있는 카테고리들 출력해보기
info_cate = sp.categories(country=None, locale=None, limit=20, offset=0)
# pprint.pprint(info_cate)

# # 그중에 쩰루 인기있는 카테고리로 픽!
top_id = info_cate['categories']['items'][0]['id']


# 카테 안의 플레이리스트의 아이디들을 추출
# cate_info = sp.category( top_id , country=None , locale=None )
cate_list = sp.category_playlists( 
category_id= top_id, country=None , limit=5 , offset=0 )
# pprint.pprint(cate_list)

# # 플레이리스트 id들을 담을 리스트 생성!
ids = []

# 플레이리스트 id들을 꺼내기 위한 준비, 리스트에 담긴 상태로 놓고
dirty_ids = cate_list['playlists']['items']

# 인덱스 하나씩 열어서 플레이리스트 아이디를 ids 리스트에 담기
for i in dirty_ids:
    single_id = i['id'] 
    ids.append(single_id)

# 플레이리스트id를 통해 가수 id 추출하기
# 추출한 id는 final 리스트에 담기
final = []
for i in ids:
    tracks = sp.playlist_items(i, fields=None , limit=1 , offset=0 , market=None , additional_types=('track' , 'episode'))
    k = tracks['items'][0]['track']['artists'][0]['id']
    final.append(k)

# 추출한 가수 id를 통해서 가수, 가수의 노래들, 노래이미지, 노래 미리듣기 추출
for i in final:
    name = sp.artist(i)
    real_name = name['name']
    real_id = name['id']
    sings = sp.artist_albums(real_id, album_type=None, country=None, limit=1, offset=0)
    sing_name = sings['items'][0]['name']
    sing_pic = sings['items'][0]['images'][0]['url']
    sing_id = sings['items'][0]['id']
    
    print(real_name)
    print(real_id)
    print(sing_name)
    print(sing_pic)

    track = sp.album_tracks(sing_id, limit=1, offset=0, market=None)
    sing_pre = track['items'][0]['preview_url']
    print(sing_pre)

    print('~'*100)
    


