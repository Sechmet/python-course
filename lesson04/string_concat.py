# String concatenation

NUMBER: int = 1980
FLOAT_NUMBER: float = 42.0

STRING: str = "abcde"

MY_LIST: list = []

MY_LIST_OF_STRINGS1: list[str] = []

MY_LIST_OF_STRINGS2: list[str] = [
    "first string",
    "second string",
]

# result = "abc" + "efg" + NUMBER
# result = "1980" + NUMBER
result = "1980" + str(NUMBER)
result = f"{STRING} {NUMBER:08}"
result = f"{STRING} {FLOAT_NUMBER:010.4f}"

result = "%s %s" % (STRING, NUMBER)

result = f"{STRING} {NUMBER:08}"
# Format "NUMBER" (=1980) with zero-padding to eight chars.
# abcde 00001980
print(result)

result = f"{STRING} {NUMBER:02}"
# Format "NUMBER" (=1980) with zero-padding to 2 chars.
# abcde 1980
print(result)
