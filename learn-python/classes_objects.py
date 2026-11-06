def short_code(name: str) -> str:
    return name.lower().replace(" ", "-")


print(short_code(232))
