#Problem 1:https://leetcode.com/problems/logger-rate-limiter/
#Test Cases passed on Leetcode 
#Binary Search Used
#Time complexity : O(k). k refers to the number of valid permutations.
#Space Complexity-O(n) size of boolean array-depth of the recursion tree
#Approach-Backtracking
class Solution:
  
    def __init__(self):
        self.count=0
    def countArrangement(self, N: int) -> int:
        #boolean array
        arr=[False for i in range(N+1)]
        index=1
        self.validate(N,1,arr)
        return self.count
        
    def validate(self,N, index,arr):
        if index>N:
                self.count+=1
                
        for i in range(1,N+1):
                
            if (arr[i]==False and (index%i==0 or i%index==0)) :
                #action
                arr[i]=True
                #recurse
                self.validate(N,index+1,arr)
                #backtrack
                arr[i]=False
            