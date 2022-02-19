from flask import current_app as app
from flask import *
from app.main import bp
from.forms import SettingsForm
import yaml


@bp.route("/", methods=["GET"])
def index():
    return render_template("pages/index.jinja")