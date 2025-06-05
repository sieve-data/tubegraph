---
title: Installing and managing Nodejs versions
videoId: ENrzD9HAZK4
---

From: [[fireship]] <br/> 

Node.js is considered one of the most valuable skills for a full-stack web developer <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Despite discussions about newer runtimes like Deno, [[introduction_to_nodejs | Node.js]] remains the recommended choice, especially for job seeking or product building, as established technologies are not easily replaced <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. Although Deno has a bright future, skills learned in Node.js are largely transferable <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

## What is Node.js?
Node.js is not a programming language itself, but a runtime environment that enables [[running_and_understanding_javascript_with_nodejs | JavaScript]] to run on a server <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. Initially, [[running_and_understanding_javascript_with_nodejs | JavaScript]] was designed for browser execution in the 1990s <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. The release of [[introduction_to_nodejs | Node.js]] in 2009 revolutionized web development by allowing developers to write [[running_and_understanding_javascript_with_nodejs | JavaScript]] code on the server, facilitating the creation of [[building_and_deploying_a_full_stack_application_with_nodejs_and_express | full-stack applications]] using a single language <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

## Installing Node.js
[[introduction_to_nodejs | Node.js]] can be installed on Windows, Mac, or Linux systems and might already be present <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

To check if [[introduction_to_nodejs | Node.js]] is installed, open your command line and run:
```bash
node -v
```
This command will display the installed version, for example, `12.16` which was the current long-term support (LTS) version at the time of the video <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. If you receive an error, [[introduction_to_nodejs | Node.js]] is not installed <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

### Managing Node.js Versions with NVM
It is highly recommended to use a package called Node Version Manager (NVM) to manage different [[introduction_to_nodejs | Node.js]] installations on your system <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. There is an NVM package for Mac and Linux, and a separate one for Windows <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. Installing NVM allows you to install and switch between any desired [[introduction_to_nodejs | Node.js]] version <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

**Example NVM commands:**
*   To install a specific version:
    ```bash
    nvm install 12.16.3
    ``` <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>
*   To use an installed version as your current runtime:
    ```bash
    nvm use 12.16.3
    ``` <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>

## Deploying Node.js Applications to the Cloud
When deploying [[introduction_to_nodejs | Node.js]] applications, services like Google App Engine offer a standard environment for [[introduction_to_nodejs | Node.js]] up to version 12 (at the time of the video) <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>. This provides a server that automatically scales with incoming traffic <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>.

To deploy, you need a Google Cloud Platform account and the Google Cloud command-line tools installed <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>.
1.  Create an `app.yaml` file in your source code to configure the cloud server. For [[introduction_to_nodejs | Node.js]], specify the runtime, e.g.:
    ```yaml
    runtime: nodejs12
    ``` <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>
2.  Ensure your `package.json` file contains a `start` script, as App Engine looks for this script to run your code:
    ```json
    {
      "scripts": {
        "start": "node ."
      }
    }
    ``` <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a>
3.  Deploy your application from the command line:
    ```bash
    gcloud app deploy
    ``` <a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>
    After deployment, a public URL will be provided to access your application <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>.