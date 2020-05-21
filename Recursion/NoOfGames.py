#No of games played between different team if only playing once

def t(n):
    if n<=1:
        return 0
    return (n-1)+t(n-1)

print(t(8))
