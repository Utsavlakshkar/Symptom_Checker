from flask import Flask,render_template,request
import pickle
import joblib
from Model import Symptom_Checker
#print(__name__)
app=Flask(__name__)
#iris=load_iris()
#print(iris.target)
#with open('C:/Users/utsav/VIT/Intenship/Mastek/Symptom Checker/model_symptom_checker.pkl','rb') as file:
#    model = pickle.load(file)
#print(model.diagnose("cough"))
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/input",methods=['POST','GET'])
def input():
    #sc=model.Symptom_Checker()
    return render_template('Symptom_Checker.html')

@app.route("/result",methods=['POST','GET'])
def result():
    #sc=model.Symptom_Checker()
    print("Loading model")
    #model=pickle.load(open("model_symptom_checker.pickle","rb"))    
    print("\nRender template")
    #return render_template("Result.html",diseases=Symptom_Checker.diagnose(request.form.get("symptoms","cough,chills,headache")))
    mj = joblib.load('model_joblib')
    mj.diagnose("cough")
    return render_template('Result.html',symptoms=mj.diagnose("cough"))

if __name__=="__main__":    
    #mj = joblib.load('model_joblib')
    #mj.diagnose("cough")
    app.run(debug=True)
#pyscript.write("output",model.diagnose('cough'),True)