---
title: Challenges of optimization in discrete and continuous spaces
videoId: lR9isPmwZ3s
---

From: [[hu-po]] <br/> 

Optimization is a high-level, generic term used to describe a process by which something is improved <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. In various fields, particularly in [[Optimization Methods in Machine Learning | machine learning]], different optimization methods are employed to achieve desired outcomes.

## Traditional Optimization: Derivative-Based Algorithms
Most optimization processes, especially in a [[Optimization Methods in Machine Learning | machine learning]] context, use variants of gradient descent <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. These methods involve calculating the derivative, gradient, or slope to determine the direction of improvement <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>. For example, when training a neural network with billions of parameters, optimization involves iteratively adjusting parameters based on how small changes affect a loss function, guiding the process towards a minimum value <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.

A crucial requirement for these derivative-based algorithms is that every part of the computational pipeline must be differentiable, enabling backpropagation through the chain rule <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. This reliance on gradients poses significant challenges for real-world applications where a gradient cannot be easily found <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

### The Complicated Loss Landscape
When optimizing a neural network, the loss landscape can be very complicated, potentially featuring multiple local minima that are not the global minimum <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. Traditional gradient-based methods might get stuck in a shallow local minimum, requiring strategies for exploration to find deeper, global minima <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.

## Discrete vs. Continuous Optimization Spaces
The nature of the optimization space profoundly impacts the applicability of traditional gradient-based methods:

### Continuous Optimization
In a continuous space, variables can take on any real value within a range.
*   **Linear Regression** is a classic example of continuous optimization <a class="yt-timestamp" data-t="00:50:37">[00:50:37]</a>. Here, the goal is to find continuous coefficients (like slope 'm' and y-intercept 'b' in y=mx+b) that best fit a set of points <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.
*   Because the parameters are continuous, their derivatives can be calculated, making them suitable for gradient-based methods <a class="yt-timestamp" data-t="00:50:51">[00:50:51]</a>.

### Discrete Optimization
In a discrete space, variables can only take on distinct, separate values.
*   The **Traveling Salesman Problem (TSP)** is a classic example of discrete optimization <a class="yt-timestamp" data-t="00:51:12">[00:51:12]</a>. It involves finding the shortest route visiting a set of cities exactly once and returning to the origin <a class="yt-timestamp" data-t="01:00:38">[01:00:38]</a>. The "solutions" are permutations of cities, which are discrete arrangements.
*   **Prompt Optimization** is another discrete optimization task <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. The goal is to find specific natural language instructions (prompts) that maximize task accuracy for a language model <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. The space of all possible sentences is very large but discrete, as it's composed of a limited vocabulary of tokens <a class="yt-timestamp" data-t="00:29:32">[00:29:32]</a>.
*   **Challenge**: For [[Continuous vs Discrete Latent Spaces in AI | discrete spaces]], it's impossible to calculate a derivative, as there's no continuous "slope" to follow <a class="yt-timestamp" data-t="00:30:19">[00:30:19]</a>. This makes traditional gradient-based methods unusable <a class="yt-timestamp" data-t="00:30:35">[00:30:35]</a>.

## [[Large Language Models as optimizers | Large Language Models (LLMs) as Optimizers (OPRO)]]
Recent research proposes using [[Large Language Models as optimizers | LLMs as optimizers]] through a method called Optimization by Prompting (OPRO) <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>. This approach leverages the LLM's ability to understand natural language <a class="yt-timestamp" data-t="00:22:06">[00:22:06]</a> and generate new solutions iteratively based on problem descriptions and previously found solutions <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

### OPRO Performance in Different Spaces
*   **Continuous (Linear Regression)**: LLMs like Palm 2 models and GPT-4 were able to find optimal solutions for linear regression problems with a relatively small number of steps <a class="yt-timestamp" data-t="00:53:04">[00:53:04]</a>. The underlying intuition suggests that the LLM performs a "pseudo slope derivative gradient" calculation in its "brain," implicitly recognizing patterns for movement in the right direction <a class="yt-timestamp" data-t="01:11:52">[01:11:52]</a>.
*   **Discrete (Traveling Salesman Problem)**: LLMs found the TSP to be significantly harder to solve, with some models (e.g., Text Bison) unable to find optimal solutions for larger node counts (e.g., 15, 20, or 50 nodes) <a class="yt-timestamp" data-t="01:07:25">[01:07:25]</a>. This contrasts with their performance in continuous problems, possibly because the discrete nature offers no implicit "slope" to follow <a class="yt-timestamp" data-t="01:07:01">[01:07:01]</a>.
*   **Discrete (Prompt Optimization)**: Despite challenges in some discrete mathematical problems, OPRO proved effective for prompt optimization. [[Large Language Models as optimizers | LLMs optimized prompts]] for tasks like grade school math word problems (GSM8K) and other Big-Bench Hard (BBH) tasks <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. The best LLM-optimized prompts often outperformed human-designed prompts by a significant margin (e.g., improving accuracy from 71% to 80% on GSM8K by adding "take a deep breath and work on this problem step by step") <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.

## General Challenges and Limitations of LLM-based Optimization
1.  **Sensitivity to Initial Conditions**: LLM-based optimization is highly sensitive to the initial conditions or starting points of the optimization process. Different initial prompts or random seeds can lead to varied convergence speeds and outcomes <a class="yt-timestamp" data-t="00:47:52">[00:47:52]</a>.
2.  **Exploration vs. Exploitation**: A fundamental challenge in optimization is balancing exploration (searching new regions of the solution space) and exploitation (refining existing promising solutions) <a class="yt-timestamp" data-t="00:40:15">[00:40:15]</a>. LLMs need to manage this balance; for instance, higher "temperature" settings can encourage more aggressive exploration <a class="yt-timestamp" data-t="00:49:50">[00:49:50]</a>.
3.  **Context Window Limitations**: Current LLMs have limited context windows, making it hard to fit large-scale optimization problem descriptions (e.g., all parameters of a large neural network) into the prompt <a class="yt-timestamp" data-t="01:09:37">[01:09:37]</a>.
4.  **"Bumpy" Loss Landscapes**: For objective functions with very "bumpy" or complex loss landscapes, LLMs might struggle to propose a correct "descending direction," leading to the optimization getting stuck <a class="yt-timestamp" data-t="01:10:13">[01:10:13]</a>.
5.  **Lack of Error Case Utilization**: The LLM optimizers do not effectively utilize information from specific error cases in the training set to infer promising directions <a class="yt-timestamp" data-t="01:46:11">[01:46:11]</a>.
6.  **Hyperparameter Sensitivity**: The performance of OPRO, like many machine learning methods, is sensitive to hyperparameters such as the number of instructions included in the metaprompt, the order of instructions (ascending order of scores often works best), and the way accuracy scores are presented (e.g., bucketing scores into 20 bins can be more effective than 100 bins or no scores) <a class="yt-timestamp" data-t="01:22:00">[01:22:00]</a>.

Despite these challenges, the ability of LLMs to perform optimization, especially in natural language contexts like prompt engineering, suggests a new frontier in applying these powerful models to complex problem-solving <a class="yt-timestamp" data-t="01:45:00">[01:45:00]</a>.