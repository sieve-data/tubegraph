---
title: Role of product managers in AI coding
videoId: BblTkXR-3eo
---

From: [[gregisenberg]] <br/> 

The emergence of [[future_of_ai_coding_tools_and_their_development_potential | AI coding]] tools has significantly reshaped the traditional workflow of product development, particularly impacting the [[role_and_skills_of_a_product_manager_in_tech | product manager]] <a class="yt-timestamp" data-t="00:18:50">[00:18:50]</a>. Previously, product managers would write detailed specifications (specs) and hand them over to engineers, who would then build the product <a class="yt-timestamp" data-t="00:35:37">[00:35:37]</a>. With [[future_of_ai_coding_tools_and_their_development_potential | AI coding]], the [[role_and_skills_of_a_product_manager_in_tech | product manager]] can now directly engage in building the product themselves <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>.

## Challenges of AI-Powered Coding

Initially, many tutorials suggest that [[using_ai_for_app_development | AI coding]] involves simply prompting an AI to build an entire application <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. However, in reality, the results are often unpredictable, leading to numerous errors due to the "hallucinatory" nature of large language models <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. This unpredictability makes it challenging to achieve a smooth and consistent outcome <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

## A Streamlined AI Coding Workflow

To address these challenges and achieve more consistent results, a structured workflow is recommended, drawing parallels from traditional product team dynamics <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>, <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. This workflow emphasizes upfront planning and clear communication with the AI, mirroring the collaboration between a [[role_and_skills_of_a_product_manager_in_tech | product manager]] and an engineering manager <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

### 1. Writing Clear and Detailed Specs

The most crucial step is to spend significant time writing very clear and detailed specifications <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. This process is considered an "art" and is vital for communicating effectively with the AI <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>, <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. A common structure for these specs includes:

*   **Project Overview** A concise description of the project's goal <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
*   **Core Functionality** A breakdown of essential features, similar to what a [[role_and_skills_of_a_product_manager_in_tech | product manager]] would outline <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>, <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>. This should be clear enough to convey the project's goals <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>.
*   **Documentation for Key Features** Including proof-of-concept code snippets for critical functionalities, which helps align the AI's understanding early on <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>, <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>. This involves researching packages, testing code, and documenting expected responses <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>, <a class="yt-timestamp" data-t="00:19:12">[00:19:12]</a>, <a class="yt-timestamp" data-t="00:31:54">[00:31:54]</a>.
*   **Current File Structure** Providing the AI with knowledge of the existing file structure prevents it from creating files in the wrong places or with incorrect dependencies <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>, <a class="yt-timestamp" data-t="00:34:06">[00:34:06]</a>.
*   **Additional Requirements** Project-specific notes that address common pitfalls or missed elements by AI, such as environment variables or error handling <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.

This detailed planning uncovers uncertainties upfront, leading to more consistent results <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

### 2. Leveraging AI as an "Engineer Manager"

After drafting the initial specs, a stronger AI model (like 01) can be used to act as an "engineer manager," filling in the intricate details of the project structure and dependencies <a class="yt-timestamp" data-t="00:35:40">[00:35:40]</a>, <a class="yt-timestamp" data-t="00:37:40">[00:37:40]</a>. This step helps define functionality in greater detail, including variables and file structures, and ultimately creates a highly detailed Product Requirements Document (PRD) <a class="yt-timestamp" data-t="00:37:40">[00:37:40]</a>, <a class="yt-timestamp" data-t="00:38:05">[00:38:05]</a>. A strong PRD reduces ambiguity and ensures the end product aligns with expectations <a class="yt-timestamp" data-t="00:38:13">[00:38:13]</a>, <a class="yt-timestamp" data-t="00:38:34">[00:38:34]</a>.

### 3. Iterative Development with AI Tools

Once the detailed specs are ready, tools like Cursor can be used to build the application in a step-by-step manner <a class="yt-timestamp" data-t="00:39:52">[00:39:52]</a>. Breaking down the development into smaller tasks reduces the likelihood of errors and allows for targeted debugging <a class="yt-timestamp" data-t="00:40:48">[00:40:48]</a>, <a class="yt-timestamp" data-t="00:27:19">[00:27:19]</a>. When errors occur, using prompts like "help me debug" or "let's think step by step" can guide the AI to a solution <a class="yt-timestamp" data-t="00:27:35">[00:27:35]</a>, <a class="yt-timestamp" data-t="00:29:25">[00:29:25]</a>.

### 4. Functionality First, UI Second

A key strategy is to focus on building the core functionality first, ignoring the UI in the initial stages <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>, <a class="yt-timestamp" data-t="00:40:21">[00:40:21]</a>. Once the functionality is established, tools like Vercel's V0 can be used to refine the user interface <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>, <a class="yt-timestamp" data-t="00:46:02">[00:46:02]</a>. This approach makes UI refinement more predictable and reduces the room for errors, as the underlying code structure is already robust <a class="yt-timestamp" data-t="00:46:13">[00:46:13]</a>, <a class="yt-timestamp" data-t="00:49:24">[00:49:24]</a>.

### 5. Reusable Modular Prompts

Developing and sharing "reusable modular prompts" for standard features like user authentication or payment systems can significantly speed up the development process <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>, <a class="yt-timestamp" data-t="00:47:00">[00:47:00]</a>, <a class="yt-timestamp" data-t="00:52:01">[00:52:01]</a>. These prompts, which encapsulate common functionalities, can be easily integrated into new applications <a class="yt-timestamp" data-t="00:51:17">[00:51:17]</a>, <a class="yt-timestamp" data-t="00:52:27">[00:52:27]</a>.

## The Future of the Product Manager Role

[[Competition and product development in AI | AI coding]] enables a wider range of individuals to become "AI coders" and act as their own product managers <a class="yt-timestamp" data-t="00:18:46">[00:18:46]</a>, <a class="yt-timestamp" data-t="00:55:01">[00:55:01]</a>, allowing those who didn't previously write code to build applications <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>. While [[ai_product_designers | AI product designers]] and coders don't replace human effort, they act as an "electric assisted bicycle," providing a "little boost" to the development process <a class="yt-timestamp" data-t="00:57:41">[00:57:41]</a>. The role of the [[role_and_skills_of_a_product_manager_in_tech | product manager]] in this evolving landscape is to embrace structured workflows, meticulous planning, and iterative development to harness the full potential of [[using_ai_tools_to_build_saas_products | AI tools to build SaaS products]] and [[using_ai_tools_for_product_design | product design]] efficiently and effectively.