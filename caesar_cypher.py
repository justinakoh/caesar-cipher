# This is a script to translate into and out of the caesar cypher. This is a simple subsitution cypher which involves substituting each letter in the message you want to be encoded, by substituting each letter by a specific number across
def main():
    print(
        "Welcome to the Caesar Cipher Encoder/Decoder! Please enter the letter you know"
    )
    letter_one = input()
    final_array = []
    if letter_one.isalpha():
        print(
            "Now please enter the letter that you would like to replace the letter with:"
        )
        replacement_letter = input()
        if replacement_letter.isalpha():
            spaces_to_shift = abs(ord(letter_one) - ord(replacement_letter))
            # work out if it works in a loop
            print("Please enter the text you want encode/decode")
            # do something so you're able to enter paragraphs
            text = input()
            for i in range(len(text)):
                final_array.append(text[i] + spaces_to_shift)
                print(text[i], "is now", final_array[i])
                print(final_array)
        else:
            raise Exception("Please enter a letter")
    else:
        raise Exception("Please enter a letter")

if __name__ == "__main__":
    main()
