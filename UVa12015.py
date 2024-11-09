tc = int(input())
for i in range(1, tc + 1):
    sites = []
    top_relevance = 1
    for _ in range(10):
        site, relevance = input().split()
        relevance = int(relevance)
        sites.append((relevance, site))
        if relevance > top_relevance:
            top_relevance = relevance
    print(f"Case #{i}:")
    for j in range(10):
        if sites[j][0] == top_relevance:
            print(sites[j][1])
