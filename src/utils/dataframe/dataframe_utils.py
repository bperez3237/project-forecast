

def array_differences(array1, array2):
    #return an array values which not shared between the two arrays
    return [x for x in array1 if x not in array2] + [x for x in array2 if x not in array1]

