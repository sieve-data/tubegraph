---
title: Continuous integration pipeline with Github Actions
videoId: scEDHsr3APg
---

From: [[fireship]] <br/> 

[[DevOps practices | DevOps]] is a set of practices designed to build, test, and release code in small, frequent steps <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. A core practice within [[DevOps practices | DevOps]] is [[continuous_integration | Continuous Integration]] (CI) <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## Understanding Continuous Integration

In [[continuous_integration | Continuous Integration]], developers commit their code to a shared repository, often on a daily basis <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Each commit then triggers an [[automated_workflow_in_ci | automated workflow]] on a CI server <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. This system can notify developers of any issues encountered when integrating their changes <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

This approach helps prevent "merge hell," a situation where incompatible features are merged much later in the development cycle, leading to failed builds and significant time and cost to resolve conflicts <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## Building a CI Pipeline with GitHub Actions

To illustrate how [[continuous_integration | CI]] prevents integration issues, a [[continuous_integration | CI]] pipeline can be built using GitHub Actions <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

### Example: Node.js Web App

Consider a Node.js web application hosted on GitHub <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. To deliver this application to customers, it typically requires three commands: `test`, `build`, and `deploy` <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. These commands can be automated in the cloud using a CI service like GitHub Actions <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

### Workflow Configuration

1.  **Create a Workflow:** The first step is to create a workflow file within the repository <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
2.  **Define Trigger:** Configure the workflow to run automatically on every `push` event to the `master` branch <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
3.  **Job Execution Environment:** This event triggers a job that runs on a Linux container in the cloud <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.
4.  **Specify Steps:** The container is instructed to perform a series of steps:
    *   Check out the code from the GitHub repository <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
    *   Set up Node.js <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
    *   Install project dependencies <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
    *   Run the defined `test`, `build`, and `deploy` commands <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

### Outcome

Once configured, any code committed to the `master` branch in this repository will automatically execute this workflow <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. If any of the steps within the workflow fail, the problematic software will not be delivered to customers, and developers will be automatically notified of the issue that needs addressing <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

## Benefits of CI/CD

[[Benefits of CI CD | CI/CD]] offers significant advantages:
*   **Automation:** It automates tasks that would otherwise require manual effort from developers, increasing development velocity <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
*   **Early Problem Detection:** It detects small problems early in the development cycle, preventing them from escalating into major disasters <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. This leads to higher code quality <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.