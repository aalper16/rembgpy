from flask import Flask, render_template, request, redirect, send_file
from rembg import remove 
import os
import random
from io import BytesIO

app = Flask(__name__)   
  
@app.route('/')   
def main():   
    return render_template("anasayfa.html")   

@app.route('/upload')
def upload():
    return render_template('yukle.html')
  
@app.route('/basarili', methods=['POST'])
def basarili():
    if request.method == 'POST':
        file = request.files['file']
        input_data = file.read()

        output_data = remove(input_data)
        fname = random.randint(0, 9999999)
        output_path = str(fname)+'.png'


        return send_file(BytesIO(output_data), download_name=output_path)

  
if __name__ == '__main__':  
    app.run(debug=True) 