def collect_items():
    """
    Collects item details (name, price, quantity) from the user
    and stores them in a list of dictionaries.
    """
    items_array = []
    while True:
        name = input("Enter item name (or 'done' to finish): ").strip()
        if name.lower() == 'done':
            break

        try:
            price = float(input(f"Enter price for {name}: "))
            quantity = int(input(f"Enter quantity for {name}: "))
        except ValueError:
            print("Invalid input for price or quantity. Please enter numbers.")
            continue

        item = {"name": name, "price": price, "quantity": quantity}
        items_array.append(item)
        print(f"'{name}' added.")

    return items_array

if __name__ == "__main__":
    collected_items = collect_items()

    if len(collected_items) >= 2:
        print("\nArray of collected items:")
        for item in collected_items:
            print(item)
    elif len(collected_items) == 1:
        print("\nOnly one item was entered:")
        print(collected_items[0])
    else:
        print("\nNo items were entered.")
