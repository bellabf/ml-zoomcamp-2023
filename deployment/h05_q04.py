import pickle
from flask import Flask, request, jsonify

app = Flask('question_5') # give an identity to your web service


dict_vect=open("dv.bin", 'rb')
dv=pickle.load(dict_vect)
logistic_reg=open("model1.bin", 'rb')
model=pickle.load(logistic_reg)

def predict_single(customer, dv, model):
    X = dv.transform([customer])  ## apply the one-hot encoding feature to the customer data 
    y_pred = model.predict_proba(X)[:, 1]
    return y_pred[0]

@app.route('/predict', methods=['POST'])  ## in order to send the customer information we need to post its data.
def predict():
    customer = request.get_json()  ## web services work best with json frame, So after the user post its data in json format we need to access the body of json.
    prediction = predict_single(customer, dv, model)
    credit = prediction >= 0.5

    result = {
        'credit_probability': float(prediction), ## we need to cast numpy float type to python native float type
        'credit': bool(credit),  ## same as the line above, casting the value using bool method
    }
    
    return jsonify(result)  ## send back the data in json format to the user



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)