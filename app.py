#http://127.0.0.1:8000/docs#/default(paste the url in to any web)

#https://openphish.com/(fake website list)


import uvicorn
from fastapi import FastAPI
import joblib,os
import requests

app = FastAPI()

url = 'https://github.com/shivkumarg3/FakeWebsiteDetection/blob/main/phishing.pkl'
response = requests.get(url)

with open('phishing.pkl', 'wb') as f:
    f.write(response.content)


#pkl
phish_model_ls = joblib.load(phishing.pkl)

# ML Aspect
@app.get('/predict/{feature}')
async def predict(features):
	X_predict = []
	X_predict.append(str(features))
	y_Predict = phish_model_ls.predict(X_predict)
	if y_Predict == 'bad':
		result = "This is a Phishing Site(fake website)"
	else:
		result = "This is not a Phishing Site(good website)"

	return (features, result)
if __name__ == '__main__':
	uvicorn.run(app,host="127.0.0.1",port=8000)
