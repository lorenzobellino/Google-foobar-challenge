
def find_subtree(h,node,root):
    if root == node:
        return -1

    if (root-2**(h-1)==node):
        parent=root
        return parent
    else:
        if (root-1==node):
            parent=root
            return parent
        else:
            if (root-(2**(h-1))>node):
                new_root=root-(2**(h-1))
                new_h = h-1
                return find_subtree(new_h,node,new_root)
            else:
                new_root=root-1
                new_h=h-1
                return find_subtree(new_h,node,new_root)
    

def answer(h,q):

    parents=[]
    for i in q:
        root=(2**h)-1
        parent = find_subtree(h,i,root)
        parents.append(parent)

    return parents
