def palindrome(s):
    return s == s[::-1]
if __name__ == '__main__':
    print(__name__, '__main__')
    s = input("Enter a strng: ")
    if palindrome(s):
        print("yay a ....")
    else:
        print("oh no...")
