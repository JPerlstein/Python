# reverse string with loop 

def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
    
s = "Greetings from Mars"

print("\n Reversed with Loop:")

print("Original string: ", end=" ")
print(s)

print("Reversed string: ", end=" ")
print(reverse(s))

# reverse string with recursion 

def reverse(originalString):
    if len(originalString) == 0:
        return originalString
    else:
        return reverse(originalString[1:]) + originalString[0]

originalString = " Jupiter is not a Planet"

print("\n Reversed with Recursion:")


print("Original String: ", end=" ")
print(originalString)

print("Reversed String: ", end=" ")
print (reverse(originalString))