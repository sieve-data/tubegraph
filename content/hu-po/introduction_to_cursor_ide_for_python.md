---
title: Introduction to Cursor IDE for Python
videoId: uvZBlufZHP4
---

From: [[hu-po]] <br/> 

Cursor is an [[features_of_cursor_ide_compared_to_vs_code_and_other_coding_environments | AI-first code editor]] that aims to integrate generative AI capabilities more deeply into the development workflow compared to traditional IDEs like VS Code <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. It operates as a startup <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a> and functions either as a mimic or an extension of VS Code, running its own instance of VS Code with Cursor features built-in <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

## AI Integration Features

Cursor's primary value proposition is its deep integration of AI functionality, specifically leveraging OpenAI's API (GPT-4) rather than its own language model <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. This contrasts with a typical workflow where a developer might switch between a browser tab with ChatGPT and their coding environment <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

### Key Features and Functionality

Cursor provides several shortcuts and tools for [[using_ai_integration_in_coding_environments | AI-driven coding]]:

*   **Edit and Write Code (Ctrl/Cmd+K):** Users can select code and prompt the AI to edit or generate new code based on instructions <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. For example, it can add docstrings to functions <a class="yt-timestamp" data-t="00:19:05">[00:19:05]</a> or refactor code <a class="yt-timestamp" data-t="00:59:00">[00:59:00]</a>.
*   **Chat (Cmd+Shift+L):** Allows users to ask questions about their code or general programming topics within the IDE <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   **Chat with Codebase:** A powerful feature that allows the AI to consider the entire codebase as context when answering questions or generating code <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. This becomes more useful as the size of the codebase increases <a class="yt-timestamp" data-t="00:23:26">[00:23:26]</a>.
*   **Auto Debug:** An agent designed to fix errors. When a terminal error occurs, a blue "Auto debug" button appears, prompting the AI to suggest fixes <a class="yt-timestamp" data-t="00:27:59">[00:27:59]</a>. While it can identify bugs and suggest solutions (e.g., removing an unused import or adding a missing argument) <a class="yt-timestamp" data-t="00:28:41">[00:28:41]</a>, it may require manual application of the suggested fix <a class="yt-timestamp" data-t="00:29:07">[00:29:07]</a>.
*   **Fix Lints:** Helps quickly resolve linting errors. Users can hover over an error and click a "fix" button <a class="yt-timestamp" data-t="00:56:41">[00:56:41]</a>. For instance, it can change `import *` statements to explicit imports or enforce global variable naming conventions <a class="yt-timestamp" data-t="00:57:23">[00:57:23]</a>.
*   **Documentation Integration (`@libraryname`):** Improves the AI's understanding of third-party libraries. Users can type `@libraryname` in chat or command K to have Cursor crawl custom documentation <a class="yt-timestamp" data-t="00:43:42">[00:43:42]</a>. This allows the AI to provide context-aware suggestions based on specific library documentation, such as the Dynamixel SDK <a class="yt-timestamp" data-t="00:46:09">[00:46:09]</a>.

### Python Environment Management

When [[setting_up_a_coding_environment_for_machine_learning | setting up a coding environment for machine learning]], Cursor allows users to select their Python interpreter <a class="yt-timestamp" data-t="00:33:01">[00:33:01]</a>. However, it may not automatically detect or utilize active conda environments, requiring manual selection of the Python executable path <a class="yt-timestamp" data-t="00:32:21">[00:32:21]</a>.

### Limitations and Challenges
*   **File Manipulation:** While the IDE allows manual drag-and-drop file movement in the UI, the AI itself cannot directly manipulate files (e.g., move scripts to a different directory) <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. It can only provide instructions on how to do so <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
*   **Slowness:** AI-driven code edits can feel slow, requiring the user to wait for the AI to generate and apply changes <a class="yt-timestamp" data-t="00:27:21">[00:27:21]</a>.
*   **Lack of Real-time Linting:** Unlike VS Code, Cursor does not provide immediate visual feedback (e.g., red highlights) for syntax errors or undefined variables <a class="yt-timestamp" data-t="00:30:06">[00:30:06]</a>.
*   **Monetization Model:** Cursor charges a subscription fee, which includes a limit on GPT-4 requests <a class="yt-timestamp" data-t="00:21:27">[00:21:27]</a>. Users cannot directly use their own OpenAI API keys for these requests through Cursor's built-in AI features <a class="yt-timestamp" data-t="00:21:55">[00:21:55]</a>.

