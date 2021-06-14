string=input("enter the string")
def most_frequents(string):
    freq={}
    for i in string:
        if i in freq:
            freq[i]+= 1
        else:
            freq[i]=1
    sorted_dict=dict(sorted(freq.items(),key=lambda item: item[1],reverse=True))
    for i in sorted_dict.keys():
        print("{0}={1}".format(i,sorted_dict.get(i)))
most_frequents(string)
