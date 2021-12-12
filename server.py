from flask import Flask, jsonify, request, abort

app = Flask(__name__,
            static_url_path='',
            static_folder='../')

dogs = [{"id":1, "Breed":"Pug", "Owner":"Michael Smith", "Price":300},
        {"id":2, "Breed":"Labrador", "Owner":"Mary Jones", "Price":500},
        {"id":3, "Breed":"Poodle", "Owner":"Sean Walsh", "Price":200},
        {"id":4, "Breed":"Collie", "Owner":"Jack Kennedy", "Price":350},
]
nextID=4

@app.route('/')
def index():
    return "Hello world"

# get all dogs
@app.route('/dogs')
def getall():
    return jsonify(dogs)

# find dogs by ID
@app.route('/dogs/<int:id>')
def findbyID(id):
    founddogs = list(filter(lambda t : t["id"]== id, dogs))
    if len(founddogs)==0:
        return jsonify({}), 204
    return jsonify(founddogs[0])

# create dog
# curl -X POST -H "content-type:application/json" -d "{\"Breed\":\"Bulldog\", \"Owner\":\"Teresa Daly\", \"Price\":650}" http://127.0.0.1:5000/dogs
@app.route('/dogs', methods = ['POST'])
def create():
    global nextID
    if not request.json:
        abort(400)
    dog = {
        "id": nextID,
        "Breed": request.json["Breed"],
        "Owner": request.json["Owner"],
        "Price": request.json["Price"]
    }
    dogs.append(dog)
    nextID += 1
    return jsonify(dog)
   

# update dog
# curl -X PUT -d "{\"Breed\":\"Rottweiler\", \"Price\":780}" -H "content-type:application/json" http://127.0.0.1:5000/dogs/3
@app.route('/dogs/<int:id>', methods = ['PUT'])
def update(id):
    founddogs = list(filter(lambda t : t["id"]== id, dogs))
    if len(founddogs)==0:
        return jsonify({}), 404
    currentDog = founddogs[0]
    if 'Breed' in request.json:
        currentDog['Breed'] = request.json['Breed']
    if 'Owner' in request.json:
        currentDog['Owner'] = request.json['Owner']
    if 'Price' in request.json:
        currentDog['Price'] = request.json['Price']
    
    return jsonify(currentDog)
    

# delete dog
@app.route('/dogs/<int:id>', methods = ['DELETE']) 
def delete(id):
    founddogs = list(filter(lambda t : t["id"]== id, dogs))
    if len(founddogs)==0:
        return jsonify({}), 404
    dogs.remove(founddogs[0])

    return jsonify({"done": True})


if __name__ == '__main__':
    app.run(debug = True)