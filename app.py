# food_delivery_app/app.py

from flask import Flask, request, jsonify
from food_delivery.food_delivery_system import FoodDeliverySystem

app = Flask(__name__)
system = FoodDeliverySystem()

@app.route('/menu', methods=['GET'])
def get_menu():
    return jsonify(system.display_menu())

@app.route('/order', methods=['POST'])
def create_order():
    data = request.get_json()
    order_id = data.get("order_id")
    items = data.get("items")
    try:
        order = system.create_order(order_id, items)
        return jsonify(order), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/order/<int:order_id>/status', methods=['PUT'])
def update_order_status(order_id):
    data = request.get_json()
    new_status = data.get("status")
    try:
        system.update_order_status(order_id, new_status)
        return jsonify({"message": "Status atualizado com sucesso"}), 200
    except KeyError:
        return jsonify({"error": "Pedido não encontrado"}), 404

@app.route('/order/<int:order_id>/modify', methods=['PUT'])
def modify_order(order_id):
    data = request.get_json()
    new_items = data.get("items")
    try:
        system.modify_order_items(order_id, new_items)
        return jsonify(system.orders[order_id]), 200
    except KeyError:
        return jsonify({"error": "Pedido não encontrado"}), 404
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/order/<int:order_id>/cancel', methods=['DELETE'])
def cancel_order(order_id):
    try:
        system.cancel_order(order_id)
        return jsonify({"message": "Pedido cancelado com sucesso"}), 200
    except KeyError:
        return jsonify({"error": "Pedido não encontrado"}), 404
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/order/<int:order_id>/invoice', methods=['GET'])
def get_invoice(order_id):
    try:
        invoice = system.generate_invoice(order_id)
        return jsonify(invoice), 200
    except KeyError:
        return jsonify({"error": "Pedido não encontrado"}), 404

@app.route('/')
def home():
    return "Bem-vindo ao Sistema de Entrega de Comida!"

@app.route('/menu', methods=['GET'])
def display_menu():
    menu = {
        "Burger": 150,
        "Pizza": 250,
        "Pasta": 200,
        "Salad": 120,
        "Beverages": 130,
        "Noodles": 150,
        "Sushi": 270,
        "Bakery": 350
    }
    return jsonify(menu)

if __name__ == '__main__':
    app.run(debug=True)
