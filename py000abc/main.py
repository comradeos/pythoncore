import collections
import re


def main():
    a = "Inna"
    c = collections.Counter(a)
    # print(c)
    sent = "Hello, world! How are you?"
    words = re.findall("\w+", sent)
    print(words)
    pass


if __name__ == '__main__':
    main()
