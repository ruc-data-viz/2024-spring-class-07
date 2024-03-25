import numba as nb
import numpy as np

@nb.vectorize
def mandelbrot(c, max_iterations):
    z = 0.0j
    iterations = 0
    while abs(z) < 2.0 and iterations < max_iterations:
        z = z**2 + c
        iterations += 1
    return iterations

def mcompute(x_min, x_max, y_min, y_max, steps, max_iterations):
    step = (x_max - x_min) / steps
    dx, dy = np.indices((steps, steps))
    dx = x_min + step * dx
    dy = y_min + step * dy
    
    data = np.array(np.vectorize(complex)(dx.T, dy.T))
    
    return mandelbrot(data, max_iterations)

@nb.vectorize
def julia(z, c, max_iterations):
    iterations = 0
    while abs(z) < 2.0 and iterations < max_iterations:
        z = z**2 + c
        iterations += 1
    return iterations

def jcompute(c, x_min, x_max, y_min, y_max, steps, max_iterations):
    step = (x_max - x_min) / steps
    dx, dy = np.indices((steps, steps))
    dx = x_min + step * dx
    dy = y_min + step * dy
    
    data = np.array(np.vectorize(complex)(dx.T, dy.T))
    
    return julia(data, c, max_iterations)