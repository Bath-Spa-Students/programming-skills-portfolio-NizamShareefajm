places_to_visit = ['Tokyo', 'Paris', 'Machu Picchu', 'Bora Bora', 'Santorini']

print("Original order:", places_to_visit)

print("Alphabetical order:", sorted(places_to_visit))

print("Original order after sorting:", places_to_visit)

print("Reverse alphabetical order:", sorted(places_to_visit, reverse=True))

print("Original order after reverse sorting:", places_to_visit)

places_to_visit.reverse()
print("Reversed order:", places_to_visit)

places_to_visit.reverse()
print("Back to original order:", places_to_visit)

places_to_visit.sort()
print("Sorted in alphabetical order:", places_to_visit)

places_to_visit.sort(reverse=True)
print("Sorted in reverse alphabetical order:", places_to_visit)
