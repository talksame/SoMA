#baekjoon 1181

case = int(input())

res = list()
word = list()
for i in range(case):
    temp = input()
    temp2 = len(temp)
    if [temp, temp2] not in word:
        word.append([temp, temp2])

res = sorted(word, key = lambda x : (x[1], x[0]))

for i in res:
    print(i[0])