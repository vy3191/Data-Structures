Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?
   Ans: Constant O(1)
2. What is the runtime complexity of `dequeue`?
   Ans: Constant O(1)
3. What is the runtime complexity of `len`?
   Ans: Constant O(1)
## Binary Search Tree

1. What is the runtime complexity of `insert`? 

2. What is the runtime complexity of `contains`?

3. What is the runtime complexity of `get_max`? 

## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?
   Ans:- Constant o(1)
2. What is the runtime complexity of `ListNode.insert_before`?
   Ans:- Constant o(1)
3. What is the runtime complexity of `ListNode.delete`?
   Ans:- Constant o(1)
4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?
   Ans:- Constant o(1) 
5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
   Ans:- Constant o(1)
6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
   Ans:- Constant o(1)
7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
   Ans:- Constant o(1)
8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?
   Ans:- Constant o(1)
9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?
   Ans:- Constant o(1)
10. What is the runtime complexity of `DoublyLinkedList.delete`?
   Ans:- Constant o(1)
    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?
    Ans:- Javascript Array.splice method changes the original array. When we delete/add the items to the array using splice method, items in the array will be shifted to the right or left. So the run time complexity is linear in the worst case i.e., O(n)

    Where as the linked list's delete runtime complexity is constant i.e., O(1)