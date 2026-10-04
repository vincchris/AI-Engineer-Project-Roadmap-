stocks = []

while True:
  print("""
    1. Add Product
    2. Show Products
    3. Search Product
    4. Update Stock
    5. Delete Product
    6. Exit
""")

  user_input = str(input("Choice : "))

  if user_input == "1":
    print("== Add Product ==")
    