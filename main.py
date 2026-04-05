def greet(name):
    if not name:
        return "Hello, World!"
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("World"))