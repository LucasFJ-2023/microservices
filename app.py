"""
Product Catalog Service:
Styrer listen over tilgængelige produkter, inklusive detaljer såsom navn, beskrivelse, pris og billeder.
Tilbyder funktionalitet til at søge, filtrere og kategorisere produkter.

"""

from flask import Flask, jsonify, request, make_response # type: ignore
import requests

app = Flask(__name__)

# DATABASE - skal skiftes til sqlite
product_db = []
data = requests.get('https://dummyjson.com/products')
product_db = data.json()['products']




# Get all products
@app.route('/products', methods=['GET'])
def view_product():
    return jsonify(product_db), 200

"""
I postman skrives:
     http://localhost:5000/products
"""




# Get product by id
@app.route('/products/<int:id>', methods=['GET'])
def view_product_by_id(id):
    # Iterer igennem listen af produkter, og finder matchende id
    for product in product_db:
        if product['id'] == id:
            return jsonify(product), 200
        
"""
I postman skrives: 
    http://localhost:5000/products/id
"""



# Search for products by category
@app.route('/products/search', methods=['GET'])
def search_product():
    # Get the query parameter 'q' from the request URL
    category = request.args.get('q')

    # Check if category is provided
    if not category:
        return jsonify({"error": "Category is required"}), 400
    
     # Iterate through product list to find a matching product by category
    matching_products = [product for product in product_db if product['category'].lower() == category.lower()] # lower() tager højde om man kan skrive efter en kategori med store eller små bogstaver

     # If any products match, return them, else return a not found error
    if matching_products:
        return jsonify(matching_products), 200
    else:
        return jsonify({"error": "No products found for the category"}), 404

"""
I postman skrives:
     http://localhost:5000/products/search?q=<kategori>
"""





# Filter and sort products by price
@app.route('/products/filter', methods=['GET'])
def filter_product_by_price():
    # Get min. and max price
    min_price = float(request.args.get('min_price', 0))     #Standard to 0
    max_price = float(request.args.get('max_price', float('inf')))      #Standard to infinity

    # Sort product by price
    sorted_products = sorted(
        (product for product in product_db if min_price <= product['price'] <= max_price),
        key=lambda product: product['price']  
    )
    return jsonify(sorted_products), 200

"""
'Key' fortæller hvilket element i hvert objekt der skal bruges som basis for sortering
'Lambda product:' tager et element fra listen (i dette tilfælde er det et produkt). 'product' er så hvert element i listen 'matching_products'
'product['price']' er hvad funktionen returnerer. I vores tilfælde tager den hvert produkt og kigger på dens pris '(price)' og sorterer ud fra den.

Ved at gøre brug af overstående, undgår vi at skulle definere en seperat funktion til sortering.


I postman skrives: 
    http://localhost:5000/products/filter?min_price=<min>&max_price=<max>
"""





# Add a product
@app.route('/products', methods=['POST'])
def add_new_product():

    new_product = request.get_json()
    new_product['id'] = max([product['id'] for product in product_db]) +1 #Generer et nyt id efter det højeste id-nummer
    product_db.append(new_product)
    return jsonify(new_product), 201

"""
I postman skrives:
     http://localhost:5000/products

- Gå til fanen 'Body' -> vælg 'raw' -> vælg 'JSON' som dataformat
    og indtast produktdata som 'JSON'
"""






# Update product by id
@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    updated_data = request.get_json()

    for product in product_db:
        if product['id'] == id:
            product.update(updated_data)
            return jsonify(product), 200
        
"""
I postman skrives: 
    http://localhost:5000/products/id

- Gå til fanen 'Body' -> vælg 'raw' -> vælg 'JSON' som dataformat
    og indtast produktdata som 'JSON'
"""





app.run(debug=True, host='0.0.0.0')