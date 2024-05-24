'''class Box:
    def __init__(self,data):
        self.data = data
        self.next = None
obj1 = Box(51)
obj2 = Box(52)
obj3 = Box(53)
obj4 = Box(54)
obj5 = Box(55)
obj6 = Box(56)
obj7 = Box(57)
obj8 = Box(58)
obj9 = Box(59)
obj10 = Box(60)
#establishing links in below 10 lines
obj1.next =obj2
obj2.next =obj3
obj3.next =obj4
obj4.next =obj5
obj5.next =obj6
obj7.next =obj8
obj8.next =obj9
obj9.next =obj10
obj10.next=None
print(obj1.data,obj1.next)
print(obj2.data,obj1.next)
print(obj3.data,obj1.next)
print(obj4.data,obj1.next)
print(obj5.data,obj1.next)
print(obj6.data,obj1.next)
print(obj7.data,obj1.next)
print(obj8.data,obj1.next)
print(obj9.data,obj1.next)
print(obj10.data,obj1.next)'''


'''class Box:
    def __init__(self,data):
        self.data = data
        self.next = None
def printLinkedList(curr):
    while curr != None:
        print(curr.data)
        curr = curr.next

obj1 = Box(51)
obj2 = Box(52)
obj3 = Box(53)
obj4 = Box(54)
obj5 = Box(55)
obj6 = Box(56)
obj7 = Box(57)
obj8 = Box(58)
obj9 = Box(59)
obj10 = Box(60)
#establishing links in below 10 lines
obj1.next =obj2
obj2.next =obj3
obj3.next =obj4
obj4.next =obj5
obj5.next =obj6
obj6.next =obj7
obj7.next =obj8
obj8.next =obj9
obj9.next = obj10
obj10.next=None
printLinkedList(obj3)
print(obj10.data,obj10)'''

## insert tail node
'''class Box:
    def __init__(self,data):
        self.data = data
        self.next = None
def printLinkedList(curr):
    while curr != None:
        print(curr.data)
        curr = curr.next
def InsertAtTailNode(head,ele):
    temp =Box(ele)
    if head == None:
        return temp
        tail = head 
 
    while tail.next != None:
        tail = tail.next 
    tail.next = temp
    return head 
head=None
nums=[10,20,30,40,50,60,70,80,90,100]
for ele in nums:
    head=InsertAtTailNode(head,ele)
printLinkedList(head)'''

#beginning at node
'''class Box:
    def __init__(self,data):
        self.data = data
        self.next = None
def printLinkedList(curr):
    while curr != None:
        print(curr.data)
        curr = curr.next
def InsertAtBeginning(head,ele):
    temp =Box(ele)
    if head == None:
        return temp
head=None
nums=[10,20,30,40,50,60,70,80,90,100]
for ele in nums:
    head=InsertAtBeginning(head,ele)
printLinkedList(head)'''

#at specificposition
class Box:
    def __init__(self,data):
        self.data = data
        self.next = None
def printLinkedList(curr):
    while curr != None:
        print(curr.data)
        curr = curr.next
def InsertAtSpecificPosition(head,position,ele):
    temp =Box(ele)
    currentIndex = 0
    currentNode = head
    while currentIndex !=position-1:
        currentIndex =+1
        currentNode=currentNode.next
        temp.next =currentNode.next
        currentNode.next = temp 
        return head
head = None
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for ele in nums:
    head = InsertAtSpecificPosition(head, 5, 1899)
    printLinkedList(head)

