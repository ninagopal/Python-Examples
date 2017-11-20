# Merge Sort Program in Python
# Divides a list into left and right parts until number of elements is 1
# merges the divided lists to  sorted list
# has a sorted final list and righlist and leftlist constantly working together to insert into
# sorted list

def mergeSort(Alist):
    #print("Splitting....",Alist)
    if len(Alist)>1:
        mid = len(Alist)//2
        leftList = Alist[:mid]
        rightList = Alist[mid:]
        
        
        mergeSort(leftList)
        mergeSort(rightList)
        i=0
        j=0
        k=0
        
        #Merge divided lists
        
        while(i<len(leftList) and j<len(rightList)):
            if (leftList[i] < rightList[j]):
                Alist[k] = leftList[i]
                i += 1
            else:
                Alist[k] = rightList[j]
                j += 1
            k += 1
            
        while (i < len(leftList)):
            Alist[k] = leftList[i]
            i += 1
            k += 1
            
        while (j < len(rightList)):
            Alist[k] = rightList[j]
            j += 1
            k += 1
            
        #print("Merged List is : ", Alist)
        return (Alist)
            
               
        
        
        
        
        
        
        
  