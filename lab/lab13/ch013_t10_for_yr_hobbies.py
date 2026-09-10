hobbies = []

# Add your code below!
for x in hobbies:
    hobby = (input("What is your hobby?"))
    hobbies.append(hobby)
    x += 1
    if (x > 3):
        break

print(hobbies)
