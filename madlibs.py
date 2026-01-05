# madlibs game
# word game where you fill in the blanks to create a story
# prompts the user for a series of words and then inserts those words into a pre-defined story template
# finally displays the completed story to the user

print("Welcome to MadLibs!")
noun1 = input("Enter a noun: ")
verb1 = input("Enter a verb: ")
adjective1 = input("Enter an adjective() ")
adverb1 = input("Enter an adverb:() ")
noun2 = input("Enter another noun: ()")
story = f"Once upon a time, there was a {adjective1} {noun1} who loved to {verb1} {adverb1}. One day, it met a {noun2} and they became friends."
print("\nHere is your story:")  
print(story)

