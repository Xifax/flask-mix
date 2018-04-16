# mix/server/main/views.py


from flask import render_template, Blueprint

# Use blueprints for each logical domain
main_blueprint = Blueprint('main', __name__,)


@main_blueprint.route('/')
def home():
    return render_template('landing.html')
