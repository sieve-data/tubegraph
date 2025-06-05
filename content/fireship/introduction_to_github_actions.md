---
title: Introduction to GitHub Actions
videoId: eB0nUzAI7M8
---

From: [[fireship]] <br/> 

One of the most effective ways to boost productivity in a software project is to [[automating_with_github_actions | automate anything manual or repetitive]] <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. [[automating_with_github_actions | GitHub Actions]] is a powerful tool that makes automation easy to implement <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This tool can significantly improve code quality and enhance productivity through DevOps practices <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## What are GitHub Actions?

[[Introduction to Git and Github | GitHub Actions]] is a feature available on [[Introduction to Git and Github | GitHub]] that allows you to automate workflows based on events that occur within a [[Introduction to Git and Github | GitHub repository]] <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

Key concepts:
*   **Events**: These are specific occurrences in a [[Introduction to Git and Github | GitHub]] repo that can trigger automation, such as starring a repo, sending a pull request, or merging code into a branch <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
*   **Workflows**: Any event can trigger an automated workflow <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. A workflow can spin up one or more containers in the cloud and then execute a set of defined steps <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. [[Introduction to Git and Github | GitHub]] logs the progress of each step, indicating success or failure <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
*   **Steps/Actions**: Instead of writing every instruction from scratch, you can use pre-implemented steps provided by the community <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. Each step is a reusable chunk of code, often referred to as an "action" <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. Hundreds of reusable actions are available on [[Introduction to Git and Github | GitHub]], each being its own [[Version Control Basics with Git | Git]] repository that can be forked and customized <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

The only prerequisite for using [[Introduction to Git and Github | GitHub Actions]] is a [[Introduction to Git and Github | GitHub repository]] <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. [[Introduction to Git and Github | GitHub]] offers a very generous free tier <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

### Workflow Configuration

Workflows are defined in YAML files located within a `.github/workflows` directory in your [[Introduction to Git and Github | repository]] <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. Any YAML file in this directory will be automatically picked up and set up as a workflow by [[Introduction to Git and Github | GitHub]] <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

A basic workflow structure includes:
*   `name`: A human-readable name for the workflow <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
*   `on`: Specifies the event(s) that trigger the workflow, such as `pull_request` or `push` <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
*   `jobs`: Defines one or more jobs to be executed <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
    *   Each job has a name (e.g., `test-pull-request`) <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
    *   `runs-on`: Specifies the virtual machine environment (e.g., Ubuntu, Windows, Mac OS) <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
    *   `steps`: A sequence of instructions that build and test your code <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. Common steps include:
        *   `uses: actions/checkout@v2`: An official action to bring your source code into the virtual machine's working directory <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
        *   `uses: actions/setup-node@v2`: An action to set up Node.js for running commands <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
        *   `run`: Executes shell commands, such as `npm ci` (for clean dependency installation), `npm test`, or `npm run build` <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

## Common Use Cases

### [[Continuous Integration with GitHub Actions | Continuous Integration (CI)]]

[[Continuous Integration with GitHub Actions | CI]] is a practice where developers frequently submit small, maintainable code changes to the main codebase, typically on a daily basis <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. These changes should be automatically tested against the main codebase <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

A typical [[Continuous Integration with GitHub Actions | CI]] workflow is triggered on a `pull_request` to the `master` branch <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. If tests fail or code fails to build, [[Introduction to Git and Github | GitHub]] displays a red checkmark, indicating that the pull request should not be merged <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. A green checkmark indicates success <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.

### Continuous Deployment (CD)

While [[Continuous Integration with GitHub Actions | CI]] focuses on merging new code into the codebase, Continuous Deployment is about automatically pushing that code out to customers <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

A CD workflow often triggers on a `push` event to the `master` branch (or a merge of a pull request) <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.

::info
To deploy to a third-party host like Firebase, you'll need to securely share a secret token with [[Introduction to Git and Github | GitHub Actions]] <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. This is done by obtaining an API key (e.g., via `firebase login --ci`) <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>, then adding it as a secret in your [[Introduction to Git and Github | GitHub repository]] settings (e.g., `FIREBASE_TOKEN`) <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>. [[Introduction to Git and Github | GitHub]] encrypts these values, allowing secure access from your CI server via `secrets.SECRET_NAME` <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.
::

Third-party actions, like the `firebase-action`, simplify deployment by handling the setup of necessary CLIs and commands <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.

### Automating Releases to Package Managers

For projects that maintain libraries, [[Introduction to Git and Github | GitHub Actions]] can automate the release process to package managers like NPM or the [[Introduction to Git and Github | GitHub]] Package Registry <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.

This type of workflow is typically triggered by a `release` event, as not every code change on the `master` branch warrants a new release <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.

Workflows can contain multiple jobs. By default, jobs run concurrently <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>. However, the `needs` keyword can be used to define dependencies between jobs, ensuring one job completes before another begins (e.g., building code before publishing it) <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. This is useful for building code once and deploying it to multiple registries <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.

### Integrating with Communication Tools

[[Introduction to Git and Github | GitHub Actions]] can also integrate with various communication tools like Slack, Discord, Jira, and Trello <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>. Many community-maintained actions exist for easy integration into workflows <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. For example, a workflow can be configured to send a Slack notification every time a new [[Introduction to Git and Github | GitHub]] issue is posted <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.

It's important to distinguish between **Actions** and **[[Introduction to Git and Github | GitHub Apps]]** found in the [[Introduction to Git and Github | GitHub]] marketplace <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>:
*   **Actions**: Reusable pieces of code used within your own workflows <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.
*   **[[Introduction to Git and Github | GitHub Apps]]**: Fully pre-built solutions that don't require you to deploy any code <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>. They can be installed by clicking a few buttons and can be used across multiple repositories simultaneously <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>.

### [[Using GitHub Actions for Scheduled Tasks | Running on a Schedule]]

[[Introduction to Git and Github | GitHub Actions]] can be configured to run on a specific schedule, similar to cron jobs <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>. This is useful for tasks that need to occur periodically, such as exporting database data <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.

The `on: schedule` event is used, followed by a cron schedule string <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>. Tools like Crontab Guru can help generate these schedules <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>. For example, a workflow could run every night at midnight to export Firestore data to a storage bucket using a Google Cloud Platform action <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>.