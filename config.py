import os

pathDev = os.path.realpath("temp/openhelp.db")
pathDev = "sqlite:///" + pathDev
print(pathDev)


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):

    SQLALCHEMY_DATABASE_URI = pathDev


class ProdConfig(Config):
    ...


environment = {
    "development": DevConfig,
    "production": ProdConfig
}
