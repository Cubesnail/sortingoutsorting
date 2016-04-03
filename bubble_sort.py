def bubble_sort(l: list) -> None:
    for i in range(len(l), 1, -1):
        for j in range(i,len(l)):
            if l[j] < l[j - 1]:
                l[j], l[j - 1] = l[j - 1], l[j]
x = [1,2,4,2,3,1,5,6,1,3]
bubble_sort(x)
print(x)