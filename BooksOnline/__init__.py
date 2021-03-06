# app factory

'''
$env:FLASK_APP="BooksOnline"
$env:FLASK_ENV="development"
flask run
'''
import os

from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'database.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # db.py
    from . import db
    db.init_app(app)

    # auth.py
    from . import auth
    app.register_blueprint(auth.bp)

    # explore.py
    from . import explore
    app.register_blueprint(explore.bp)
    app.add_url_rule('/', endpoint='index')

    # check.py
    from . import check
    app.register_blueprint(check.bp)

    return app