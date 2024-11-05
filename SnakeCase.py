def camel_to_snake(camel_case):

    snake_case = ""
    for char in camel_case:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char
    return snake_case
camel_case_input = input("Enter a camelCase variable: ")
print("snake_case:", camel_to_snake(camel_case_input))
