#Creating a Password

first_word = input("Type First Word: ")
second_word = input("Type Second Word: ")
number = input("Type a whole number: ")

combined_word = f"{first_word}_{second_word}"

combined_number = f"{number}{first_word}{number}"


print(f"You entered:", first_word, second_word, number)
print("\nFirst password:", combined_word)
print('Second password:', combined_number)

count1 = len(combined_word)
count2 = len(combined_number)

print(f"\nNumber of characters in {combined_word}:", count1)
print(f"Number of characters in {combined_number}:", count2)