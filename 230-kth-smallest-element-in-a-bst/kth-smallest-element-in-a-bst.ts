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

function kthSmallest(root: TreeNode | null, k: number): number {
    let counter = 0; 
    let result: number | null = null; 
    
    function inOrderTraversal(node: TreeNode | null): void {
        if (node === null || result !== null) {
            return;
        }
        
        inOrderTraversal(node.left);
        
        counter++;
        if (counter === k) {
            result = node.val;
            return;
        }
        
       
        inOrderTraversal(node.right);
    }
    
    inOrderTraversal(root);
    return result as number; 
}