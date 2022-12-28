from flask import Flask,request, render_template
import pickle
import numpy as np
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

Fmodel=pickle.load(open('TEKmodel.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template("TEKhackathon page.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    prediction=Fmodel.predict(final)
    output='{0:.{1}f}'.format(prediction[0][1], 2)

    if output>str(0.5):
        return render_template('TEKhackathon page.html',pred='Customer will Discontinue the subscription')
    else:
        return render_template('TEKhackathon page.html',pred='Customer will Continue the subscription')


if __name__ == '__main__':
    #app.run(debug=True)
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()