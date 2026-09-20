from flask import Flask
from flask_cors import CORS
from configdb import credentials

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://localhost:5173", "http://127.0.0.1:5173"]}})
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config.from_object(credentials)

if __name__ == '__main__':
    app.run(debug=True)