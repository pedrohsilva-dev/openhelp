import os
from app.system.extensions import config

from werkzeug.utils import secure_filename
from flask_login import logout_user, login_user, login_required, current_user
from flask import jsonify, request, render_template, url_for, redirect, abort, send_from_directory
# v from urlparse2.urlparse2 import urljoin, urlparse
from flask import request, url_for
from app.system.models.follow import Follow
from app.website.forms.company import Company as CompanyForm
from app.website.forms.company import CompanyLogin
from app.system.models.message import Message
from app.website.forms.warning import WarningForm
from app.system.models.company import Company
from app.system.models.client import Client
from app.system.models.warning import Warnings
from app.system.models.speech import Speech
from app.website.utils import dir_file, generate_namefile


@login_required
def homeView():
    clientsData = Client.query.all()
    return render_template("clients.html", clients=clientsData)


def loginView():
    """ Access: /login [done] """
    form = CompanyLogin()

    if request.method == "POST":
        email = str(form.email.data)
        password = str(form.password.data)
        company = Company.sign(email, password)

        if (company != None):
            login_user(company)
            next = request.form.get('next', None)

            if next != None:
                return redirect(next)

            return redirect(url_for("index"))

        else:
            return redirect(url_for("index"))

    return render_template("login.html", form=form)


@login_required
def warningsView():
    """"Access: /warnings (done)"""
    warnings = Warnings.query.filter_by(company_id=int(current_user.id))

    return render_template("posts.html", warnings=warnings)


@login_required
def warningsFormView():
    """"Access: /warnings/form (done)"""
    form = WarningForm()

    if (request.method == 'POST'):
        if form.validate_on_submit():
            title = form.title.data
            content = form.content.data
            photo = form.photo.data

            filename_photo = generate_namefile(
                secure_filename(photo.filename), photo.content_type
            )
            photo.save(dir_file(filename_photo))

            warning = Warnings(title=title, content=content,
                               image=filename_photo, company_id=int(current_user.id))

            warning.save()

        warnings = Warnings.query.all()
        return redirect(url_for("warningsView"))

    return render_template("register_post.html", form=form)


def registerView():
    """ Access: /register (done)"""
    if str(request.method) == "GET":
        form = CompanyForm()
        return render_template("register.html", form=form)
    elif str(request.method) == "POST":
        form = CompanyForm()
        if form.validate_on_submit():
            username = form.fantasy_name.data
            email = form.email.data
            password = form.password.data
            city = form.city.data
            state = form.state.data

            photo = form.photo.data

            filename_photo = generate_namefile(
                secure_filename(photo.filename), photo.content_type
            )
            photo.save(dir_file(filename_photo))

            company = Company(username, email, password,
                              city, state, filename_photo)

            company.save()

        form = CompanyLogin()
        return render_template("login.html", form=form)


@login_required
def messagesView():
    """ Access: /messages (done) """
    return render_template("messages.html")


@login_required
def messageWarningImageView(photo_id=None):
    """ Access: /warning/image/<int:photo_id> (done) """
    photo_warning: Warnings = Warnings.query.get(int(photo_id))

    image = photo_warning.image

    if (photo_id):

        return send_from_directory(
            os.path.realpath("files"), image, as_attachment=True
        ), 200

    else:
        return None, 404


@login_required
def messageClientImageView(photo_id: int = None):
    """ Access: /client/image/<int:photo_id> (done) """
    photo_client = Client.query.filter_by(id=photo_id)
    image = photo_client.photo_profile

    if (photo_id is None):

        return send_from_directory(
            str(config['UPLOAD_FOLDER']), image, as_attachment=True
        ), 200

    else:
        return None, 404


@login_required
def index():
    return render_template("index.html")


@login_required
def companyImageView():
    photo_company = Company.find(current_user.id)
    print(photo_company)
    image = photo_company.photo_profile
    if (current_user.id != None):

        return send_from_directory(
            os.path.realpath("files"), image, as_attachment=True
        )

    else:
        return photo_company, 200


@login_required
def messageOuve(company=None, client=None):
    """ Access: /message/<int:company>/<int:client> (done) """
    return render_template("ouve.html")


@login_required
def logoutView():
    logout_user()
    return redirect(url_for("loginView"))


@login_required
def profile():
    return render_template("profile.html", user=current_user.id)


def testeView():
    ...
    # formTest = Teste()

    # if request.method == "POST":
    #     if formTest.validate_on_submit():
    #         print("Campos")
    #         print(formTest.campo.data)
    #         print(formTest.teste.data)

    # return render_template("form.html", form=formTest)


@login_required
def updateView():

    if request.method == "POST":
        formCompany = CompanyForm()
        if formCompany.validate_on_submit():
            fantasy_name = formCompany.fantasy_name.data
            email = formCompany.email.data
            password = formCompany.password.data
            city = formCompany.city.data
            state = formCompany.state.data
            company = Company.query.filter_by(id=current_user.id)
            data = {
                "company_name": fantasy_name,
                "email": email,
                "city": city,
                "state": state
            }

            if (password != None):
                data["password"] = str(password)

            Company.update_company(old=company, new=data)
    elif (request.method == "GET"):
        formCompany = CompanyForm()

        formCompany.fantasy_name.data = current_user.company_name
        formCompany.email.data = current_user.email
        formCompany.password.data = current_user.password
        formCompany.city.data = current_user.city
        formCompany.state.data = current_user.state

    return render_template("update.html", form=formCompany)


@login_required
def deleteView():
    if request.method == "POST":
        company: Company = Company.query.filter_by(id=int(current_user.id))
        # deleta client
        Company.delete_object(company)
    else:
        return render_template("confirm_delete.html")

    return redirect(url_for("loginView"))


@login_required
def showClients(client_id=None):
    if (client_id == None):
        follows_clients = Follow.query.filter_by(company_id=1).all()
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
def messageRegister(follow_id):
    content = request.form.get("message", None)
    message = Message("Qualquer um", content, "COM")
    message.save()
    speech = Speech(follow_id=follow_id, message_id=message.id)
    speech.save()
    return redirect(url_for("showClients", client_id=follow_id))
