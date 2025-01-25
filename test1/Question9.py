#function to get user input
def get_input():
    entered_string = input("Enter a string to know it's components")
    return entered_string
#function to count the number of vowels, consonants, digits and special characters
def count(entered_string):
    vowel_count = 0
    special_character_count = 0
    consonant_count = 0
    digit_count = 0
    for i in entered_string:
        if i.isalpha():
            if i in "aeiouAEIOU":
                vowel_count += 1
            else:
                consonant_count += 1
        elif i.isdigit():
            digit_count += 1
        else:
            special_character_count += 1
    return vowel_count, consonant_count, digit_count, special_character_count
#function to reverse the string
def reverse_string(entered_string):
    return entered_string[::-1]
#main function
def main():
    entered_string = get_input()
    vowel_count, consonant_count, digit_count, special_character_count = count(entered_string)
    print(f"Vowels: {vowel_count}")
    print(f"Consoneants: {consonant_count}")
    print(f"Digits: {digit_count}")
    print(f"Special Characters: {special_character_count}")
    print(f"Reversed String: {reverse_string(entered_string)}")    
main()
