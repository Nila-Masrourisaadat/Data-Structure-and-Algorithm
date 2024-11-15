class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        ROWS, COLS = len(board), len(board[0])
        visit = set()

        def dfs(r,c,i):
            if i==len(word): # we have reached the end of the word so we have found a result
                return True
            
            if r<0 or r==ROWS or c<0 or c==COLS or (r,c) in visit or board[r][c]!=word[i]:
                return False #this means down that path there is not gonna be an equivalant to the word so we return false for that path to first of all backtrack but also not go down that path again

            #choose
            visit.add((r,c))
            #explore the path
            res=False
            for dr,dc in directions:
                row=r+dr
                col=c+dc
                res= res or dfs(row,col,i+1) #this explores all 4 path adjacent to board[r][c] and everytime it will return true or false for each path, we only need one true for it to work
                if res:
                    return True #if after exploring all of those path any of them was true then we found a path with the word
            
            #unchoose or backtrack if res wasnt true
            visit.remove((r,c))

            #at the end, after all the exploration if none of the paths was true
            return False


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]==word[0]:
                    if dfs(r,c,0):
                        return True
        return False