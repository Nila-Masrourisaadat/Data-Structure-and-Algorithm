class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        # output=[0]*num_people
        # i=0
        # round=0
        # while candies:
        #     if i==0:
        #         addition=round*num_people+1
        #     if candies>=addition+i:
        #         output[i]+=addition+i
        #         candies-=addition+i
        #     else:
        #         break
        #     if i<num_people-1:
        #         i+=1
        #     else:
        #         round+=1
        #         i=0
            
        # output[i]+=candies
        # return output

        candy=0
        output=[0]*num_people
        while candies>0:
            for i in range(num_people):
                candy+=1
                output[i]+=min(candy,candies)
                candies-=candy
                if candies<0:
                    break
        return output