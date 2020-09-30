from flask import Flask, request,render_template
import numpy as np
import pickle
import pandas as pd

app=Flask(__name__)

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "<h1>Welcome All</h1>"

@app.route('/predict',methods=["GET",'POST'])
def predict_note_authentication():
	s,a,b,c,d='','','','',''
	if(request.method=='POST'):
		variance=request.form.get("variance")
		skewness=request.form.get("skewness")
		curtosis=request.form.get("curtosis")
		entropy=request.form.get("entropy")
		prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
		q='YES' if prediction[0]==1 else 'NO'
		a,b,c,d=variance,skewness,curtosis,entropy
		s=f"Hello The answer is {q}"
	return render_template("data.html",data=s,a=a,b=b,c=c,d=d)

if __name__=='__main__':
    app.run(debug=True)
