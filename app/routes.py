from flask import Blueprint, jsonify

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask App!"})

@main_blueprint.route('/health')
def health():
    return jsonify({"status": "OK"})
