from flask import Flask, request, jsonify
import requests

# GOOGLE_API_KEY = 'AIzaSyAbrlPIb1ltEpKERsbl-2LsiHajiskV7Jk'
GOOGLE_API_KEY = 'AIzaSyDVnZWRCak8VekdhI2Ur3dbPg-5C2cz6eU'

def geocode(address):
    if not address:
        return jsonify({'error': 'Endereço é obrigatório'}), 400

    url = f'https://maps.googleapis.com/maps/api/geocode/json'
    params = {'address': address, 'key': GOOGLE_API_KEY}
    response = requests.get(url, params=params)
    data = response.json()

    if data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']    
        return location
    else:
        return False
