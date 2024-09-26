# Data-structure
Heap- is a data structure that is a complete binary tree and satisfies the heap property where for every node the value of its children is less than or equal to its own value

HEAP PROPERTIES
Heaps are implemented in an array.
Parent node in Max-heap tree has a larger value than its children nodes.
Parent node in min-heap tree has a value smaller than its children nodes.
All levels in a heap should be full.

ADVANTAGE OF HEAPS
Requires less memory compared to other data structures.
Stores elements in a complete binary tree structure.
Guaranteed access to min/max elements.
Fast insertion and deletion of elements.
Fast access to highest-priority elements.

DISADVANTAGE OF HEAPS
Cannot search for a specific element in a heap.
Managing memory allocated for the heap can be a challenge.
Order of equal elements may not be preserved when constructing a heap.
It is not flexible because it is designed to maintain a certain order of elements.

ACCESSING ITEMS IN HEAPS

Insertion
Add the new element  to the bottom-rightmost position
Compare its values to the parent node
Repeat the above step till the heap property gets satisfied

Deletion
Remove the last element and place it at the root
Compare this new root with child nodes
If the heap is a max heap, swap the root with the greater child if the child>root. If the heap is a min-heap, swap the root with its smaller child if the child is smaller than the root.
Repeat the above step till the property is restored

