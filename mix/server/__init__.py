# mix/server/__init__.py


import os

from flask import Flask, render_template
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

# instantiate the extensions
login_manager = LoginManager()
bcrypt = Bcrypt()
toolbar = DebugToolbarExtension()
db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()


def create_app(script_info=None):

    # instantiate the app
    app = Flask(
        __name__,
        template_folder='../client/templates',
        static_folder='../client/build'
    )

    # set config
    app_settings = os.getenv(
        'APP_SETTINGS', 'mix.server.config.DevelopmentConfig')
    app.config.from_object(app_settings)

    # set up extensions
    login_manager.init_app(app)
    bcrypt.init_app(app)
    toolbar.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)

    # register blueprints
    from mix.server.user.views import user_blueprint
    from mix.server.main.views import main_blueprint
    app.register_blueprint(user_blueprint)
    app.register_blueprint(main_blueprint)

    # flask login
    from mix.server.models import User
    login_manager.login_view = 'user.login'
    login_manager.login_message_category = 'danger'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.filter(User.id == int(user_id)).first()

    # error handlers
    @app.errorhandler(403)
    def forbidden_page(error):
        return render_template('errors/403.html'), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def server_error_page(error):
        return render_template('errors/500.html'), 500

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
