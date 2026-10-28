# def make_counter(start_value=0):
#     count = start_value

#     def counter():
#         nonlocal count
#         count += 1
#         return count

#     return counter


# counter = make_counter(start_value=10)
# print(counter())
# print(counter())
# print(counter())





# import time
# from functools import wraps


# def log_execution(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f"Running {func.__name__}...")
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"Executed in {end_time - start_time:.2f} seconds.")
#         return result
#     return wrapper


# @log_execution
# def calculate_sum(a, b):
#     """Returns the sum of two numbers."""
#     time.sleep(1)
#     return a + b


# print(calculate_sum(10, 20))
# print(calculate_sum.__name__)
# print(calculate_sum.__doc__)




from functools import wraps


def require_role(allowed_role="admin"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user_role = kwargs.get("user_role", None)
            if user_role == allowed_role:
                return func(*args, **kwargs)
            else:
                print(f"Permission Denied: User is not an {allowed_role}.")
        return wrapper
    return decorator


@require_role(allowed_role="admin")
def delete_user(username, user_role=None):
    print(f"User '{username}' has been deleted.")


delete_user("john_doe", user_role="admin")
delete_user("john_doe", user_role="student")
