from flask import Blueprint, jsonify

ontological_concepts_bp = Blueprint('ontological_concepts', __name__)

data = {
    "type_2_diabetes": {
        "id": "ICD10:E11",
        "name": "Type 2 diabetes mellitus",
        "associated_conditions": ["obesity", "hypertension", "dyslipidemia"],
        "complications": ["nephropathy", "retinopathy", "neuropathy", "cardiovascular_disease"]
    }
}

@ontological_concepts_bp.route('/')
def get_ontological_concepts():
    return jsonify(data)
