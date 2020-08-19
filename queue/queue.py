class Node:
  def __init__(self,value,next_node=None):
    self.value = value
    self.next_node = next_node
  def get_value(self):
    return self.value
  def get_next_node(self):
    return self.next_node
  def set_next_node(self,new_next_node):
    self.next_node = new_next_node  
  def __repr__(self):
    return f'<Node: {self.value}'

class Linked_List:
  def __init__(self,head=None,tail=None):
    self.head = head
    self.tail = tail
    self.count = 0
  def add_to_head(self,value):
    #if there no node at all
    node = Node(value)
    if self.head == None:
       self.head = node
       self.tail = node
    else:
       node.set_next_node(self.head)
       self.head = node
    self.count += 1   
      
  def add_to_tail(self, value):    
    node = Node(value)
    #if there is only one node at all in the list
    if self.head == None:
      self.head = node
      self.tail = node
    else:
      self.tail.set_next_node(node)
      self.tail = node  
    self.count += 1  

  def remove_from_head(self):
    #if there is no node
    deleted_head_value = None
    if self.head == None:
      return None
    # if there in one node
    elif self.head == self.tail:
      deleted_head_value = self.head.get_value()
      self.head = None
      self.tail = None
      self.count -= 1 
    # if there are more than one node
    else:
      deleted_head_value = self.head.get_value()
      self.head = self.head.get_next_node()
      self.count -= 1 
    return deleted_head_value

  def find_length(self):
    return self.count     
    

class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    # Answer:- We use linked_lists for constructing Queue
    self.storage = Linked_List()

  def enqueue(self, item):
    # self.storage.append(item)
    self.storage.add_to_tail(item)
    self.size +=1
  
  def dequeue(self):
    if self.size < 1:
      return None
    else:
      self.size -= 1
      return self.storage.remove_from_head()

  def len(self):    
    count = self.storage.find_length()
    self.size = count
    return self.size