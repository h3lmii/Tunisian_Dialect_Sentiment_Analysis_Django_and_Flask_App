from flask import Flask,render_template,request
import pickle
import string
from  fun import text_process
loaded_model = pickle.load(open("tn_model.pkl", "rb"))

def SentimentPredictor(s):
    
    preds = loaded_model.predict([s])
    return preds




app = Flask(__name__)


@app.route('/',)
def index():
    return render_template("form.html") 


@app.route('/result', methods = ['POST'])
def result():
    if request.method == 'POST':
        s = request.form.to_dict()
        print(s)
        if SentimentPredictor(s['txt'])[0]== -1:
                prediction ='Hassen mant9ek ya khraaa'
        else:
                prediction ='Sa7it ya metrobi'    
        return render_template("result.html", prediction = prediction)

app.run(debug=True)