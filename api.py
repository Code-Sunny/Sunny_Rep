from flask import Blueprint, request, session, jsonify
from db import db
api = Blueprint('api', __name__, url_prefix="/api")

@api.route("/like-btn", methods=["POST"])
def new_like():
  if not "username" in session:
    return jsonify({"error": "로그인 되지 않은 이용자입니다."})
  else:
    return jsonify({"ok": True, "msg": "Like updated"})

@api.route("/show-like", methods=["GET"])
def show_like():
  args = request.args.get()
  track_id = args["track_id"]
  return None