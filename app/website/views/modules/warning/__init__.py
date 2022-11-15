import os
from flask import current_app, redirect, render_template, request, flash, send_from_directory, url_for
from flask_login import current_user, login_required
from app.system.models.warning import Warnings

from app.website.utils import dir_file, generate_namefile
from app.website.forms.warning import WarningForm
from werkzeug.utils import secure_filename


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
            try:
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
                flash("Cadastro de aviso bem sucedido!!!", "success")
            except:
                flash("Erro no cadastro de aviso!!!", "error")

        return redirect(url_for("warningsView"))

    return render_template("register_post.html", form=form)


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
def deleteWarningView(_id=None):

    if request.method == "POST" and _id == None:
        try:
            warning = Warnings.query.get(request.form.get("_id", None))
            filePhoto = os.path.join(current_app.config.get(
                "UPLOAD_FOLDER"), warning.image)
            os.remove(filePhoto)
            warning.delete()
            flash("Aviso deletado com sucesso!!!", "success")
            warnings = Warnings.query.filter_by(
                company_id=int(current_user.id))

            return render_template("posts.html", warnings=warnings)

        except:
            flash("Erro ao deletar aviso!!!", "error")
            warnings = Warnings.query.filter_by(
                company_id=int(current_user.id))

            return render_template("posts.html", warnings=warnings)
    else:
        _id = int(_id)
        return render_template("confirm_delete_warning.html", id_warning=_id)
