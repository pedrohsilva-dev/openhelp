import os
from flask import current_app, redirect, render_template, request, send_from_directory, url_for, flash
from flask_login import current_user, login_required, login_user, logout_user
from app.website.forms.company import Company as CompanyForm
from app.website.forms.company import CompanyLogin
from app.system.models.company import Company
from werkzeug.utils import secure_filename
from app.website.utils import dir_file, generate_namefile


def registerView():
    """ Access: /register (done)"""
    if str(request.method) == "GET":
        form = CompanyForm()
        return render_template("register.html", form=form)
    elif str(request.method) == "POST":
        try:
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
                flash("Cadastro bem sucedido!!!", "success")

        except:
            flash("Erro no cadastro!!!", "error")

    form = CompanyLogin()
    return render_template("login.html", form=form)


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
def profile():
    return render_template("profile.html", user=current_user.id)


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
            flash("Atualizado com sucesso!!!", "success")
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
        company: Company = Company.query.get(int(current_user.id))
        # deleta client
        filePhoto = os.path.join(current_app.config.get(
            "UPLOAD_FOLDER"), company.photo_profile)
        os.remove(filePhoto)
        Company.delete_object()
        flash("Deletado com sucesso!!!", "success")
    else:
        return render_template("confirm_delete.html")

    return redirect(url_for("loginView"))


@login_required
def logoutView():
    logout_user()
    return redirect(url_for("loginView"))


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
            flash("Credenciais errada, confirme o email ou a senha!!!", "error")
            return redirect(url_for("loginView"))

    return render_template("login.html", form=form)
