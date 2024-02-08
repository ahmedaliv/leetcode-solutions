function minEatingSpeed(piles: number[], h: number): number {
    let l = 1;
    let r = Math.max(...piles);  
    while (l <= r) {
        let mid = Math.floor((l + r) / 2);
        let hours_needed = piles.reduce((acc, pile) => acc + Math.ceil(pile / mid), 0);
        if (hours_needed <= h) {
            r = mid - 1;
        } else {
            l = mid + 1;
        }
    }
    return l;
}
