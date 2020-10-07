def increasingSubstrings(s):
    letters = s[0]
    output = []
    for i in range(1, len(s)):
        if ord(s[i]) - ord(s[i-1]) == 1:
            letters += s[i]
        else: 
            output.append(letters)
            letters = s[i]
    output.append(letters)
    return output