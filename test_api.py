import pytest
import json
from convertapi import *

def test_get_all_units():
    credentials = base64.b64encode(b"jace:pwdintanai").decode('utf-8')
    response = app.test_client().get('/units', headers={"Authorization": f"Basic {credentials}"})
    assert response.status_code == 200

def test_get_single_units_by_id():
    credentials = base64.b64encode(b"jace:pwdintanai").decode('utf-8')
    response = app.test_client().get('/units/3', headers={"Authorization": f"Basic {credentials}"})
    res = json.loads(response.data.decode('utf-8'))
    assert response.status_code == 200
    assert type(res[0]) is dict
    assert res[0]['type'] == 'Thailand'
    assert res[0]['name'] == 'Rai'

def test_get_single_units_by_name():
    credentials = base64.b64encode(b"jace:pwdintanai").decode('utf-8')
    response = app.test_client().get('/units/Square Meter', headers={"Authorization": f"Basic {credentials}"})
    res = json.loads(response.data.decode('utf-8'))
    assert response.status_code == 200
    assert type(res[0]) is dict
    assert res[0]['type'] == 'Philippines'
    assert res[0]['name'] == 'Square Meter'

def test_add_unit():
    credentials = base64.b64encode(b"jace:pwdintanai").decode('utf-8')
    response = app.test_client().post('/units', json = {
        "type" : "testland",
        "name" : "unitone"
    }, headers={"Authorization": f"Basic {credentials}"}
    )
    assert response.status_code == 201

def test_update_unit():
    credentials = base64.b64encode(b"jace:pwdintanai").decode('utf-8')
    response = app.test_client().put('/units/2', json = {
        "type" : "Philippines",
        "name" : "Square Meter"
    }, headers={"Authorization": f"Basic {credentials}"})
    assert response.status_code == 200

def test_delete_unit():
    credentials = base64.b64encode(b"jace:pwdintanai").decode('utf-8')
    response = app.test_client().delete('/units/4', headers={"Authorization": f"Basic {credentials}"})
    assert response.status_code == 200

def test_get_all_conversion():
    credentials = base64.b64encode(b"jace:pwdintanai").decode('utf-8')
    response = app.test_client().get('/conversions', headers={"Authorization": f"Basic {credentials}"})
    assert response.status_code == 200

def test_get_single_conversion_by_id():
    credentials = base64.b64encode(b"jace:pwdintanai").decode('utf-8')
    response = app.test_client().get('/conversions/1', headers={"Authorization": f"Basic {credentials}"})
    res = json.loads(response.data.decode('utf-8'))
    assert response.status_code == 200
    assert type(res[0]) is dict
    assert res[0]['unit1'] == 'Rai'
    assert res[0]['unit2'] == 'Square Meter'
    assert res[0]['ratio'] == 1600

def test_get_single_conversion_by_name():
    credentials = base64.b64encode(b"jace:pwdintanai").decode('utf-8')
    response = app.test_client().get('/conversions/Rai/Square Meter', headers={"Authorization": f"Basic {credentials}"})
    res = json.loads(response.data.decode('utf-8'))
    assert response.status_code == 200
    assert type(res[0]) is dict
    assert res[0]['unit1'] == 'Rai'
    assert res[0]['unit2'] == 'Square Meter'
    assert res[0]['ratio'] == 1600

def test_add_conversion():
    credentials = base64.b64encode(b"jace:pwdintanai").decode('utf-8')
    response = app.test_client().post('/conversions', json = {
        "unit1" : "Square Meter",
        "unit2" : "Square Cent",
        "ratio" : 10000
    }, headers={"Authorization": f"Basic {credentials}"})
    assert response.status_code == 201

def test_update_conversion():
    credentials = base64.b64encode(b"jace:pwdintanai").decode('utf-8')
    response = app.test_client().put('/conversions/2', json = {
        "unit1" : "Square Meter",
        "unit2" : "Square Centimeter",
        "ratio" : 10000
    }, headers={"Authorization": f"Basic {credentials}"})
    assert response.status_code == 200

def test_delete_conversion():
    credentials = base64.b64encode(b"jace:pwdintanai").decode('utf-8')
    response = app.test_client().delete('/conversions/2', headers={"Authorization": f"Basic {credentials}"})
    assert response.status_code == 200

def test_convert_1():
    credentials = base64.b64encode(b"jace:pwdintanai").decode('utf-8')
    response = app.test_client().post('/convert', json = {
        "unit1" : "Rai",
        "unit2" : "Square Meter",
        "value" : 2
    }, headers={"Authorization": f"Basic {credentials}"})
    res = json.loads(response.data.decode('utf-8'))
    assert response.status_code == 200
    assert res['value'] == 3200