# project/server/user/views.py


from flask import Blueprint

user_blueprint = Blueprint('user', __name__, )


@user_blueprint.route('/hello')
def register():
    pass
