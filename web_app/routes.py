from flask import Blueprint, render_template, request, jsonify, url_for, flash, redirect
from models import storage
from models.new_result import Result

views = Blueprint('route', __name__)
"""Define the global variable to store selected LGAs"""
selected_lgas = []

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
    global selected_lgas
    if request.method == 'POST':
        selected_lgas = request.get_json().get('selected_lgas', [])

        redirect_url = url_for('route.summed_results_data')
        """redirect page"""
        response_data = {
            'redirect_url': redirect_url
        }
        """Return the summed results as JSON"""
        return jsonify({'data': response_data})
    
    lga = storage.get_lga()
    return render_template('summed_results.html', title='Summed Result', 
                           local_governments=lga)

@views.route('/summed_results_data', methods=['GET'])
def summed_results_data():
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
    return render_template('summed_results_data.html', title='Summed Result Data for All LGAs', summed_results=summed_results)

@views.route('/new_result', methods=['GET', 'POST'])
def new_result():
    parties = storage.get_parties()
    if request.method == 'POST':
        """Loop through the parties to extract results"""
        polling_unit_name = request.form.get('polling_unit_name')
        pdp = int(request.form.get('PDP'))
        dpp = int(request.form.get('DPP'))
        acn = int(request.form.get('ACN'))
        ppa = int(request.form.get('PPA'))
        cdc = int(request.form.get('CDC'))
        jp = int(request.form.get('JP'))
        anpp = int(request.form.get('ANPP'))
        labour = int(request.form.get('LABOUR'))
        cpp = int(request.form.get('CPP'))

        result = Result(
            polling_unit_name=polling_unit_name,
            pdp=pdp,
            dpp=dpp,
            acn=acn,
            ppa=ppa,
            cdc=cdc,
            jp=jp,
            anpp=anpp,
            labour=labour,
            cpp=cpp
        )
        """Add the new_result to the database"""
        storage.new(result)
        storage.save()
        flash('New Entry Saved Successfully', category='success')
        return redirect(url_for('route.new_result'))
    return render_template('store_new_result.html', title='Store New Result', parties=parties)