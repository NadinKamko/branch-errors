def is_polindrome(s: str) -> bool:
    s = s.lower().replace(" ", "")
    return s ==s[::-1]
print(is_polindrome("А роза упала на лапу Азора"))
print((is_polindrome("Это не палиндром")))




