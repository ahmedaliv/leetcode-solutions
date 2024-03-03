// we would use backtracking for generating all possible combinations
// so the key idea is to have parenthesis (open / close) equal to n 
// but how do we put them ?
//  we have 2 conditions
// the first one is to have open count < n like this ((( ,
//  and any addition of another open parenthesis would result in a wrong parenthesis
// so we can only do this ( or (( or ((( in case of n ===3 
// and only then we can add close parenthesis 
// the second condition to help us generate only valid parenthesis is to have close count < open count
// like this (() to be able to add a closed parenthesis -> (()), and any addition of close  would result in a wrong parenthesis 
function generateParenthesis(n: number): string[] {
    const result: string[] = [];

    function backtrack(str: string, open: number, close: number) {
        if(open===n && close===n) {
            result.push(str);
            return;
        }
        if (open < n) {
            backtrack(str + '(', open + 1, close);
        }
        if (close < open) {
            backtrack(str + ')', open, close + 1);
        }
    }

    backtrack('', 0, 0);
    return result;
};