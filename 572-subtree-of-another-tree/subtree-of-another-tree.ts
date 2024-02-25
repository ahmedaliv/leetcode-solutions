function isSubtree(root: TreeNode | null, subRoot: TreeNode | null): boolean {
    if (root === null && subRoot === null) {
        return true; 
    }
    if (root === null || subRoot === null) {
        return false; 
    }
    return isSameTree(root, subRoot) || isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
}

function isSameTree(p: TreeNode | null, q: TreeNode | null): boolean {
    if (p === null && q === null) {
        return true; 
    }
    if (p === null || q === null) {
        return false; 
    }
    return p.val === q.val && isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
}
