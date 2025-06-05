---
title: Deploying and hosting applications with Firebase
videoId: iWEgpdVSZyg
---

From: [[fireship]] <br/> 

Firebase offers versatile tools for deploying and hosting both mobile and web applications, streamlining the development and distribution process.

## General Deployment Principles

To deploy code to a Firebase project, ensure you have the Firebase command-line tools installed globally on your system, as well as the Google Cloud SDK <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. This provides access to the `firebase` and `gcloud` commands locally <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

If you are [[setting_up_and_managing_firebase_projects | building a serious application]], it's recommended to create two separate Firebase projects: one for development and another for production <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. This setup provides a sandbox for testing and experimentation while keeping customer data pristine in the production environment <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

## Mobile Application Distribution

For iOS or Android applications, [[flutter_app_integration_with_firebase | Firebase App Distribution]] can be used to distribute your app to testers <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. This service allows you to bypass platforms like TestFlight and the Google Play Store for easier internal testing <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

## Web Application Hosting with Firebase Hosting

Firebase Hosting is designed for web applications and offers robust features for deployment and management.

### Initial Setup and Deployment

If you are building a web application, you will likely use a package manager like NPM <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. Install `firebase-tools` into your project's development environment <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. This allows you to write NPM scripts that utilize the Firebase CLI tools <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

For projects with separate development and production environments, you can use the `--project` flag in your NPM scripts to specify which Firebase project to deploy to <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>. For example, you can have distinct commands to deploy to your development project and your production project <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

After deployment, your site will be available at a domain like `your-project.web.app` through the Firebase console <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

### Custom Domains and Multi-Site Hosting

You can connect your own [[setting_up_and_managing_firebase_projects | custom domain]] to your Firebase-hosted site <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. Firebase Hosting is not limited to a single domain; it supports multi-site hosting, allowing you to host multiple sites, such as an admin site and a customer-facing site, within the same Firebase project <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

To configure multi-site hosting, modify your `firebase.json` file. Change the `hosting` value to an array and set up different targets representing the different sites you wish to deploy <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

### Advanced Hosting Features

Firebase Hosting supports more than just static files:
*   **Server-Side Rendering (SSR):** You can rewrite traffic to a [[cloud_functions_and_integration_with_firebase | Cloud Function]] or a Cloud Run instance <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. This enables SSR with frameworks like [[deploying_angular_applications_using_firebase | Angular Universal]] or Next.js <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
*   **Dynamic Links:** Set up Firebase Hosting rewrites for dynamic links to send users to the optimal app experience <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. For instance, a link opened on an iPhone can direct the user to a specific screen within the iPhone app <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
*   **Custom Headers:** Specify headers for static files in your hosting configuration, such as changing CORS settings for font files <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
*   **Caching Control:** Firebase Hosting automatically caches static files for performance <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. You can modify this caching behavior by setting different cache headers <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

### Continuous Deployment

To automate your deployment workflow, integrate Firebase Hosting with Google Cloud Build <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. This allows for [[continuous_deployment_using_firebase | continuous deployment]], where every Git commit to your project triggers a new version of your site to be deployed to your hosting account <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.