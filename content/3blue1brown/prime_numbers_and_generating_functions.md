---
title: Prime numbers and generating functions
videoId: bOXCLR3Wric
---

From: [[3blue1brown]] <br/> 

The study of [[prime_numbers_and_their_regularities | prime numbers]], particularly their distribution and density, can sometimes involve surprisingly advanced mathematical tools, including complex numbers and functions that act like generating functions [00:00:31].

## Complex Numbers in Discrete Mathematics
It might seem absurd to use complex numbers for problems involving only whole numbers and their sums [00:00:09]. However, complex numbers are "unreasonably useful" for discrete mathematics [00:00:25]. A prominent example is the modern understanding of [[prime_numbers_and_density | prime numbers]] [00:00:33]. Questions about their distribution and density are studied by analyzing specially designed functions whose inputs and outputs are complex numbers [00:00:40].

### The Riemann Hypothesis
The famous [[connection_between_zeta_function_and_prime_numbers | Riemann hypothesis]] is centered on such a function [00:00:46]. This function, smooth and complex-valued, initially appears unrelated to the discrete world of [[prime_numbers_and_their_regularities | primes]] [00:00:52]. Yet, it encodes all the necessary information about those discrete [[prime_numbers_and_their_regularities | prime numbers]] [00:00:57]. Certain questions about [[prime_numbers_and_their_regularities | primes]] become easier to answer by analyzing this function than by directly analyzing the [[prime_numbers_and_their_regularities | primes]] themselves [00:01:02].

## Generating Functions
A [[generating_functions_and_subsets | generating function]] is a mathematical tactic where a question with an answer associated with each positive integer is encoded as coefficients in a polynomial [00:09:30]. By mathematically manipulating and analyzing the properties of this polynomial, insights can be gained about the original question [00:09:47].

For example, when constructing a polynomial where each coefficient $c_n$ represents the number of subsets that add up to a particular value $n$, the polynomial's expansion mirrors the act of constructing subsets [00:09:02]. The exponent in a term equals the sum of the corresponding subset, and the coefficient of that term indicates the number of subsets with that specific sum [00:08:49].

This idea extends to other areas, such as studying Fibonacci numbers, where coefficients of an infinite polynomial (power series) are Fibonacci numbers [00:10:02].

## Parallel with Prime Number Study
The techniques used to solve problems involving generating functions, especially with complex numbers, are similar in spirit to the setup that led to the [[connection_between_zeta_function_and_prime_numbers | Riemann Hypothesis]] and the [[distribution_of_prime_numbers_and_dirichlets_theorem | Prime Number Theorem]] [00:01:21].

### Riemann's Approach to Primes
Just like in problems involving generating functions, Riemann's study of [[prime_numbers_and_their_regularities | primes]] involved:
1.  **A Discrete Sequence**: Identifying a discrete sequence that carries information about [[prime_numbers_and_their_regularities | prime numbers]] [00:31:39].
2.  **A Related Function**: Considering a function whose coefficients are the terms in that sequence [00:31:47]. In Riemann's case, this is not a polynomial but a related structure known as a **Dirichlet series** [00:31:55].
3.  **Complex Valued Inputs**: Information about these coefficients is sussed out by studying how this function behaves with complex valued inputs [00:32:02].

While Riemann's techniques are more sophisticated due to his pioneering work in complex analysis, the fundamental principle remains: extending the domain of study beyond real numbers to the complex plane offers significant power in making deductions about the coefficients of such functions [00:32:12].

### Why Complex Numbers?
The effectiveness of complex numbers in these contexts, particularly for [[prime_numbers_and_density | prime number]] theory, can be attributed to their ability to represent and analyze frequency information [00:33:00]. When working with generating functions, plugging in different inputs reveals hidden information about the coefficients [00:32:40]. The complex plane offers a richer space of numbers for these inputs [00:32:47].

Specifically, the use of values on the unit circle and [[roots of unity]] (complex numbers that, when raised to a certain power, result in 1) is crucial [00:33:17]. These values allow for the detection of cycling or periodic behavior in successive products, which corresponds to frequency information [00:33:08]. This core idea underlies concepts like Fourier transforms and Fourier series, demonstrating its widespread utility in mathematics and fields like quantum computing (e.g., Shor's algorithm for factoring large numbers) [00:33:49].