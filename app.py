from flask import Flask, request, jsonify
from flask_cors import CORS , cross_origin
import joblib
import os

app = Flask(__name__)
CORS(app)

model = joblib.load('export_model.pkl')
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
#        app.run(debug=False, host='0.0.0.0' , port=5000 )




# For Heroku 
if __name__ == '__main__':
    port = int(os.environ.get('PORT' , '5000' ))
    app.run(debug=False, host='0.0.0.0' , port=port )


