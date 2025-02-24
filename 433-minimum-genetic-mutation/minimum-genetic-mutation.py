class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        directions=['A','C','G','T']
        q=collections.deque()
        q.append(startGene)
        visit=set()
        level=0
        while q:
            for _ in range(len(q)):
                state=q.popleft()
                if state==endGene:
                    return level 
                for i,char in enumerate(state):
                    for dir in directions:
                        new_state=state[:i]+dir+state[i+1:]
                        if new_state in bank and new_state not in visit:
                            q.append(new_state)
                            visit.add(new_state)
            level+=1

        return -1 