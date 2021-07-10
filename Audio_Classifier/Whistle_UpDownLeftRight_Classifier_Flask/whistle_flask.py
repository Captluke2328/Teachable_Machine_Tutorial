from flask import  Flask, render_template, request, redirect, Response
app = Flask(__name__)

@app.route('/', methods=['GET'])
def show_index_html():
    app.logger.info('Load the html...')
    return render_template('index.html')

# Send data to set the end point
@app.route('/', methods=['POST'])
def get_data_from_html():
    data = request.form['audio']
    print("Audio command is " + data)

    #return "Data Sent..."
    return render_template('index.html')

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()