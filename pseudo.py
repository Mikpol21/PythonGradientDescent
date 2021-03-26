
def countNodesAtGivenDepth(Binary Tree tree, int level, int depth){
    if(tree == null)
        return 0
    if(depth == level)
        return 1
    if(depth != level)
        ret1 = countNodesAtGivenDepth(tree.getleft(), level, depth + 1)
        ret2 = countNodesAtGivenDepth(tree.getright(), level, depth + 1)
        return ret1 + ret2
}