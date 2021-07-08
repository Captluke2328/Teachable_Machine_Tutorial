from flask import Flask, render_template, request, redirect, Response
app = Flask(__name__)


@app.route('/', methods=['GET'])
def show_index_html():
    app.logger.warning('testing warning log')
    return render_template('index.html')


#"""Set send data to set the end point"""
#@app.route('/send_data', methods=['POST'])

"""Remove /send_data if only don't want to set the end point"""
@app.route('/', methods=['POST'])
def get_data_from_html():
    data = request.form['object']
    print("Info is " + data)

    """Adding this line allow it only one time execution"""
    #return "Data sent. Please check your program log"

    """Adding this line will allow it continue with the detection"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
