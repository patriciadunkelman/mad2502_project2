import numpy as np

def get_escape_time(c: complex, max_iterations: int) -> int | None:
    """
    Function: The function returns the number of iterations it takes for c to escape or None if c does not escape in max_iterations.

    Args:
        c (complex): Complex number
        max_iterations (int): Maximum number of iterations before None is returned

    Returns:
        int or None: Iterations it took for c to escape or None
    """

    z = c #sets z to be c
    num_calls = 0 #creates num_calls
    while num_calls <= max_iterations: #runs loop while the iterations do not exceed max
        if abs(z) > 2: #only runs the following if the magnitude is more than 2 and thus trends towards infinity
            return num_calls #returns the escape time
        else:
            z = np.power(z,2) + c #changes zn to zn+1
            num_calls += 1 #increases the number of calls
    return None #if num_calls becomes greater than max_iters before it returns the calls, then it returns None

def get_complex_grid(
    top_left: complex,
    bottom_right: complex,
    step: float
) -> np.ndarray:
    """
    Function: This function will return an array whose contents will be complex numbers evenly spaced between `top_left` and (but not including) `bottom_right`.

    Args:
        top_left (complex): Top left coordinate
        bottom_right (complex): Bottom right coordinate
        step (float): Step size

    Returns:
        np.ndarray: Array of complex numbers

    References:
        https://www.geeksforgeeks.org/complex-numbers-in-python-set-1-introduction/#
    """

    real = np.arange(top_left.real, bottom_right.real, step) #creates array for the real values
    imag = np.arange(top_left.imag, bottom_right.imag, -step) #creates array for the imaginary values
    imag = imag.reshape(len(imag), 1) #turns imaginary values to column

    ret = real + 1j * imag
    return ret

def get_escape_time_color_arr(
    c_arr: np.ndarray,
    max_iterations: int
) -> np.ndarray:
    """
    Function: The function will return an array of the same shape as c_arr with color values in [0,1] according to the escape time of each c-value.

    Args:
        c_arr (np.ndarray): Array of complex numbers
        max_iterations (int): Maximum number of iterations before None is returned

    Returns:
        np.ndarray: Array of floats determined by the escape time of each c-value
    """
    color_arr = np.zeros(c_arr.shape, dtype =np.float64) # create array with same shape as c_arr

    for index, val in np.ndenumerate(c_arr): # iterate through each point on the grid
        et = get_escape_time(val, max_iterations)
        if et is None: #Checks if the point did not escape
            color_arr[index] = 0.0 # Set the point to black
        else: # if point does escape, do the following
            color_arr[index] = (max_iterations - et + 1) / (max_iterations + 1) # Use formula to calculate color
    return color_arr #return final array


def get_julia_color_arr(
    c_arr: np.ndarray,
    constant: complex,
    max_iterations: int
) -> np.ndarray:
    """
    Function: The function uses the same logic as the Mandelbrot functions, but uses the Julia iterative formula to return a Julia Set.

    Args:
        c_arr (np.ndarray): Array of complex numbers
        constant (complex): A constant complex number to be used in every iteration
        max_iterations (int): Maximum number of iterations before None is returned

    Returns:
        np.ndarray: Array of floats determined by the escape time of each c-value
    """

    color_arr = np.zeros(c_arr.shape, dtype =np.float64) # creates zeros array with shape of c_arr
    for index, val in np.ndenumerate(c_arr): # iterates through each point on the grid
        z = val # set initial value of z to the current complex value

        for et in range(1, max_iterations + 1): # Loop to determine escape times
            if abs(z) > 2: #Check if magnitude is greater than 2, if so, then it escapes
                color_arr[index] = (max_iterations - et + 1) / (max_iterations + 1) # Use formula to calculate color
                break #exit loop when escape time is reached
            z = z**2 + constant #update z using Julia set formula
    return color_arr # return final array







