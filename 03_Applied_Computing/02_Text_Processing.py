# 02_Text_Processing.py

def main():
    raw_text = "   Hello Python World!  This is CSE101.   "
    print(f"Original: '{raw_text}'")

    # 1. Strip & Lower
    clean_text = raw_text.strip().lower()
    print(f"Cleaned:  '{clean_text}'")

    # 2. Word Frequency Counter
    sentence = "python is great and python is easy"
    word_list = sentence.split()
    frequency = {}

    for word in word_list:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
            
    print(f"\nWord Frequency in '{sentence}':")
    print(frequency)

if __name__ == "__main__":
    main()
