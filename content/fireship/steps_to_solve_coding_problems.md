---
title: Steps to solve coding problems
videoId: UFc-RPbq8kg
---

From: [[fireship]] <br/> 

[[problemsolving_skills_in_software_development | Problem-solving]] is considered the most important skill for a software developer <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. While many new developers initially focus on learning a programming language, experienced developers prioritize [[problemsolving_skills_in_software_development | problem-solving]] over memorizing every language feature <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. Top companies often use whiteboarding problems in interviews to gain insight into a candidate's thought process when approaching a software development problem <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. This skill is harder to learn than syntax and requires years of practice <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

There is no single "right way" to solve a problem, as everyone's brain is different <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. The following steps provide a general framework that can be adapted to individual instincts and preferences <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

## 1. Identify and Understand the Problem <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>

The initial step involves clearly defining the nature of the problem <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. If given an hour to solve a problem, it's recommended to spend 55 minutes thinking about the problem itself and only five minutes on solutions <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

Software problems can vary widely, from internal optimizations to fixing bugs in existing software or addressing abstract user experience issues <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. Complex problems, like user experience, are often broken down into smaller components such as epic stories and themes using an agile approach <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

When defining a problem, a structured approach helps:
*   **Context:** Describe the current situation (e.g., "more than 600 pull requests on GitHub that must be merged") <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
*   **Issue:** Explain why it's a problem (e.g., "it would take hours of mindless code review and button clicking") <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   **Solution Justification:** Summarize why the problem should be solved (e.g., "it can be automated with the GitHub API to save time and money") <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

Once the problem is identified and its worth established, it can be broken down into smaller, manageable sub-problems <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. This [[importance_of_breaking_down_large_problems | breakdown]] helps overcome the initial hurdle of "where do I start?" when facing a clear vision but uncertain implementation <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

## 2. Research and Refine the Problem <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>

After understanding the problem, research what others have done to solve similar challenges <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. It is acceptable and often encouraged to use existing solutions as a starting point, provided there's a confident understanding of what the code does <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.

For specialized problems, discussing ideas with other developers can be invaluable <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. This collaboration can lead to identifying further sub-problems or discovering suitable tools, such as the GitHub GraphQL API, to retrieve necessary information <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.

The problem can be further refined into smaller, achievable objectives. For example, retrieving all pull requests and then merging each one individually <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. Researching API documentation confirms whether tools support these requirements <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

> [!info] Weighing Alternatives
> In many situations, there will be multiple ways to solve a problem (e.g., using a GraphQL API or a REST API). It's crucial to weigh the pros and cons of alternative approaches <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

## 3. Pseudocode <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>

The goal of this step is to write an outline for how the code will be implemented <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. This can be done on a whiteboard, paper, or directly in an editor <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. The focus is on the logic, without worrying about syntax or implementation details <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. If comfortable with a specific language, writing pseudocode in that language can be beneficial <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

Pseudocode helps in:
*   **Structuring the program:** Defining main functions, clients, authentication, queries, and loops <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Adding comments:** Outlining validations or specific actions within functions <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
*   **Naming things:** Focusing on meaningful names for variables and functions before the code gets complex, which greatly improves code readability <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.

## 4. Explore the API (if applicable) <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>

When working with APIs, it's highly valuable to explore them before writing any code <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>. Tools like Insomnia can be used to make requests and understand the API's behavior <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. GraphQL, for instance, allows seeing the entire schema of the API, making it easier to determine required fields and operations <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>. Understanding the API thoroughly simplifies the implementation phase <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.

## 5. Test-Driven Development (TDD) <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>

[[testing_strategies_in_software_development | Test-driven development]] is an optional but highly recommended approach, especially for critical features <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>. An experienced developer understands which tests are valuable for a given feature <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.

The basic TDD process involves:
1.  **Write a failing test:** Describe what is being tested and expect a certain outcome <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
2.  **Implement code:** Write just enough code to make the test pass <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.
3.  **Refactor:** Simplify or optimize the code while ensuring tests still pass <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.

Writing tests before code (the "red-green-refactor" process) forces developers to think about what they are trying to achieve <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. Good tests quickly catch issues and help prevent regressions when refactoring code later <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.

## 6. Implementation <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>

The implementation phase focuses on getting the code working quickly, aiming for a working prototype with all tests passing in the least amount of time <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>. The code doesn't need to be perfect at this stage <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.

> [!tip] Psychological Benefit of Small Wins
> Solving a big problem is a collection of small steps. Trying to perfect every small step can prolong the process and be discouraging <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>. Rushing to implement an initial version, like in a hackathon, builds confidence that the problem can be solved <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.

## 7. Reflection and Refinement <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>

Once a full working prototype is achieved, take time to reflect on the code <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.

> [!tip] Take a Break
> If struggling with a small problem for hours, take a 15-minute break and focus on something else. The subconscious mind continues to work on the problem, often leading to a quick solution upon return <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>. This is why "aha moments" often occur before sleep or in the shower <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

Areas for improvement include:
*   Improving readability by better naming and adding comments <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.
*   Removing duplication <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
*   Improving the time and space complexity of algorithms <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.
*   Adding caching to reduce costs and improve performance <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
*   Improving error handling <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.

It's much easier to improve an existing working piece of code than to write a perfect piece of code from the start <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.

## Ongoing Improvement <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>

[[problemsolving_skills_in_software_development | Problem-solving]] is a skill that is continuously learned <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>, with an infinite number of unique challenges <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.

*   **Practice Seriously:** Like a musical instrument, mastery requires significant practice and pushing oneself to overcome new challenges <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. Consistent practice builds the ability to look at a problem and visualize how a computer system can solve it <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. Repetition helps techniques become intuitive <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.
*   **Get Feedback:** Seek feedback from other developers, especially more experienced ones <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>. While it can be self-conscious, regular feedback accelerates learning <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.

Ultimately, the most important aspect is solving the problem, regardless of the specific language, philosophy, or framework used <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.