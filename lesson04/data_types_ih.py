first = "Irene"
last = 4.8

print(type(first))
print("")
print(type(last))
print(isinstance(first, str))
print(isinstance(last, str))

# Declare and initialise a variable with "type hints":
BEST_PRICE: int = 80

# Declare and initialise a variable with "constructor":
SOME_PRICE = int(80)

FUTURE_PRICE: int | None = None
