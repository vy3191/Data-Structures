class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # 1. Compare if the new node's value is less than the given value, if yes,
         # a. Find if there is a child or not, if there is no child then insert the new node
         # b. Repeat the same process  -- check if the new node is greater than or less than
    # 2. Compare if the new node's value is greater than the given value, if yes
         # a. Find if there is a child or not, if there is no child then insert the new node
         # b. Repeat the same process -- check if the new node is greater than or less than
    if self.value > value:
      if not self.left:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)  
    else:
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)        

  def contains(self, target):    
    # if there is no node in the tree 
    if self.value == None:
      return False
    # if the self.value(top) is equal to target
    elif self.value == target:
      return True
    # left side values
    elif self.value > target:
      if self.left == None:
        return False
      elif self.left == target:
        return True
      else:
        return self.left.contains(target)
    # right side values
    else:
      if not self.right:
        return False
      elif self.right == target:
        return True
      else:
        return self.right.contains(target)  

  def get_max(self):    
    if self.right is None:
      return self.value
    elif self.right == self.value:
      return self.value
    else:
      return self.right.get_max()



  def for_each(self, cb):
    pass