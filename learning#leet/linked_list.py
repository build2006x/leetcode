#
## practice the linked list -- syntax to get better at solving problem 
class Nodelist:
    def __init__(self,data):
        self.data = data
        self.next  = None

    def  Create_node(self,val):
         curr = Nodelist(val)
         while curr.next is not None:
             print(curr.data,"->")
             curr = curr.next
          

res = Nodelist(10)
s = res.Create_node(10)
print(res)