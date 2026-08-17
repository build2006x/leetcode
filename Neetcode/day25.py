# ### hey hi today i am working on the hashmap function implementation question 
# class MyHashMap:
#      def __init__(self):
#                     self.arr = {}

#      def show(self):
#           return  self.arr

#      def add(self,key:int,val:int) -> None:
#           if key not in self.arr:
#                self.arr[key] = val

#      def get(self,key:int):
#           if key in self.arr:
#                return self.arr[key]
#           return -1

#      def delete(self,key:int):
#           if key in self.arr:
#                del self.arr[key]

#      def put(self,key:int,value:int):
#             self.arr[key] = value
          
# obj =  MyHashMap()

# obj.add(3,1)
# obj.put(3,4)
# print(obj.show())


class MyHashMap:

        def __init__(self):
                self.arr = {}

        def put(self, key: int, value: int) -> None:
                 if key  in  self.arr:
                            self.arr[key]  = value
            
        def get(self, key: int) -> int:
                        if key in self.arr:
                                  return self.arr[key]
                        return -1

        def remove(self, key: int) -> None:
                        if key in self.arr:
                                       del self.arr[key]


obj = MyHashMap()
obj.put(3,4)
param_2 = obj.get(3)
print(param_2)