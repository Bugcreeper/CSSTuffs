import numpy as np
np.random.seed(1920)

def problem1():
    arr1 = np.arange(10,50))
    arr2 = np.zeros([3,4])
    identity = np.identity(3)
    linspace_arr = np.linspace(0,5,10)
    random_arr = np.random.rand(2,5)
    return arr1, arr2, identity, linspace_arr, random_arr

def problem2():
    arr_a = np.array([[1,2,3], [4,5,6], [7,8,9]])
    arr_b= np.array[10,20,30]
    result_add = arr_a + arr_b
    result_multiply = arr_a * arr_b
    result_square = arr_a ** 2
    column_means = np.mean(arr_a, axis=0)
    centered_arr = arr_a - column_means
    return result_add, result_multiply, column_means, centered_arr
def problem3():
    arr = np.arange(1,26).reshape(5,5)
    third_row = arr[2, :]
    last_column = arr[:, 4]
    center_subarray = arr[1:3,1:3]
    greater_than_15 = arr[arr > 15]
    arr_copy = arr.copy()
    for prt in arr_copy:
        if prt%2 == 0:
            prt = prt-1
    return third_row, last_column, center_subarray, greater_than_15, arr_copy

def problem4():
    scores = np.array([[85, 90, 78, 92],
        [79, 85, 88, 91],
        [92, 88, 95, 89],
        [75, 72, 80, 78],
        [88, 91, 87, 94]])
    student_averages = np.mean(scores, axis=1)
    test_averages = np.mean(scores, axis=0)
    student_max_scores = np.max(scores, axis=1)
    test_std = np.std(scores, axis=0)
    high_performers = student_averages[student_averages>85]
    return student_averages, test_averages, student_max_scores, test_std, high_performers

def problem6():
    import time
    size = 100000
    python_list = list(range(size))
    numpy_array = np.arange(size)
    start_time = time.time()
    list_result = [x**2 for x in python_list]
    list_time = time.time() - start_time
    start_time = time.time()
    array_result = numpy_array**2
    numpy_time = time.time() - start_time
    speedup = list_time/numpy_array
    return  {
        'list_time': list_time,
        'numpy_time': numpy_time,
        'speedup': speedup,
        'conclusion': f"NumPy is {speedup:.1f}x faster than Python lists for this operation"
        }

#test = problem1()
#print(test)