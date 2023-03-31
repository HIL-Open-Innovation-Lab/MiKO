from flask import Blueprint, jsonify

events_bp = Blueprint('events', __name__)

data = {
    "type_2_diabetes": {
        "diagnosis": ["FPG", "2hPG", "HbA1c"],
        "monitoring": ["self-monitoring blood glucose", "HbA1c", "lipid_profile"],
        "treatments": ["metformin", "sulfonylureas", "GLP-1 receptor agonists", "lifestyle_modifications"]
    }
}

@events_bp.route('/')
def get_events():
    return jsonify(data)
