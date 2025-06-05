---
title: Problemsolving skills in software development
videoId: UFc-RPbq8kg
---

From: [[fireship]] <br/> 

Problem-solving is considered by many to be the most important skill for a software developer <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. While learning a [[programming_software | programming language]] is essential, highly experienced developers prioritize problem-solving over knowing every feature of a language <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. This is why top companies use whiteboarding problems in interviews to gain insight into a candidate's thought process when approaching a software development problem <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. This skill is more challenging to learn than memorizing syntax and takes years of practice <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

## Core Purpose of Software

One of the most fundamental problems that software aims to solve is the elimination of manual, repetitive work <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. An example of this is automating the merging of over 600 pull requests to avoid manually clicking a button multiple times <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## [[steps_to_solve_coding_problems | Steps to Solve Coding Problems]]

While there's no single "right" way to solve a problem, several techniques can help quickly and reliably solve coding problems <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

### 1. Identify and Understand the Nature of the Problem

The first critical step is to identify and understand the problem <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. It's often recommended to spend most of your allocated time thinking about the problem itself rather than immediately brainstorming solutions <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

Software problems can vary:
*   **Internal Optimization**: Saving time and money by automating repetitive tasks, like merging pull requests <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   **Bug Fixing**: Identifying the root cause of issues in existing software by examining stack traces <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   **Abstract Problems**: Issues like user experience, which often require [[importance_of_breaking_down_large_problems | breaking down]] into smaller "epic stories" or "themes" using agile approaches <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

When defining a problem, it's helpful to:
1.  **Start with context**: Describe the situation (e.g., "more than 600 pull requests on GitHub that must be merged") <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
2.  **Explain the issue**: Detail why it's a problem (e.g., "it would take hours of mindless code review and button clicking") <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
3.  **Summarize why it should be solved**: State the benefit of solving it (e.g., "it can be automated with the GitHub API to save us time and money") <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

### 2. Research and Refine the Problem

Once a problem is defined and deemed worthwhile, it should be [[importance_of_breaking_down_large_problems | broken down]] into smaller, manageable sub-problems <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. Researching how others have solved similar problems is highly encouraged <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. This often involves searching online resources like Stack Overflow <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. When using existing solutions, ensure you confidently understand the code before implementing it <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

Discussing ideas with other developers can provide valuable insights and lead to breaking down the problem further <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. For instance, merging pull requests might reveal a need to validate each one first, leading to a smaller problem of "how do we validate each individual pull request?" <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

Researching APIs (like the GitHub GraphQL API) can confirm if they support the necessary requirements before writing any code <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. Problems can often be refined into smaller objectives, such as "retrieve all pull requests" and "merge each one individually" <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

Always weigh the pros and cons of alternative approaches when multiple solutions exist (e.g., GraphQL API versus REST API) <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

### 3. Pseudocode

Pseudocode involves writing an outline for code implementation, focusing on logic rather than syntax or specific implementation details <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. This can be done on a whiteboard, paper, or directly in an editor <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. For those comfortable with a specific language (e.g., JavaScript), writing pseudocode in that language can be beneficial <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

An added benefit of pseudocode is the ability to focus on naming conventions early, which significantly improves code readability later <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.

### 4. Explore APIs

When working with APIs, it's valuable to explore them before diving into code <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>. Tools like Insomnia allow making requests to an API to understand its structure and capabilities (e.g., GraphQL's schema) <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. Understanding the API structure makes implementing the solution much easier <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>. [[applications_of_graphs_in_software | Graph applications]] like GraphQL can make API exploration particularly intuitive <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.

### 5. [[testing_strategies_in_software_development | Test-Driven Development (TDD)]]

While optional, TDD is highly recommended for critical features <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. An experienced developer understands what tests add value to a feature <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.

The basic TDD process involves the "red-green-refactor" cycle:
1.  **Red**: Write a failing test that defines what you're trying to achieve, forcing you to think about the goal <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
2.  **Green**: Implement the minimum code necessary to make the test pass <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.
3.  **Refactor**: Reflect on the implemented code and simplify or optimize it <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.

Good test specs help catch issues quickly, prevent regressions during refactoring, and provide confidence in the code's ability to handle various situations <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.

### 6. Implementation Details

When implementing code, the initial goal should be to achieve a working prototype with all tests passing as quickly as possible, even if the code isn't perfect <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>. This "hackathon" approach builds confidence that the problem can be solved <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. Perfecting every small step can be discouraging and prolong the development process <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

If stuck on a small problem for hours, taking a break for 15 minutes and focusing on something else can surprisingly lead to a solution upon returning <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>. This phenomenon is attributed to the subconscious mind continuing to work on the problem <a class="yt="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.

### 7. Reflection and Improvement

Once a working prototype is established, take time to reflect on the code <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>. It's much easier to improve a working piece of code than to write a perfect one from the start <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.

Areas for improvement include:
*   Improving readability through better naming <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.
*   Adding comments <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
*   Removing duplication <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.
*   Improving time and space complexity of algorithms <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.
*   Adding caching to reduce costs and improve performance <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
*   Improving error handling <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.

## Continuous Learning and Practice

Problem-solving is a skill that developers continuously learn and refine <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. It requires serious and consistent practice, much like learning a musical instrument <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. Through practice and repetition, the ability to visualize how a computer system can solve a problem becomes intuitive <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. The ultimate goal is to solve the problem, regardless of the [[programming_software | programming language]], philosophy, or framework used <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.

## Seek Feedback

To accelerate skill development, seek feedback from other developers, especially those more experienced <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>. While it's natural to feel self-conscious about code, frequent feedback helps in quickly improving <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.