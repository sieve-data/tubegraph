---
title: Research and use of APIs in programming
videoId: UFc-RPbq8kg
---

From: [[fireship]] <br/> 

[[programming_software | Programming]] is a powerful tool used to solve problems, especially those involving repetitive manual work <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>. When faced with the challenge of merging over 600 pull requests manually, leveraging code and APIs becomes a viable solution <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. This article explores the steps involved in researching and effectively utilizing APIs to tackle such problems.

## Identifying the Problem and Its Context

The first crucial step in problem-solving is to identify and thoroughly understand the nature of the problem <a class="yt-timestamp" data-t="01:42:00">[01:42:00]</a>. For instance, having over 600 pull requests on GitHub that require merging poses a significant issue because it would demand hours of mindless code review and button clicking <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>. This specific scenario represents an internal optimization problem, aiming to save time and money through automation <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>.

The problem can be automated using the GitHub API <a class="yt-timestamp" data-t="02:32:00">[02:32:00]</a>. Before diving into solutions, it's beneficial to break down the larger problem into smaller, manageable sub-problems <a class="yt-timestamp" data-t="02:38:00">[02:38:00]</a>.

## Researching and Refining with APIs

When beginning development, new developers often ask "Where do I start?" even with a clear vision of what they want to build <a class="yt-timestamp" data-t="02:41:00">[02:41:00]</a>. This leads to the second step: research and refine the problem <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>.

### Leveraging Existing Solutions
It's common and encouraged to research what others have done to solve similar problems, as you're likely not the first one to encounter it <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>. While platforms like Stack Overflow can provide starting points, it's vital to confidently understand what the code does before using it <a class="yt-timestamp" data-t="03:17:00">[03:17:00]</a>.

### Discussing with Other Developers
For specialized problems, discussing ideas with other developers can be invaluable <a class="yt-timestamp" data-t="03:27:00">[03:27:00]</a>. For example, a bash script might be suggested as a starting point, but further research might reveal additional requirements, such as validating each pull request to ensure only authorized files were modified <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>. This refinement helps break the larger problem into smaller, more specific ones, like "how do we validate each individual pull request?" <a class="yt-timestamp" data-t="03:50:00">[03:50:00]</a>.

### Deep Diving into API Documentation
For tasks involving external services, APIs become central. GitHub, for instance, offers a GraphQL API that can retrieve information from its servers <a class="yt-timestamp" data-t="03:55:00">[03:55:00]</a>. Before writing any code, it's crucial to research the API to ensure it supports the desired functionality <a class="yt-timestamp" data-t="04:03:00">[04:03:00]</a>.

The problem can be further refined into objectives such as:
*   Retrieving all pull requests from GitHub <a class="yt-timestamp" data-t="04:10:00">[04:10:00]</a>.
*   Merging each pull request individually <a class="yt-timestamp" data-t="04:11:00">[04:11:00]</a>.

Researching the API documentation helps confirm these requirements are met <a class="yt-timestamp" data-t="04:13:00">[04:13:00]</a>. Often, there will be multiple ways to solve a problem, such as using the GraphQL API or the [[introduction_to_restful_apis | REST API]] for GitHub <a class="yt-timestamp" data-t="04:27:00">[04:27:00]</a>. It's important to weigh the pros and cons of alternative approaches <a class="yt-timestamp" data-t="04:33:00">[04:33:00]</a>.

## Pseudocoding API Interactions

With the problem broken down and API tools identified, the next step is pseudocode <a class="yt-timestamp" data-t="04:37:00">[04:37:00]</a>. The goal is to outline the code's implementation, focusing on logic rather than syntax or specific details <a class="yt-timestamp" data-t="04:39:00">[04:39:00]</a>. If comfortable with a language like JavaScript, pseudocoding in that language can be beneficial <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>.

For API interactions, the pseudocode might include:
*   Initializing a GraphQL client <a class="yt-timestamp" data-t="05:01:00">[05:01:00]</a>.
*   Authenticating with the GitHub API using an auth token <a class="yt-timestamp" data-t="05:06:00">[05:06:00]</a>.
*   Retrieving open pull requests using a GraphQL query <a class="yt-timestamp" data-t="05:10:00">[05:10:00]</a>.
*   Creating a function to validate each pull request <a class="yt-timestamp" data-t="05:14:00">[05:14:00]</a>.
*   Iterating through pull requests and merging valid ones with a GraphQL mutation <a class="yt-timestamp" data-t="05:34:00">[05:34:00]</a>.

Pseudocoding also provides an opportunity to focus on naming conventions, which greatly improves code readability <a class="yt-timestamp" data-t="05:27:00">[05:27:00]</a>.

### Exploring the API Before Implementation
When [[using_apis_and_third_party_services | working with an API]], it's highly valuable to explore it before diving into implementation <a class="yt-timestamp" data-t="05:44:00">[05:44:00]</a>. Tools like Insomnia allow developers to make requests to the API and understand its responses before writing code <a class="yt-timestamp" data-t="05:50:00">[05:50:00]</a>. GraphQL is particularly helpful here, as it allows viewing the entire schema of the API within the tool <a class="yt-timestamp" data-t="05:55:00">[05:55:00]</a>.

Understanding the API will significantly simplify the implementation of the solution <a class="yt-timestamp" data-t="06:19:00">[06:19:00]</a>.

## Implementing the Solution

When it comes to the actual implementation, a strategy of rapid prototyping can be effective: aim to get a working prototype with all tests passing as quickly as possible, even if the code isn't perfect <a class="yt-timestamp" data-t="07:54:00">[07:54:00]</a>. Solving a large problem is a series of small steps, and trying to perfect each step can be discouraging due to the long time it takes to reach the finish line <a class="yt-timestamp" data-t="08:05:00">[08:05:00]</a>.

Once a full working prototype is achieved, confidence is gained that the problem can be solved <a class="yt-timestamp" data-t="08:25:00">[08:25:00]</a>. This is the point to reflect on the code and improve it <a class="yt-timestamp" data-t="08:30:00">[08:30:00]</a>. It's much easier to improve a working piece of code than to write a perfect one from the start <a class="yt-timestamp" data-t="09:16:00">[09:16:00]</a>.

Some areas for improvement include:
*   Improving readability by naming things better <a class="yt-timestamp" data-t="09:03:00">[09:03:00]</a>.
*   Adding comments <a class="yt-timestamp" data-t="09:06:00">[09:06:00]</a>.
*   Removing duplication <a class="yt-timestamp" data-t="09:07:00">[09:07:00]</a>.
*   Improving the time and space complexity of algorithms <a class="yt-timestamp" data-t="09:08:00">[09:08:00]</a>.
*   Adding caching to reduce costs <a class="yt-timestamp" data-t="09:10:00">[09:10:00]</a>.
*   Improving error handling <a class="yt-timestamp" data-t="09:13:00">[09:13:00]</a>.

## Continuous Learning and Practice

Problem-solving, especially with tools like APIs, is a skill that requires continuous learning <a class="yt-timestamp" data-t="09:23:00">[09:23:00]</a>. There's an infinite number of problems, each with unique challenges <a class="yt-timestamp" data-t="09:26:00">[09:26:00]</a>. The best way to get good at this skill is through consistent practice, much like learning a musical instrument <a class="yt-timestamp" data-t="09:45:00">[09:45:00]</a>. Regular practice helps develop the ability to visualize how a computer system can solve a problem <a class="yt-timestamp" data-t="10:00:00">[10:00:00]</a>.

Finally, seeking feedback from more experienced developers is crucial for growth <a class="yt-timestamp" data-t="10:13:00">[10:13:00]</a>.