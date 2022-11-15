from flask import request
from flask_restful import Resource, reqparse, marshal_with, fields
from app.system.models.message import Message
from app.system.models.speech import Speech
from app.system.models.follow import Follow
from app.system.services.lib_jwt import auth_jwt_required

parserSpeech = reqparse.RequestParser()
parserSpeech.add_argument("follow_id", type=int, location='args')

parserMessage = reqparse.RequestParser()
parserMessage.add_argument("follow_id", type=int)
parserMessage.add_argument("content")

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
    "company_name": fields.String,
    "pub_date": fields.DateTime,
    "follow_id": fields.Integer(),
    "image_company": fields.String,
}
messageResource = {
    "id": fields.Integer,
    "content": fields.String,
    "pub_date": fields.DateTime,
    "who": fields.String
}


class SpeechResource(Resource):
    @auth_jwt_required
    @marshal_with(success_resource)
    def post(self, current_user):
        args = parserSpeech.parse_args(request)
        follow_value_id = args.get("follow_id", None)
        message = Message(
            content="criou uma conversa", who="CLI")
        message.save()

        speech = Speech(message_id=int(message.id),
                        follow_id=int(follow_value_id))

        speech.save()

        return {
            "success": "Sucesso no cadastro da mensagem"
        }

    @auth_jwt_required
    @marshal_with(speeches_resource)
    def get(self, current_user):

        follows = Follow.query.filter_by(client_id=current_user.id).all()

        speeches = []
        for i in follows:
            speech = Speech.query.filter_by(follow_id=i.id).first()
            if (speech):
                speeches.append({
                    "id": speech.id,
                    "company_name": i.company.company_name,
                    "pub_date": speech.pub_date,
                    "follow_id": i.id,
                    "image_company": f"/companies/image/{i.company.id}"
                })
        return speeches


class MessageResource(Resource):
    @auth_jwt_required
    @marshal_with(success_resource)
    def post(self, current_user):
        args = parserMessage.parse_args(request)
        content = args.get("content", None)
        follow_id = int(args.get("follow_id", None))
        message = Message(content, "CLI")
        message.save()
        speech = Speech(follow_id=follow_id, message_id=message.id)
        speech.save()

    @auth_jwt_required
    @marshal_with(messageResource)
    def get(self, current_user):
        args = parserSpeech.parse_args(request)

        speeches = Speech.query.filter_by(
            follow_id=int(args.get("follow_id", None))).all()
        messages = []
        for i in speeches:
            messages.append(i.message)

        return messages
