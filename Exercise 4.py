#Write a function that accepts any number of numeric positional arguments and returns their total, mean and count. Decide how the function should handle zero arguments
def number_count(*args):
    total=sum(args)
    mean_num=total/len(args)
    lenght=len(args)
    return total,mean_num,lenght

print(number_count(1,3,4,6,7))
