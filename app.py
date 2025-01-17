from frontend import cropSystem

from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def home():
    if request.method=='POST':
        n= request.form.get('Nitrogen')
        p= request.form.get('Phosphorous')
        k= request.form.get('Potassium')
        temp= request.form.get('Temparature')
        h= request.form.get('Humidity')
        ph= request.form.get('pH')
        rf= request.form.get('Rainfall')

        try:
            cropName = cropSystem(n, p, k, temp, h, ph, rf)
            data = {'result': cropName}
            return render_template('result.html', data=data)
        except Exception as e:
            return f"Error: {str(e)}"
        
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True)
