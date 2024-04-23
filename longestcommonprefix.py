def longestCommonPrefix(v):
    ans = ""
    if not v:
        return ans

    v = sorted(v)
    first = v[0]
    last = v[-1]
    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return ans
        ans += first[i]
    return ans

strings = ["flower", "flow", "floight"]
print("Longest common prefix:", longestCommonPrefix(strings))