def main(s):
    """
    A string of numbers is given. Find how many odd numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    x=0
    y=0
    while x<len(s):
        if int(s[x])%2==1:
            y+=1
        x+=1
    return y
print(main("1567534"))