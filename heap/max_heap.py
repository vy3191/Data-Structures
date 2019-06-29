class Heap:
  def __init__(self):
    self.storage = []
    self.size = 0

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage)-1)
    self.size += 1
    

  def delete(self):
    # if there are no nodes in the storage
    if len(self.storage) == 0:
      return None
    # if there is exactly only one node in the storage  
    elif len(self.storage) == 1:
      self.size -=1
      return self.storage.pop(0)
    # if there are more than one node in the storage  
    else:
      # Grab the last element in the storage
      last = self.storage.pop()
      # assign it as a first node in the storage
      self.storage[0] = last
      # tickle down the tree
      self._sift_down(0)
      self.size -=1
      return self.storage[0]
    
  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return self.size

  def _bubble_up(self, index):
    # 1. Check to see if the index is greater than zero
    while index > 0:

    # 2. Grab the parent index
      parent = (index-1)//2
    # 3. Check if current value is greater than or less than parent value
      if self.storage[index] > self.storage[parent]:
        self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
        index = parent
         # a. If current is greater than
         # b. Swap
    # 4. Current is less than parent
      else:
        break
         # a. Leave it alone - break     

  def _sift_down(self, index):
    left = (index *2) + 1
    right = (index * 2) + 2
    max = index

    if self.storage[max] < self.storage[left]:
      max = left
    if self.storage[max] > self.storage[right]:
      max = right
    if max != index:
      max, index = index, max
      self._sift_down(max)    

