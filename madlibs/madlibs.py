# # string concatenation(aka how to put strings together)
# # suppose we want to create a string that says "subscribe to ____"
# youtuber = " " # some string variable



# # a few ways to do this
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("enter adj : ")
verb1 = input("verb1: ")
verb2 = input("verb2 :")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so {adj}! It makes me so exited all the because \
     I love to {verb1}.Stay hydrated and {verb2} Like you are {famous_person}!"
print(madlib)      