import timeit
def my_function():
    pass
def sum_with_for_loop(lst):
    total = 0
    for num in lst:
        total += num
    return total
def sum_with_sum_function(lst):
    return sum(lst)

t = timeit.Timer(lambda: my_function())

time_taken = t.timeit(number=1000) / 1000

print("Tiempo de ejecución promedio: {:.6f} segundos".format(time_taken))

numbers = list(range(1, 10001))
time_taken1 = timeit.timeit(lambda: sum_with_for_loop(numbers), number=1000)
time_taken2 = timeit.timeit(lambda: sum_with_sum_function(numbers), number=1000)

print("Tiempo de ejecución con for loop: {:.6f} segundos".format(time_taken1))
print("Tiempo de ejecución con sum() function: {:.6f} segundos".format(time_taken2))