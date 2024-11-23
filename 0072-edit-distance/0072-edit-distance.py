class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        #memoization and recursive
        dp = {}

        def dfs(i, j):
            # Base cases
            if i == len(word1):  # If word1 is exhausted, insert remaining characters of word2
                return len(word2) - j
            if j == len(word2):  # If word2 is exhausted, delete remaining characters of word1
                return len(word1) - i
            
            if (i, j) in dp:  # Check memoization table
                return dp[(i, j)]

            # If characters match, move to the next characters in both words
            if word1[i] == word2[j]:
                dp[(i, j)] = dfs(i + 1, j + 1)
            else:
                # If characters don't match, consider the three possible operations
                insert = dfs(i, j + 1)    # Insert a character in word1
                delete = dfs(i + 1, j)    # Delete a character from word1
                replace = dfs(i + 1, j + 1)  # Replace a character in word1
                dp[(i, j)] = 1 + min(insert, delete, replace)  # Take the minimum cost

            return dp[(i, j)]

        # Call the function starting from the beginning of both words
        return dfs(0, 0)


        #bottom up and iterative
        dp=[[float("inf")]*(len(word2)+1) for _ in range(len(word1)+1)]
        
        for j in range(len(word2)+1):
            dp[len(word1)][j]=len(word2)-j
        for i in range(len(word1)+1):
            dp[i][len(word2)]=len(word1)-i

        for i in range(len(word1)-1,-1,-1):
            for j in range(len(word2)-1,-1,-1):
                if word1[i]==word2[j]:
                    dp[i][j]=dp[i+1][j+1]
                else:
                    dp[i][j]=min(dp[i+1][j],dp[i][j+1],dp[i+1][j+1])+1
                
        return dp[0][0]
            