from app.system.extensions import config
from flask_login import logout_user, login_user, login_required, current_user
from flask import request, render_template, url_for, redirect, abort, send_from_directory
# v from urlparse2.urlparse2 import urljoin, urlparse
from flask import request, url_for
from app.website.forms.company import Company as CompanyForm
from app.website.forms.company import CompanyLogin
from app.website.forms.warning import WarningForm
from app.system.models.company import Company
from app.system.models.client import Client
from app.system.models.warning import Warnings
from app.website.utils import generate_namefile


@login_required
def homeView():
    clientsData = Client.query.all()
    return render_template("clients.html", clients=clientsData)


# def is_safe_url(target):
#     ref_url = urlparse(request.host_url)
#     test_url = urlparse(urljoin(request.host_url, target))
#     return test_url.scheme in ('http', 'https') and \
#         ref_url.netloc == test_url.netloc


def loginView():
    """ Access: /login [done] """
    form = CompanyLogin()

    if request.method == "POST":
        email = str(request.form.get("email"))
        password = str(request.form.get("password"))
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
    warnings = Warnings.query.all()

    return render_template("posts.html", warnings=warnings)


@login_required
def warningsFormView():
    """"Access: /warnings/form (done)"""
    form = WarningForm()

    if (request.method == 'POST'):
        title = request.form.get('title')
        content = request.form.get('content')
        photo = request.files.get('photo')

        filename_photo = generate_namefile(
            photo.filename, photo.content_type)
        photo.save(filename_photo)
        warnings = Warnings.query.all()

        warning = Warnings(title=title, content=content,
                           image=filename_photo)

        warning.save()
        return render_template("posts.html", warnings=warnings)

    return render_template("register_post.html", form=form)


def registerView():
    """ Access: /register (done)"""
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


@login_required
def messagesView():
    """ Access: /messages (done) """
    return render_template("messages.html")


@login_required
def messageWarningImageView(photo_id: int = None):
    """ Access: /warning/image/<int:photo_id> (done) """
    photo_warning: Warnings = Warnings.query.filter_by(id=photo_id)

    image = photo_warning.image

    if (photo_id is None):

        return send_from_directory(
            str(config['UPLOAD_FOLDER']), image, as_attachment=True
        ), 200

    else:
        return None, 404


@login_required
def messageClientImageView(photo_id: int = None):
    """ Access: /client/image/<int:photo_id> (done) """
    photo_client = Client.query.filter_by(id=photo_id)
    print(photo_client)
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
def messageCompanyImageView(photo_id: int = None):
    """ Access: /company/image/<int:photo_id> """
    photo_company: Company = Company.query.filter_by(id=photo_id)

    image = photo_company.photo_profile

    if (photo_id is None):

        return send_from_directory(
            str(config['UPLOAD_FOLDER']), image, as_attachment=True
        ), 200

    else:
        return None, 404


@login_required
def messageOuve(company=None, client=None):
    """ Access: /message/<int:company>/<int:client> (done) """
    return render_template("ouve.html")



@login_required
def logoutView():
    logout_user()
    return redirect(url_for("loginView"))
