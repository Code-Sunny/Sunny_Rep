from pymongo import MongoClient

# from datetime import datetime

client = MongoClient("localhost", 27017)
db = client.sunny

# Schema, MongoDB가 저장되는 document의 형태를 인지하도록 미리 설정해주는
# 설명문과 같다. 새로운 데이터가 저장될 때 이 구조에 맞는 지 확인하여 맞을 때만 받아들인다.
# 설정을 하면 좋겠지만, 현재 프로젝트에 꼭 필요할지는 의문
# UserSchema = {
#     "$jsonSchema": {
#         "title": "User_schema",
#         "description": "User information",
#         "requried": ["username", "password", "createdAt"],
#         "uniqueItems": ["username"],
#         "properties": {
#             "username": {
#                 "bsontype": "string",
#                 "minlength": 5,
#                 "description": "Username은 최소 5글자 이상이어야 합니다.",
#             },
#             "password": {
#                 "bsontype": "string",
#             },
#             "createdAt": {"bsontype": "string", "default": datetime.now()},
#         },
#     }
# }
# 노래 document의 schema를 구성해보았고, user의 schema와 연동할 수 있으면 좋겠다
# 생각하여 $ref를 지정해보았으나 테스트 해 보지는 못함
# SongSchema = {
#     "$jsonSchema": {
#         "title": "Song_schema",
#         "description": "Song information",
#         "required": ["artistId", "trackTitle"],
#         "uniqueItems": ["artistId"],
#         "properties": {
#             "artistName": {"bsontype": "string"},
#             "artistId": {
#                 "bsontype": "string",
#             },
#             "trackTitle": {"bsontype": "string"},
#             "trackImage": {
#                 "bsontype": "string",
#                 "pattern": "^(http|https)://i.scdn.co/image/[a-zA-Z0-9]",
#             },
#             "trackPreview": {
#                 "bsontype": "string",
#             },
#             "weatherLikes": {
#                 "bsontype": "object",
#                 "required": ["sunny", "cloudy", "rainy", "snowy"],
#                 "properties": {
#                     "users": {
#                         "bsontype": "array",
#                         "properties": {
#                             "userId": {"bsontype": "objectId", "$ref": UserSchema}
#                         },
#                     },
#                     "sunny": {"bsontype": "int", "default": 0},
#                     "cloudy": {"bsontype": "int", "default": 0},
#                     "rainy": {"bsontype": "int", "default": 0},
#                     "snowy": {"bsontype": "int", "default": 0},
#                 },
#             },
#         },
#     }
# }

db.create_collection("Users")
db.create_collection("Songs")

# db.command({"collMod": "Users", "validator": UserSchema})
# db.command({"collMod": "Songs", "validator": SongSchema})
