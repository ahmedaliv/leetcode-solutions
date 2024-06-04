function lengthOfLongestSubstring(s: string): number {
    let maxLen = 0;
    let charSet = new Set();
    let l=0,r=0;
    while(l<s.length && r<s.length){
        if(!charSet.has(s[r])){
            charSet.add(s[r]);
            r++;
        }
        else {
           while(charSet.has(s[r])){
            charSet.delete(s[l]);
            l++;
           }
        }
        maxLen = Math.max(charSet.size,maxLen);
    }

    return maxLen;
};