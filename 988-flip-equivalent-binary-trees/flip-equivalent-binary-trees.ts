/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function flipEquiv(root1: TreeNode | null, root2: TreeNode | null): boolean {
    // if one or both are null
    if(!root1 || !root2 ){
        return !root1 && !root2;
    }
    // check roots
    if(root1.val !== root2.val){
        return false;
    }
    // check if the two subtrees are equivalent without any flips
    const noFlip = flipEquiv(root1.left,root2.left)  && flipEquiv(root1.right,root2.right);
    // check if euqivalent with flips
    const flip = flipEquiv(root1.left,root2.right)  && flipEquiv(root1.right,root2.left);
    // return whatever is true
    return noFlip || flip ;
};