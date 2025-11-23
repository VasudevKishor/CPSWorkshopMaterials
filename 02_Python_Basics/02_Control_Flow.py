# 02_Control_Flow.py

def check_grade(score):
    # SELECTION: Making decisions
    if score >= 90:
        return "A - Excellent"
    elif score >= 80:
        return "B - Good"
    elif score >= 50:
        return "C - Pass"
    else:
        return "F - Fail"

def main():
    print("--- Grade Checker System ---")
    
    # REPETITION: While loop runs until a condition is false
    while True:
        user_input = input("\nEnter student score (or type 'exit' to stop): ")
        
        if user_input.lower() == 'exit':
            print("Exiting program...")
            break # Breaks out of the loop
            
        # Error Handling: What if they type "fifty" instead of 50?
        try:
            score = int(user_input)
            if 0 <= score <= 100:
                result = check_grade(score)
                print(f"Grade: {result}")
            else:
                print("Error: Please enter a number between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    main()
