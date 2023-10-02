from flask import Blueprint, render_template, request, jsonify, url_for
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


@views.route('/summed_results', methods=['GET', 'POST'])
def summed_results():

    if request.method == 'POST':
        selected_lgas = request.get_json().get('selected_lgas', [])
        """Query the database to fetch the polling units in the selected local government"""
        polling_units = storage.get_polling_units_by_ids(selected_lgas)

        """Initialize a dictionary to store summed results for each party"""
        summed_results = {}

        """Loop through each polling unit and sum the results for each party"""
        for polling_unit in polling_units:

            polling_unit_id = polling_unit.uniqueid
            results = storage.get_polling_unit_results(polling_unit_id)

            """Sum the results for each party"""
            for result in results:
                party_abbreviation = result.party_abbreviation
                party_score = result.party_score

                """Add or update the party's total score in the summed_results dictionary"""
                if party_abbreviation in summed_results:
                    summed_results[party_abbreviation] += party_score
                else:
                    summed_results[party_abbreviation] = party_score
        # redirect_url = url_for('route.summed_results')

        # response_data = {
        #     'summed_results': summed_results, 
        #     'redirect_url': redirect_url
        # }
        """Return the summed results as JSON"""
        return jsonify({'summed_results': summed_results})
    
    lga = storage.get_lga()
    return render_template('summed_results.html', title='Summed Result', 
                           local_governments=lga)