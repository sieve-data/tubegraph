---
title: Automating with GitHub Actions
videoId: eB0nUzAI7M8
---

From: [[fireship]] <br/> 

Automating manual or repetitive tasks is one of the most effective ways to boost productivity in a software project <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This can be easily achieved using a tool like [[introduction_to_github_actions | GitHub Actions]] <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. By leveraging the power of DevOps, [[introduction_to_github_actions | GitHub Actions]] can enhance code quality and streamline development processes <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## What are [[introduction_to_github_actions | GitHub Actions]]?

[[introduction_to_github_actions | GitHub Actions]] is a service built into [[introduction_to_git_and_github | GitHub]] that allows you to automate workflows based on events occurring in a [[introduction_to_git_and_github | GitHub repository]] <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. The service offers a generous free tier <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

### Events and Workflows

In a [[introduction_to_git_and_github | GitHub]] repository, various events can occur, such as starring a repository, sending a pull request, or merging code into the main branch <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. Any of these events can trigger an automated workflow <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

A workflow is a configurable automated process defined in a YAML file within a `.github/workflows` directory in your repository <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. It can spin up one or more containers in the cloud to execute a predefined set of steps <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. [[introduction_to_github_actions | GitHub]] logs the progress of each step, indicating clearly if anything failed <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

### Jobs and Steps

Every workflow consists of one or more jobs, each running on a specified virtual machine (e.g., Ubuntu, Windows, or macOS) <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. Within each job, you define a sequence of steps, which are instructions for the container to perform a task <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

### Reusable Actions

Instead of writing all steps from scratch, you can use pre-implemented steps called "actions," which are reusable chunks of code <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. Hundreds of reusable actions are available on [[introduction_to_git_and_github | GitHub]], each solving common problems and often residing in their own [[introduction_to_git_and_github | Git]] repositories that can be forked and customized <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

## [[continuous_integration_with_github_actions | Continuous Integration (CI)]]

[[continuous_integration_with_github_actions | Continuous Integration]] (CI) is a practice where developers submit their code to the main codebase in small, maintainable chunks, typically on a daily basis <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. These changes are then automatically tested against the main codebase <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

### Setting up the CI Workflow

To implement CI, you can configure a workflow to run a test suite whenever a pull request is made to the `master` branch <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. If tests or the build fail, a red checkmark appears, signaling not to merge the pull request; a green checkmark indicates success <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.

A CI workflow YAML file will typically include:
*   `name`: A descriptive name for the workflow, e.g., "Node Continuous Integration" <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
*   `on`: The event that triggers the workflow, such as `pull_request` targeting the `master` branch <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
*   `jobs`: One or more jobs to be executed.
    *   Each job specifies `runs-on` to define the virtual machine environment (e.g., `ubuntu-latest`) <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
    *   `steps`: A sequence of actions. Common steps include:
        *   Using the `checkout` action to get the source code into the VM <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
        *   Using the `setup-node` action to configure Node.js <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
        *   Running `npm ci` to install dependencies <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
        *   Executing test commands (e.g., `npm test`) <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
        *   Running build commands (e.g., `npm run build`) to ensure compilation <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.

> [!NOTE]
> For complex test suites like end-to-end tests with Cypress, there are often existing actions to set up the test runner automatically <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

### Testing the CI Workflow

After committing the workflow file to the `master` branch, you can test it by creating a new branch, making changes that might cause tests to fail, and then creating a pull request <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. The [[introduction_to_github_actions | GitHub Actions]] tab will show real-time logging of the checks <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. If tests fail, you can review the logs, fix the code, and push another commit to the same branch, which will automatically re-run the workflow <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

## [[continuous_deployment_using_firebase | Continuous Deployment (CD)]]

While [[continuous_integration_with_github_actions | continuous integration]] focuses on merging new code into the codebase, [[continuous_deployment_using_firebase | continuous deployment]] is about automatically pushing that code out to customers <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

### Setting up Authentication (Secrets)

To allow a remote CI server to deploy code, you need to authenticate it with your hosting service (e.g., Firebase) <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. This is typically done by sharing a secret token with [[introduction_to_github_actions | GitHub]] <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

For Firebase, you can obtain a token by running `firebase login --ci` in your terminal <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>. This token acts as an API key <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>. This secret value should then be added to your [[introduction_to_git_and_github | GitHub]] repository's settings under "Secrets," providing a name (e.g., `FIREBASE_TOKEN`) and pasting the token value <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. [[introduction_to_github_actions | GitHub]] encrypts this value, allowing secure access from your CI server <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

### Setting up the CD Workflow

A CD workflow will typically be triggered by a `push` event to the `master` branch <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. This means it runs when code is pushed directly to `master` or when a pull request is merged into it <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>.

The job structure is similar to CI, including checking out the code, setting up Node.js, and running the build command <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. For deployment, a third-party action, such as the Firebase action, can be used <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>. This action can set up the Firebase CLI on the server and execute deployment commands (e.g., `firebase deploy --only hosting`), using the securely stored `FIREBASE_TOKEN` environment variable <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.

Once the CD workflow is committed to the `master` branch, merging a pull request will automatically build and deploy the code to Firebase, reflecting changes on the website <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.

## Beyond CI/CD: Other Automation Examples

[[introduction_to_github_actions | GitHub Actions]] can automate various other tasks beyond typical CI/CD pipelines <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.

### Automating Package Releases (NPM)

For library maintainers, [[introduction_to_github_actions | GitHub Actions]] can automate the release of new versions to package registries like NPM <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>. This workflow can be triggered by a `release` event, ensuring a new package is only pushed when an actual release is cut, not for every code change <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.

Workflows can have multiple jobs that run in a specific order using the `needs` keyword <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>. For instance, a "publish" job might `need` a "build" job to complete first, ensuring the code is built once and then pushed to multiple registries (e.g., NPM and [[introduction_to_git_and_github | GitHub]] Package Registry) <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

### Integrating with Third-Party Tools (GitHub Apps vs. Actions)

[[introduction_to_github_actions | GitHub Actions]] can integrate with various communication and project management tools like Slack, Jira, and Trello <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>. The [[introduction_to_git_and_github | GitHub]] Marketplace offers both "Actions" and "Apps" <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>:

*   **Actions** are reusable code pieces that you incorporate into your workflows <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>. For example, a workflow can be set up to trigger on [[introduction_to_git_and_github | GitHub]] issues and use a Slack action to post notifications directly to a Slack channel <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.
*   **Apps** are pre-built solutions that don't require deploying any code <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>. They can be installed on your account with a few clicks and used across multiple repositories simultaneously <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>. [[introduction_to_git_and_github | GitHub]] Apps can perform tasks like code quality analysis, dependency updates, and image optimization automatically <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.

### [[using_github_actions_for_scheduled_tasks | Scheduled Tasks]]

[[introduction_to_github_actions | GitHub Actions]] can also run on a specific schedule, making them ideal for [[using_github_actions_for_scheduled_tasks | scheduled tasks]] <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>. This is achieved using the `on.schedule` event, which accepts a cron schedule syntax <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>. Tools like `crontab.guru` can help generate these schedules <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.

For example, a workflow can be configured to run daily at midnight to export Firestore data into a storage bucket, automating database backups <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>. This uses actions maintained by platforms like Google Cloud Platform to set up necessary CLIs (e.g., Gcloud CLI) and execute commands <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>.