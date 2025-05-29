---
title: Deploying applications online with Vercel
videoId: sV3pI_xH_Q0
---

From: [[gregisenberg]] <br/> 

[[introduction_to_vercel_and_vzer | Vercel]] is a platform used for deploying web applications online. The process can be significantly streamlined using AI tools like Cursor Agent, which can handle much of the work automatically <a class="yt-timestamp" data-t="00:55:46">[00:55:46]</a>.

## Deployment Process Overview

The general steps for deploying an application to [[introduction_to_vercel_and_vzer | Vercel]] involve:
1.  Creating a GitHub repository for your project <a class="yt-timestamp" data-t="00:55:10">[00:55:10]</a>.
2.  Instructing Cursor Agent to deploy the app to [[introduction_to_vercel_and_vzer | Vercel]] and commit the changes to GitHub <a class="yt-timestamp" data-t="00:56:01">[00:56:01]</a>.
3.  Setting up the project within the [[introduction_to_vercel_and_vzer | Vercel]] platform, often initiated by the Cursor Agent itself <a class="yt-timestamp" data-t="00:57:56">[00:57:56]</a>.
4.  Configuring necessary environment variables (API keys) in [[introduction_to_vercel_and_vzer | Vercel]]'s settings <a class="yt-timestamp" data-t="01:05:12">[01:05:12]</a>.
5.  Authorizing the deployed domain in third-party services (like Firebase) if required <a class="yt-timestamp" data-t="01:09:43">[01:09:43]</a>.

## Step-by-Step Deployment with Cursor Agent

### 1. Preparing the Project
Initially, a project is created from an empty folder using Cursor. This project can be based on a template, such as a Next.js blank canvas <a class="yt-timestamp" data-t="01:10:04">[01:10:04]</a>. The template used in this example has Firebase built in <a class="yt-timestamp" data-t="00:39:33">[00:39:33]</a>.

### 2. GitHub Integration
The application's code needs to be pushed to a GitHub repository. Cursor Agent can assist in this by committing the app to GitHub <a class="yt-timestamp" data-t="00:56:01">[00:56:01]</a>.

### 3. Deploying via Vercel CLI
Cursor Agent can utilize the [[introduction_to_vercel_and_vzer | Vercel]] CLI to deploy the application <a class="yt-timestamp" data-t="00:58:16">[00:58:16]</a>. The process includes:
*   Automatic login to [[introduction_to_vercel_and_vzer | Vercel]] via a success link <a class="yt-timestamp" data-t="00:58:28">[00:58:28]</a>.
*   Prompting to set up and deploy (select "yes") <a class="yt-timestamp" data-t="00:58:45">[00:58:45]</a>.
*   Choosing between a personal or business account <a class="yt-timestamp" data-t="00:58:51">[00:58:51]</a>.
*   Selecting "no" if linking to an existing project if one hasn't been created yet <a class="yt-timestamp" data-t="00:58:56">[00:58:56]</a>.
*   Naming the project (e.g., "Riley Greg pod 4") <a class="yt-timestamp" data-t="00:59:03">[00:59:03]</a>.
*   Confirming the code directory (often by pressing Enter) <a class="yt-timestamp" data-t="00:59:15">[00:59:15]</a>.
*   Not modifying default settings <a class="yt-timestamp" data-t="00:59:21">[00:59:21]</a>.

Once these steps are completed, [[introduction_to_vercel_and_vzer | Vercel]] begins building the deployment, which usually takes about a minute and a half <a class="yt-timestamp" data-t="01:00:04">[01:00:04]</a>.

### 4. Handling Deployment Failures and API Keys
Deployment can sometimes fail, often due to missing API tokens <a class="yt-timestamp" data-t="01:01:04">[01:01:04]</a>. To resolve this:
*   Navigate to your [[introduction_to_vercel_and_vzer | Vercel]] projects <a class="yt-timestamp" data-t="01:03:01">[01:03:01]</a>.
*   Go to the specific project's settings <a class="yt-timestamp" data-t="01:04:56">[01:04:56]</a>.
*   Find "Environment Variables" <a class="yt-timestamp" data-t="01:05:12">[01:05:12]</a>.
*   Add the necessary API tokens (e.g., `REPLICATE_API_TOKEN`) <a class="yt-timestamp" data-t="01:06:55">[01:06:55]</a>.
*   Redeploy the project <a class="yt-timestamp" data-t="01:07:04">[01:07:04]</a>.

### 5. Authorizing Domains for External Services

For applications using services like Google Firebase, the deployed [[introduction_to_vercel_and_vzer | Vercel]] domain (e.g., `rileygregppod.vercel.app`) must be authorized within the external service's settings <a class="yt-timestamp" data-t="01:09:43">[01:09:43]</a>. This ensures that the online application can properly interact with the backend services.

### Conclusion of Deployment
After these steps, the application becomes accessible on the internet <a class="yt-timestamp" data-t="01:08:47">[01:08:47]</a>. The described process allows for the creation of a full-stack application within approximately an hour and 15 minutes <a class="yt-timestamp" data-t="01:11:51">[01:11:51]</a>.