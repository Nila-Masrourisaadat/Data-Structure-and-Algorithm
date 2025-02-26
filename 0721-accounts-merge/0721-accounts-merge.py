class UnionFind():
    def __init__(self,n):
        #initialization
        self.par=[i for i in range(n)]#account indexes
        self.rank=[1]*n

    def find(self,idx):# to find the leader aka account index/name?
        node=idx
        while node!=self.par[node]:
            self.par[node]=self.par[self.par[node]]#path compression 
            node=self.par[node]
        return node


    def union(self,idx1,idx2):# to merge the emails and disjoint sets if they have the same email and account name
        #rank based merging
        p1,p2=self.find(idx1),self.find(idx2)

        if p1==p2:
            return False
        if self.rank[p1]<self.rank[p2]:
            self.par[p1]=p2
            self.rank[p2]+=self.rank[p1]
        else:
            self.par[p2]=p1
            self.rank[p1]+=self.rank[p2]
        return True

class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        email_to_idx={}
        uf=UnionFind(len(accounts))#create an instance/object of the Union find class

        #iterate through emails
        for idx,account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_idx: #that means we encountered a mutual email so it is same account now and we have to merge them
                    uf.union(idx,email_to_idx[email]) #merging the new idx account index with the one already saved with the mutual email
                else:
                    email_to_idx[email]=idx
        
        #so far we have unioned the indexes based on the mutual email and we have the par and rank created in the class
        #now we need to group the emails in the format we need now that we have the email_to_idx

        emailGroups=collections.defaultdict(list)
        for email , idx in email_to_idx.items():
            emailGroups[uf.find(idx)].append(email)# finding the leader of each cluster

        # converting it to the format accepted
        output=[]
        for idx, emails in emailGroups.items():
            name=accounts[idx][0]
            output.append([name]+sorted(emails))

        return output

        
