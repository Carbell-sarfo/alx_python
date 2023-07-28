def fibonacci_sequence(n):
    if n <= 0:
        return []

    fibonacci_list = [0, 1]

    for i in range(2, n):
        next_fibonacci = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(next_fibonacci)

    return fibonacci_list[:n]