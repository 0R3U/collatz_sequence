import matplotlib.pyplot as plt


def get_positive_integer():
    while True:
        user_input = input("Please enter a positive integer or 'q' to quit: ")
        if user_input.lower() == 'q':
            quit()  # Exit the program if 'q' is entered
        try:
            n = int(user_input)
            if n <= 0:
                raise ValueError("Please enter a positive integer!")
            return n
        except ValueError as e:
            print(e)


def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return tuple(sequence)


def plot_collatz_sequence(sequence):
    plt.style.use("ggplot")
    plt.plot(sequence, marker='o')
    plt.xlabel('Iteration')
    plt.ylabel('Value')
    plt.title('Collatz Sequence')
    plt.grid(True)
    plt.show()


def main():
    while True:   
        n = get_positive_integer()
        sequence = collatz_sequence(n)
        print("Collatz sequence:", sequence)
        plot_collatz_sequence(sequence)

if __name__ == '__main__':
    main()
