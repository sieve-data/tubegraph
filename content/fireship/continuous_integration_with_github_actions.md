---
title: Continuous Integration with GitHub Actions
videoId: eB0nUzAI7M8
---

From: [[fireship]] <br/> 

Automating manual or repetitive tasks can significantly boost productivity in software projects <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. [[introduction_to_github_actions | GitHub Actions]] offers a straightforward way to implement such automation, improving code quality and streamlining development through DevOps practices <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## What are [[introduction_to_github_actions | GitHub Actions]]?

[[introduction_to_github_actions | GitHub Actions]] allows you to automate workflows based on events happening in a [[introduction_to_git_and_github | GitHub repository]] <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. Events can include starring a repo, sending a pull request, or merging code into a branch <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. Any event can trigger an automated workflow, which spins up one or more cloud containers to execute a series of defined steps or instructions <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. [[introduction_to_github_actions | GitHub]] logs the progress of each step, clearly indicating any failures <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

Instead of writing steps from scratch, you can utilize community-implemented "actions," which are reusable chunks of code <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. Hundreds of these reusable actions are available, each being its own [[introduction_to_git_and_github | Git]] repo that can be forked and customized <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

## Understanding Continuous Integration (CI)

[[automating_with_github_actions | Continuous Integration]] (CI) involves developers regularly submitting their code to the main codebase in small, maintainable chunks, often daily <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. These changes are then automatically tested against the main codebase <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. The goal is to ensure that new code integrates seamlessly and doesn't introduce regressions.

### Setting up a CI Workflow

To get started, you primarily need a [[introduction_to_git_and_github | GitHub repository]] <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. The [[introduction_to_git_and_github | GitHub]] service provides a generous free tier <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

1.  **Repository Setup**:
    *   The example project uses `just` for automated tests and `webpack` to build the application <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
    *   The application is a simple website that tells the day of the week, with JavaScript logic in `app.js` and tests in `app.test.js` <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
    *   You can clone the example repo or use your own project, as these principles apply to any [[introduction_to_git_and_github | GitHub repo]] <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

2.  **Accessing the Actions Tab**:
    *   On your [[introduction_to_git_and_github | GitHub]] code page, the "Actions" tab monitors your workflows <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. When a workflow is triggered, it provides a log of server activities <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
    *   For CI, the test suite should run whenever there's a pull request to the master branch <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. A red checkmark indicates test or build failure, preventing merge, while a green checkmark signals success <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

3.  **Workflow Configuration (YAML File)**:
    *   Create a `.github/workflows` directory in your repo <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. Any YAML file in this directory will be automatically picked up by [[introduction_to_github_actions | GitHub]] as a workflow <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
    *   Example: `integrate.yml`
        ```yaml
        name: Node Continuous Integration # Workflow name
        on:
          pull_request: # Trigger on pull requests
            branches:
              - master # To the master branch
        jobs:
          test_pull_request: # Job name
            runs-on: ubuntu-latest # VM to run on (Ubuntu, Windows, Mac OS available)
            steps:
              - uses: actions/checkout@v2 # Action to get source code into VM
              - uses: actions/setup-node@v2 # Action to set up Node.js
                with:
                  node-version: '14' # Specify Node.js version
              - name: Install Dependencies # Step name
                run: npm ci # Clean install dependencies
              - name: Run Tests
                run: npm test # Execute tests
              - name: Build Code
                run: npm run build # Build the application
        ```
    *   The `actions/checkout` action brings your source code into the current working directory of the virtual machine <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.
    *   The `actions/setup-node` action sets up Node.js, allowing you to run Node-based commands <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
    *   `npm ci` performs a clean install of dependencies, suitable for CI servers <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
    *   For complex test suites (e.g., end-to-end tests with Cypress), existing actions often simplify runner setup <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.

### Triggering and Monitoring CI

1.  **Commit and Push**: Commit the workflow file to your master branch and push it to the remote repository <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
2.  **Create a Pull Request**: To trigger the workflow, create a new branch, make changes, commit them, and push the branch to the remote repo <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. Then, create a pull request on [[introduction_to_git_and_github | GitHub]] <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.
3.  **Monitor Status**: [[introduction_to_github_actions | GitHub]] will indicate that checks are running <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. The "Actions" tab will show real-time logging of the process <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.
4.  **Resolve Failures**: If tests fail (red checkmark), developers can examine the logs to identify issues <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. For open pull requests, pushing new commits to the branch will automatically rerun the workflow <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>. Once tests pass (green checkmark), the code is ready for merging <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.

Once [[automating_with_github_actions | Continuous Integration]] ensures code quality, the next phase is typically [[continuous_deployment_using_firebase | Continuous Deployment]] <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.