from django.shortcuts import render
import pickle

import string

loaded_model = pickle.load(open("./model/tn_model.pkl", "rb"))


def SentimentPredictor(s):
    
    preds = loaded_model.predict([s])
    return preds


def index(request):
    return render(request,'form.html')



def result(request):
	if request.method=='POST':
		s=request.POST.get('txt')
		#print(s)
		if SentimentPredictor(s)== -1:
			prediction ='Hassen mant9ek meyjich hakka'
		else:
			prediction ='Sa7it ya metrobi'    
		return render(request,'result.html',{'prediction':prediction})

