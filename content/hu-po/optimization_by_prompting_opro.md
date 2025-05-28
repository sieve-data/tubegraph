---
title: Optimization by prompting OpRo
videoId: lR9isPmwZ3s
---

From: [[hu-po]] <br/> 

Optimization by Prompting (OpRo) is a novel approach proposed by Google DeepMind that leverages [[Optimization Methods in Machine Learning | large language models (LLMs)]] as generic optimizers <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>. This method describes optimization tasks in natural language, allowing LLMs to iteratively generate new solutions based on problem descriptions and previously found solutions <a class="yt-timestamp" data-t="05:52:00">[05:52:00]</a> <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>.

## LLMs as Optimizers: A New Paradigm

Traditional optimization, particularly in machine learning, heavily relies on derivative-based algorithms like gradient descent <a class="yt-timestamp" data-t="03:21:00">[03:21:00]</a>. These methods require the ability to calculate a derivative or gradient (slope) to determine the direction of improvement <a class="yt-timestamp" data-t="03:45:00">[03:45:00]</a>. However, many real-world applications lack a clear gradient, posing significant [[challenges_of_optimization_in_discrete_and_continuous_spaces | challenges for optimization]] <a class="yt-timestamp" data-t="03:27:00">[03:27:00]</a>.

OpRo addresses this by enabling LLMs to optimize without explicitly calculating the slope <a class="yt-timestamp" data-t="05:25:00">[05:25:00]</a>. The core idea is that LLMs, being [[General Pattern Machines | general pattern machines]], are exceptionally good at finding and extrapolating from patterns <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>. Optimization itself can be viewed as a form of pattern matching <a class="yt-timestamp" data-t="02:36:00">[02:36:00]</a>.

OpRo involves an iterative process where the LLM generates new solutions from a "metaprompt" that includes previously generated solutions and their associated values <a class="yt-timestamp" data-t="06:10:00">[06:10:00]</a> <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>. This means the LLM is given examples of inputs (previous prompts) and their corresponding outputs (scores), and then asked to generate a new input that is likely to yield a better output <a class="yt-timestamp" data-t="03:55:00">[03:55:00]</a>.

### Key Components

*   **Optimizer LLM**: The language model responsible for generating new solutions (e.g., new prompts or parameter values) <a class="yt-timestamp" data-t="01:14:04">[01:14:04]</a>. This LLM often uses a higher sampling temperature (e.g., 1.0) to encourage exploration of the search space <a class="yt-timestamp" data-t="01:21:20">[01:21:20]</a> <a class="yt-timestamp" data-t="01:49:50">[01:49:50]</a>.
*   **Score LLM**: An LLM (which can be the same or different from the optimizer LLM) that evaluates the generated solutions by computing an objective function, such as task accuracy <a class="yt-timestamp" data-t="01:13:51">[01:13:51]</a>. The score LLM typically operates with a temperature of 0.0 for deterministic decoding <a class="yt-timestamp" data-t="01:20:43">[01:20:43]</a>.
*   **Metaprompt**: The prompt provided to the optimizer LLM, consisting of two main parts <a class="yt-timestamp" data-t="03:46:00">[03:46:00]</a>:
    1.  Previously generated solutions with their corresponding scores (often sorted in ascending order of score) <a class="yt-timestamp" data-t="03:47:00">[03:47:00]</a>.
    2.  A natural language description of the optimization problem, including exemplars (randomly selected examples from the training set) to illustrate the task <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>.

## Applications of OpRo

OpRo has been demonstrated in various optimization contexts, from simple mathematical problems to more complex prompt engineering tasks.

### Mathematical Optimization

As a motivational example, OpRo was tested on two classic optimization problems <a class="yt-timestamp" data-t="07:50:00">[07:50:00]</a>:

