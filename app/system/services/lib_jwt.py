import datetime
from functools import wraps

from flask_restful import marshal, fields, abort

from app.system.models.client import Client
from flask import current_app, request
import jwt


def generate_token(current_id: int, secret: str, time_minutes: int = 30):
    encoded_jwt = jwt.encode(
        {"id": current_id, "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=time_minutes)}, secret, algorithm="HS256")
    return encoded_jwt


def auth_jwt_required(f):
    @wraps(f)
    def apply(*args, **kwargs):
        token = None

        if ("Authorization" in request.headers):
            token = request.headers["Authorization"]
        print(token)
        if (not token):
            return abort(403)

        if (not "Bearer" in token):
            return abort(401)

        try:
            token_extracted = token.replace("Bearer ", "")
            result = jwt.decode(
                token_extracted, current_app.config["SECRET_KEY"], algorithms=["HS256"])
            current_user = Client.query.get(int(result.get("id")))

            return f(current_user=current_user, *args, **kwargs)
        except:
            return abort(403)

    return apply
