from flask import request
from flask_restful import Resource, reqparse, marshal_with, fields
from app.system.models.message import Message
from app.system.models.speech import Speech
from app.system.models.follow import Follow
from app.system.services.lib_jwt import auth_jwt_required

parserSpeech = reqparse.RequestParser()
parserSpeech.add_argument("title", type=str)
parserSpeech.add_argument("follow_id", type=int)

success_resource = {
    "success": fields.String()
}
follow_resource_fields = {
    "id": fields.Integer(),
    "client_id": fields.Integer(),
    "company_id": fields.Integer(),
}

speeches_resource = {
    "id": fields.Integer(),
    "title": fields.String(),
    "message_id": fields.Integer(),
    "follow_id": fields.Integer(),
    "follow": fields.Nested(follow_resource_fields)
}


class SpeechResource(Resource):
    @auth_jwt_required
    @marshal_with(success_resource)
    def post(self, current_user):
        args = parserSpeech.parse_args(request)
        follow_value_id = args.get("follow_id", None)
        title_value = args.get("title", None)
        message = Message(
            title=f"Conversando com {current_user.username}", content="criou uma conversa", who="CLI")
        message.save()

        speech = Speech(title=title_value, message_id=int(message.id),
                        follow_id=int(follow_value_id))

        speech.save()

        return {
            "success": "Sucesso no cadastro da mensagem"
        }

    @auth_jwt_required
    @marshal_with(speeches_resource)
    def get(self, current_user):
        follows = Follow.query.filter_by(client_id=current_user.id).all()
        print(follows)
        speeches = []
        for i in follows:
            speeches.append(Speech.query.filter_by(follow_id=i.id).first())
        print(speeches)
        return speeches


class MessageResource(Resource):
    @auth_jwt_required
    @marshal_with(success_resource)
    def post(self, current_user):
        args = None
        content = args.get("message", None)
        title = args.get("title", None)
        follow_id = args.get("follow_id", None)
        message = Message(title, content, "CLI")
        message.save()
        speech = Speech(follow_id=follow_id, message_id=message.id)
        speech.save()

    @auth_jwt_required
    @marshal_with(success_resource)
    def get(self, current_user):
        speeches = Speech.query.filter_by(follow_id=2).all()
        messages = []
        for i in speeches:
            messages.append(i.message.content)
        print(messages)
        return None
