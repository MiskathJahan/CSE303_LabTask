def largest_number_2019_2_60_056(list):
    max=-9999999
    for i in range(0, len(list)):
        if(list[i]>max):
            max = list[i]
    return max
def smallest_number_2019_2_60_056(list):
    min=9999999
    for i in range(0, len(list)):
        if(list[i]<min):
            min = list[i]
    return min
list=[2,4,6,9,11,13,14,18,29,40]
print("Largest_number is :",largest_number_2019_2_60_056(list))
print("Smallest_number is :",smallest_number_2019_2_60_056(list))