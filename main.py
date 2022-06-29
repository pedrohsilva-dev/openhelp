import os
from app import create_app
import config

app = create_app(config.environment[
    os.environ.get("FLASK_ENV", "development")
])
