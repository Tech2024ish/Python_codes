def coke_machine():
    total_due = 50
    accepted_coins = [25, 10, 5]
    
    while total_due > 0:
        print(f"Amount due: {total_due} cents")
        coin = int(input("Insert coin (25, 10, 5): "))
        if coin in accepted_coins:
            total_due -= coin
        if total_due <= 0:
            break
    
    change = abs(total_due)
    if change > 0:
        print(f"Change owed: {change} cents")
    else:
        print("No change owed")

# Run the coke machine simulation
coke_machine()