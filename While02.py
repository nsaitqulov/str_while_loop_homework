def main(s):
    """
    A variable of type str is given. Find how many letters it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    x=0
    y=0
    while x<len(s):
        if s[x].isalpha():
            y+=1
        x+=1

    return y

print(main("Python 2022"))
    