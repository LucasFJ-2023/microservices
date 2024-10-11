# Product Catalog Service

Dette repository indeholder en Flask-baseret Product Catalog Service, der henter produkter fra et eksternt API og giver funktionalitet til at søge, filtrere og kategorisere produkter.

## Endpoints 

- **GET /products**
    Returnerer en liste over alle produkter.
    
    ```bash
    curl http://localhost:5000/products
    ```

- **GET /products/<id>**
    Returnerer enkelt produkt ud fra produkt-ID. 
    
    ```bash
    curl http://localhost:5000/products/1
    ```

- **GET /products/search?q=<category>**
    Returnerer en liste af produkterne i den søgte kategori. 
    
    ```bash
    curl http://localhost:5000/search?q=beauty
    ```

- **GET /products/filter?min_price=<min>&max_price=<max>**
    Returnerer produkter inden for valgt price range. 

    ```bash
    curl http://localhost:5000/filter?min_price=2&max_price=10
    ```

- **POST /products** 
    Tilføjer et produkt til produkt kataloget. 
    
    ```bash
    curl http://localhost:5000/products
    ```


- **PUT /products/<id>**
    Opdatér produkt, som fx pris
    
    ```bash
    curl http://localhost:5000/products/1
    ```