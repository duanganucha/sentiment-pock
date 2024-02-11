from flask import Flask, request, jsonify
from flask_cors import CORS , cross_origin
import joblib
import os
import requests


app = Flask(__name__)
CORS(app)


model_url = "https://firebasestorage.googleapis.com/v0/b/test-e33fb.appspot.com/o/model-sentiment%2Fexport_model.pkl?alt=media&token=3231478c-8075-48d4-9cfa-3668a04127c3"
model_path = 'export_model.pkl'
if not os.path.exists(model_path):
    print("Downloading model...")
    response = requests.get(model_url)
    with open(model_path, 'wb') as f:
        f.write(response.content)

model = joblib.load(model_path)
# model = joblib.load('export_model.pkl')
vectorizer = joblib.load('export_vectorizer.pkl')


@app.route('/', methods=['GET'])
def get():
    return "server is running...."

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data['text']
    text_vectorized = vectorizer.transform([text])
    prediction = model.predict(text_vectorized)
    prediction_list = prediction.tolist()
    return jsonify({'prediction': prediction_list})


#  For Build Docker AND Run ปกติ
# gunicorn --bind 0.0.0.0 wsgi:app       
# if __name__ == '__main__':
#        app.run(debug=False, host='0.0.0.0' , port=6000 )




# For Heroku 
if __name__ == '__main__':
    port = int(os.environ.get('PORT' , '5000' ))
    app.run(debug=False, host='0.0.0.0' , port=port )


