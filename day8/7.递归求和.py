def sum(n):
    # 结束条件写在return之前
    if 1==n:
        return 1
    return n+sum(n-1)

def step(n):
    if 1==n or 2==n:
        return n
    return step(n-1)+step(n-2)

if __name__ == '__main__':
    print(sum(100))
    print(step(5))