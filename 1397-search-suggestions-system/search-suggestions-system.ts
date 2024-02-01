// brute force solution
function suggestedProducts(products: string[], searchWord: string): string[][] {
    products.sort(); 

    const result: string[][] = [];
    let prefix = '';

    for (let i = 0; i < searchWord.length; i++) {
        prefix += searchWord[i];
        
        const suggested = products.filter(product => product.startsWith(prefix)).slice(0, 3);
        result.push(suggested);
    }

    return result;
}