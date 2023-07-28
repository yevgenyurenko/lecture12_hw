def count_local_variables(func):
    num_locals = func.__code__.co_nlocals

    return num_locals

