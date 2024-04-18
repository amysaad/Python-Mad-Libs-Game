#Author: Amy Saad
#Due Date: 11/24/2023
#Program description: Python program that will implements a short Mad Libs game. 
#The program asks the user to give random words like adjectives, nouns, adverbs, etc. without any context.

NameofUser = input("Enter your name: ")

print(f"Hi, {NameofUser}!")

prompt1 = input("Give an adjective: ")
prompt2 = input("Give a person's name: ")
prompt3 = input("Give a type of vehicle: ")
prompt4 = input("Give another adjective: ")
prompt5 = input("Give an adverb: ")
prompt6 = input("Give a creature name: ")
prompt7 = input("Give one more adjective: ")

print(f"It was a {prompt1} fall night.")
print(f"{prompt2} and I were excited to go to the pumpkin patch.")
print(f"We drove a {prompt3} there and found the place {prompt4}.")
print("We", prompt5, "picked our pumpkins and went to leave when all of a sudden—")
print(f"A {prompt6} jumped in our path! How {prompt7}!")
