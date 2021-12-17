from flask import Flask, jsonify, request, abort
from dogDao import dogDao

app = Flask(__name__,
            static_url_path='',
            static_folder='staticpages')

@app.route('/')
def index():
    return "Hello world"

# get all dogs
@app.route('/dogs')
def getall():
    return jsonify(dogDao.getAll())

# find dogs by ID
# curl http://127.0.0.1:5000/dogs/123
@app.route('/dogs/<int:ID>')
def findbyID(ID):
    return jsonify(dogDao.findbyID(ID))

# create dog
# curl -X POST -H "content-type:application/json" -d "{\"ID\":125, \"Breed\":\"Bulldog\", \"Ownedby\":\"Teresa Daly\", \"Price\":650}" http://127.0.0.1:5000/dogs
@app.route('/dogs', methods = ['POST'])
def create():
    if not request.json:
        abort(400)
    dog = {
        "ID": request.json['ID'],
        "Breed": request.json["Breed"],
        "Ownedby": request.json["Ownedby"],
        "Price": request.json["Price"]
    }

    return jsonify(dogDao.create(dog))
   

# update dog
# curl -X PUT -d "{\"Breed\":\"Rottweiler\", \"Price\":780}" -H "content-type:application/json" http://127.0.0.1:5000/dogs/3
@app.route('/dogs/<int:ID>', methods = ['PUT'])
def update(ID):
    founddog = dogDao.findbyID(ID)
    if len(founddog)=={}:
        return jsonify({}), 404
    currentDog = founddog
    if 'Breed' in request.json:
        currentDog['Breed'] = request.json['Breed']
    if 'Owner' in request.json:
        currentDog['Ownedby'] = request.json['Ownedby']
    if 'Price' in request.json:
        currentDog['Price'] = request.json['Price']
    dogDao.update(currentDog)
    return jsonify(currentDog)
    

# delete dog
# curl -X DELETE http://127.0.0.1:5000/dogs/1
@app.route('/dogs/<int:ID>', methods = ['DELETE']) 
def delete(ID):
    dogDao.delete(ID)

    return jsonify({"done": True})


if __name__ == '__main__':
    app.run(debug = True)