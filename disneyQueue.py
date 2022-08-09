# program to demonstrate queue implementation
# disneyland rides 

# initialize queue 
disneyQueue = []

# adding rides to the queue! 
disneyQueue.append('Peter Pan')
disneyQueue.append('Dumbo')
disneyQueue.append('Winnie the Pooh')
disneyQueue.append('Thunder Mountain')
disneyQueue.append('King Arthur Carousel')
disneyQueue.append('Matterhorn')
disneyQueue.append('Teacups')

print("\nInitial queue:")
print(disneyQueue)

# removing elements from queue 
# removing all but one element
print('\nElements dequeued from queue:')
print(disneyQueue.pop(0))
print(disneyQueue.pop(0))
print(disneyQueue.pop(0))
print(disneyQueue.pop(0))
print(disneyQueue.pop(0))
print(disneyQueue.pop(0))

# only the teacups remain 
print("\nQueue after removing all but one element")
print(disneyQueue)
