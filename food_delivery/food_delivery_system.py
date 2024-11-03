# food_delivery/food_delivery_system.py

class FoodDeliverySystem:
    def __init__(self):
        self.orders = {}

    def display_menu(self):
        return {
            "Burger": 150,
            "Pizza": 250,
            "Pasta": 200,
            "Salad": 120,
            "Beverages": 130,
            "Noodles": 150,
            "Sushi": 270,
            "Bakery": 350
        }
    
    def create_order(self, order_id, items):
        menu = self.display_menu()
        total = 0
        for item, quantity in items.items():
            if item in menu:
                total += menu[item] * quantity
            else:
                raise ValueError(f"Item {item} não está no menu")
        self.orders[order_id] = {
            "items": items,
            "total": total,
            "status": "Aguardando retirada"
        }
        return self.orders[order_id]
    
    def update_order_status(self, order_id, new_status):
        if order_id in self.orders:
            self.orders[order_id]["status"] = new_status
        else:
            raise KeyError(f"Pedido {order_id} não encontrado")

    def modify_order_items(self, order_id, new_items):
        if order_id in self.orders:
            if self.orders[order_id]["status"] == "Aguardando retirada":
                menu = self.display_menu()
                total = 0
                for item, quantity in new_items.items():
                    if item in menu:
                        total += menu[item] * quantity
                    else:
                        raise ValueError(f"Item {item} não está no menu")
                self.orders[order_id]["items"] = new_items
                self.orders[order_id]["total"] = total
            else:
                raise ValueError("Itens do pedido não podem ser modificados após a retirada")
        else:
            raise KeyError(f"Pedido {order_id} não encontrado")
        
    def cancel_order(self, order_id):
        if order_id in self.orders:
            if self.orders[order_id]["status"] == "Aguardando retirada":
                del self.orders[order_id]
            else:
                raise ValueError("Pedido não pode ser cancelado após a retirada")
        else:
            raise KeyError(f"Pedido {order_id} não encontrado")
        
    def generate_invoice(self, order_id):
        if order_id in self.orders:
            base_total = self.orders[order_id]["total"]
            if base_total > 1000:
                tax = base_total * 0.10
            else:
                tax = base_total * 0.05
            total_with_tax = base_total + tax
            return {"base_total": base_total, "tax": tax, "total_with_tax": total_with_tax}
        else:
            raise KeyError(f"Pedido {order_id} não encontrado")