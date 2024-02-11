# -> returns None to hit return type -> None
# -> returns str
def meow(n: int) -> str:
    """
    Meow n times.
    :param n: Numer of times to meow
    :type n: int
    :raise TypeError: If n is not an integer
    :return: A n string of meows, one per line
    :rtype: str
    """
    return "meow\n" * n


number: int = int(input("Enter a number: "))
meows: str = meow(number)
print(meows, end ="")


