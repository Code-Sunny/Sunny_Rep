from pymongo import MongoClient
from datetime import datetime

client = MongoClient("localhost", 27017)
db = client.sunny


UserSchema = {
    "$jsonSchema": {
        "title": "User_schema",
        "description": "User information",
        "requried": ["username", "password", "createdAt"],
        "uniqueItems": ["username"],
        "properties": {
            "username": {
                "bsontype": "string",
                "minlength": 5,
                "description": "Username은 최소 5글자 이상이어야 합니다.",
            },
            "password": {
                "bsontype": "string",
            },
            "createdAt": {"bsontype": "string", "default": datetime.now()},
        },
    }
}

SongSchema = {
    "$jsonSchema": {
        "title": "Song_schema",
        "description": "Song information",
        "required": ["artistId", "trackTitle"],
        "uniqueItems": ["artistId"],
        "properties": {
            "artistName": {"bsontype": "string"},
            "artistId": {
                "bsontype": "string",
            },
            "trackTitle": {"bsontype": "string"},
            "trackImage": {
                "bsontype": "string",
                "pattern": "^(http|https)://i.scdn.co/image/[a-zA-Z0-9]",
            },
            "trackPreview": {
                "bsontype": "string",
            },
            "weatherLikes": {
                "bsontype": "object",
                "required": ["sunny", "cloudy", "rainy", "snowy"],
                "properties": {
                    "users": {
                        "bsontype": "array",
                        "properties": {
                            "userId": {"bsontype": "objectId", "$ref": UserSchema}
                        },
                    },
                    "sunny": {"bsontype": "int", "default": 0},
                    "cloudy": {"bsontype": "int", "default": 0},
                    "rainy": {"bsontype": "int", "default": 0},
                    "snowy": {"bsontype": "int", "default": 0},
                },
            },
        },
        "dependencies": [],
    }
}

db.create_collection("Users")
db.create_collection("Songs")

db.command({"collMod": "Users", "validator": UserSchema})
db.command({"collMod": "Songs", "validator": SongSchema})
