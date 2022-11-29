def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    x=0
    y=0
    while x<len(s):
        if s[x].isdigit() or s[x].isalpha():
            y+=1
        x+=1
    return len(s)-(y)
print(main("#hashtag@$"))