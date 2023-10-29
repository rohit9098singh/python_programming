import multiprocessing as mp
import time
import math

result_a = []
result_b = []
result_c = []
result_d = []

def makecalculation_1(numbers):
    for number in numbers:
        result_a.append(math.sqrt(number**3))

def makecalculation_2(numbers):
    for number in numbers:
        result_b.append(math.sqrt(number**4))

def makecalculation_3(numbers):
    for number in numbers:
        result_c.append(math.sqrt(number**5))

if __name__ == '__main__':

    number_list = list(range(10000))

    p1 = mp.Process(target=makecalculation_1, args=(number_list,))
    p2 = mp.Process(target=makecalculation_2, args=(number_list,))
    p3 = mp.Process(target=makecalculation_3, args=(number_list,))

    start = time.time()
    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()
    end = time.time()
    print("The time taken by multiprocessing is", end - start)

    temp_a=result_a
    temp_b=result_b
    temp_c=result_c

    start = time.time()
    makecalculation_1(number_list)
    makecalculation_2(number_list)
    makecalculation_3(number_list)
    end = time.time()
    print("The time taken without multiprocessing is", end - start)

    print(temp_a==result_a)
    print(temp_a==result_b)
    print(temp_a==result_c)
