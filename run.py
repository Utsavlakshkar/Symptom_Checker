from flask import Flask,request,jsonify,render_template,url_for
import pickle
import pyscript
app=Flask(__name__)
model=pickle.load(open("model_symptom_checker.pkl","rb"))
@app.route('/result',methods=['GET'])
def result():
    sc=model.Symptom_Checker()
pyscript.write("output",model.Symptom_Checker(),True)