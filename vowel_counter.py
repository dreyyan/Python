print("Vowel Counter")

vowel_list = ['a', 'e', 'i', 'o', 'u']
string_input = input("Enter a word/sentence: ")

vowel_counter = 0

for letter in string_input:
    for vowel in vowel_list:
        if letter == vowel:
            vowel_counter += 1

print("# of Vowels: " + str(vowel_counter))