class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1

        def children(lock):
            res = []
            
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
            return res
                
        
        q = deque([('0000', 0)])
        visited = set()
        visited.add('0000')
        while q:
            lock, cnt = q.popleft()
            if lock == target:
                return cnt
            
            for child in children(lock):
                if child not in visited and child not in deadends:
                    visited.add(child)
                    q.append([child, cnt+1])
        
        return -1