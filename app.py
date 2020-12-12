from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

from google_scrapper import google_scrapper_results, google_scrapper_autocomplete

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def hello():
    return "Hello, it is my app!"


@app.route('/results/')
@cross_origin()
def get_results():
    text = request.args.get('text')
    return jsonify(google_scrapper_results(text))

@app.route('/autocomplete/')
@cross_origin()
def get_autocomplete():
    text = request.args.get('text')
    return jsonify(google_scrapper_autocomplete(text))


if __name__ == '__main__':
    app.run()
