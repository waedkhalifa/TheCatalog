from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route('/search/<string:topic>', methods=['GET'])
def searchByBookTopic(topic):
    displayed = []

    f = open('FourEntries.json', )
    data = json.load(f)

    for i in data['books']:
        if i['topic'] == topic:
            displayed.append({'id': i['id'], 'title': i['title']})

    f.close()

    return jsonify(displayed)


@app.route('/info/<int:id>', methods=['GET'])
def searchByBookId(id):
    displayed = []

    f = open('FourEntries.json', )
    data = json.load(f)

    for i in data['books']:
        if int(id) == i['id']:
            displayed.append({'title': i['title'], 'quantity': i['quantity'], 'price': i['price']})
            f.close()
            return jsonify(displayed)




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=7000)
