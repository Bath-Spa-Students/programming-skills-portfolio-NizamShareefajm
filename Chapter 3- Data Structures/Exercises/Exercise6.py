guests = ['Nikola Tesla', 'Maya Angelou', 'Albert Einstein', 'Leonardo da Vinci']

print("Unfortunately, the new dinner table won't arrive in time, and I can only invite two people for dinner.")

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry, {removed_guest}, I won't be able to invite you to dinner this time.")

for guest in guests:
    print(f"Dear {guest},")
    print("I would like to invite you for dinner.")
    print("Please let me know if you would be available. Dinner will be a delightful occasion!")
    print("\n")

del guests[:]

print("After the dinner, the guest list is now:", guests)
