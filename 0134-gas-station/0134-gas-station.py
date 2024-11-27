class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        #first we find the index that have bigger gas than cost
        #because there is only one unique solution, only one of them can be the solution
#         The greedy choice property in this problem ensures that:

# If at any station the cumulative gas_remain becomes negative, it implies that starting from any station before or at the current station will lead to failure.
        if sum(gas)<sum(cost):
            return -1
        
        gas_remain=0
        index=0
        for i in range(len(cost)):
            gas_remain+=gas[i]-cost[i]
            
            if gas_remain<0:
                gas_remain=0
                index=i+1

        return index if gas_remain>=0 else -1


        # from the first index that the gas_remain is + onward it has to be positive because if not the whole sum (by sum i mean sum(gas)-sum(cost)) is negative and we dont have answer but if we do the whole sum should be positive(sum(gas)>sum(cost)) and it has to also be a positive that its quantity is more than all the sum of behind it which was negative up until that point (as if we are partitioning the array to two parts first part is up until the first index we find and the second part is the part after till the end) 
   
            
           
            
        
