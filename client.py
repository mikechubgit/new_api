import json
import requests


user_input = {"age": 24, "job": "admin.", "marital": "single", "education": "university.degree", "default": "no", "housing": "no", "loan": "no", "contact": "cellular", "month": "aug", "day_of_week": "fri", "campaign": 1, "pdays": 999, "previous": 2, "poutcome": "failure", "emp.var.rate": -1.7, "cons.price.idx": 94.027, "cons.conf.idx": -38.3, "euribor3m": 0.905, "nr.employed": 4991.6}


resp = requests.post('http://web-production-b234e.up.railway.app:8000/')

print(resp.status_code)
	
	
	
if resp.status_code == 200:
	result = resp.json()
	print(result)


