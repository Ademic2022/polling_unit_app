from flask import Blueprint, render_template
from models import storage

views = Blueprint('route', __name__)


@views.route('/')
def home():
    polling_unit = storage.get_polling_unit()
    return render_template('index.html', title='Polling Unit', polling_units=polling_unit)

@views.route('/polling_unit/<int:polling_unit_id>')
def polling_unit(polling_unit_id):
    polling_unit = storage.get_polling_unit_by_id(polling_unit_id)
    unit_name = polling_unit.polling_unit_name
    polling_unit_results = storage.get_polling_unit_results(polling_unit_id)
    return render_template('result.html', title='Polling Unit Result', 
                           polling_unit_results=polling_unit_results,
                           polling_unit_name=unit_name)