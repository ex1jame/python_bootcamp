ls = [1,2,3,4,5,6,7,8,9,10,11,12,13,15,21]
left = 0
right = len(ls) - 1
mid = len(ls) // 2
value = 10

# print(ls[right])
while ls[mid] != value and left <= right:
    if value < ls[mid]:
        right = mid - 1
    else:
        left = mid + 1
    mid = (left + right) // 2
if left > right:
    print('Not found')
else:
    print(f'{value} = {ls[mid]} id: {mid}')
