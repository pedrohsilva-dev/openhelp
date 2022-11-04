from flask import Flask, Response, send_from_directory, current_app
from app.system.models.warning import Warnings
from app.system.models.company import Company
from app.system.services.lib_jwt import auth_jwt_required


@auth_jwt_required
def warningAPIImageView(current_user, id: int = None):
    """ Access: /client/image/<int:photo_id> (done) """
    if (current_user):
        warning = Warnings.query.get(id)
        if (warning):
            image = warning.image

            return send_from_directory(
                str(current_app.config['UPLOAD_FOLDER']), image, as_attachment=True
            ), 200
        else:
            return None, 404
    else:
        return None, 404


@auth_jwt_required
def companyAPIImageView(current_user, id):
    """ Access: /client/image/<int:photo_id> (done) """
    if (current_user):
        company = Company.query.get(id)
        if (company):
            image = company.photo_profile

            return send_from_directory(
                str(current_app.config['UPLOAD_FOLDER']), image, as_attachment=True
            ), 200
        else:
            return None, 404
    else:
        return None, 404


@auth_jwt_required
def clientAPIImageView(current_user):
    """ Access: /client/image/<int:photo_id> (done) """
    if (current_user):
        image = current_user.photo_profile

        print(image)

        return send_from_directory(
            str(current_app.config['UPLOAD_FOLDER']), image, as_attachment=True
        ), 200
    else:
        return None, 404


def api_image_application(server: Flask = None):
    server.add_url_rule('/api/warnings/image/<int:id>',
                        view_func=warningAPIImageView, provide_automatic_options=False)
    server.add_url_rule('/api/clients/image/profile',
                        view_func=clientAPIImageView, provide_automatic_options=False)
    server.add_url_rule('/api/companies/image/<int:id>',
                        view_func=companyAPIImageView, provide_automatic_options=False)
    return server
