from flask import Blueprint, make_response, request
from server.app import db
from server.models.restaurant import Restaurant
from server.models.restaurant_pizza import RestaurantPizza

restaurant_bp = Blueprint('restaurants', __name__)

@restaurant_bp.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return make_response([r.to_dict() for r in restaurants], 200)

@restaurant_bp.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return make_response({ "error": "Restaurant not found" }, 404)
    data = restaurant.to_dict()
    data['pizzas'] = [rp.pizza.to_dict() for rp in restaurant.restaurant_pizzas]
    return make_response(data, 200)

@restaurant_bp.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return make_response({ "error": "Restaurant not found" }, 404)
    db.session.delete(restaurant)
    db.session.commit()
    return '', 204
