from model import *

@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password

### Units ###

# route to get all units
@app.route('/units', methods=['GET'])
@auth.login_required
def get_all_units():
    '''function to get all units in database'''
    if len(Units.get_units()) == 0:
        response = Response("No units in database", 400, mimetype='application/json')
        return response 
    return jsonify({'Units': Units.get_units()})


# route to get unit by id
@app.route('/units/<int:id>', methods=['GET'])
@auth.login_required
def get_unit_by_id(id):
    '''function to get unit in database using id as parameters'''
    return_value = Units.get_unit_id(id)
    if len(return_value) == 0:
        response = Response("No this id in unit database", 400, mimetype='application/json')
        return response
    return jsonify(return_value)

# route to get unit by name
@app.route('/units/<name>', methods=['GET'])
@auth.login_required
def get_unit_by_name(name):
    '''function to get unit in database using name as parameters'''
    return_value = Units.get_unit_name(name)
    if len(return_value) == 0:
        response = Response("No this name in unit database", 400, mimetype='application/json')
        return response
    return jsonify(return_value)


# route to add new unit
@app.route('/units', methods=['POST'])
@auth.login_required
def add_unit():
    '''function to add unit to database'''
    request_data = request.get_json()
    Units.add_unit(request_data["name"], request_data["type"])
    response = Response("Unit added", 201, mimetype='application/json')
    return response


# route to update unit with PUT method
@app.route('/units/<int:id>', methods=['PUT'])
@auth.login_required
def update_unit(id):
    '''function to update unit in database using id as parameters'''
    request_data = request.get_json()
    if Units.query.filter_by(id=id).first() == None:
        response = Response("Fail to Update Unit", 400, mimetype='application/json')
        return response
    Units.update_unit(id, request_data['name'], request_data['type'])
    response = Response("Unit Updated", status=200, mimetype='application/json')
    return response


# route to delete unit using the DELETE method
@app.route('/units/<int:id>', methods=['DELETE'])
@auth.login_required
def remove_unit_id(id):
    '''function to remove unit in database using id as parameters'''
    if Units.query.filter_by(id=id).first() == None:
        response = Response("Fail to Delete Unit", 400, mimetype='application/json')
        return response
    Units.delete_unit_id(id)
    response = Response("Unit Deleted", status=200, mimetype='application/json')
    return response

# route to delete unit using the DELETE method
@app.route('/units/<name>', methods=['DELETE'])
@auth.login_required
def remove_unit_name(name):
    '''function to remove unit in database using name as parameters'''
    if Units.query.filter_by(name=name).first() == None:
        response = Response("Fail to Delete Unit", 400, mimetype='application/json')
        return response
    Units.delete_unit_name(name)
    response = Response("Unit Deleted", status=200, mimetype='application/json')
    return response

### Conversion Units ###

# route to get all conversions
@app.route('/conversions', methods=['GET'])
@auth.login_required
def get_all_conversions():
    '''function to get all conversions in database'''
    if len(Conversions.get_conversions()) == 0:
        response = Response("No Conversions in database", 400, mimetype='application/json')
        return response
    return jsonify({'Conversions': Conversions.get_conversions()})


# route to get conversion by id
@app.route('/conversions/<int:id>', methods=['GET'])
@auth.login_required
def get_conversion_by_id(id):
    '''function to get conversion in database using id as parameters'''
    return_value = Conversions.get_conversion_id(id)
    if len(return_value) == 0:
        response = Response("No this Conversion in database", 400, mimetype='application/json')
        return response
    return jsonify(return_value)

# route to get conversion by name two units
@app.route('/conversions/<unit1>/<unit2>', methods=['GET'])
@auth.login_required
def get_conversion_by_units(unit1,unit2):
    '''function to get conversion in database using unit1, unit2 as parameters'''
    return_value = Conversions.get_conversion_units(unit1,unit2)
    if len(return_value) == 0:
        response = Response("No this Conversion in database", 400, mimetype='application/json')
        return response
    return jsonify(return_value)


# route to add new conversion
@app.route('/conversions', methods=['POST'])
@auth.login_required
def add_conversion():
    '''function to add conversion to database'''
    request_data = request.get_json()
    Conversions.add_conversion(request_data["unit1"], request_data["unit2"], request_data["ratio"])
    response = Response("Conversion units added", 201, mimetype='application/json')
    return response


# route to update conversion with PUT method
@app.route('/conversions/<int:id>', methods=['PUT'])
@auth.login_required
def update_conversion(id):
    '''function to update conversion in database'''
    request_data = request.get_json()
    if Conversions.query.filter_by(id=id).first() == None:
        response = Response("Fail to Update Conversion", 400, mimetype='application/json')
        return response
    Conversions.update_conversion(id, request_data["unit1"], request_data["unit2"], request_data["ratio"])
    response = Response("Conversion units Updated", status=200, mimetype='application/json')
    return response


# route to delete conversion using the DELETE method
@app.route('/conversions/<int:id>', methods=['DELETE'])
@auth.login_required
def remove_conversion_id(id):
    '''function to delete conversion in database using id as parameters'''
    if Conversions.query.filter_by(id=id).first() != None :
        Conversions.delete_conversion_id(id)
        response = Response("Conversion units Deleted", status=200, mimetype='application/json')
    else:
        response = Response("Fail to Delete Conversion", status=400, mimetype='application/json')
    return response

# route to delete conversion using by two units name the DELETE method
@app.route('/conversions/<_unit1>/<_unit2>', methods=['DELETE'])
@auth.login_required
def remove_conversion_units(_unit1,_unit2):
    '''function to delete conversion in database using unit1, unit2 as parameters'''
    if Conversions.query.filter_by(unit1=_unit1, unit2=_unit2).first() != None :
        Conversions.delete_conversion_units(_unit1, _unit2)
    elif Conversions.query.filter_by(unit1=_unit2, unit2=_unit1).first() != None :
        Conversions.delete_conversion_units(_unit2, _unit1)
    else:
        response = Response("Fail to Delete Conversion", status=400, mimetype='application/json')
        return response
    response = Response("Conversion units Deleted", status=200, mimetype='application/json')
    return response

# route convert a value from one unit to another
@app.route('/convert', methods=['POST'])
@auth.login_required
def covert_unit_value():
    '''function to convert a value from one unit to another'''
    request_data = request.get_json()
    if Conversions.query.filter_by(unit1=request_data["unit1"], unit2=request_data["unit2"]).first() != None :
        conversion_units = Conversions.query.filter_by(unit1=request_data["unit1"], unit2=request_data["unit2"]).first()
    elif Conversions.query.filter_by(unit1=request_data["unit2"], unit2=request_data["unit1"]).first() != None:
        conversion_units = Conversions.query.filter_by(unit1=request_data["unit2"], unit2=request_data["unit1"]).first()
    else:
        response = Response("Convert error", 400, mimetype='application/json')
        return response
    _unitorg = request_data["unit1"]
    _unitdst = request_data["unit2"]
    ratio = conversion_units.ratio
    if conversion_units.unit1 == request_data["unit1"]:
        result = request_data["value"] * ratio
    else:
        result = request_data["value"] / ratio

    return jsonify({
        'convert': f"{_unitorg} ---> {_unitdst}",
        'value' : result
    })


if __name__ == "__main__":
    app.run(port=8742, debug=True)