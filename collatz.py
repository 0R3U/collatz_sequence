def collatz(n):
    """Prints the Collatz sequence for a given positive integer n."""
    while n != 1:
        print(n)
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    print(n)



def main():

    message = "Please enter a positive integer."
    print(message)
    while True:
        try:
            n = int(input(">>> "))
            if n <= 0:
               print("Please only enter a positive integer!")
            else:
               break
        except ValueError:
            print("Please only enter a positive integer!")
        

      

    collatz(n)
    

if __name__ == '__main__':
    main()
        