class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

# все тут
def tree_by_levels(node):
    A = []
    if not node:
        return A
    Q = [node]
    while Q:
        for i in range(len(Q[:2])):
            if Q[i].left:
                Q += [Q[i].left]
            if Q[i].right:
                Q += [Q[i].right]
        A.append(Q[0].value)
        Q = Q[1:]

    return A

if __name__ == '__main__':
    tree = Node(Node(None, None, 2), Node(None, None, 3), 1)
    tree3 = Node(None,None,None)
    P = [tree]
    #print(P[0].left)
    #print(tree.left)
    tree2 = Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1)

   # print(tree2.left.value)
    print(tree_by_levels(tree2))


# print(tree2.getRootVal())
    #print(tree2.right.right.getRootVal())
'''

 def insertLeft(self, nL, nR, nn):
        #if self.left == None:
         #   self.left = Node(nL, nR, nn)
        #else:
        #buf = self.left
            #buf.left = self.left
        self.left = Node(nL, nR, nn)

    def insertRight(self, nL, nR, nn):
        if self.left == None:
            self.right = Node(nL, nR, nn)
        else:
            buf = Node(nL, nR, nn)
            buf.right = self.right
            self.right = buf

    def getRootVal(self):
        return self.value

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

    def getTree(self):
        l = self.left
        r = self.right
        return l, r, self.value
def newTree(r):
    return [r,[],[]]



def insertLeft(tree,newBranch):
    buf=tree.pop(1)
    if buf:
        tree.insert(1,[newBranch,[buf],[]])
    else:
        tree.insert(1,[newBranch,[],[]])

def insertRight(tree,newBranch):
    buf=tree.pop(2)
    if buf:
        tree.insert(2,[newBranch,[],[buf]])
    else:
        tree.insert(2,[newBranch,[],[]])

def insertNode(tree, item):
    if tree==None:
        pass

def getRootVal(tree):
    
    return tree[0]

def setRootVal(tree,newRoot):
    
    tree[0]=newRoot

def insertItem(tree, item):
    if item < getRootVal(tree):
        if len(tree[1])<1:
            insertLeft(tree,item)
        else: insertItem(getLeftChild(tree),item)
    else:
        if len(tree[2])<1:
            insertRight(tree,item)
        else: insertItem(getRightChild(tree),item)

def downlod():
    with open('input.txt') as inf:
        array = list(map(int,inf.readline().split()))
        #array = [i for i,_ in groupby(array2)]
    return array

def createTree(array):
    repeat=[]
    myTree = newTree(array[0])
    i=1
    repeat.append(array[0])
    while array[i]>0:
        #insertItem(myTree, array[i])
        if array[i] not in repeat:
            insertItem(myTree,array[i])
            repeat.append(array[i])
        i+=1
    return myTree

def getLeftChild(tree):
    
    return tree[1]

def getRightChild(tree):
    
    return tree[2]



def getDepth(tree):
    if tree==None:
        return 0
    left=1
    right=1
    if getLeftChild(tree):
        left = 1 + getDepth(getLeftChild(tree))
    else: left -= 1
    if getRightChild(tree):
        right = 1 + getDepth(getRightChild(tree))
    else: right -= 1

    if left > right:
        maxi = left
    else: maxi = right
    return maxi;


myTree = createTree(downlod())

outf=open('output.txt','w')
print(getDepth(myTree)+1,file=outf)


tree=BinaryTree(2)
print(tree.getRootVal())
tree.insertLeft(3)
tree.insertRight(4)
tree.leftChild.insertLeft(5)
print(tree.getRightChild().getRootVal())
print(tree.getLeftChild().getLeftChild().getRootVal())




class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            buf=BinaryTree(newNode)
            buf.leftChild = self.leftChild
            self.leftChild = buf

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            buf = BinaryTree(newNode)
            buf.rightChild = self.rightChild
            self.rightChild = buf

    def getRootVal(self):
        return self.key

    def setRootVal(self, newVal):
        self.key = newVal

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

tree=BinaryTree(2)
print(tree.getRootVal())
tree.insertLeft(3)
tree.insertRight(4)
tree.rightChild.insertRight(9)
tree.leftChild.insertLeft(5)
print(tree.getRightChild().getRootVal())
print(tree.getLeftChild().getLeftChild().getRootVal())
'''