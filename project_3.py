
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    list = random.choice(characters , k=length)
    password = "".join(list)
    return password


def main():

    print("WELCOME TO THE SECURE PASSWORD GENERATOR")

    length = int(input("Enter the desired length of your password: "))

    print(generate_password(length))


if __name__ == "__main__":
    main()