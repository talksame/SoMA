#baejjoon 1188


def gcd(a, b):
    return gcd(b , a%b) if b else a

a, b = map(int, input().split())
print( b - gcd(a,b))

