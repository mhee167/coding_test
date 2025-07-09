def preorder(nodes,idx):
    if idx<len(nodes): #nodes 길이보다 작을 때만 확인
        ret = str(nodes[idx])+ " "
        ret += preorder(nodes,idx*2+1)
        ret += preorder(nodes, idx*2+2)
        return ret
    else:
        return ""

def inorder(nodes,idx):
    if idx< len(nodes):
        ret= inorder(nodes,idx*2+1)
        ret+=str(nodes[idx])+ " "
        ret+= inorder(nodes, idx*2+2)
    else:
        return ""
    
def postorder(nodes,idx):
    if idx<len(nodes):
        ret=postorder(nodes,idx*2+1)
        ret+= postorder(nodes,idx*2+2)
        ret+=str(nodes[idx])+ " "
    else: 
        return ""
    
def solution(nodes):
    return [
        preorder(nodes,0)[:-1] #마지막 요소 제거
        inorder(nodes,0)[:-1]
        postorder(nodes,0)[:-1],

    ]
