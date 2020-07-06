# This is a script to translate into and out of the caesar cypher.
# This is a simple subsitution cypher which involves substituting each letter
# in the message you want to be encoded, by substituting each letter by a
# specific number across

def main():
    enter_alg = input(
        "This is a caesar cipher encoder/decoder. Do you wish to continue? Y/n"
    )
    if enter_alg == "" or enter_alg == "y" or enter_alg == "Y":
        known_letter = input("Please enter a letter you'd like to replace: ")
        replacement_letter = input(
            "Now please enter the letter you'd like to replace it with: "
        )
        num_of_spaces_to_shift_by = calc_spaces_to_shift_by(
            known_letter, replacement_letter
        )
        text_to_translate = input(
            "Please enter the text that you want to encode/decode: "
        )
        text = encode_text(text_to_translate, num_of_spaces_to_shift_by)
        print(text)
    else:
        # return "Exiting the program now"
        exit()


def encode_text(text_to_translate, num_of_spaces_to_shift_by):
    encoded_text = ""
    for letter in text_to_translate:
        encoded_text += output_letter(letter, num_of_spaces_to_shift_by)
    return encoded_text


# This calculates the spaces to shift the alphabet by
def calc_spaces_to_shift_by(known_letter, replacement_letter):
    if ord(known_letter) <= ord(replacement_letter):
        return abs(ord(known_letter) - ord(replacement_letter))
    else:
        return (ord("z") - ord(known_letter)) + (ord(replacement_letter) - ord("a") + 1)


# This will output the actual letter
def output_letter(original_letter, num_of_spaces_to_shift_by):
    letter = chr((ord(original_letter) + num_of_spaces_to_shift_by)%122)
    return letter;
    # number = ord(original_letter) + num_of_spaces_to_shift_by
    # if number <= 122:
    #     return chr(number)
    # else:
    #     return chr(ord("a") + (number - ord("z") - 1))


if __name__ == "__main__":
    main()
