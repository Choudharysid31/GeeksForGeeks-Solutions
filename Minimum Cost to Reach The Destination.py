def costing(n, arr):
    i=0
    cost=0
    while i<n-1:
        if i+3<n and abs(arr[i+3]-arr[i])<=abs(arr[i+1]-arr[i]):
            cost+=abs(arr[i+3]-arr[i])
            i+=3
        else:
            cost+=abs(arr[i+1]-arr[i])
            i+=1
    return(cost)
    

a = int(input())
b = list(map(int, input().split()))

print(costing(a,b))
