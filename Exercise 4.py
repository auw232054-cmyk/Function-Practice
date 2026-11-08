def number_count(*args):
    total=sum(args)
    mean_num=total/len(args)
    lenght=len(args)
    return total,mean_num,lenght

print(number_count(1,3,4,6,7))
