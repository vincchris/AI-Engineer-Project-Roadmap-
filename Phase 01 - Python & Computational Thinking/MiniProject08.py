stocks = []
product = []

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

    add_products = str(input("Product : ").strip())
    stock = int(input("Initial Stock : "))

    products = {
      "Product": add_products,
      "Stock": stock
    }
    product.append(products)
    print("Successfully Add Product")

  elif user_input == "2":
    print("== Show Products ==")
    if not products:
      print("There isn't Product")
    else:
      for idx, item in enumerate(product, 1):
        print(f"[{idx}] {item['Product']} | Stock: {item['Stock']}")

  elif user_input == "3":
    print("== Search Product ==")
    search_product = str(input("Search Product : ").strip().lower())
    found = False

    for item in product:
      if search_product in item['Product'].lower():
        print(f"Product : {item['Product']}")
        print(f"Stock : {item['Stock']}")
        found = True
        break

    if not found:
      print("There isn't Product")

  elif user_input == "4":
    target_product = input("Enter Product Name to Update : ").strip().lower()
    found = False

    for item in product:
      if item['Product'].lower() == target_product:
        add_stock = int(input(f"Current Stock is {item['Stock']}. Add Stock Amount : "))
        item['Stock'] += add_stock  # Update stok di dalam dictionary
        print(f"Updated! {item['Product']} now has {item['Stock']} stock.")
        found = True
        break

      if not found:
        print("Product not found.")

  elif user_input == "5":
    print("== Delete Product ==")
    delete_input = input("Enter a Delete Name : ").lower().strip()
    found = False

    for item in product:
      if item['Product'].lower() == delete_input:
        product.remove(item)
        print(f"Product '{item['Product']}' delete successfully!")
        found = True
        break

    if not found:
      print("There isn't Product")

  elif user_input == "6":
    print("Goodbye!")
    break

  else:
    print("Chooice the valid Input")