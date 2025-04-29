userName = input("Hello! What is your name? ")

print("Greetings, ", userName)
feeling = input("How are you feeling today? ")

if feeling.lower() == "good" or feeling.lower() == "cool":
    print("That's great! Glad to hear.")
elif feeling.lower() == "bad" or feeling.lower() == "unwell":
    print("I'm sorry to hear that.")
else:
    print("Interesting!")


