n = int(input())
arr = list(map(int, input().split())) 
a = max(arr)
arr.remove(max(arr))
for i in range (n):
    if a == max(arr):
        arr.remove(max(arr))
    i +=1
print(max(arr)) 
