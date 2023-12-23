from flask import Flask
from flask_mysql_connector import MySQL
from flask_bootstrap import Bootstrap
from config import DB_USERNAME, DB_PASSWORD, DB_NAME, DB_HOST, SECRET_KEY, BOOTSTRAP_SERVE_LOCAL
from flask_wtf.csrf import CSRFProtect

mysql = MySQL()
bootstrap = Bootstrap()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=SECRET_KEY,
        MYSQL_USER=DB_USERNAME,
        MYSQL_PASSWORD=DB_PASSWORD,
        MYSQL_HOST=DB_HOST,
        MYSQL_DATABASE=DB_NAME
    )

    bootstrap.init_app(app)
    mysql.init_app(app)
    CSRFProtect(app)

    from .controller.admin import user
    from .controller.college import college
    from .controller.course import course
    from .controller.student import student


    app.register_blueprint(user)
    app.register_blueprint(college)
    app.register_blueprint(course)
    app.register_blueprint(student)

    return app