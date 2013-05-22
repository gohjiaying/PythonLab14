class Node:
    def __init__(self,new_name,new_contact):
        self.name = new_name
        self.contact = new_contact
        self.link =None

class LinkedList:
    def __init__(self):
        self.head = None

    def AddNode(self,new_name,new_contact):
        return Node(new_name,new_contact)

    def Insert(self, new_name, new_contact):
        new_node = self.AddNode(new_name, new_contact)
        #handle 4 cases
        if self.head == None: #emptylist
            self.head = new_node

        else:
            curr = self.head
            prev = curr
            #find poisition to insert
            while(curr!=None)and (curr.name < new_name):
                prev = curr
                curr = curr.link

            if prev == curr :#insert to front
                new_node.link = curr
                self.head = new_node
                
            elif curr == None:#inser to end
                prev.link =new_node
                
            else:#insert in betweem
                new_node.link = curr
                prev.link = new_node

    def Delete(self, del_name):
        curr = self.head
        prev = curr
        while (curr != None) and (curr.name < del_name) and (curr.name != del_name):
            prev = curr
            curr =curr.link

        #if it is the first node
        if prev == self.head :
            prev.link = curr.link
        #if it is the last node
        elif curr.link == None:
            prev.link = None

        #else the other node
        else:
            prev.link = curr.link
            
    def Search(self, search_name):
        curr = self.head
        prev = curr
        while (curr != None) and (curr.name < search_name):
            prev = curr
            curr = curr.link
        if curr == None:
            return -1

        else:
            return curr.contact

    def Display(self):
        curr = self.head
        prev = curr
        while (curr != None):
            print( 'Name: ' + str(curr.name) + "\nContact: " + str(curr.contact))
            prev = curr
            curr = curr.link
    
        
            
            
                
#create new empty linked list
#insert to empty list
#insert to front
#insert to end
#insert in between
    #linkedlist.insert("healthy","well in status")
#show list contents

elist = LinkedList()

elist.Insert("jane", 9999999)
elist.Insert("peter", 23323232)
elist.Insert("david", 666345345)
elist.Insert("harry", 23478223)

elist.Display()

elist.Delete("jane")

print ("--------------------")
elist.Display()
print(elist.Search("harry"))
