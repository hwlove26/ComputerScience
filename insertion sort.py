my_list = [4,2,6,1,8,7]

for i in range(1,len(my_list)):
    key = my_list[i]
    j = i-1
    while j >= 0 and my_list[j] > key:
        my_list[j+1] = my_list[j]
        j -= 1
    my_list[j+1] = key
    print(my_list, j, i, key)

print(my_list)

'''
DECLARE my_list : ARRAY[0:10]
DECLARE key : INTEGER
DECLARE j : INTEGER

my_list <-- [4,2,6,1,8,7]

FOR i <-- 2 TO 11 //repeat from start+1 to length of array -1
    key <-- my_list[i] //key, which will be main number being sorted
    j <-- i-1 //j is index for being changed
    WHILE j >= 0 AND my_list[j] > key //compare j with 0 so detect it is end and compare key and item to make sure key is smaller then item being changed
        my_list[j+1] <-- my_list[j] //move 1 back
        j <-- j-1 //for next item to compare
    ENDWHILE
    my_list[j+1] <-- key //for next key
NEXT i

OUTPUT my_list


'''