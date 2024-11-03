# tests/test_food_delivery_system.py

from food_delivery.food_delivery_system import FoodDeliverySystem
import pytest

def test_display_menu():
    fds = FoodDeliverySystem()
    assert fds.display_menu() == {
        "Burger": 150,
        "Pizza": 250,
        "Pasta": 200,
        "Salad": 120,
        "Beverages": 130,
        "Noodles": 150,
        "Sushi": 270,
        "Bakery": 350
    }

def test_create_order():
    fds = FoodDeliverySystem()
    order = fds.create_order(order_id=1, items={"Burger": 2, "Pizza": 1})
    assert order == {
        "items": {"Burger": 2, "Pizza": 1},
        "total": 550,  # 2 * 150 + 1 * 250
        "status": "Aguardando retirada"
    }
    assert fds.orders[1] == order

def test_create_order_invalid_item():
    fds = FoodDeliverySystem()
    with pytest.raises(ValueError):
        fds.create_order(order_id=2, items={"InvalidItem": 1})

def test_update_order_status():
    fds = FoodDeliverySystem()
    fds.create_order(order_id=1, items={"Burger": 2})
    fds.update_order_status(order_id=1, new_status="Retirado")
    assert fds.orders[1]["status"] == "Retirado"

def test_update_order_status_invalid_order():
    fds = FoodDeliverySystem()
    with pytest.raises(KeyError):
        fds.update_order_status(order_id=99, new_status="Retirado")

# tests/test_food_delivery_system.py

def test_modify_order_items():
    fds = FoodDeliverySystem()
    fds.create_order(order_id=1, items={"Burger": 2})
    fds.modify_order_items(order_id=1, new_items={"Pizza": 1})
    assert fds.orders[1]["items"] == {"Pizza": 1}
    assert fds.orders[1]["total"] == 250  # Pizza: 1 * 250

def test_modify_order_items_after_pickup():
    fds = FoodDeliverySystem()
    fds.create_order(order_id=1, items={"Burger": 2})
    fds.update_order_status(order_id=1, new_status="Retirado")
    with pytest.raises(ValueError):
        fds.modify_order_items(order_id=1, new_items={"Pizza": 1})

def test_cancel_order():
    fds = FoodDeliverySystem()
    fds.create_order(order_id=1, items={"Burger": 2})
    fds.cancel_order(order_id=1)
    assert 1 not in fds.orders

def test_cancel_order_after_pickup():
    fds = FoodDeliverySystem()
    fds.create_order(order_id=1, items={"Burger": 2})
    fds.update_order_status(order_id=1, new_status="Retirado")
    with pytest.raises(ValueError):
        fds.cancel_order(order_id=1)

# tests/test_food_delivery_system.py

def test_generate_invoice_low_total():
    fds = FoodDeliverySystem()
    fds.create_order(order_id=1, items={"Burger": 2})  # Total = 300
    invoice = fds.generate_invoice(order_id=1)
    assert invoice["base_total"] == 300
    assert invoice["tax"] == 15  # 5% de 300
    assert invoice["total_with_tax"] == 315

def test_generate_invoice_high_total():
    fds = FoodDeliverySystem()
    fds.create_order(order_id=2, items={"Pizza": 5})  # Total = 1250
    invoice = fds.generate_invoice(order_id=2)
    assert invoice["base_total"] == 1250
    assert invoice["tax"] == 125  # 10% de 1250
    assert invoice["total_with_tax"] == 1375

def test_generate_invoice_invalid_order():
    fds = FoodDeliverySystem()
    with pytest.raises(KeyError):
        fds.generate_invoice(order_id=99)

