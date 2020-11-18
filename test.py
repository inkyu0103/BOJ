# Disjoint set object test

class Disjoint :
    def __init__(self,n):
        # 자기 자신을 가리키면 root
        self.parent = [i for i in range(n+1)]

        # 최적화에 필요한 rank (path comprehension) 대상 노드가 root인 경우 높이를 저장해 놓는다.
        self.rank = [1 for i in range(n+1)]

    def find(self, u):
        if u == self.parent[u]:
            return u

        #재귀적으로 찾아가라 임마
        return self.find(u)


    def merge(self,u,v):
        # u의 root
        u = self.find(u)

        #v의 root
        v = self.find(v)

        #root가 같으면 합칠 필요가 없다.
        if u==v :
            return ;

        #root가 같은 경우

        # v rank 가 더 높은 경우...? swap(u,v) 의 의미는 뭐지 ? rank v가 rank u 이상이므로... u를 v의 자식으로 넣는다.
        '''
            지금 u = find(u). 즉, u의 root를 의미한다.
                v = find(v). 즉 , v의 root를 의미한다.
                
                rank[u] : u의 root의 height
                rank[v] : v의 root의 height
                
                따라서 rank[u] > rank[v] 는 u의 root의 height가 더 높은 경우...
                v의 root를 u의 root에다가 붙이겠다는 의미이다.
                
                그렇다면 swap(u,v)는 u = find(v) / v = find(u) 를 의미하는 것일텐데. 
                즉, u는 v의 루트가 되는 것이고, v는 u의 루트가 되는 것이다.
                
                parent[u] = v --> 즉 v의 parent는 u의 root가 되는 것이다. 근데 굳이 이렇게 바꿔야 하는 이유가 있나...
                
                  
        '''

        if self.rank[u] > self.rank[v]:
            u,v = v,u

        self.parent[u] = v;

        if self.rank[u] == self.rank[v]:
            self.rank += 1





ds = Disjoint(5)
print(ds.parent)
print(ds.rank)






