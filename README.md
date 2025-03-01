# USCIS Case Status API

This is a **Flask-based API** that connects to the **USCIS Case Status API** to fetch real-time immigration case updates.

## 🚀 Features:
- ✅ Retrieve **USCIS case status** by entering a **receipt number**.
- ✅ Returns **case status, processing center, and last updated date**.
- ✅ Built using **Flask** and **Requests**.

## 🔹 How to Use:
Check case status via API request:
GET /check-status?receipt_number=WAC1234567890
Replace `WAC1234567890` with your USCIS receipt number.

## 📌 Deployment:
- Hosted on **Render.com** (or AWS for scalability).
- Uses `gunicorn` to serve requests.

## 👩‍💻 Setup for Local Development:
```sh
pip install flask requests
python uscis_api_integration.py
