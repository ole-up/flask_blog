class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SECRET_KEY = '43tgvergh4534t34gf54545geg'
    MAIL_SERVER = 'smtp.yandex.ru'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = "oleg-741@yandex.ru"
    MAIL_PASSWORD = ""
    FLASK_ADMIN_SWATCH = 'cerulean'