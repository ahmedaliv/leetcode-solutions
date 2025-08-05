def length_of_longest_substring_k_distinct(s: str, k: int) -> int:
    """
    Returns the length of the longest substring with at most k distinct characters.

    Time Complexity: O(n)
        - Each character is processed at most twice (once by right, once by left).
    Space Complexity: O(k)
        - The hashmap stores at most k distinct characters.
    """
    from collections import defaultdict

    n = len(s)
    if k == 0 or n == 0:
        return 0

    left = 0
    max_len = 0
    char_freq = defaultdict(int)

    for right in range(n):
        char_freq[s[right]] += 1

        while len(char_freq) > k:
            char_freq[s[left]] -= 1
            if char_freq[s[left]] == 0:
                del char_freq[s[left]]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len
