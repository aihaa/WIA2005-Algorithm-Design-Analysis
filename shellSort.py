#code by group 7 (Athirah Lokman)

def shell_sort(arr):
    size = len(arr)
    gap = size//2
    
    while gap>0:
        for i in range(gap, size):
            anchor = arr[i] 
            j = i           
            
            while j >= gap and arr[j-gap] > anchor:        #compare the elements with element in anchor
                arr[j] = arr[j-gap]                                             #swap 
                j -= gap           
            arr[j] = anchor                                                     #replace anchor value       
        gap = gap //2                                                           #update gap value
                  
if __name__ == '__main__':
    elements = [16, 30, 95, 51, 84, 23, 62, 44]
    shell_sort(elements)
    print(elements)
