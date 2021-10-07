vowels = 'aeiou'
# create your list here
input_text = input()
vowels_in_input = [letter for letter in input_text if letter in vowels]
print(vowels_in_input)
