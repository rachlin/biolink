from flask import Flask, jsonify, request
from flask_cors import CORS
import simplejson
import json

from dao import EntityDao

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
        dao = EntityDao("Gene")
    elif node == "disease":
        dao = EntityDao("Disease")
    else:
        return jsonify({})
    
    return jsonify(dao.getEntities(page))


@app.route('/<node>/<nodeName>', methods=['GET'])
def getNodeDetails(node, nodeName):
    if node == "gene":
        dao = EntityDao("Gene")
    elif node == "disease":
        dao = EntityDao("Disease")
    else:
        return jsonify({})

    return jsonify(dao.getEntityInfo(nodeName))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)