## Comparison with VS Code and GitHub Copilot

Cursor's functionality is often compared to [[features_of_cursor_ide_compared_to_vs_code_and_other_coding_environments | VS Code with GitHub Copilot]].
*   **Tab Autocomplete:** GitHub Copilot excels at anticipating and auto-completing code with context, often generating full test cases or function implementations with a simple `Tab` key press <a class="yt-timestamp" data-t="01:01:56">[01:01:56]</a>. This can feel more intuitive for quick code generation than Cursor's explicit "edit with AI" commands <a class="yt-timestamp" data-t="01:02:31">[01:02:31]</a>.
*   **Underlying Technology:** Both rely on large language models (primarily GPT-4 for Cursor, and similar models for Copilot). The core AI capabilities are comparable, meaning the "better code suggestions" might not differ significantly <a class="yt-timestamp" data-t="01:25:22">[01:25:22]</a>.
*   **Feature Parity:** Microsoft, with its resources and ownership of VS Code and GitHub, is likely developing and integrating similar AI features into Copilot and VS Code natively <a class="yt-timestamp" data-t="01:06:17">[01:06:17]</a>. GitHub Next, for example, is exploring advanced AI-driven coding tools like "Copilot Voice" and "Code Brushes" <a class="yt-timestamp" data-t="01:26:03">[01:26:03]</a>.

## Cost and Sustainability Concerns

Cursor operates on a subscription model, costing around $20 per month <a class="yt-timestamp" data-t="00:21:29">[00:21:29]</a>. This cost is in addition to any existing OpenAI API usage or Copilot subscriptions. The long-term viability of Cursor as a standalone product is questioned given Microsoft's potential to integrate similar, if not superior, features directly into VS Code <a class="yt-timestamp" data-t="01:06:36">[01:06:36]</a>. An acquisition by a larger company like Microsoft is seen as a possible exit strategy for Cursor <a class="yt-timestamp" data-t="01:06:52">[01:06:52]</a>.

## Real-world Application: Robotic Cat Toy Project

The capabilities of Cursor IDE were demonstrated in the context of developing a robotic cat toy project <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. This project involves:
*   **Hardware:** Servos and a Raspberry Pi <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   **Control:** Using a Large Language Model (LLM) to directly output servo commands, similar to Google's RT-2 approach <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
*   **[[python_scripting_for_3d_applications_and_workflows | Python scripting for 3D applications and workflows]] (or robotics in this case):** Python scripts control the functionality, including `gpt.py` (for LLM interaction), `camera.py` (for camera control using CV2), and `servo.py` (for servo control using Dynamixel SDK) <a class="yt-timestamp" data-t="01:13:06">[01:13:06]</a>.
*   **Code Refactoring:** Cursor was used to suggest and implement improvements to the project's directory structure <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>, refactor code for better maintainability (e.g., using a single port handler for multiple servos in `servo.py`) <a class="yt-timestamp" data-t="00:47:50">[00:47:50]</a>, and implement bulk read/write operations for servos using the Dynamixel SDK documentation <a class="yt-timestamp" data-t="00:51:53">[00:51:53]</a>.
*   **[[importing_python_libraries | Importing Python libraries]]** like `openai` and `cv2` were key, and Cursor assisted in adding necessary imports and ensuring correct usage <a class="yt-timestamp" data-t="00:30:58">[00:30:58]</a>.
*   **Logging:** The IDE helped convert `print` statements to structured logging using a shared logger object across different Python modules <a class="yt-timestamp" data-t="01:09:52">[01:09:52]</a>.

```python
# Example of AI-suggested refactoring for logging
import logging
from src.utils.logger import PlayLogger  # Assuming PlayLogger is defined

class Robot:
    def __init__(self, device_name, baud_rate, protocol_version, servo_ids):
        self.log = PlayLogger(logging.DEBUG)  # Initialize logger
        # ... rest of init
        self.log.info("Robot initialized.") <a class="yt-timestamp" data-t="01:10:42">[01:10:42]</a>

    def move(self, goal_positions):
        self.log.debug(f"Attempting to move servos to: {goal_positions}") <a class="yt-timestamp" data-t="01:09:52">[01:09:52]</a>
        # ... bulk write logic
        self.log.info("Servos moved.") <a class="yt-timestamp" data-t="01:10:04">[01:10:04]</a>
```
This example illustrates how [[exploring_functionality_and_limitations_of_aidriven_coding_tools | AI-driven coding tools]] can streamline development by automating common tasks.