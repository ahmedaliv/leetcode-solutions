function maxProfit(prices: number[]): number {
    let maxProfit = 0;
    let minDay = prices[0];
    for (let i=1; i<prices.length;i++){
        if(prices[i]<minDay){
            minDay = prices[i];
            continue;
        }
        maxProfit = Math.max(maxProfit,prices[i]-minDay);
    }
    return maxProfit;
};