---
title: Error handling and workflow scheduling in n8n
videoId: Nsu9BzQv5C4
---

From: [[colemedin]] <br/> 

[[ai_automation_with_n8n | n8n]] is a powerful no-code AI automation tool used to build AI agents and integrate with over 500 applications <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. To make [[ai_automation_with_n8n | n8n]] workflows production-ready and efficient, it's crucial to understand how to handle errors and schedule workflows.

## Error Workflows

Error workflows are essential for making your [[ai_automation_with_n8n | n8n]] workflows production-ready by handling situations when something goes wrong <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

### Setting Up Error Workflows
To set up an error workflow:
1.  Create a new workflow in [[ai_automation_with_n8n | n8n]] <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
2.  Add an "Error Trigger" node as the starting point <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. This trigger is found by searching for "error" in the node options <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.
3.  Within this error workflow, you can define actions to take when an error occurs, such as sending a Slack message with error details to alert you <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.

### Connecting to Main Workflows
To hook an error workflow into another workflow:
1.  Open the workflow you want to monitor for errors <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
2.  Click on the three dots in the top right corner of the workflow interface <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.
3.  Go to "Settings" <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.
4.  Select the error workflow you created to be triggered when an error occurs in the current workflow <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.
5.  Click "Save" <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

Once set up, if anything goes wrong in the monitored workflow, the designated error workflow will trigger, for example, sending a Slack message <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. This is highly useful for production monitoring <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.

## Workflow Scheduling

The schedule trigger is an underutilized feature in [[ai_automation_with_n8n | n8n]] that allows workflows to trigger on a consistent interval <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.

### Benefits of Scheduling
*   **Consistent Execution:** Workflows can trigger every day, every hour, or at any custom interval <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>.
*   **Time-Based Tasks:** It's perfect for tasks that cannot be event-based and need to run at a set time periodically <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

### Example Use Case
A common application for the schedule trigger is generating reports <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>. For instance, you could schedule a workflow to:
1.  Fetch all overdue tasks in a project (e.g., from Asana) <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.
2.  Send a Slack message alerting users that these tasks need to be completed <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>.

This type of task doesn't rely on an external event within an app but rather needs to run at specific, predefined times <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.