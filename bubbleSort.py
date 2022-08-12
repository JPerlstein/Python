# practicing bubble sort 
# program repeatedly swaps adjacent elements
# if elements are in wrong order
def bubblesort(myElements): 
  swapped = False
  # loop from size of array from last index[-1] to index[0]
  for n in range(len(myElements)-1, 0, -1):
    for i in range(n): 
      if myElements[i] > myElements[i + 1]:
        swapped = True
        # swap data if element is less than next element in array
        myElements[i], myElements[i + 1] = myElements[i + 1], myElements[i]
    if not swapped:
      # exit function if no swaps were made
      # thus, indicating the array is already sorted
       return
myElements = [7, 22, 81, 91, 16, 45, 100, 896, 1200, 59]

print("UNSORTED: ")
print(myElements)
bubblesort(myElements)
print("SORTED: ")
print(myElements) 