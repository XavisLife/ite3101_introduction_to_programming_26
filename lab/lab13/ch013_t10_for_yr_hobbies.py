hobbies = []

# Add your code below!
for x in hobbies:
    if x <= 3:
        hobby = (input("What is your hobby?"))
        hobbies.append(hobby)
    else:
        break

print(hobbies)
