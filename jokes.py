import pyjokes

def tell_a_joke():
    # Generate and print a random programming joke
    joke = pyjokes.get_joke()
    print(joke)

if __name__ == "__main__":
    print("Here's a programming joke for you:")
    tell_a_joke()