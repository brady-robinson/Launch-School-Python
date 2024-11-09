# numbers = [1, 2, 3]
# numbers[6] = 5

# str1 = "Come over here!"  # True
# str2 = "What's up, Doc?"  # False

# print(str1.endswith("!"))
# print(str2.endswith("!"))

# famous_words = "seven years ago..."
# new_str = "Four score and " + famous_words
# new_str_2 = " ".join(["Four score and", famous_words])
# new_str_3 = f"Four score and {famous_words}"
# print(new_str)
# print(new_str_2)
# print(new_str_3)

# munsters_description = "the Munsters are CREEPY and Spooky."
# # => 'The munsters are creepy and spooky.'
# print(munsters_description.capitalize())

# munsters_description = "The Munsters are creepy and spooky."
# print(munsters_description.swapcase())

# str1 = "Few things in life are as important as house training your pet dinosaur."
# str2 = "Fred and Wilma have a pet dinosaur named Dino."

# print([True if str1.find("Dino") > -1 else False][0])
# print([True if str2.find("Dino") > -1 else False][0])

# flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
# flintstones.extend(["Dino", "Happy"])

# advice = "Few things in life are as important as house training your pet dinosaur."
# # Expected output:
# # Few things in life are as important as
# print(advice[:advice.find("house")])

advice = "Few things in life are as important as house training your pet dinosaur."
print(advice.replace("important", "urgent"))