*   **Linear Regression**: A continuous optimization problem where the goal is to find linear coefficients (slope and intercept) that best fit a set of points <a class="yt-timestamp" data-t="08:10:00">[08:10:00]</a> <a class="yt-timestamp" data-t="05:07:00">[05:07:00]</a>.
    *   LLMs successfully captured optimization directions <a class="yt-timestamp" data-t="05:16:00">[05:16:00]</a>.
    *   GPT-4 and Text Bison models showed comparable performance, outperforming GPT-3.5 Turbo in convergence speed (fewer steps to Optima) <a class="yt-timestamp" data-t="05:52:00">[05:52:00]</a>.
    *   Models found it harder to optimize when the ground truth was further from the starting region or involved negative or large numbers <a class="yt-timestamp" data-t="05:31:00">[05:31:00]</a> <a class="yt-timestamp" data-t="05:55:00">[05:55:00]</a>.
*   **Traveling Salesman Problem (TSP)**: A discrete optimization problem where the goal is to find the shortest route traversing all nodes and returning to the starting node <a class="yt-timestamp" data-t="08:53:00">[08:53:00]</a> <a class="yt-timestamp" data-t="01:00:06">[01:00:06]</a>.
    *   OpRo performed on par with some handcrafted heuristic algorithms for small-scale TSP <a class="yt-timestamp" data-t="01:45:26">[01:45:26]</a>.
    *   GPT-4 significantly outperformed GPT-3.5 Turbo and Text Bison, reaching the global optimum about four times faster <a class="yt-timestamp" data-t="01:07:43">[01:07:43]</a>.
    *   Text Bison and GPT-3.5 often got stuck at local optima, indicating a potential inability to effectively explore the discrete search space <a class="yt-timestamp" data-t="01:07:53">[01:07:53]</a>.
    *   Performance degraded dramatically on problems with larger sizes, highlighting a limitation for [[challenges_of_optimization_in_discrete_and_continuous_spaces | larger, bumpier optimization landscapes]] <a class="yt-timestamp" data-t="01:08:05">[01:08:05]</a>.

### Prompt Optimization

This is considered the primary and most applicable demonstration of OpRo <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>. The objective is to find instructions (prompts) that maximize task accuracy for another LLM <a class="yt-timestamp" data-t="09:42:00">[09:42:00]</a>.

*   **Benchmarks**: GSM8K (8.5K grade school math word problems) <a class="yt-timestamp" data-t="01:11:58">[01:11:58]</a> and Big Bench Hard (BBH, a comprehensive Google-created benchmark with 200 diverse tasks) <a class="yt-timestamp" data-t="01:14:20">[01:14:20]</a>.
*   **Results**: OpRo-optimized prompts consistently outperformed human-designed prompts by a significant margin (over 50%) <a class="yt-timestamp" data-t="01:45:32">[01:45:32]</a>.
    *   An empty prompt on GSM8K yielded 34% accuracy <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>.
    *   Adding "Let's think step by step" increased accuracy to 71% <a class="yt-timestamp" data-t="01:14:56">[01:14:56]</a>.
    *   An OpRo-optimized prompt like "Take a deep breath and work on this problem step by step" further boosted accuracy to 80% <a class="yt-timestamp" data-t="01:09:55">[01:09:55]</a>.
    *   Surprisingly, a shorter prompt like "Break this down" achieved nearly 80% accuracy, similar to the longer, more verbose prompts <a class="yt-timestamp" data-t="01:38:10">[01:38:10]</a>. This highlights the complex and sometimes counterintuitive nature of LLM behavior <a class="yt-timestamp" data-t="01:40:49">[01:40:49]</a>.

### Prompt Characteristics and Placement

*   **Position of Instruction**: The placement of the engineered prompt matters <a class="yt-timestamp" data-t="01:36:53">[01:36:53]</a>. Adding the instruction at the end of the question (Q_end) generally yielded better results (e.g., 68% accuracy) compared to the beginning of the question (Q_begin, 64% accuracy) <a class="yt-timestamp" data-t="01:39:13">[01:39:13]</a>. This aligns with the concept of "recency bias" in LLMs, where tokens closer to the generation point have more influence <a class="yt-timestamp" data-t="01:24:18">[01:24:18]</a>.
*   **Style of Instructions**: Different optimizer LLMs generated varying styles of prompts. Palm 2 Lit and Text Bison produced concise instructions, while GPT models generated longer, more detailed ones <a class="yt-timestamp" data-t="01:40:32">[01:40:32]</a>.
*   **Task Specificity**: Optimized prompts are often model and task-specific; a prompt that works well for one task or model may not generalize to others <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>. The appendices of the paper provide examples of task-specific optimized prompts for BBH, including phrases like "Choose the option that wickedly embodies a sarcasm" for snark detection <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>.

