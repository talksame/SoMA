#baek 1966 Print Queue


case = int(input())
res = list()

for i in range(case):
    doc, where = map(int, input().split())
    docs = list(map(int, input().split()))
    cnt = 0
    while True:
        if where == 0:
            if docs[where] == max(docs):
                cnt += 1
                res.append(cnt)
                break
            else:
                docs.append(docs[0])
                del docs[0]
                where = len(docs) -1
        elif where >= 1:
            if docs[0] == max(docs):
                del docs[0]
                where -= 1
                cnt += 1
            elif docs[0] < max(docs):
                docs.append(docs[0])
                del docs[0]
                where -= 1

for i in range(case):
    print(res[i])

