#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Name: Christine Outlaw
# Student ID: 1912737
# Email: CHAPMAN_EMAIL_HERE
# Course: PHYS220/MATH220/CPSC220 Fall 2017
# Assignment: HOMEWORK_OR_CLASSWORK_NUMBER

# Name: Baylee Mumma
# Student ID: 2274844
# Email: mumma103@mail.chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2017
# Assignment: CW4
###

"""Classwork 04
This classwork introduces numpy arrays and compares their performance to
python lists.
"""

import math
import numpy as np
import pandas as pd

def gen_gaussian_list(a, b, n=1000):
    """gen_gaussian_list(a, b, n=1000)
    Generate a discrete approximation of a Gaussian function, including its
    domain and range, stored as a pair of vanilla python lists.
    
    Args:
        a (float) : Lower bound of domain
        b (float) : Upper bound of domain
        n (int, optional) : Number of points in domain, defaults to 1000.
    
    Returns:
        (x, g) : Pair of lists of floats
            x  : [a, ..., b] List of n equally spaced floats between a and b
            g  : [g(a), ..., g(b)] List of Gaussian values matched to x
    """
    dx = (b-a)/(n-1)                         # spacing between points
    x = [a + k*dx for k in range(n)]         # domain list
    
    # Local implementation of a Gaussian function
    def gauss(x):
        return (1/math.sqrt(2*math.pi))*math.exp(-x**2/2)
    
    g = [gauss(xk) for xk in x]                  # range list
    return (x, g)


def gen_gaussian_array(a, b, n=1000):
    """gen_gaussian_array(a, b, n=1000)
    Generate a discrete approximation of a Gaussian function, including its
    domain and range, stored as a pair of numpy arrays.
    
    Args:
        a (float) : Lower bound of domain
        b (float) : Upper bound of domain
        n (int, optional) : Number of points in domain, defaults to 1000.
    
    Returns:
        (x, g) : Pair of numpy arrays of float64
            x  : [a, ..., b] Array of n equally spaced float64 between a and b
            g  : [g(a), ..., g(b)] Array of Gaussian values matched to x
    """
    x = np.linspace(a,b,n)
    def gauss(x):
        return (1/np.sqrt(2*np.pi))*np.exp(-x**2/2)
    g = gauss(x)
    return (x,g)

def gen_sinc_list(a, b, n=1000):
    """gen_sinc_list(a, b, n=1000)
    Generate a discrete approximation of a sinc function, including its
    domain and range, stored as a pair of vanilla python lists.
    
    Args:
        a (float) : Lower bound of domain
        b (float) : Upper bound of domain
        n (int, optional) : Number of points in domain, defaults to 1000.
    
    Returns:
        (x, s) : Pair of lists of floats
            x  : [a, ..., b] List of n equally spaced floats between a and b
            s  : [s(a), ..., s(b)] List of sinc values matched to x
    """
    dx = (b-a)/(n-1)                         # space between points
    x = [a + k*dx for k in range(n)]         # domain list
    
    # implementation of a sinc function
    def sinc(x):
        if x == 0:
            return 1
        else:
            return (math.sin(x)/x)

    s = [sinc(xk) for xk in x]                 
    return (x, s)

def gen_sinc_array(a, b, n=1000):
    """gen_sinc_array(a, b, n=1000)
    Generate a discrete approximation of a Sinc function, including its
    domain and range, stored as a pair of numpy arrays.
    
    Args:
        a (float) : Lower bound of domain
        b (float) : Upper bound of domain
        n (int, optional) : Number of points in domain, defaults to 1000.
    
    Returns:
        (x, s) : Pair of numpy arrays of float64
            x  : [a, ..., b] Array of n equally spaced float64 between a and b
            s  : [s(a), ..., s(b)] Array of sinc values matched to x
    """
    
    
    
    x = np.linspace(a,b,n)
    
    def sinc(x):
        if x==0:
            return 1
        else:
            return (np.sin(x)/x)
        
    s = np.vectorize(sinc(x))
    return (x,s)

def gen_sinf_list(a, b, n=1000):
    """gen_sinf_list(a, b, n=1000)
    Generate a discrete approximation of a sinf function, including its
    domain and range, stored as a pair of vanilla python lists.
    
    Args:
        a (float) : Lower bound of domain
        b (float) : Upper bound of domain
        n (int, optional) : Number of points in domain, defaults to 1000.
    
    Returns:
        (x, sf) : Pair of lists of floats
            x  : [a, ..., b] List of n equally spaced floats between a and b
            sf  : [sf(a), ..., sf(b)] List of sinf values matched to x
    """
    dx = (b-a)/(n-1)                         # spacing between points
    x = [a + k*dx for k in range(n)]         # domain list
    
    #List implementations of a frequency-chirped sine
    def sinf(x):
        if x == 0:
            return 1
        else:
            return (math.sin(1/x))
    
    f = [sinf(xk) for xk in x]                  
    return (x, f)




def gen_sinf_array(a, b, n=1000):
    """gen_sinf_array(a, b, n=1000)
    Generate a discrete approximation of a frequency-chirped sine wave function, including its
    domain and range, stored as a pair of numpy arrays.
    
    Args:
        a (float) : Lower bound of domain
        b (float) : Upper bound of domain
        n (int, optional) : Number of points in domain, defaults to 1000.
    
    Returns:
        (x, g) : Pair of numpy arrays of float64
            x  : [a, ..., b] Array of n equally spaced float64 between a and b
            f  : [f(a), ..., f(b)] Array of sinf values matched to x
    """
    x = np.linspace(a,b,n)
    def sinf(x):
        if x == 0:
            return 1
        else:
            return (np.sin(1/x))
    f = np.vectorize(sinf(x))
    return (x, f)



def main(a,b,n=1000):
    """main(a, b, n=1000)
    Main function for command line operation. Prints result of Gaussian to screen.
    
    Args:
        a (float) : Lower bound of domain
        b (float) : Upper bound of domain
        n (int, optional) : Number of points in domain, defaults to 1000.
    
    Returns:
        None
    
    Effects:
        Prints Gaussian to screen.
    """
    # You can unpack tuples as return values easily
    x, g = gen_gaussian_list(a,b,n)
    # The zip function takes two lists and generates a list of matched pairs
    for (xk, gk) in zip(x, g):
        # The format command replaces each {} with the value of a variable
        print("({}, {})".format(xk, gk))


# Protected main block for command line operation
if __name__ == "__main__":
    # The sys module contains features for running programs
    import sys
    # The sys.argv list variable contains all command line arguments
    #    sys.argv[0] is the program name always
    #    sys.argv[1] is the first command line argument, etc
    if len(sys.argv) == 4:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        n = int(sys.argv[3])
        main(a,b,n)
    elif len(sys.argv) == 3:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        main(a,b)
    else:
        print("Usage: cw04.py a b [n]")
        print("  a : float, lower bound of domain")
        print("  b : float, upper bound of domain")
        print("  n : integer, number of points in domain")
        exit(1)

