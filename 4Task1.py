def nested_sum(nested_list):
    total=0
    for x in nested_list:
        if isinstance(x, int):
            total=total+x
        else:
            for n in x:
                total=total+n
    return total


s=[4,5,6,[1,2,3],5]
print (nested_sum(s))