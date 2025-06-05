---
title: DevOps practices
videoId: scEDHsr3APg
---

From: [[fireship]] <br/> 

DevOps is defined as a set of practices designed to build, test, and release code in small, frequent steps <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Core Practices

One of the core practices of DevOps is [[continuous_integration | continuous integration]] (CI) <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. In CI, developers commit their code to a shared repository, often on a daily basis <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Each commit then triggers an [[automated_workflow_in_ci | automated workflow]] on a CI server <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. This system notifies developers of any issues integrating their changes <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

### Preventing "Merge Hell"

By evolving a repository in small steps, CI helps prevent what is known as "merge Hell" <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. This scenario describes a situation where features developed independently over time become completely incompatible when it's time to merge them, leading to failed builds and significant time and cost to resolve conflicts <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

## Continuous Integration Pipeline Example

A [[continuous_integration_pipeline_with_github_actions | continuous integration pipeline]] can be built using services like GitHub Actions <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. For a Node.js web application, the necessary commands are typically `test`, `build`, and `deploy` <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

### Automating with GitHub Actions

To automate this process using GitHub Actions, a workflow is created and configured to run on every push to the master branch <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. This event triggers a job that executes on a Linux container in the cloud <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. The container follows a series of steps:
1.  Checks out the code from the GitHub repository <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
2.  Sets up Node.js <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
3.  Installs dependencies <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
4.  Runs the test, build, and deploy commands <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

If any of these steps fail, the problematic software will not be delivered to customers, and developers are automatically notified of the issue that needs addressing <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

## Benefits

[[benefits_of_ci_cd | CI/CD]] (Continuous Integration/Continuous Deployment) offers two main benefits <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>:
*   **Automation**: It automates tasks that would otherwise require manual intervention by [[developer_productivity_tools | developers]] <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. This automation helps increase development velocity <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
*   **Early Problem Detection**: It detects small problems early in the development cycle before they can escalate into major disasters <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. This proactive approach results in higher code quality <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.