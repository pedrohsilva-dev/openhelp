# import os
# from app import create_app
# import config

# app = create_app(config.environment[
#     os.environ.get("FLASK_ENV")
#  ])


from app import create_app
from config import ProdConfig


app = create_app(ProdConfig)

app.run("localhost", 8080, False, True)
