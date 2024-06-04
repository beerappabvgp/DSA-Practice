
# size = int(input("enter size"))
# arr = list(map(int, input("enter elements space separated").split()))

def hash(arr):
    hash_arr = [0] * len(arr)
    for e in arr:
        hash_arr[e] += 1
    return hash_arr

h = hash([1,2,3,4,1,1,3])
print(h)