## Ablation Studies and Factors Affecting Performance

Ablation studies revealed several factors influencing OpRo's effectiveness:

*   **Order of Instructions**: Sorting previous solutions by score in ascending order (lowest to highest) in the metaprompt generally yielded the best final accuracies, outperforming descending or random orders <a class="yt-timestamp" data-t="01:24:52">[01:24:52]</a>.
*   **Accuracy Scores Representation**: Rounding accuracies into 20 "buckets" (discrete values) generally performed better than 100 buckets or no scores at all, suggesting that too much precision or absence of scores can hinder the optimizer LLM <a class="yt-timestamp" data-t="01:25:42">[01:25:42]</a>.
*   **Number of Exemplars**: Including a few examples (e.g., three) from the training set in the metaprompt was critical for providing task context <a class="yt-timestamp" data-t="01:29:38">[01:29:38]</a>. However, more exemplars did not necessarily improve performance and could even "distract" the optimizer from other important components <a class="yt-timestamp" data-t="01:30:43">[01:30:43]</a>. This implies a balance is needed to avoid "overfitting the prompt" <a class="yt-timestamp" data-t="01:31:31">[01:31:31]</a>.
*   **Number of Generated Instructions per Step**: Generating multiple solutions (e.g., eight) at each optimization step improved stability, allowing the LLM to explore various possibilities <a class="yt-timestamp" data-t="01:48:06">[01:48:06]</a>.
*   **Initial Conditions**: The starting prompt (e.g., an empty string or "Let's solve the problem") significantly influences the optimization trajectory, with LLMs tending to "riff" on the initial input <a class="yt-timestamp" data-t="01:32:47">[01:32:47]</a>.

## Limitations and Future Research

Despite its promise, OpRo faces several limitations and opens avenues for future research <a class="yt-timestamp" data-t="01:40:40">[01:40:40]</a>:

*   **Context Window Limits**: The finite context window of current LLMs restricts the size of optimization problems that can be described in the prompt <a class="yt-timestamp" data-t="01:09:37">[01:09:37]</a>. Larger context windows could enable more complex optimization tasks.
*   **"Bumpy" Loss Landscapes**: LLMs can struggle to navigate highly complex or "bumpy" optimization landscapes, leading to getting stuck in suboptimal regions <a class="yt-timestamp" data-t="01:09:57">[01:09:57]</a>.
*   **Sensitivity to Initialization**: OpRo remains sensitive to its initial starting conditions, a common challenge in many optimization algorithms <a class="yt-timestamp" data-t="01:45:44">[01:45:44]</a>.
*   **Utilizing Error Cases**: The optimizer LLM does not effectively leverage specific error cases in the training set to infer promising directions <a class="yt-timestamp" data-t="01:46:11">[01:46:11]</a>.
*   **Black Box Nature**: The precise reasons *why* certain prompts work remain unclear <a class="yt-timestamp" data-t="02:18:00">[02:18:00]</a>. Attributing human-like psychological behaviors (e.g., "distracting the optimizer") to LLMs might be anthropomorphizing their internal mechanisms <a class="yt-timestamp" data-t="01:30:51">[01:30:51]</a>.

The paper suggests future work could explore richer feedback about error cases or summarizing key features distinguishing high- and low-quality prompts <a class="yt-timestamp" data-t="01:46:55">[01:46:55]</a>.
The possibility of LLMs directly optimizing the weights and biases of neural networks, rather than just prompts, is a speculative but potentially groundbreaking future direction <a class="yt-timestamp" data-t="01:10:27">[01:10:27]</a>. This could even extend to LLMs optimizing the "meta-instructions" given to other optimizer LLMs, leading to a recursive, self-improving system <a class="yt-timestamp" data-t="01:18:00">[01:18:00]</a>.