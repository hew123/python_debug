class node():
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value
        

def isBinaryTree(node,min,max):
    if node == None:
        return True
    else:
        '''
        if (node.right != None) and node.right.value < node.value and node.right.value > max:
            return False
        
        if (node.left != None) and node.left.value > node.value and node.left.value < min:
            return False
        '''
        
        #print("the range is " + str(min)+ "," + str(max))
        print(f"the range is {min} , {max}")
        if node.value < min or node.value > max:
            return False
        
        
        if node.left != None:
            temp = max
            max = node.value
            if not isBinaryTree(node.left,min,max): return False
            max = temp
            
        if node.right != None:
            temp = min
            min = node.value
            if not isBinaryTree(node.right,min,max): return False
            min = temp
 
        return True
            
#standard
def isBST(node, range_):
    if node == None:
        return True
    else:
        min_ , max_ = range_
        if node.value < min_ or node.value > max_:
            return False

        return isBST(node.left, (min_,node.value-1)) \
            and isBST(node.right,(node.value+1, max_))


def main():
    a = node(5)
    b = node(3)
    c = node(6)
    a.left = b
    a.right = c
    d = node(10)
    b.right = d
    print(isBinaryTree(a,-1,10000))
    print(isBST(a,(-1,100000)))
    
main()


"""    
       5
 3.        6
   4

"""
