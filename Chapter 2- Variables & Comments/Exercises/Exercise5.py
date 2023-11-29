def calculate_usb_sticks(budget, usb_price):
    num_usb_sticks = budget // usb_price
    
    remaining_pounds = budget % usb_price
    
    return num_usb_sticks, remaining_pounds

budget = 50
usb_price = 6

num_sticks, remaining = calculate_usb_sticks(budget, usb_price)

print(f"She can buy {num_sticks} USB sticks and will have £{remaining} left.")
