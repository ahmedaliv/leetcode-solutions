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
// the main idea here is to know how can u uniquely identify each subtree and how to save them
// in this solution i used preorder and put each subtree in a string and saved it in a map

function findDuplicateSubtrees(root: TreeNode | null): Array<TreeNode | null> {
    const result: Array<TreeNode | null> = [];
    const subtreeMap: Map<string, number> = new Map();

    function traverse(sub: TreeNode | null):string{
        if(sub === null){
            return "#" // # -> null
        }
        const curSubSer = `${sub.val},${traverse(sub.left)},${traverse(sub.right)}`
        const count = subtreeMap.get(curSubSer) || 0;
        if(count === 1){
            result.push(sub);
        }

        subtreeMap.set(curSubSer, count + 1);
        return curSubSer;

    }
    traverse(root)
    return result;
}