sentence = input("Enter a sentence: ")

while True:
    print("\nChoose an Operation:")
    print("1. Reverse the Sentence")
    print("2. Count vowels")
    print("3. Check if palindrome")
    print("4. Find and replace a word")
    print("5. Format title case")
    print("6. Split into words")
    print("7. Word Frequency counter")
    print("8. Swap Case")
    print("9. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        print("Reversed:", sentence[::-1])
    elif choice == "2":
        vowels = "aeiouAEIOU"
        count = sum(1 for ch in sentence if ch in vowels)
        print("Number of vowels:", count)
    elif choice == "3":
        cleaned = "".join(ch.lower() for ch in sentence if ch.isalnum())
        if cleaned == cleaned[::-1]:
            print("It is a palindrome!")
        else:
            print("Not a palindrome.")
    elif choice == "4":
        old = input("Enter the word to find: ")
        new = input("Enter the word to replace with: ")
        sentence = sentence.replace(old, new)
        print("Updated sentence:", sentence)
    elif choice == "5":
        print("Title Case:", sentence.title())
    elif choice == "6":
        print("Words:", sentence.split())
    elif choice == "7":
        words = sentence.lower().split()
        freq = {}
        for word in words:
            freq[word] = freq.get(word, 0) + 1
        print("Word Frequency:")
        for word, count in freq.items():
            print(f"{word}: {count}")
    elif choice == "8":
        print("Swap Case:", sentence.swapcase())

    elif choice == "9":
        print("Exiting program... Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
