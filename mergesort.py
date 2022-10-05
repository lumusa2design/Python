def mergesort(lista):
    if len(lista) > 1:
        left_arr = lista[:len(lista)//2]
        right_arr = lista[len(lista)//2:]
        print(str(left_arr) +  str(right_arr))
        
        #recursion
        mergesort(left_arr)
        mergesort(right_arr)
        
        #merged function
        i = 0
        j = 0
        k = 0
        
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                lista[k] = left_arr[i]
                i += 1
                k += 1
                print(lista)
            else:
                lista[k] =  right_arr[j]
                j += 1
                k += 1
                print(lista)
            
        while i < len(left_arr):
            lista[k] = left_arr[i]
            i += 1
            k += 1
            print(lista)
                
        while j < len(right_arr):
            lista[k] = right_arr[j]
            j += 1
            k += 1
            print(lista)
                
                
lista1 = [3, 564, 8, 90, 45, 5, 12, 2]
mergesort(lista1)