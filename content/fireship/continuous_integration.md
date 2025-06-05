---
title: Continuous integration
videoId: scEDHsr3APg
---

From: [[fireship]] <br/> 

[[devops_practices|DevOps]] involves a set of practices for building, testing, and releasing code in small, frequent steps <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. One of the core [[devops_practices|DevOps practices]] is **Continuous Integration (CI)** <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## How Continuous Integration Works
In CI, developers commit their code to a shared repository, often on a daily basis <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Each commit triggers an [[automated_workflow_in_ci|automated workflow]] on a CI server, which can notify developers of any issues encountered when integrating their changes <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. This process of evolving a repository in small steps helps prevent what is known as "merge hell" <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

### Preventing "Merge Hell"
"Merge hell" can occur when developers work on separate features for an extended period without integrating their changes. For example, if a back-end developer builds a new API and a front-end developer starts work on a new UI, and they don't integrate their work for several months, their features may become completely incompatible when it's time to merge them <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. This incompatibility can lead to build failures, requiring significant time and money to resolve the conflicts <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. CI prevents these issues by constantly integrating changes.

## Building a Continuous Integration Pipeline with GitHub Actions
A [[continuous_integration_pipeline_with_github_actions|continuous integration pipeline]] can be built using services like GitHub Actions <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. For a Node.js web application on GitHub, delivering the app to customers typically involves running commands such as `test`, `build`, and `deploy` <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. This entire process can be automated in the cloud using a CI service like GitHub Actions <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

To set up an [[continuous_integration_pipeline_with_github_actions|automated workflow with GitHub Actions]]:
1.  **Create a workflow**: Define the CI process <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
2.  **Set trigger**: Configure the workflow to run on every push to the master branch <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
3.  **Define jobs**: The event triggers a job that runs on a Linux container in the cloud <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.
4.  **Specify steps**: Within the container, a series of steps are executed:
    *   Checking out the code from the GitHub repository <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
    *   Setting up Node.js <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
    *   Installing dependencies <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
    *   Running `test`, `build`, and `deploy` commands <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

Anytime code is committed to the master branch, this workflow will run <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. If any of the steps fail, the problematic software will not be delivered to customers, and developers will be automatically notified of the issue that needs to be addressed <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

## Benefits of CI/CD
[[benefits_of_ci_cd|CI/CD offers two main benefits]]:
1.  **Automation**: It automates tasks that developers would otherwise have to perform manually, increasing development velocity <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. This contributes to better [[developer_productivity_tools|developer productivity]].
2.  **Early Problem Detection**: CI detects small problems early in the development cycle, preventing them from escalating into major issues <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. This ultimately leads to higher code quality <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.