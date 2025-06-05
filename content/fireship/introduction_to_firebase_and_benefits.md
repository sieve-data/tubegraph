---
title: Introduction to Firebase and benefits
videoId: 9kRgVxULbag
---

From: [[fireship]] <br/> 

Firebase is a platform designed to simplify backend development by completely abstracting it away, allowing developers to focus on building applications with ease <a class="yt-timestamp" data-t="00:39:00">[00:39:00]</a>. It's considered an excellent platform for building apps <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>, supporting development primarily with JavaScript <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>, and doesn't require prior coding experience to follow along with basic usage <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>.

## Core Benefits of Firebase

The speaker uses Firebase for clients for three main reasons:
*   **Developer Experience** Firebase is well-documented, easy to use, and its team is responsive to developer feedback <a class="yt-timestamp" data-t="00:50:00">[00:50:00]</a>.
*   **Minimization of Cost** Firebase offers a free tier for small, experimental projects and scales linearly with user growth and design choices, avoiding sudden, high charges after reaching certain thresholds <a class="yt-timestamp" data-t="00:58:00">[00:58:00]</a>.
*   **Maximization of Time** Firebase facilitates creating the most value in the least amount of time <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a>.

## Getting Started with Firebase

To begin, users need an editor like VS Code and Node.js installed locally <a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a>. Users can then go to Firebase and [[setting_up_and_managing_firebase_projects | create a new project]] <a class="yt-timestamp" data-t="01:32:00">[01:32:00]</a>. A project serves as a container for Google Cloud Platform resources such as databases, file storage, and web hosting <a class="yt-timestamp" data-t="01:34:00">[01:34:00]</a>. All app resources can be managed from the Firebase admin console <a class="yt-timestamp" data-t="01:44:00">[01:44:00]</a>. Projects can span multiple platforms, as Firebase provides SDKs for web, iOS, Android, Unity, and more <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a>. Project credentials integrate seamlessly with other Google Cloud Platform APIs like Cloud Vision or Google Maps <a class="yt-timestamp" data-t="02:01:00">[02:01:00]</a>.

After project creation, the Firebase command-line tools can be installed globally using `npm install firebase-tools -g` <a class="yt-timestamp" data-t="02:11:00">[02:11:00]</a>.

## Key Development Resources

Firebase offers several core development resources for building applications:

### Hosting
Firebase allows for quick and easy [[deploying_and_hosting_applications_with_firebase | deployment and hosting of projects]] from the command line <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>. Running `firebase init hosting` creates necessary files like `firebase.json` for hosting rules, `.firebaserc` for project identification, and a `public` folder with `index.html` for the app <a class="yt-timestamp" data-t="02:31:00">[02:31:00]</a>.
The Firebase web SDK can be imported module by module, which helps with page load performance <a class="yt-timestamp" data-t="02:52:00">[02:52:00]</a>. Scripts are deferred until the page finishes loading <a class="yt-timestamp" data-t="03:03:00">[03:03:00]</a>.
To test locally, `firebase serve` spins up a web server <a class="yt-timestamp" data-t="03:24:00">[03:24:00]</a>. To deploy, `firebase deploy` makes the app accessible on a live hosted URL with an SSL certificate for HTTPS support and leverages Google's content delivery network (CDN) for highly performant static resource serving <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>.

### Authentication
Firebase simplifies user authentication, turning complex authorization tasks into a few lines of code <a class="yt-timestamp" data-t="04:42:00">[04:42:00]</a>. It supports various OAuth providers like Google, Twitter, Facebook, and GitHub, as well as email/password and anonymous authentication <a class="yt-timestamp" data-t="05:33:00">[05:33:00]</a>. Authentication uses JSON Web Tokens (JWTs) for browser-based session management, which are easier to work with than cookies for JavaScript applications <a class="yt-timestamp" data-t="06:38:00">[06:38:00]</a>. The Firebase console allows managing user accounts, disabling accounts, updating email templates, and performing text message verification <a class="yt-timestamp" data-t="07:08:00">[07:08:00]</a>.

### Databases
Firebase offers two NoSQL database options:
*   **Realtime Database** <a class="yt-timestamp" data-t="07:33:00">[07:33:00]</a>: Suited for simple data sets that are read frequently <a class="yt-timestamp" data-t="08:03:00">[08:03:00]</a>. It charges $5 per gigabyte stored and $1 per gigabyte downloaded <a class="yt-timestamp" data-t="07:47:00">[07:47:00]</a>.
*   **Cloud Firestore** <a class="yt-timestamp" data-t="07:36:00">[07:36:00]</a>: Generally preferred for larger, more complex relational data sets <a class="yt-timestamp" data-t="08:09:00">[08:09:00]</a>. It charges 18 cents per gigabyte stored, plus charges for individual document read and write operations <a class="yt-timestamp" data-t="07:54:00">[07:54:00]</a>.

