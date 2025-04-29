name = input("What is your name? ")

positiveEmotions = ["happy", "good", "excited"]
negativeEmotions = ["sad", "dull", "unwell"]

print(f"Good day, {name}! How are you feeling today?\n")
print(f"Are you feeling good today like {positiveEmotions}?\n")
print(f"or are you feeling bad today like {negativeEmotions}?\n")

emotion = input("How are you feeling: ")

if emotion in positiveEmotions:
    print("Thats great! Glad to hear.")
elif emotion in negativeEmotions:
    print("Aw, I'm sorry to hear that.")
else:
    newEmotion = input("Interesting. Shall I add that to the list of emotions? Yes or No? ")
    if newEmotion.lower() == "yes":
        posOrNeg = input(f"Great! Is '{emotion}' a positive or negative emotion? ")
        if posOrNeg == "positive":
            positiveEmotions.append(emotion)
        elif posOrNeg == "negative":
            negativeEmotions.append(emotion)

        print("Okay, thanks! Here are your new lists: \n",
              positiveEmotions, negativeEmotions)

    else:
        print("Alright. Maybe some other time.")

print("Nice chatting with you,", name, "I'll see you next time!") 