# Authors: Peter Shultz, Sam Freedman, Anna Hayman, Sagar Singichetti
# uniqnames: pshultz, samjfree, amhayman, singichs
# Date: December 1, 2014
# Purpose: generation.py is the location of every statistical method (generating random numbers, implementation of various statistical distributions)
# Description: Returns various values via IGM and other varous statistical distributions depending on the function that is called (Bernoulli, Binomial, Geometric, Exponential, Normal)

import sys
import random
import math

"""
Requires: nothing
Modifies: nothing
Effects: generates numbers randomly from a Uniform(0,1) distribution

This function is implemented for you.
"""


def uniformGen():
	return random.random()


"""
Requires: seed is a value generated from a Uniform(0,1) distribution
		  p is the probability of success
Modifies: nothing
Effects: returns a randomly generated value from a Bernoulli(p) distribution,
	using the inverse method described in the spec
"""


def generateFromBernoulli(seed, p):

	#Declare and initialize some variables

    if (1 - p) < seed:
        return 1
    else:
        return 0

"""
Requires: seed is a value generated from a Uniform(0,1) distribution
		  p is the probability of success
		  n is the number of trials
Modifies: nothing
Effects: returns a randomly generated value from a Binomial(n,p) distribution,
	using the inverse method described in the spec
"""


def generateFromBinomial(seed, n, p):

	# Declare and initialize necessary variables
	chooseVariable = 0
	sumOfPMFs = 0
	productOfMultiplication = 0
	pmfValues = []
	cdfValues = []

	# The first phase: computing the PMF values
	for theState in range(n):
		chooseVariable = math.factorial(n) / math.factorial(theState) / math.factorial(n - theState)
		productOfMultiplication = chooseVariable * math.pow(p, theState)
		productOfMultiplication = productOfMultiplication * math.pow((1 - p), (n - theState))

		pmfValues.append(productOfMultiplication)

	#The second phase: computing the CDF values
	for theStateAgain in range(0, n + 1):
		for theLowerState in range (0, theStateAgain):
			sumOfPMFs = sumOfPMFs + pmfValues[theLowerState]

		cdfValues.append(sumOfPMFs)
		sumOfPMFs = 0


	#The final phase: comparing CDF values with seed
	for allTheStates in range(0, n + 1):

		if seed < cdfValues[allTheStates]:
			return (allTheStates - 1)

	return 0
	

"""
Requires: seed is a value generated from a Uniform(0,1) distribution
		  p is the probability of success
Modifies: nothing
Effects: returns a randomly generated value from a Geometric(p) distribution,
	using the inverse method described in the spec
"""


def generateFromGeometric(seed, p):
	numFailures = 0;
	while (1 - math.pow((1 - p), (numFailures - 1))) < seed:
		numFailures += 1
	return (numFailures - 1)
		

"""
NOTE FOR THE FOLLOWING TWO FUNCTIONS: You WILL lose points on the bare-bones
	portion of the project if you simply make a call to the corresponding
	function in the random library. The idea is that everyone gains an
	understanding of how to write code to analyze data, and these distributions
	are the easiest implementations of the inverse method for continuous random
	variables.
"""

"""
Requires: seed is a value generated from a Uniform(0,1) distribution
		  a is the beginning of the interval
		  b is the end of the interval
Effects: returns a randomly generated value from a Uniform(a,b) distribution,
	using the inverse method described in the spec
"""


def generateFromUniform(seed, a, b):
	k = a + seed * (b - a)

	return k


"""
Requires: seed is a value generated from a Uniform(0,1) distribution
		  ld (lambda) is the rate at which the distribution decays
Modifies: nothing
Effects: returns a randomly generated value from a Exponential(ld) distribution,
	using the inverse method described in the spec
"""


def generateFromExponential(seed, ld):
	returnValue = (-1.0 / ld) * math.log(1 - seed)

	return returnValue


"""
Generating from a normal distribution in a non-hacky way is nearly impossible,
so we provide you with a function that calls the library for you.

Requires: mu is the mean of the distribution
		  sigma is the standard deviation of the distribution
Effects: Returns a randomly generated sample from a Normal(mu, sigma)
	distribution
"""


def generateFromNormal(mu, sigma):
	return random.gauss(mu, sigma)


"""
The following function is not required, but your dataset may need you to
implement it. If you would like to implement it, remove the "pass" statement
and implement your function as normal.
"""

"""
Requires: seed is a value generated from a Uniform(0,1) distribution
		  ld (lambda) is the approximation of n*p from the Binomial(n,p)
			distribution
Modifies: nothing
Effects: returns a randomly generated value from a Poisson(ld) distribution,
	using the inverse method described in the spec
"""


def generateFromPoisson(seed, ld):
	pass


