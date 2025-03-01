import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# USCIS API Base URL
USCIS_API_URL = "https://api-int.uscis.gov/case-status"

@app.route('/check-status', methods=['GET'])
def check_status():
    """
    API Endpoint to check USCIS case status.
    Example usage: /check-status?receipt_number=WAC1234567890
    """
    receipt_number = request.args.get('receipt_number')
    if not receipt_number:
        return jsonify({"error": "Missing receipt number"}), 400
    
    try:
        response = requests.get(f"{USCIS_API_URL}/{receipt_number}")
        data = response.json()
        
        if response.status_code == 200:
            return jsonify({
                "receipt_number": receipt_number,
                "case_status": data.get("status"),
                "processing_center": data.get("processing_center"),
                "last_updated": data.get("last_updated"),
                "message": "Case status retrieved successfully"
            })
        else:
            return jsonify({"error": "Invalid receipt number or USCIS system unavailable"}), 400
    
    except Exception as e:
        return jsonify({"error": "Error fetching case status", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
