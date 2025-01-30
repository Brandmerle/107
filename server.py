from flask import Flask, request
import json
from http import HTTPStatus

app = Flask(__name__)  #2 underscores on each side.  __name__ means using the name as the folder name

@app.get("/") #this is the homepage
def home():
    return "Hello from Flask"

# @app.post("/")
# @app.put("/")
# @app.patch("/")


@app.get("/test") # this is the page called test
def test():
    return "this is another endpoint"

#this is a JSON implementation
@app.get("/api/about")
def about():
    name={"name": "Brandon"}
    return json.dumps(name)


products = []

# GET all products
@app.get("/api/products")
def get_products():
    return json.dumps(products), HTTPStatus.OK


#POST a product
@app.post("/api/products")
def save_product():
    product = request.get_json()
    print(f"product {product}")
    products.append(product)
    return "Product saved", 201


#PUT a product
@app.put("/api/products/<int:index>")
def update_product(index):
    updated_product=request.get_json()
    print(f"update the product with the index {index}")

    if 0<= index < len(products):
        products[index] = updated_product
        return json.dumps(updated_product),200
    else:
        return "That index does not exist",404


#DELETE a product
@app.delete("/api/products/<int:index>")
def delete_product(index):
    print(f"delete the product with the index {index}")

    if index >= 0 and index < len(products):
        deleted_product=products.pop(index)
        return json.dumps(deleted_product)
    else:
        return "That index does not exist", HTTPStatus.NOT_FOUND
    
    return "Product deleted"


app.run(debug=True)

