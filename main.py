from flask import Flask, jsonify
import json

app = Flask(__name__)

f = open('BooksFourEntries.json', )
data = json.load(f)


@app.route('/search/<string:topic>', methods=['GET'])
def searchByBookTopic(topic):
    displayed = []
    for i in data['books']:
        if i['topic'] == topic:
            displayed.append({'id': i['id'], 'title': i['title']})
    return jsonify(displayed)

@app.route('/info/<id>', methods=['GET'])
def searchByBookId(id):
    for i in data['books']:
        if int(id) == i['id']:
            return jsonify(i)
    f.close()


if __name__ == '__main__':
    app.run(debug=True)
