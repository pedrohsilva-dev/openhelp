from flask import Flask,  request
from flask.templating import render_template
from app.forms.company import Company as CompanyForm
from app.forms.company import CompanyLogin
from app.models.company import Company
from app.models.client import Client


def start_web(flask: Flask):

    @flask.route("/home", methods=["GET"])
    def homeView():
        clientsData = Client.query.all()
        return render_template("clients.html", clients=clientsData)

    @flask.route("/login", methods=["GET"])
    def loginView():
        form = CompanyLogin()
        return render_template("login.html", form=form)

    @flask.route("/register", methods=["GET", "POST"])
    def registerView():

        if str(request.method) == "GET":
            form = CompanyForm()
            return render_template("register.html", form=form)
        elif str(request.method) == "POST":
            form = CompanyForm()
            username = request.form.get('fantasy_name')
            email = request.form.get('email')
            password = request.form.get('password')
            city = request.form.get('city')
            state = request.form.get('state')

            company = Company(username, email, password,
                              city, state, "disfishd")

            company.save()

            form = CompanyLogin()
            return render_template("login.html", form=form)

    @flask.route("/chat", methods=["GET"])
    def chatView():
        return render_template("chat.html")

    @flask.route("/messages", methods=["GET"])
    def messagesView():
        return render_template("messages.html")

    return flask
