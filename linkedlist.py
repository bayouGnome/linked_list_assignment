from node import Node

class LinkedList():
    def __init__(self):
        self.head = None

    def __str__(self):
        string = ""
        if self.head == None:
            print("The list is empty.")
        else:
            tmp = self.head
            while tmp != None:
                string += tmp.client_obj.name + " " + tmp.client_obj.phone + " " + tmp.client_obj.birthdate + "\n"
                tmp = tmp.next
        return string

    def __contains__(self, target):
        tmp = self.head
        while tmp != None:
            if tmp.client_obj.name == target:
                return True
            tmp = tmp.next
        return False
               
    def append(self,client_obj):
        new_node = Node(client_obj)
        if self.head == None:
            self.head = new_node
        else:
            searcher = self.head
            while searcher.next != None:
                searcher = searcher.next
            searcher.next = new_node

    def delete(self, to_delete):
        searcher = self.head
        if searcher.client_obj.name == to_delete:
            self.head = searcher.next
        else:
            while searcher.next != None:
                previous_ptr = searcher
                searcher = searcher.next
                if searcher.client_obj.name == to_delete:
                    searcher.next = previous_ptr.next
        
        
            
        #make a temp holder for the previous node.next  
        #cycle through data to find client to delete
        #temp holder is set to current node.next