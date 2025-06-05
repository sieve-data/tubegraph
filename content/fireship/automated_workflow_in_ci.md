---
title: Automated workflow in CI
videoId: scEDHsr3APg
---

From: [[fireship]] <br/> 

An automated workflow is a core component of [[continuous_integration | continuous integration]] (CI) within [[devops_practices | DevOps]] practices, designed to automate the process of building, testing, and releasing code <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## What is an Automated Workflow?

In a [[continuous_integration | CI]] environment, an automated workflow is a sequence of predefined steps that are automatically executed upon specific triggers <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. This process aims to integrate changes and detect issues early, preventing "merge hell" – situations where incompatible code changes lead to build failures and significant time and cost spent resolving conflicts <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## Triggers and Execution

An automated workflow is typically triggered by a developer committing code to a shared repository, often on a daily basis <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. This commit initiates the workflow on a CI server, which can then notify developers of any integration issues <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

For instance, using a CI service like GitHub Actions, a workflow can be configured to run on every push to a specific branch, such as the master branch <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. This event triggers a job that runs on a cloud-based Linux container <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

## Workflow Steps Example

A common automated workflow for a Node.js [[web_application_tools_for_developers | web app]] might involve the following sequence of commands:
1.  **Checkout Code**: The workflow first retrieves the code from the GitHub repository <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
2.  **Setup Environment**: It then sets up the necessary environment, such as Node.js <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
3.  **Install Dependencies**: All required project dependencies are installed <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
4.  **Run Tests**: Automated tests are executed to ensure functionality <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
5.  **Build Application**: The application is built <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
6.  **Deploy Application**: The built application is deployed <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

If any of these steps fail, the workflow stops, preventing the deployment of faulty software to customers and immediately alerting developers to the issue <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## Advantages

The use of automated workflows in CI provides significant [[benefits_of_ci_cd | benefits of CI/CD]]:
*   **Automation**: It automates tasks that would otherwise require manual effort from developers, increasing development velocity <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
*   **Early Problem Detection**: Automated workflows help detect small problems early in the development cycle before they escalate into major issues <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. This leads to higher code quality <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.