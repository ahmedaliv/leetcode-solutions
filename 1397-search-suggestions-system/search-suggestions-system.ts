// Trie solution
class TrieNode {
    children: Map<string, TrieNode>;
    suggestions: string[];

    constructor() {
        this.children = new Map();
        this.suggestions = [];
    }
}

class Trie {
    root: TrieNode;

    constructor() {
        this.root = new TrieNode();
    }

    insert(word: string) {
        let node = this.root;

        for (const char of word) {
            if (!node.children.has(char)) {
                node.children.set(char, new TrieNode());
            }

            node = node.children.get(char)!;
            node.suggestions.push(word);
            node.suggestions.sort().splice(3);
        }
    }

    search(prefix: string): string[] {
        let node = this.root;

        for (const char of prefix) {
            if (!node.children.has(char)) {
                return [];
            }

            node = node.children.get(char)!;
        }

        return node.suggestions;
    }
}

function suggestedProducts(products: string[], searchWord: string): string[][] {
    const trie = new Trie();

    for (const product of products) {
        trie.insert(product);
    }

    const result: string[][] = [];
    let prefix = '';

    for (let i = 0; i < searchWord.length; i++) {
        prefix += searchWord[i];
        result.push(trie.search(prefix));
    }

    return result;
}