Firestore structures data as collections of documents, similar to MongoDB <a class="yt-timestamp" data-t="08:26:00">[08:26:00]</a>. Documents have unique IDs (either custom or auto-generated) and fields that hold data <a class="yt-timestamp" data-t="08:46:00">[08:46:00]</a>. For more advanced [[using_firebase_databases_and_data_modeling_techniques | data modeling techniques]], users can refer to external resources <a class="yt-timestamp" data-t="08:37:00">[08:37:00]</a>.

A major advantage of Firebase is the direct integration of its user authentication system with the database <a class="yt-timestamp" data-t="09:22:00">[09:22:00]</a>. Security rules can be written to define backend security logic, controlling data access for logged-in users <a class="yt-timestamp" data-t="09:29:00">[09:29:00]</a>. Firestore also builds indices by default for every field, and custom indices can be created for multi-field queries <a class="yt-timestamp" data-t="09:49:00">[09:49:00]</a>.

Firestore supports real-time listening to data changes <a class="yt-timestamp" data-t="11:03:00">[11:03:00]</a>. If data is shared among multiple users and changes, all users are notified instantly, a feature extremely difficult to build from scratch <a class="yt-timestamp" data-t="11:09:00">[11:09:00]</a>. When updating data, Firestore performs optimistic updates (latency compensation), immediately updating the view without waiting for server response, which improves user experience <a class="yt-timestamp" data-t="12:37:00">[12:37:00]</a>. Queries can be made on collections using `where` clauses for specific conditions, `orderBy` for sorting, and `limit` to cap the number of returned documents <a class="yt-timestamp" data-t="13:08:00">[13:08:00]</a>.

### Storage
Firebase Storage provides a cloud storage bucket integrated with the Firebase project, suitable for user-generated content like uploaded images and videos <a class="yt-timestamp" data-t="14:52:00">[14:52:00]</a>. Storage rules can be configured to control who can upload files <a class="yt-timestamp" data-t="15:07:00">[15:07:00]</a>. Files can be uploaded and existing file URLs can be downloaded programmatically <a class="yt-timestamp" data-t="15:59:00">[15:59:00]</a>.

### Cloud Functions
[[cloud_functions_and_integration_with_firebase | Firebase Cloud Functions]] allow developers to run backend code on demand using Node.js, forming microservices that perform specific tasks <a class="yt-timestamp" data-t="16:51:00">[16:51:00]</a>. Anything that can be done in Node.js, including installing NPM packages, can be done in a function <a class="yt-timestamp" data-t="17:19:00">[17:19:00]</a>. Functions can be initialized in a project by running `firebase init functions` <a class="yt-timestamp" data-t="17:31:00">[17:31:00]</a>.

Functions can be triggered in various ways, including database triggers (e.g., a new document creation in Firestore) <a class="yt-timestamp" data-t="17:41:00">[17:41:00]</a>. This allows for sharing information between backend code and the database <a class="yt-timestamp" data-t="18:02:00">[18:02:00]</a>. The Firebase Admin SDK, usable only in a backend environment like a Cloud Function, can bypass security rules defined in the Firebase app <a class="yt-timestamp" data-t="18:20:00">[18:20:00]</a>. After defining a function, it can be deployed to Firebase using `firebase deploy functions` <a class="yt-timestamp" data-t="19:40:00">[19:40:00]</a>.

## Mobile App Specific Features

Beyond core development resources, Firebase offers additional features particularly beneficial for native mobile applications:

*   **Testing and Stability** Firebase includes a Robo testing tool where app builds can be uploaded, and it runs a suite of tests to identify common issues that cause mobile apps to crash, providing screenshot results of each test <a class="yt-timestamp" data-t="20:21:00">[20:21:00]</a>.
*   **Analytics** Various analytic tools are available, including Stream View, which provides a real-time global geographic representation of the entire user base <a class="yt-timestamp" data-t="20:40:00">[20:40:00]</a>.
*   **Push Notifications** Firebase simplifies sending push notifications based on user segments, specific topics, or to single devices <a class="yt-timestamp" data-t="20:55:00">[20:55:00]</a>. It also supports A/B testing for notifications and tracking conversion rates <a class="yt-timestamp" data-t="21:06:00">[21:06:00]</a>.