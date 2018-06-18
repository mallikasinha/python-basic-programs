Ip_address = input("enter Ip Address")
if Ip_address[-1] !='.':
    Ip_address +='.'
segment=1
segment_lenght =0

# character = ""

for charater in Ip_address:
    if charater ==".":
        print("segment {} has {} character".format(segment,segment_lenght))
        segment +=1
        segment_lenght =0
    else:
        segment_lenght +=1

# if charater != ".":
#     print("segment {} has {} character".format(segment,segment_lenght))
