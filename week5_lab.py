#week5_lab.py
#Alexander R. Missagia
#Business Domain: Aviation research

product_name = "Aviation Research" # str
status= "pending" # str
quanity = 3 # int
unit_price = 450.00 # float
is_over_limit = unit_price * quanity > 1000 # bool

print(type(product_name), type(status), type(quanity), type(unit_price), type(is_over_limit))

# tax
# total
# requires approval

subtotal = unit_price * quanity
tax = subtotal * 0.07
total = subtotal + tax
requires_approval = total > 1000

print('=== purchase request summary ===')
print(f'Product Name: {product_name}')
print(f'Quantity: {quantity}')
print(f'Subtotal: ${subtotal:.2f}')
print(f'Tax: ${tax:.2f}')
print(f'Total: ${total:.2f}')
print(f'Requires Approval: {new_total > 1000}')

user_qty = int(input('Enter a new quantity: '))
new_total = unit_price * user_qty * 1.07
print(f'New total for {user_qty} units: ${new_total:.2f}')
print(f'New total exceeds limit: {new_total > 1000}')