---
title: Common coding interview questions
videoId: 1t1_a1BZ04o
---

From: [[fireship]] <br/> 

[[technical_interview_challenges | Technical interviews]] are described as a "high-stakes life or death game" for software engineers, with a six-figure salary on one side [00:00:14]. While the interview process may seem broken, it is something that candidates must engage with to succeed [00:00:20].

## The Technical Interview Experience

A common scenario involves a candidate who has spent a significant amount of time learning to code and preparing for an interview, often through resources like LeetCode and Udemy courses [00:00:45]. The interviewer often starts with what appears to be a simple, classic problem [00:01:18].

### Example: The FizzBuzz Question

A classic interview question is FizzBuzz, which requires printing numbers from 1 to 100 with specific conditions [00:01:20]:
*   If a number is divisible by 3, print "fizz" [00:01:25].
*   If a number is divisible by 5, print "buzz" [00:01:28].
*   If a number is divisible by both 3 and 5, print "fizzbuzz" [00:01:31].

Initially, candidates might overthink simple problems, expecting complex solutions from "big scary tech corporations" [00:01:44].

## Strategies for High-Pressure Problem Solving

Navigating a [[technical_interview_challenges | technical interview]] successfully involves more than just writing code; it requires strong [[problemsolving_and_coding_practice | problem-solving]] and communication skills [00:00:31].

### Managing Anxiety and Composure
A common experience is to "black out" or panic when faced with a coding challenge, feeling like an imposter [00:01:52]. However, once the pressure of "failing" is removed, anxiety can dissipate, allowing for clearer thought [00:02:06]. Maintaining composure is crucial [00:04:09].

### Breaking Down the Problem
Before writing any code, it's essential to talk about how to approach the problem [00:02:01].
*   **Identify Conditions:** For problems like FizzBuzz, recognize the conditional statements involved [00:02:14].
*   **Visualize:** Representing the logic with a flowchart on a whiteboard or through pseudocode can help clarify the solution without worrying about syntax [00:02:19].
*   **Pseudocode Example:**
    *   Loop through numbers [00:02:29].
    *   If divisible by 3 AND 5, print "fizzbuzz" [00:02:30].
    *   Else if divisible by 3, print "fizz" [00:02:33].
    *   Else if divisible by 5, print "buzz" [00:02:35].
    *   Else, print the number [00:02:37].

### Choosing a Programming Language
It's generally recommended to use the language one is most comfortable with for the implementation, such as [[choosing_the_right_programming_language | JavaScript]] [00:03:00].

### The "Always Be Chatting" (ABC) Rule
One of the most important [[interview_preparation_strategies | interview preparation strategies]] is to **think out loud** and explain decisions throughout the process [00:03:16]. Saying something is almost always better than saying nothing [00:03:36]. Practicing articulating thoughts while solving problems can help candidates become more comfortable with this [00:03:44]. If confused, it's better to ask a clarifying question than to sit silently [00:03:58].

### Implementing the Solution
*   **Loop Structure:** A traditional `for` loop might be chosen over a `forEach` loop if performance is considered a factor, even if the reasoning is not perfectly correct, as it demonstrates a thought process [00:03:22].
*   **Divisibility Check:**
    *   Initially, one might consider checking if `number / target` results in an integer [00:04:39].
    *   However, the **modulo operator (%)** is the preferred and more robust method [00:05:08]. It provides the remainder of a division, and if the remainder is 0, the number is a multiple [00:05:16]. This approach is less dependent on language-specific "magic" and is available in most programming languages [00:05:27].

### Refactoring and Scalability
An initial solution might use a series of `if/else if/else` statements [00:05:57].
*   **Order of Conditions:** It's important to check the "fizzbuzz" condition (divisible by both 3 and 5) first, before the individual "fizz" or "buzz" conditions, to ensure correct output [00:05:56].
*   **Avoiding Anti-Patterns:** While some might consider `else` statements an anti-pattern, for specific problems like FizzBuzz, they can lead to simpler and more correct code [00:05:51].
*   **Handling More Conditions:** For increased scalability (e.g., adding a "bass" for 7), it's advisable to extract data out of the conditional statements [00:06:23]. This can involve defining a variable to build the output string and conditionally mutating it, which allows for eliminating redundant checks and better scalability [00:06:28].

> [!NOTE] GitHub Copilot
> Some developers might use tools like GitHub Copilot during coding to assist, though this is often kept "on the download" during an interview [00:06:38]. The use of such AI tools relates to the [[impact_of_ai_on_coding_and_programming_skills | impact of AI on coding and programming skills]] and a [[comparison_with_other_ai_models_in_coding | comparison with other AI models]].

### Discussing Algorithm Performance (Big O Notation)
Interviewers often ask about the performance of an algorithm using **Big O notation** [00:07:08].
*   For a problem that iterates a fixed number of times (e.g., 100 steps for FizzBuzz), the time complexity simplifies to O(1) or constant time, even if a loop suggests O(N) linear time for an infinite game [00:07:22]. This falls under [[capabilities and limitations of o1 in coding benchmarks | capabilities and limitations of O(1) in coding benchmarks]].

## Post-Interview Realities
After successfully navigating the [[technical_interview_challenges | technical interview]], sometimes external factors like hiring freezes can lead to job offers being rescinded, which can be a [[common_frustrations_in_software_engineering | common frustration in software engineering]] [00:08:08].