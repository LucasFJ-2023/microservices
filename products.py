
import sqlite3

# Function to create the products table
def create_product_table():
    with sqlite3.connect('products.db') as conn:
        cur = conn.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            title TEXT,
            description TEXT,
            price REAL,
            images TEXT,
            category TEXT,
            stock INTEGER
        )""")
        conn.commit()

# Call the function to create the table
create_product_table()




def insert_sample_products(products):
    with sqlite3.connect('products.db') as conn:
        cur = conn.cursor()
        for product in products:
            cur.execute('''INSERT INTO products 
                        (id, 
                        title, 
                        description, 
                        price, 
                        images, 
                        category, 
                        stock)
                           VALUES (?, ?, ?, ?, ?, ?, ?)''', 
                        (product['id'], product['title'], product['description'], product['price'],
                         ','.join(product['images']), product['category'], product['stock']))
        conn.commit()

