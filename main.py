def cky(G,string):
    n = len(string)+1
    table = [[[] for i in range(n)] for j in range(n)]
    for length in range(1, n):
        for i in range(n-length):
            j = i + length
            if length == 1:
                for key in G:
                    if string[i] in G[key]:
                        table[j][i].append(key)
            else:
                for k in range(i+1, j):
                    for key in G:
                        for rule in G[key]:
                            if len(rule) == 2:
                                if rule[0] in table[k][i] and rule[1] in table[j][k]:
                                    table[j][i].append(key)
    return 'S' in table[n-1][0]

def main():
    cases = int(input())
    for _ in range(cases):
        l = input()
        n = [int(i) for i in l.split()]
        G = {}
        j = 0
        while j < n[0]:
            l = input()
            l = l.split()
            G[l[0]] = []
            for i in range(1, len(l)):
                G[l[0]].append(l[i])
            j += 1
        i = 0
        while i < n[1]:
            l = input()
            ans = cky(G, l)
            if ans:
                print('yes')
            else:
                print('no')
            i += 1

main()