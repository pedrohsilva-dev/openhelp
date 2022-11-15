from flask_login import login_required
from flask import request, render_template, url_for, redirect

from flask import request, url_for

from app.system.models.message import Message
from app.system.models.client import Client
from app.system.models.speech import Speech

# modules
from app.website.views.modules.company import *
from app.website.views.modules.warning import *
from app.website.views.modules.chat import *
from app.website.views.modules.client import *

# Initial page


@login_required
def homeView():
    clientsData = Client.query.all()
    return render_template("clients.html", clients=clientsData)


@login_required
def index():
    return render_template("index.html")


@login_required
def messageRegister(follow_id):
    content = request.form.get("message", None)
    message = Message(content, "COM")
    message.save()
    speech = Speech(follow_id=follow_id, message_id=message.id)
    speech.save()
    return redirect(url_for("showClients", client_id=follow_id))
