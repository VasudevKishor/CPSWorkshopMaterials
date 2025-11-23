# 03_Data_Structures.py

def main():
    # 1. LISTS: Ordered, mutable, allows duplicates
    cart = ["Apples", "Milk", "Bread", "Apples"] 
    print(f"Original Cart: {cart}")
    
    cart.append("Eggs")       # Add item
    cart.remove("Apples")     # Removes only the first occurrence
    print(f"Updated Cart: {cart}")
    print(f"First Item: {cart[0]}") 

    print("-" * 20)

    # 2. SETS: Unordered, NO duplicates
    tags = {"python", "coding", "python", "computer", "coding"}
    print(f"Unique Tags: {tags}") 

    print("-" * 20)

    # 3. DICTIONARIES: Key-Value pairs
    student = {
        "name": "Vasudev",
        "id": "CSE101",
        "marks": [85, 90, 88]
    }
    
    print(f"Student Name: {student['name']}")
    
    # Dictionary Logic: Calculate average
    avg_mark = sum(student['marks']) / len(student['marks'])
    print(f"Average Score: {avg_mark:.2f}")

if __name__ == "__main__":
    main()
