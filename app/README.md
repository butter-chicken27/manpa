# Steps to run in local
- pip install -r requirements.txt
- python -m uvicorn main:app --ssl-keyfile=../certs/key.pem --ssl-certfile=../certs/cert.pem --reload --port=5000
Note: remove SSL certificate ops if running on http