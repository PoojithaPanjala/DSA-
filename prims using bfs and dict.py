from collections import defaultdict
import heapq
def prims(u,v):
    vi=set()
    q=[]
    heapq.heappush(q,(0,u))
    min_h=[]
    m=0
    while q:
        w,u=heapq.heappop(q)
        if u not in vi:
            vi.add(u)
            min_h.append(w)
            m+=w
        for i,w in d[u]:
            if i not in vi:
                heapq.heappush(q,(w,i))
    print(m)
a=[[10,5,2],[10,7,4],[5,8,3],[5,7,1],[7,8,1],[8,3,1],[5,3,2],[8,9,2]]
d=defaultdict(list)
for i,j,w in a:
    d[i].append([j,w])
    d[j].append([i,w])
prims(10,3)