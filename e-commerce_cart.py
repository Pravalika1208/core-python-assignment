def calculate(cart):
    total=sum(cart.values())
    if len(cart)>5:
        total*=0.9
    return total
cart={'lap':50000,'headphones':2000,'mouse':3500,'key':1500,'monitor':8000,'usb':1000}
print(f"cart items:{cart}")
print(f"total price:{calculate(cart)}")