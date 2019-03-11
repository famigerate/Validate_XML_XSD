#!flask/bin/python
from flask import Flask, jsonify,request
import ValidationXSD_XML

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/validate', methods=['GET'])
def index():
    xml_path = request.args.get('xml', type=str)
    xsd_path = request.args.get('xsd', type=str)
    validObj = ValidationXSD_XML.Validation(xsd_path, xml_path)
    return jsonify(validObj.validate())


if __name__ == '__main__':
    app.run()
