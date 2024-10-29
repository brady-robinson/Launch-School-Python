value = 7

match value:
    case 5:
        print("value is 5")
    case 6:
        print("value is 6")
    case _:
        print("value is neither 5 nor 6")


# ternary expressions

print("Yes" if 5 < 4 else "No")