def print_table(num):
    for i in range(1, 11):
        end_char = '->' if i < 10 else ''
        print(i * num, end=end_char)
    print()


def main():
    print("Hello from githubpoc!")
    print_table(2)
    print_table(3)
    

if __name__ == "__main__":
    main()
