from flask import Blueprint, jsonify
import requests

api = Blueprint('api', __name__)

@api.route('/people', methods=['GET'])
def get_people():
    response = requests.get('https://swapi.dev/api/people/')
    return jsonify(response.json()), response.status_code

@api.route('/people/<int:person_id>', methods=['GET'])
def get_person(person_id):
    response = requests.get(f'https://swapi.dev/api/people/{person_id}/')
    return jsonify(response.json()), response.status_code

@api.route('/planets', methods=['GET'])
def get_planets():
    response = requests.get('https://swapi.dev/api/planets/')
    return jsonify(response.json()), response.status_code

@api.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    response = requests.get(f'https://swapi.dev/api/planets/{planet_id}/')
    return jsonify(response.json()), response.status_code
