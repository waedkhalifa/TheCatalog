from flask import Flask, jsonify, request
import json
import requests
app = Flask(__name__)


@app.route('/search/<string:topic>', methods=['GET'])
def searchByBookTopic(topic):
    displayed = []

    f = open('FourEntries.json', )
    data = json.load(f)

    for i in data['books']:
        if i['topic'] == topic:
            displayed.append({'id': i['id'],'price':i['price'],'quantity': i['quantity'],'title': i['title'],'tpoic':i['topic']})
    f.close()

    if len(displayed) == 0:
        return '404 ERROR, NOT FOUND', 404
    else:
        print('dddddoneeee')
        return jsonify(displayed)


@app.route('/info/<int:id>', methods=['GET'])
def searchByBookId(id):
    displayed = []

    f = open('FourEntries.json', )
    data = json.load(f)

    for i in data['books']:
        if int(id) == i['id']:
            f.close()
            return jsonify(i)
    f.close()
    return '404 ERROR, NOT FOUND', 404


@app.route('/updateinfo/<int:id>', methods=['PUT'])
def updateQuantity(id):
    update_req = request.get_json()
    displayed = []
    arr=[]
    f = open('FourEntries.json', )
    data = json.load(f)

    key_to_update = update_req['quantity']  # quantity


    for i in data['books']:
        if int(id) == i['id']:
            if key_to_update < 0:
                f.close()
                return 'NOT ACCEPTABLE', 406

            else:
                m=i['quantity']
                print(m)
                i['quantity'] = key_to_update
                displayed.append({'id': i['id'], 'price': i['price'], 'quantity': i['quantity'], 'title': i['title'],'topic': i['topic']})

                requests.put('http://192.168.56.104:7777/update/{}'.formate(id),json=(key_to_update))
                requests.post('http://192.168.56.102:6000/invalidate', json=(displayed))
    f.close()

    FEfile = open("FourEntries.json", "w")
    json.dump(data, FEfile)
    FEfile.close()

    return jsonify(displayed)
@app.route('/update/<int:id>',methods=['PUT'])
def update2(id):
    update_req =request.get_json()
    f=open('FourEntries.json','r')
    data=json.load(f)
    for i in  data['books']:
        if int(id) == i['id']:
            i['quantity'] = update_req
            
    f.close()
    FEfile = open("FourEntries.json", "w")
    json.dump(data, FEfile)
    FEfile.close()
    return ''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=7000)
