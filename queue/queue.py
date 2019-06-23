class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    # Answer:- We use linked_lists for constructing Queue
    self.storage = []

  def enqueue(self, item):
    self.storage.append(item)
    self.size +=1
  
  def dequeue(self):
    if self.size < 1:
      return None
    else:
      self.size -= 1
      return self.storage.pop(0)

  def len(self):
    return len(self.storage)
