# Flask settings
FLASK_DEBUG = True  # Do not use debug mode in production

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False

# SQLAlchemy settings
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username@host/database_name'
SQLALCHEMY_TRACK_MODIFICATIONS = False

#path to flanken json files
MOUNT_POINT = '/nfs/PROBIO/autoseq-output'
#MOUNT_POINT = '/home/kaikala/test/PROBIO/autoseq-output'
