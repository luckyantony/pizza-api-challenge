# Pizza Restaurant API

A simple RESTful API for managing pizza restaurants built with Flask. No frontend — test using Postman.

## Project Structure

pizza-api-challenge/
├── server/
│   ├── app.py
│   ├── config.py
│   ├── seed.py
│   ├── models/
│   │   ├── restaurant.py
│   │   ├── pizza.py
│   │   └── restaurant_pizza.py
│   └── controllers/
│       ├── restaurant_controller.py
│       ├── pizza_controller.py
│       └── restaurant_pizza_controller.py
├── migrations/
└── README.md

## Setup Instructions

1. Clone the repository
2. Create virtual environment and install dependencies:

pipenv install flask flask_sqlalchemy flask_migrate
pipenv shell

3. Run migration and create the database:

export FLASK_APP=server/app.py
flask db init
flask db migrate -m "initial"
flask db upgrade

4. Seed the database:

python server/seed.py

5. Run the server:

flask run

## Models

Restaurant:
- id: integer, primary key
- name: string
- address: string
- has many RestaurantPizzas

Pizza:
- id: integer, primary key
- name: string
- ingredients: string
- has many RestaurantPizzas

RestaurantPizza:
- id: integer, primary key
- price: integer (must be between 1 and 30)
- restaurant_id: FK
- pizza_id: FK
- belongs to Restaurant and Pizza

## API Routes

GET /restaurants  
Returns list of all restaurants.

Example Response:
[
  { "id": 1, "name": "Domino's", "address": "123 Pizza St" }
]

GET /restaurants/<id>  
Returns one restaurant with its pizzas.

Success Response:
{
  "id": 1,
  "name": "Domino's",
  "address": "123 Pizza St",
  "pizzas": [
    {
      "id": 1,
      "name": "Margherita",
      "ingredients": "Dough, Tomato Sauce, Cheese"
    }
  ]
}

Error Response:
{ "error": "Restaurant not found" }

DELETE /restaurants/<id>  
Deletes restaurant and related records.

Success: 204 No Content  
Error: { "error": "Restaurant not found" }

GET /pizzas  
Returns list of all pizzas.

Example Response:
[
  {
    "id": 1,
    "name": "Margherita",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  }
]

POST /restaurant_pizzas  
Creates a new RestaurantPizza.

Request:
{
  "price": 10,
  "pizza_id": 1,
  "restaurant_id": 1
}

Success Response:
{
  "id": 1,
  "price": 10,
  "pizza_id": 1,
  "restaurant_id": 1,
  "pizza": {
    "id": 1,
    "name": "Margherita",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  },
  "restaurant": {
    "id": 1,
    "name": "Domino's",
    "address": "123 Pizza St"
  }
}

Validation Error:
{ "errors": ["Price must be between 1 and 30"] }

## Postman Testing

1. Open Postman
2. Click Import
3. Upload: challenge-1-pizzas.postman_collection.json
4. Test each route using GET, POST, DELETE

Built with 💻, ❤️ and ☕ by Luckyantony Leshan
