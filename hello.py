def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    name = input("Enter your name: ")
    if not name.strip():
        print("Name cannot be empty!")
    else:
        print(greet(name))
