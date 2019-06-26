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
    pass

     
       


  def get_max(self):
    pass

  def for_each(self, cb):
    pass