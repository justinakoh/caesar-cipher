# This is a script to translate into and out of the caesar cypher. This is a simple subsitution cypher which involves substituting each letter in the message you want to be encoded, by substituting each letter by a specific number across
def main():
    enter_alg = input(
        "This is a caesar cipher encoder/decoder. Do you wish to continue? Y/n"
    )
    if enter_alg == "" or enter_alg == "y" or enter_alg == "Y":
        known_letter = input("Please enter a letter you'd like to replace")
        replacement_letter = input(
            "Now please enter the letter you'd like to replace it with"
        )
        calc_spaces_to_shift_by(known_letter, replacement_letter)
    else:
        return "Exiting the program now"
        exit()


# This calculates the spaces to shift the alphabet by
def calc_spaces_to_shift_by(known_letter, replacement_letter):
    if ord(known_letter) <= ord(replacement_letter):
        return abs(ord(known_letter) - ord(replacement_letter))
    else:
        return (ord("z") - ord(known_letter)) + (ord(replacement_letter) - ord("a") + 1)

#This will output the actual letter
def output_letter(original_letter, num_of_spaces_to_shift_by):
    raise NotImplementedError

if __name__ == "__main__":
    main()
