def function_external(x:int):
    def function_internal(y:int):
        import math
        return math.sqrt(math.fabs(x + y))
    return function_internal

result = outer_function(3)(-5)
print(result)
