function numDecodings(s: string): number {
    let memo = {};

    function decodeWays(index) {
        if (index in memo) return memo[index];
        if (index === s.length) return 1;
        if (s[index] === '0') return 0;
        if (index > s.length) return 0;

        let ways = decodeWays(index + 1);
        if (index + 1 < s.length && parseInt(s.substring(index, index + 2)) <= 26) {
            ways += decodeWays(index + 2);
        }

        memo[index] = ways;
        return ways;
    }

    return decodeWays(0);
}
