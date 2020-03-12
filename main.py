from flask import Flask, request, jsonify
from src.models import product  # call model file
from flask_cors import CORS  # avoid cors errors if called from frontend

app = Flask(__name__)
CORS(app)

product = product.Product()


# product routes
@app.route('/products-retail/', methods=['GET'])
def get_tasks():
    return jsonify(product.find({})), 200


@app.route('/products-retail/<string:product_id>/', methods=['GET'])
def get_task(product_id):
    return product.find_by_id(product_id), 200


@app.route('/products-retail', methods=['POST'])
def add_tasks():
    if request.method == "POST":
       product_id = request.json['product_id']
       current_price = request.json['current_price']
       currency_code = request.json['currency_code']
       created_by = request.json['created_by']
       updated_by = request.json['updated_by']
       
       response = product.create({'product_id': product_id, 
                                  'current_price':current_price, 
                                  'currency_code': currency_code, 
                                  'created_by': created_by, 
                                  'updated_by': updated_by})
       return response, 201


@app.route('/products-retail/<string:product_id>', methods=['PUT'])
def update_tasks(product_id):
    if request.method == "PUT":
        product_id = request.json['product_id']
        current_price = request.json['current_price']
        currency_code = request.json['currency_code']
        updated_by = request.json['updated_by']
        response = product.update(product_id, {'product_id': product_id, 
                                                'current_price': current_price,
                                                'currency_code':currency_code,
                                                'updated_by':updated_by})
        return response, 201


@app.route('/products-retail/<string:product_id>', methods=['DELETE'])
def delete_tasks(product_id):
    if request.method == "DELETE":
        product.delete(product_id)
        return "Record Deleted"


if __name__ == '__main__':
    app.run(port=5002,debug=True)
