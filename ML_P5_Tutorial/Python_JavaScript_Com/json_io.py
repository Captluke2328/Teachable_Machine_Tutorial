from flask import Flask, render_template, request, redirect, Response
app = Flask(__name__)
import sys

@app.route('/', methods=['GET', 'POST'])
def gfg():
    if request.method == 'POST':
        first_name = request.form.get('fname')
        last_name = request.form.get('lname')
        
        return "Your Name is " + first_name + last_name
    return render_template('index.html')
   
def main():
    app.run(debug=True, port=12345)

if __name__ == '__main__':
    main()
