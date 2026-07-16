class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parents = [i for i in range(n)]
        rank = [1] * n

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(x, y):
            root_x, root_y = find(x), find(y)

            if root_x == root_y:
                return False
            
            if rank[root_x] < rank[root_y]:
                parents[root_x] = root_y
                rank[root_y] += rank[root_x]
            else:
                parents[root_y] = root_x
                rank[root_x] += rank[root_y]

            return True
        
        # email -> ind
        emailToAccnt = {}
        
        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToAccnt:
                    union(i, emailToAccnt[e])
                else:
                    emailToAccnt[e] = i
        
        # ind -> [email]
        emailGroup = defaultdict(list)

        for e, i in emailToAccnt.items():
            leader = find(i)
            emailGroup[leader].append(e)
        
        res = []
        for i, emails in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emails))
        
        return res