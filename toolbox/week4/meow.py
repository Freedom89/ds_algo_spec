# python3
n = int(input())
seq = [int(i) for i in input().split()]

def divide_func(seq, l, r):
    # print(seq[l:r])
    if l+1==r:
        return seq[l]
    elif l+2==r:
        return seq[l]
    m = (l+r)//2
    left = divide_func(seq, l, m)
    right = divide_func(seq, m, r)
    c1, c2 = 0, 0
    for i in seq[l:r]:
        if i == left:
            c1+=1
        elif i == right:
            c2+=1
    print("this",seq[l:r],left,right,c1,c2)
    if c1>(r-l)//2 and left != -1:
        return left
    elif c2>(r-l)//2 and right != -1:
        return right
    else: 
        return -1
# divide_func([1,2],0,2)
# seq = [3,1,1,3,2,3,2,2,3,3,3]
seq=[1,2]
n = len(seq)
divide_func(seq,0,n)

print(int(divide_func(seq, 0, n) != -1))