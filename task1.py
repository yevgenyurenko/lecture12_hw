def choose_func(nums: list, func1, func2):
    
    all_positive = True

    for num in nums:
        if num <= 0:
            all_positive = False
            break

    if all_positive:
        return func1(nums)  
    else:
        return func2(nums)  