def is_safe(items_list: list) -> bool:
    items_tuple = tuple(sorted(items_list))
    
    unsafe_states = {
        ("chicken", "corn"),
        ("chicken", "fox")
    }
    
    if len(items_tuple) == 2 and items_tuple in unsafe_states:
        return False
    
    return True


def chicken_crossing_puzzle():
    river_left = ["chicken", "fox", "corn"]
    river_right = []
    
    print("=" * 80)
    print("CHICKEN-FOX-CORN RIVER CROSSING PUZZLE")
    print("=" * 80)
    print("\nInitial state:")
    print(f"Left: {river_left} -> Right: {river_right}\n")
    
    river_left.remove("chicken")
    river_right.append("chicken")
    print("Step 1: Farmer takes chicken to right")
    print(f"Left: {river_left} -> Right: {river_right}")
    print(f"Safe? {is_safe(river_left) and is_safe(river_right)}\n")
    
    print("Step 2: Farmer returns alone")
    print(f"Left: {river_left} -> Right: {river_right}")
    print(f"Safe? {is_safe(river_left) and is_safe(river_right)}\n")
    
    river_left.remove("fox")
    river_right.append("fox")
    print("Step 3: Farmer takes fox to right")
    print(f"Left: {river_left} -> Right: {river_right}")
    
    river_right.remove("chicken")
    river_left.append("chicken")
    print("Step 4: Farmer brings chicken back to left")
    print(f"Left: {river_left} -> Right: {river_right}")
    print(f"Safe? {is_safe(river_left) and is_safe(river_right)}\n")
    
    river_left.remove("corn")
    river_right.append("corn")
    print("Step 5: Farmer takes corn to right")
    print(f"Left: {river_left} -> Right: {river_right}")
    print(f"Safe? {is_safe(river_left) and is_safe(river_right)}\n")
    
    print("Step 6: Farmer returns alone")
    print(f"Left: {river_left} -> Right: {river_right}")
    print(f"Safe? {is_safe(river_left) and is_safe(river_right)}\n")
    
    river_left.remove("chicken")
    river_right.append("chicken")
    print("Step 7: Farmer takes chicken to right")
    print(f"Left: {river_left} -> Right: {river_right}")
    print(f"Safe? {is_safe(river_left) and is_safe(river_right)}\n")
    
    print("=" * 80)
    if len(river_right) == 3 and len(river_left) == 0:
        print("✓ Successfully transported all items!")
    print("=" * 80)


if __name__ == "__main__":
    chicken_crossing_puzzle()
