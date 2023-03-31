from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Import and register blueprints for each microservice
from ontological_concepts import ontological_concepts_bp
from genomics import genomics_bp
from events import events_bp
from system_layers import system_layers_bp
from communication_layers import communication_layers_bp
from care_processes import care_processes_bp

app.register_blueprint(ontological_concepts_bp, url_prefix='/ontological_concepts')
app.register_blueprint(genomics_bp, url_prefix='/genomics')
app.register_blueprint(events_bp, url_prefix='/events')
app.register_blueprint(system_layers_bp, url_prefix='/system_layers')
app.register_blueprint(communication_layers_bp, url_prefix='/communication_layers')
app.register_blueprint(care_processes_bp, url_prefix='/care_processes')

if __name__ == '__main__':
    app.run(debug=True)
