[+] root node - node with no parent
==/ node can have multiple children but one node cant have multiple parent

Binary Tree
children <= 2 or in inclusive range of [0,2]
 ___________
|Binary Tree|
|
|-> [1] Full Binary Tree node ---- with 0 or 2 children (no node can have 1 children only)
|-> [2] Complete Binary Tree  ---- leaf ke phle wale lvl tak saare nodes k children 2 ho aur leaf node wale lvl mei leftmost side se bhra ho
|-> [3] Perfect Binary Tree   --- if all leaf nodes are on same lvl
## Perfect binary tree is complete and full binary tree

[+] Leaf Nodes --- number of children == 0 
[+] Internal Nodes --- Nodes except Leaf Nodes

[++++]
!!property!!
	Leaf Nodes = Internal Nodes + 1       (Full Binary Tree)

 
lvl                 0   |  1   | 2    | 3 
children(siblings) 2**0 | 2**1 | 2**2 | 2**3
Sum of nodes(total number of Nodes) 2^0 + 2^1 +2^2 ... = 2^k = 2^(k+1) - 1

Perfect Binary Tree = number of nodes = 2^(k+1) -1 = leaf + Internal
L = I + 1

[--------------] 
[--]INDEXING[--]
[--------------]

                 0
              1     2 
            3   4  5  6
   P (parent) -> C1 , C2
    Addr. of C1 = 2p+1
    Addr. of C2 = 2p+2
    For example ., Node5 : 2*2 + 1


[--------------] 
[--TRAVERSALS--]
[--------------]

|data | Left | Right

              N
            L   R

[1] InOrder    ---\                     LNR
[2] PreOrder   --- |=> Stacks\          NLR
[3] PostOrder  ---/\                    LRN
[4] Level Order  ---> Queue


               a
            b     c
          d   e  

   InOrder : dbeac
   PreOrder : abdec
   PostOrder : debca

Level Order (Levelwise left to Right) : abcde

