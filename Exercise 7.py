#Write a function that receives a list and returns a new list with duplicates removed while preserving first-appearance order.
def data_li(numbers):
    unique_li=[]
    for i in numbers:
        if i in unique_li:
            continue
        else:
            unique_li.append(i)
    return unique_li
print(data_li([1,2,1,3,3,4,3,6]))
