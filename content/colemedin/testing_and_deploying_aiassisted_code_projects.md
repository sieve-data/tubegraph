---
title: Testing and deploying AIassisted code projects
videoId: SS5DYx6mPw8
---

From: [[colemedin]] <br/> 

To ensure high-quality outputs consistently when [[using_ai_coding_assistance | using AI to code]], a well-defined process is essential <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. This process includes structured testing and deployment phases.

## Importance of Testing AI-Assisted Code

It is crucial to ask the AI coding assistant to write tests for its code, ideally after every new feature is implemented, to achieve consistent output <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. While some AI coding assistants might not initially create tests or update documentation, these steps can be requested in follow-up prompts <a class="yt-timestamp" data-t="00:21:27">[00:21:27]</a>, <a class="yt-timestamp" data-t="00:25:25">[00:25:25]</a>.

### Testing Best Practices

Best practices for testing can be included in the AI coding assistant's global rules or system prompts <a class="yt-timestamp" data-t="00:26:25">[00:26:25]</a>, <a class="yt-timestamp" data-t="00:26:30">[00:26:30]</a>. These rules ensure the AI follows desired guidelines:
*   **Dedicated Test Directory** Ensure tests are placed in a specific directory <a class="yt-timestamp" data-t="00:26:43">[00:26:43]</a>.
*   **Mocking Calls** Mock calls to databases and Large Language Models (LLMs) so tests are fast and free <a class="yt-timestamp" data-t="00:26:47">[00:26:47]</a>.
*   **Scenario Coverage** Test for successful scenarios, proper error handling, and edge cases <a class="yt-timestamp" data-t="00:26:53">[00:26:53]</a>.

Test files can sometimes be longer than the base code file itself due to the need to cover all scenarios <a class="yt-timestamp" data-t="00:28:34">[00:28:34]</a>. Once tests are created, they can be run using commands like `pytest` from the terminal <a class="yt-timestamp" data-t="00:28:02">[00:28:02]</a>. For example, testing a Superbase MCP server involved 14 passing tests, covering successful cases, failures, and edge scenarios for each tool <a class="yt-timestamp" data-t="00:28:11">[00:28:11]</a>.

### Version Control and Backups

Before implementing new features or making significant changes (e.g., adding a README or tweaking functionality), it's highly recommended to make a Git commit to save the current state of the project <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>, <a class="yt-timestamp" data-t="00:24:05">[00:24:05]</a>. This allows for reverting to a working state if the AI coding assistant introduces breaking changes, preventing situations where the project becomes too broken to recover <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>. AI IDEs often have native commands for Git operations, or a Git MCP server can be used <a class="yt-timestamp" data-t="00:24:30">[00:24:30]</a>.

## Deploying AI-Assisted Applications

Once a project developed with [[building_applications_with_ai_assistance | AI assistance]] reaches a deployable state, AI coding assistants can assist with packaging and shipping it to the cloud or sharing with others <a class="yt-timestamp" data-t="00:29:21">[00:29:21]</a>.

### Using Docker for Deployment

A common and effective method for deployment is using Docker or similar services like Podman <a class="yt-timestamp" data-t="00:29:37">[00:29:37]</a>. LLMs are proficient at working with Docker due to the abundance of training data available online <a class="yt-timestamp" data-t="00:29:42">[00:29:42]</a>.

AI coding assistants can help:
*   **Create Dockerfiles** To package and deploy the application, potentially using a `requirements.txt` file for Python dependencies <a class="yt-timestamp" data-t="00:29:51">[00:29:51]</a>, <a class="yt-timestamp" data-t="00:30:00">[00:30:00]</a>.
*   **Provide Commands** Output the necessary commands to build the container <a class="yt-timestamp" data-t="00:29:57">[00:29:57]</a>, <a class="yt-timestamp" data-t="00:30:06">[00:30:06]</a>.

This process enables users to clone a repository, build the container, and set up the configuration within their AI IDE (e.g., Windsurf, Cursor) or other tools <a class="yt-timestamp" data-t="00:30:50">[00:30:50]</a>. This demonstrates a complete workflow from ideation to implementation, testing, documentation, and finally, [[deploying_ai_applications_without_coding | deploying the AI-assisted project]] <a class="yt-timestamp" data-t="00:31:01">[00:31:01]</a>.