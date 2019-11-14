from flask import Flask, jsonify, request
from flask_cors import CORS
import simplejson
import json

from dao import GeneDao, DiseaseDao

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    info = {}
    return jsonify(info)


@app.route('/<node>', methods=['GET'])
def getNodes(node):
    import sys
    print('Hello world!', file=sys.stderr)
    page = 0
    if "page" in request.args:
        page = int(request.args.get("page"))

    if node == "gene":
        gd = GeneDao()
        return jsonify(gd.getGenes(page))
    elif node == "disease":
        dd = DiseaseDao()
        return jsonify(dd.getDiseases(page))
    else:
        return jsonify({})


@app.route('/<node>/<nodeName>', methods=['GET'])
def getNodeDetails(node, nodeName):
    if node == "gene":
        gd = GeneDao()
        return jsonify(gd.getGeneInfo(nodeName))

    elif node == "disease":
        dd = DiseaseDao()
        return jsonify(dd.getDiseaseInfo(nodeName))

    else:
        return jsonify({})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)