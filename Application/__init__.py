from flask import Flask, render_template, url_for
from werkzeug import exceptions
from instance import IApplicationConfiguration
from sqlalchemy.orm import MappedAsDataclass, DeclarativeBase
from flask_sqlalchemy import SQLAlchemy
from .ui_components import CardComponent

class Base(MappedAsDataclass, DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

def create_app(config: IApplicationConfiguration, /) -> Flask:
    app: Flask = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)

    # import Application.error_handlers as errhndl
    # app.register_error_handler(exceptions.HTTPException, errhndl.toastify_default_errors)
    # app.register_error_handler(exceptions.NotFound, errhndl.handle_notfound_errors)

    from Application.blueprints import bootstrap_form_practice, nice_admin
    app.register_blueprint(bootstrap_form_practice.bp)
    app.register_blueprint(nice_admin.bp)

    db.init_app(app)
    from Application.blueprints.bootstrap_form_practice.models import Student
    with app.app_context():
        db.create_all()


    @app.get('/')
    def home():
        cards = [
            CardComponent(thumbnail_path=url_for('static', filename='thumbnails/form1_screenshot.png'), title='Student Registration Form', preview_path=url_for('BootstrapFormPractice.form1')),
            CardComponent(thumbnail_path=url_for('static', filename='thumbnails/form2_screenshot.png'), title='Identity Registration Form', preview_path=url_for('BootstrapFormPractice.form2')),
            CardComponent(thumbnail_path=url_for('static', filename='thumbnails/form3_screenshot.png'), title='Delivery Registration Form', preview_path=url_for('BootstrapFormPractice.form3')),
            CardComponent(thumbnail_path=url_for('static', filename='thumbnails/form4_screenshot.png'), title='Finance Form', preview_path=url_for('BootstrapFormPractice.form4')),
            CardComponent(thumbnail_path=url_for('static', filename='thumbnails/nice_admin_screenshot.png'), title='Nice Admin', preview_path=url_for('NiceAdmin.home'))
        ]
        return render_template('index.html', cards=cards)
            
    return app