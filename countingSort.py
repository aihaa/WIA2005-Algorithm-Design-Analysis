# code by Group 7 (Hanan Nizam)

def counting_Sort(input):
   # Find the maximum element in the inputArray
   maxEl= max(input)

   # 3 Arrays: Input Array, Count Array, Output Array

   # Initialize the cntArray with zeros
   # index:    ..16...23...30...44...51...62...84...95
   # cntArray : [0,..,0,..,0,..,0,..,0,..,0,..,0,..,0]
   cntArray = [0] * (maxEl+1)

   # Traverse the inputArray and increase the corresponding count for every element by 1
   # Input Array:        [16,  30,  95,  51,  84,  23,  62,  44]
   # index:             ..16...23...30...44...51...62...84...95
   # cntArray Initially: [0,..,0,..,0,..,0,..,0,..,0,..,0,..,0]
   # cntArray After    : [1,..,1,..,1,..,1,..,1,..,1,..,1,..,1]
   for j in input:
       cntArray[j] = cntArray[j] + 1

   # For each element in the cntArray, sum up its value with the value of the previous
   # element, and then store that value as the value of the current element
   # index  : ..16..23..30..44..51..62..84..95
   # cntArray: [1,..,1,..,1,..,1,..,1,..,1,..1,..1] <- sum up = previous element + current element
   # cntArray= [1,..,2,..,3,..,4,..,5,..,6,..7,..8]
   for i in range(1, maxEl+1):
       cntArray[i] = cntArray[i] + cntArray[i-1]

   # Initialize a new array (output) to store the sorted values
   # output= [0, 0, 0, 0, 0, 0, 0, 0]
   output = [0] * len(input)
   # Initialize a pointer
   i = len(input) - 1  # i = 7
   # [16, 30, 95, 51, 84, 23, 62, 44]
   while i >= 0:
       # The pointer will start counting from the end of the array
       # [16, 30, 95, 51, 84, 23, 62, 44] <- pointer is at index 7 which is 44
       currentElement = input[i]

       # Find the index in the cntArray that is equal to the value of the current element input[i]
       # in this case, index 44
       # Subtract 1 from the value of the cntArray[i] to know the index in the output array
       # index =     16....23....30....44....51....62....84...95
       # cntArray = [1,.., 2,.., 3,.., 4,.., 5,.., 6,.., 7,..,8]
       # cntArray = [1,.., 2,.., 3,.., 3,.., 5,.., 6,.., 7,..,8]
       cntArray[currentElement] = cntArray[currentElement] - 1

       # store the value of the input[i] into the output array
       # index:       [0, 1, 2, 3, 4, 5, 6, 7]
       # OutputArray: [0, 0, 0, 44, 0, 0, 0, 0]
       temp = cntArray[currentElement]  # temp = 44
       output[temp] = currentElement
       i = i - 1  #iterate to the next element of inputArray[i] (6, 5, 4, 3, 2, 1, 0)
   return output

Array = [16, 30, 95, 51, 84, 23, 62, 44]
print("Input: ", Array)

# Call the function
result = counting_Sort(Array)
print("Result: ", result)

