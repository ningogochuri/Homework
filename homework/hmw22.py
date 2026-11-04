# import time
# import multiprocessing
# from concurrent.futures import ProcessPoolExecutor


# def factorial(n):
#     result = 1

#     for i in range(1, n + 1):
#         result *= i

#     return result


# def multiply_range(numbers):
#     start, end = numbers
#     result = 1

#     for i in range(start, end + 1):
#         result *= i

#     return result


# if __name__ == '__main__':

#     n = 100000

#     start = time.time()

#     single_result = factorial(n)

#     end = time.time()

#     single_time = end - start

#     print("Single-process time:", single_time)


#     start = time.time()

#     num_processes = multiprocessing.cpu_count()

#     chunk_size = (n + num_processes - 1) // num_processes

#     numbers = [
#         (i, min(i + chunk_size - 1, n))
#         for i in range(1, n + 1, chunk_size)
#     ]

#     with ProcessPoolExecutor(max_workers=num_processes) as executor:
#         results = list(executor.map(multiply_range, numbers))

#     multi_result = 1

#     for result in results:
#         multi_result *= result

#     end = time.time()

#     multi_time = end - start

#     print("Multiprocessing time:", multi_time)

#     print("Results are equal:", single_result == multi_result)

#     print("Single-process:", single_time, "seconds")
#     print("Multiprocessing:", multi_time, "seconds")




# import threading
# import time
# import requests


# def fetch_data(post_id):
#     url = f'https://jsonplaceholder.typicode.com/posts/{post_id}'

#     response = requests.get(url, timeout=10)
#     response.raise_for_status()

#     print(response.json())


# start = time.time()

# thread_list = []

# for i in range(1, 101):
#     thread = threading.Thread(target=fetch_data, args=(i,))
#     thread_list.append(thread)

# for thread in thread_list:
#     thread.start()

# for thread in thread_list:
#     thread.join()

# end = time.time()

# print(f"Total time taken: {end - start} seconds")





import time
import requests
from concurrent.futures import ThreadPoolExecutor


def fetch_data(post_id):
    url = f'https://jsonplaceholder.typicode.com/posts/{post_id}'

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    return response.json()


start = time.time()

post_ids = range(1, 101)

with ThreadPoolExecutor(max_workers=10) as executor:
    results = list(executor.map(fetch_data, post_ids))

end = time.time()

thread_pool_time = end - start

print("ThreadPoolExecutor time:", thread_pool_time)
print("Total posts:", len(results))
