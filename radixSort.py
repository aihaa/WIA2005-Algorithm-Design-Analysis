#code by Group 7 (Athirah Lokman)

#Using counting sort to sort the elements in the basis of significant places
def countingSort(array,place):
    size = len (array)                                 #Initialize size as equal to length of input array
    output = [0]* size                              #Create output array with size "size", with elements initialization zero in it
    count = [0]* 10                                  #Create count array with length =10; possible value 0-9

    #Calculate count of elements in the input array
    for i in range (0,size):                             
        index = array [i] // place                       # Count occurence of each element and store in count array
        count [index % 10] +=1                   

    #Calculate cumulative count by adding value at the current index
    # with the value at the previous index
    #Cumulative count will be stored in the count array

    for i in range (1, 10):
        count[i] += count [i-1]                        #Current count + Previous count
                                                       
    i = size -1
    while i>=0:                                                                   
        index = array [i]//place                        #Find the index (-1) for the element
        output [count[index%10]-1] = array [i]          #Assign the element in the output array - sorted 
        count [index % 10] -=1                          #Reduce the sorted element's count by 1 
        i-=1                              

    for i in range (0, size):
        array[i] = output[i]                            #Copy the output to the input array 

#Main function to implement Radix Sort
def radixSort(array):

    #Get maximum element
        max_element = max(array)                       

    #Apply counting sort to sort elements based on place value
        place=1                                                             #Start with 1s place value (LSB)    
        while max_element// place >0:
            countingSort(array,place)
            place *=10                                                      #Continue to sort for the next 10’s place                                                    

data = [16, 30, 95, 51, 84, 23, 62, 44]
radixSort(data)
print(data)
