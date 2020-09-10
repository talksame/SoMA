'''
백준 1076 저항

저학은 3개의 색을 통해서 옴을 나타냄
처음 2개는 저항의 값 마지막 값은 공해야함.

4 + 7 *

'''

def square(a):
    res = 1
    for i in range(a):
        res *= 10
    return res

st = input()
mid = input()
end = input()

res = ['black' ,
       'brown' ,
       'red' ,
       'orange' ,
       'yellow' ,
       'green' ,
       'blue' ,
       'violet' ,
       'grey' ,
       'white']

temp_st = res.index(st)
temp_mid = res.index(mid)
temp_end = 1
if end == 'black':
    temp_end = 1
else:
    temp_end = square(res.index(end))

ans = (temp_st*10 + temp_mid) * temp_end
print(ans)