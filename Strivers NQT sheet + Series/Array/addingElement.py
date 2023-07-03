def insert_front(arr,element):
    arr.insert(0,element)

def insert_last(arr,element):
    arr.append(element)

def insert_givenPos(arr,pos,element):
    arr.insert(pos, element)

list = [1,2,3,4,5]
insert_front(list,8)
insert_last(list,9)
insert_givenPos(list,3,7)
print(list)