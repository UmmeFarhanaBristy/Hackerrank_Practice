if __name__ == '__main__':
    s = input()

    # Print True if  has any alphanumeric characters. Otherwise, print False.
    print(any(x.isalnum() for x in s))

    # Print True if  has any alphabetical characters. Otherwise, print False.
    print(any(x.isalpha() for x in s))

    # Print True if  has any digits. Otherwise, print False.
    print(any(x.isdigit() for x in s))

    # Print True if  has any lowercase characters. Otherwise, print False.
    print(any(x.islower() for x in s))

    # Print True if  has any uppercase characters. Otherwise, print False.
    print(any(x.isupper() for x in s))
