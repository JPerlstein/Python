# practicing stack implentation 
# using list 
# and POKEMON! 

firstStack = []

# push element in stack using append 
firstStack.append('Charmander')
firstStack.append('Squirtle')
firstStack.append('Bulbasaur')
firstStack.append('Pikachu')

print('\nMy first stack!')
print(firstStack)

# pop element from stack 
# last in first out 
print('\nElements popped from stack:')
print(firstStack.pop())
print(firstStack.pop())
print(firstStack.pop())
print(firstStack.pop())

print('\nStack after elements popped:')
print(firstStack)