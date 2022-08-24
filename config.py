import os


if os.environ.get("SQLALCHEMY_DATABASE_URI") != None:
    PATH = os.environ.get("SQLALCHEMY_DATABASE_URI")
else:
    tmp = os.path.realpath("temp/database.db")
    PATH = "sqlite:///" + tmp
    del tmp


class Config:
    '''
    Configuration Global
    '''
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "osdfkqwdnfbuybewsdhfvbfidfsjdieheqdpj"
    SECRET_KEY = "jbdiçsgpweregtergerwgfejbgileçhjfuqehrbf"


class DevConfig(Config):
    '''
    Development Configuration
    '''
    SQLALCHEMY_DATABASE_URI = PATH


class ProdConfig(Config):
    '''
    Production Configuration
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")


environment = {
    "development": DevConfig,
    "production": ProdConfig
}
