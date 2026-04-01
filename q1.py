def longest_palindromic_substring(s):
    longest = 0
    end = ""
    for i in range(len(s)):
        l = i
        r = i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > longest:
                longest = r - l + 1
                end = s[l:r+1]
            l -= 1
            r += 1
        l = i
        r = i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > longest:
                longest = r - l + 1
                end = s[l: r+1]
            l -= 1
            r += 1
    if longest < 2:
        return ""
    return end