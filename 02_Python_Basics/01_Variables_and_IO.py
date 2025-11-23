# 01_Variables_and_IO.py

def main():
    print("--- Welcome to the Age Calculator ---")

    # 1. Input: Getting data from the user (Always comes in as a String)
    name = input("Enter your name: ")
    birth_year_str = input("Enter your year of birth (YYYY): ")

    # 2. Type Casting: Converting String to Integer for math
    birth_year = int(birth_year_str)
    current_year = 2025

    # 3. Logic: Basic Math
    age = current_year - birth_year

    # 4. Output: Using f-strings (formatted strings) for clean output
    print(f"\nHello, {name}!")
    print(f"You are approximately {age} years old.")
    
    # 5. Variable Types check
    print(f"\nDebug Info: Type of 'name' is {type(name)}")
    print(f"Debug Info: Type of 'birth_year' is {type(birth_year)}")

if __name__ == "__main__":
    main()
