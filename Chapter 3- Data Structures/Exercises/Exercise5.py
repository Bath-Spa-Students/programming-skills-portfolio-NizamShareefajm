guests = ['Nikola Tesla', 'Maya Angelou', 'Albert Einstein']

guest_unavailable = guests.pop(guests.index('Maya Angelou'))
print(f"Unfortunately, {guest_unavailable} can't make it to the dinner.")

new_invitee = 'Leonardo da Vinci'
guests.append(new_invitee)

for guest in guests:
    print(f"Dear {guest},")
    print("I would like to invite you for dinner.")
    print("Please let me know if you would be available. Dinner will be a delightful occasion!")
    print("\n")
