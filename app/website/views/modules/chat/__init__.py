from flask import render_template
from flask_login import login_required, current_user

from app.system.models.speech import Speech

from app.system.models.follow import Follow


@login_required
def showClients(client_id=None):
    if (client_id == None):
        follows_clients = Follow.query.filter_by(
            company_id=current_user.id).all()
        list_follow_clients = []
        for follow in follows_clients:
            hasSpeech = Speech.list_message_follow(follow_id=follow.id)
            if hasSpeech:
                list_follow_clients.append(
                    {"follow": follow, "speech": hasSpeech}
                )
            else:
                list_follow_clients.append(
                    {"follow": follow, "speech": None}
                )

        return render_template("clients.html", follows=list_follow_clients)
    else:
        speeches = Speech.list_messages(client_id)

        return render_template("ouve.html", speeches=speeches, follow_id=client_id)


@login_required
def messageOuve(company=None, client=None):
    """ Access: /message/<int:company>/<int:client> (done) """
    return render_template("ouve.html")


@login_required
def messagesView():
    """ Access: /messages (done) """
    return render_template("messages.html")
