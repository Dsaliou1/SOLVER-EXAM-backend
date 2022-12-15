class DevConfig:
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    SESSION_TYPE='sqlalchemy'
    ALCHEMICAL_DATABASE_URL='sqlite:///data.sqlite'
    SECRET_KEY='qBOq5mSssHdGqTN6I9CUDBloZUngVTyy'
    SQLALCHEMY_TRACK_MODIFICATIONS = False