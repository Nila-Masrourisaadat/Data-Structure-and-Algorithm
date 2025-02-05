class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        if "0000" in deadends:
            return -1
        
        q=collections.deque()
        visit=set()
        level=0

        q.append("0000")
        while q:
            level+=1
            for _ in range(len(q)):
                s=q.popleft()
                if s==target:
                    return level-1
                for i,char in enumerate(s):
                    new_s=s[:i]+str((int(char)+1)%10)+s[i+1:]
                    if new_s not in visit and new_s not in deadends:
                        q.append(new_s)
                        visit.add(new_s)
                    new_s=s[:i]+str(((int(char)-1)+10)%10)+s[i+1:]
                    if new_s not in visit and new_s not in deadends:
                        q.append(new_s)
                        visit.add(new_s)
        return -1 
            