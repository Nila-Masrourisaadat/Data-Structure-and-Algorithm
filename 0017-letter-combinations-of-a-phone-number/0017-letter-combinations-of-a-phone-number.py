class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping={"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
        res=[]
        subset=""
        if not digits:
            return []
        def dfs(i,subset):
            if i>=len(digits):
                res.append(subset[:])
                return
            for dig in mapping[digits[i]]:
                dfs(i+1,subset+dig)
        dfs(0,subset)
        return res
