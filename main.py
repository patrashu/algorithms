import sys
# sys.stdin = open('input.txt','rt')
input = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, input().split())
    known = set(list(map(int, input().split()))[1:])
    parties = []
    cnt = []
    
    for _ in range(m):  
        party = set(map(int, input().split()[1:]))
        if party:
            parties.append(party)
            cnt.append(1)
    
    for _ in range(m):
        for i, p in enumerate(parties):
            if known & p:
                cnt[i] = 0
                known.update(p)
                
    print(sum(cnt))
