class Node:
    
    def __init__(self,data=None):
        self.data=data 
        self.next=None
        self.head = None
        self.tail = None
class link_list:
    
    def __init__(self):
          self.head = None
    
    def append(self,data):
          new_node= Node(data)
          if self.head == None:
            self.head= new_node
            self.tail = new_node
            return
          
          current_node = self.head
          while current_node.next != None:
            current_node= current_node.next
          current_node.next=new_node
          self.tail=new_node

        
    def print_link_list(self):
         cursor=self.head
         while cursor != None:
              print(cursor.data, end="   ->  ")
              cursor=cursor.next
    
    def getTail(self):
        return self.tail
    
    def convertToList(self):
        temp=self.head
        value_list=list()
        while temp!= None:
            value_list.append(temp.data)
            temp=temp.next
        return value_list
    
    def convertToIntegerString(self):
        temp=self.head
        integer_string=""
        while temp!= None:
            integer_string+=str(temp.data)
            temp=temp.next
        return integer_string
    
          
listOne=link_list()
listOne.append(2)
listOne.append(4)
listOne.append(3)


listTwo= link_list()
listTwo.append(5)
listTwo.append(6)
listTwo.append(4)


def summation(linked_listOne : link_list, linked_listTwo : link_list):
    integerOne = int(linked_listOne.convertToIntegerString())
    integerTwo = int(linked_listTwo.convertToIntegerString())
    result_integer =integerOne + integerTwo
    return result_integer

def reverse_number(target : int , list_representation : link_list , index=2):
     int_to_linkList=list(str(target))
     
     # Base Case
     if index < 0:
         return list_representation
     else:
         list_representation.append(int_to_linkList[index])
         return reverse_number(target,list_representation,index -1) # recrusion step






        
sum_list = list()
sum_result=summation(listOne,listTwo)


empty_link_list= link_list()
re_list=reverse_number(sum_result,empty_link_list,2)
re_list.print_link_list()


# listOne.print_link_list()


# print(f'End of the list: {list_tail.data}')









# indexes= [1,2,3,4]
# for i in range(len(indexes)):
#     n.insertAtIndex(i+1,i)




# linked_list= n.getHead()
# n.print_list(linked_list)




    
