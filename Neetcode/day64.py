### hey hi toady i am focusing on the linked list leaning process
class Node:
     def __init__(self,data):
          self.data = data
          self.next: Node | None = None

class Linkedlist:
     def __init__(self) -> None:
          self.head = None

     def insert_beginning(self,data):
               NewNode = Node(data)
               NewNode.next = self.head
               self.head = NewNode
               

     def display(self):
          cur = self.head

          while cur is not None:
                    print(cur.data ,end="->")
                    cur = cur.next          


mylist = Linkedlist()

mylist.insert_beginning(10)
mylist.display()

