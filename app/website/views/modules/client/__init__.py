from flask import current_app, send_from_directory
from flask_login import login_required

from app.system.models.client import Client


@login_required
def messageClientImageView(photo_id: int = None):
    """ Access: /client/image/<int:photo_id> (done) """
    photo_client = Client.query.filter_by(id=photo_id)
    image = photo_client.photo_profile

    if (photo_id is None):

        return send_from_directory(
            str(current_app.config['UPLOAD_FOLDER']), image, as_attachment=True
        ), 200

    else:
        return None, 404
