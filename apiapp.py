from fastapi import FastAPI

app = FastAPI()

# Data produk dengan lebih banyak atribut
products = [
    {
        "id": 1,
        "name": "iPhone 14",
        "price": "1200 USD",
        "category": "Smartphone",
        "description": "The latest iPhone with advanced features.",
        "stock": 50
    },
    {
        "id": 2,
        "name": "Samsung Galaxy S22",
        "price": "1100 USD",
        "category": "Smartphone",
        "description": "Premium smartphone with an excellent camera.",
        "stock": 30
    },
    {
        "id": 3,
        "name": "MacBook Pro",
        "price": "2500 USD",
        "category": "Laptop",
        "description": "Powerful laptop for professionals and creatives.",
        "stock": 20
    },
    {
        "id": 4,
        "name": "Sony WH-1000XM4 Headphones",
        "price": "350 USD",
        "category": "Headphones",
        "description": "Noise-canceling headphones with great sound quality.",
        "stock": 100
    },
    {
        "id": 5,
        "name": "Apple Watch Series 7",
        "price": "400 USD",
        "category": "Smartwatch",
        "description": "The ultimate smartwatch with health features.",
        "stock": 60
    },
    {
        "id": 6,
        "name": "Dell XPS 13",
        "price": "1400 USD",
        "category": "Laptop",
        "description": "Compact and powerful ultrabook.",
        "stock": 25
    },
    {
        "id": 7,
        "name": "Bose QuietComfort 35 II",
        "price": "300 USD",
        "category": "Headphones",
        "description": "Comfortable noise-canceling headphones.",
        "stock": 80
    },
    {
        "id": 8,
        "name": "Google Pixel 6",
        "price": "600 USD",
        "category": "Smartphone",
        "description": "A smartphone with a fantastic camera.",
        "stock": 40
    },
    {
        "id": 9,
        "name": "iPad Pro 11",
        "price": "800 USD",
        "category": "Tablet",
        "description": "Powerful tablet with M1 chip.",
        "stock": 15
    },
    {
        "id": 10,
        "name": "Fitbit Charge 5",
        "price": "180 USD",
        "category": "Fitness Tracker",
        "description": "Advanced fitness tracker with health features.",
        "stock": 75
    }
]

@app.get("/products")
def get_products():
    return products
