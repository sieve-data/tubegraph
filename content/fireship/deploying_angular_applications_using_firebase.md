---
title: Deploying Angular applications using Firebase
videoId: G0bBLvWXBvc
---

From: [[fireship]] <br/> 

[[Deploying and hosting applications with Firebase | Deploying and hosting]] Angular applications, especially as Progressive Web Apps (PWAs), can be streamlined using tools like [[Firebase|Firebase]] for hosting <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. This process involves building the application for production and then leveraging a hosting service to make it accessible online <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>.

## Preparing for Deployment

Before deploying an Angular application, it needs to be built for a production environment <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>. This step compiles the TypeScript code into JavaScript, which is then placed in a `dist` folder <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>. This `dist` folder contains the minified and bundled code ready for a production hosting account or server <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>.

The Angular CLI makes this process straightforward:
1.  **Build the application:** Run `ng build` to compile the application's TypeScript code into JavaScript <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>. This command also handles minification and generates multiple bundles for differential loading, ensuring the smallest possible JavaScript bundle is loaded based on the browser's features <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

## Integrating Firebase for Hosting

[[Firebase]] is a popular choice for hosting Angular applications, partly because its hosting services are available on the free tier <a class="yt-timestamp" data-t="00:19:30">[00:19:30]</a>.

To add [[Firebase]] to an Angular project:
1.  **Install AngularFire:** Use the `ng add` command with `@angular/fire` <a class="yt-timestamp" data-t="00:19:22">[00:19:22]</a>.
    ```bash
    ng add @angular/fire
    ```
2.  **Connect to a Firebase project:** The command will prompt you to select or connect to an existing [[Setting up and managing Firebase projects | Firebase project]] <a class="yt-timestamp" data-t="00:19:24">[00:19:24]</a>. A [[Firebase account|Firebase account]] is required <a class="yt-timestamp" data-t="00:19:29">[00:19:29]</a>.

## Deploying the Application

Once [[Firebase]] is integrated, [[Continuous Deployment using Firebase | deploying]] the application is simplified:
1.  **Run `ng deploy`**: This command automatically [[Continuous Deployment using Firebase | deploys]] the production-ready Angular app to the [[Firebase hosting|Firebase hosting]] account <a class="yt-timestamp" data-t="00:19:37">[00:19:37]</a>.
    ```bash
    ng deploy
    ```
2.  **Access the application**: Upon successful deployment, [[Firebase]] provides the hosting URL, allowing access to the application on the web <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>.

## Progressive Web App (PWA) Capabilities

Angular makes it easy to convert an application into a Progressive Web App (PWA), which enhances its functionality and installability <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>.

To add PWA features:
1.  **Install PWA schematic:** Use `ng add` with `@angular/pwa` <a class="yt-timestamp" data-t="00:18:26">[00:18:26]</a>.
    ```bash
    ng add @angular/pwa
    ```
This command adds:
*   JavaScript code to load a service worker, which primarily enables the app to work offline and allows customization of how pages are cached <a class="yt-timestamp" data-t="00:18:36">[00:18:36]</a>.
*   A configuration file for the service worker <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>.
*   A manifest file and icons for the app's install button <a class="yt-timestamp" data-t="00:18:53">[00:18:53]</a>.

### Benefits of PWA Deployment
When deployed, a PWA-enabled Angular app provides several advantages:
*   **Installability**: The app becomes installable on various devices, including desktop (e.g., Windows) and mobile, appearing and behaving like a native application <a class="yt-timestamp" data-t="00:19:57">[00:19:57]</a>.
*   **Offline Support**: Service workers enable the app to function even without an internet connection <a class="yt-timestamp" data-t="00:18:45">[00:18:45]</a>.
*   **Performance**: PWAs often offer faster load times and smoother interactions due to caching and optimized delivery.
*   **Discoverability**: They are accessible via URLs and can be found through search engines, similar to traditional websites.

Developers can verify PWA compliance by checking the audits tab in browser developer tools (e.g., Chrome DevTools) for confirmation of a valid PWA <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>.