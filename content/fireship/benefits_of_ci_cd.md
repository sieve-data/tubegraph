---
title: Benefits of CI CD
videoId: scEDHsr3APg
---

From: [[fireship]] <br/> 

[[devops_practices | DevOps]] is a set of practices designed to build, test, and release code in small, frequent steps <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. A core practice within [[devops_practices | DevOps]] is [[continuous_integration | continuous integration]] <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## What is Continuous Integration?
[[continuous_integration | Continuous integration]] involves developers committing their code to a shared repository, often on a daily basis <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. Each commit initiates an [[automated_workflow_in_ci | automated workflow]] on a CI server, which can alert developers to any integration issues with their changes <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

This approach of evolving a repository in small, incremental steps helps prevent a common issue known as "merge hell" <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

> [!EXAMPLE] Merge Hell Scenario
> Imagine a backend developer, Mary, builds a new API <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. Shortly after, a frontend developer, Jane, begins work on a new UI <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. If they work in isolation for months, when it's time to merge their features, they might find them completely incompatible, leading to build failures and significant time and money spent resolving conflicts <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

## Building a CI Pipeline
A [[continuous_integration | continuous integration]] pipeline can prevent such issues <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. For a Node.js web application, delivering the product to customers might require running three commands: `test`, `build`, and `deploy` <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. This entire process can be automated in the cloud using a CI service like GitHub Actions <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

### Workflow Setup
1.  **Create a workflow**: Define the CI process <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
2.  **Trigger event**: Configure the workflow to run on every push to the master branch <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
3.  **Job execution**: The event triggers a job that runs on a Linux container in the cloud <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.
4.  **Series of steps**: The container executes a defined sequence of actions <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>:
    *   Checks out the code from the GitHub repository <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
    *   Sets up Node.js <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
    *   Installs dependencies <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
    *   Runs the `test`, `build`, and `deploy` commands <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

Anytime code is committed to the master branch, this workflow will execute <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. If any step fails, the problematic software will not be delivered to customers, and developers will automatically be notified of the issue <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

## Key Benefits of CI/CD

CI/CD offers two primary advantages <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>:

*   **Automation of Manual Tasks**: It automates processes that would otherwise need to be performed manually by developers <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. This automation significantly increases development velocity <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
*   **Early Problem Detection**: CI/CD systems detect small problems early in the development cycle before they can escalate into major disasters <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. This early detection leads to higher code quality <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.