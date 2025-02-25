def count_words(text):
    """
    Function to count the number of words in a given text.
    - Splits the text by whitespace and filters out empty strings.
    - Returns the total word count.
    """
    words = text.split()
    return len(words)

def main():
    """
    Main function to handle user input, process the text, and display the word count.
    """
    print("Welcome to the Word Counter Program!")
    print("------------------------------------")
    user_input = input("Please enter a sentence or paragraph: ").strip()
    if not user_input:
        print("Error: Input cannot be empty. Please try again.")
        return
    word_count = count_words(user_input)
    print(f"\nThe number of words in your input is: {word_count}")
if __name__ == "__main__":
    main()