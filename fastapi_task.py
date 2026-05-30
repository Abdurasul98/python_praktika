# from fastapi import FastAPI, Path
# from typing import Optional
# from pydantic import BaseModel

# app = FastAPI()

# orders = {
#     1:{
#         "product_name":"Malina",
#         "price":4,
#         "quantity":10,
#         "is_paid":True
#     },
#     2:{
#         "product_name":"Telefon",
#         "price":7,              
#         "quantity":7,
#         "is_paid":False
#     },
#     3:{
#         "product_name":"Non",
#         "price":100,
#         "quantity":1,
#         "is_paid":True
#     }
# }

# class Product(BaseModel):
#     product_name: str 
#     price: float 
#     quantity: int 
#     is_paid: bool



# @app.get("/orders/{order_id}")
# def get_order(
#     order_id: int = Path(...),
#     min_price: Optional[float] = None,
#     only_paid: Optional[bool] = False,
#     short: Optional[bool] = False
# ): 
#     if order_id not in orders:
#         return {"message": "Order not found"} 
    
#     order = orders[order_id]


#     if min_price is not None:  
#         if order["price"] < min_price:
#             return {"message": "Price is too low"}
        
#     if only_paid:
#         if not order["is_paid"]:
#             return {"message": "Order not paid"}
        

#     if short:
#         return {
#           "product_name": order["product_name"],
#           "price": order["price"]
#         }
    
#     return order

