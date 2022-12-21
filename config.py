class DevConfig:
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    SESSION_TYPE='sqlalchemy'
    ALCHEMICAL_DATABASE_URL='sqlite:///data.sqlite'
    SECRET_KEY='qBOq5mSssHdGqTN6I9CUDBloZUngVTyy'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    APIFAIRY_TITLE = "SOLVER-EXAM-API"
    APIFAIRY_VERSION = 1.0
    APIFAIRY_UI = "swagger_ui"