from flask import Blueprint, jsonify

genomics_bp = Blueprint('genomics', __name__)

data = {
    "type_2_diabetes": {
        "genes": ["TCF7L2", "SLC30A8", "CDKAL1"],
        "variants": [
            {"gene": "TCF7L2", "rsID": "rs7903146", "risk_allele": "T"},
            {"gene": "SLC30A8", "rsID": "rs13266634", "risk_allele": "C"},
            {"gene": "CDKAL1", "rsID": "rs7756992", "risk_allele": "A"}
        ]
    }
}

@genomics_bp.route('/')
def get_genomics():
    return jsonify(data)
