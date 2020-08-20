#Problem 1:https://leetcode.com/problems/logger-rate-limiter/
#Test Cases passed on Leetcode 
#Binary Search Used
#Time Complexity-O(1)
#Space Complexity-O(N)-Size of incoming messages 
class Logger:
   
    def __init__(self):
        self.msg_dict={}
    def shouldPrintMessage(self, timestamp, message) :
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        
        if message not in self.msg_dict:
            self.msg_dict[message]=timestamp
            return True
        else:
            old_timestamp=self.msg_dict[message]
            if timestamp-old_timestamp>=10:
                self.msg_dict[message]=timestamp
                return True
            
        return False

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)