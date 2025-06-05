---
title: Enhancing applications with Firebase extensions and integrations
videoId: iWEgpdVSZyg
---

From: [[fireship]] <br/> 

Firebase provides various extensions and robust integration capabilities to enhance applications, streamline development, and add advanced features. These features allow developers to leverage existing services and technologies alongside their Firebase projects.

## Firebase Extensions

Firebase extensions are pre-packaged solutions designed to automate common tasks or integrate with third-party services.

*   **Distributed Counter**
    For scenarios with high write throughput on a single document, such as frequently updated counters, a distributed counter can be set up using a Firebase extension <a class="yt-timestamp" data-t="13:17:00">[13:17:00]</a>. This addresses the limitation of one write per document per second in Firestore <a class="yt-timestamp" data-t="13:09:00">[13:09:00]</a>.
*   **Image Resizer**
    If users can upload image files, the Firebase image resizer extension allows for easy resizing of images to different resolutions suitable for various devices <a class="yt-timestamp" data-t="17:11:00">[17:11:00]</a>.

## Firebase Integrations with Google Services

Firebase projects are built on top of the Google Cloud Platform (GCP) <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>, allowing seamless integration with other Google services.

*   [[setting_up_and_managing_firebase_projects | Google Analytics]]
    [[setting_up_and_managing_firebase_projects | Firebase]] can automatically set up [[setting_up_and_managing_firebase_projects | Google Analytics]] for iOS, Android, and web applications, providing insights into user behavior <a class="yt-timestamp" data-t="00:47:00">[00:47:00]</a>, <a class="yt-timestamp" data-t="00:49:00">[00:49:00]</a>, <a class="yt-timestamp" data-t="06:29:00">[06:29:00]</a>. To maximize its utility, tracking custom events and user properties is recommended <a class="yt-timestamp" data-t="22:49:00">[22:49:00]</a>. [[setting_up_and_managing_firebase_projects | Firebase Analytics]] allows for the creation of custom audiences for targeted messaging, A/B testing, and funnels <a class="yt-timestamp" data-t="23:04:00">[23:04:00]</a>. Developers can also use audience data to customize UI elements based on user location or audience membership <a class="yt-timestamp" data-t="23:18:00">[23:18:00]</a>.
*   **Google Cloud Build**
    [[deploying_and_hosting_applications_with_firebase | Firebase Hosting]] can be extended by setting it up with Google Cloud Build, enabling automatic deployment of new site versions with every Git commit to a project <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>.
*   **Google Cloud Storage**
    A dedicated Cloud Storage bucket can be used for regular database backups <a class="yt-timestamp" data-t="04:32:00">[04:32:00]</a>. For cost savings, this backup bucket can be set to "cold line" storage <a class="yt-timestamp" data-t="15:53:00">[15:53:00]</a>.
*   **BigQuery**
    For advanced analytics and machine learning, all [[setting_up_and_managing_firebase_projects | Firebase Analytics]] and [[working_with_firebase_firestore_and_realtime_updates | Firestore]] data can be exported to BigQuery. This raw data can then be used to train custom TensorFlow models <a class="yt-timestamp" data-t="24:03:00">[24:03:00]</a>.
*   **Cloud Functions**
    [[cloud_functions_and_integration_with_firebase | Cloud Functions]] can communicate with other [[cloud_functions_and_integration_with_firebase | Cloud Functions]] or other GCP services using Pub/Sub functions for secure internal messaging, as an alternative to HTTP functions that require authentication validation <a class="yt-timestamp" data-t="20:39:00">[20:39:00]</a>. [[cloud_functions_and_integration_with_firebase | Callable functions]] simplify authentication by including the user's auth context <a class="yt-timestamp" data-t="21:12:00">[21:12:00]</a>.

## Third-Party Integrations

Firebase supports integration with various third-party services to add specific functionalities.

*   **MySQL**
    For use cases requiring a full relational database, MySQL can be integrated into a [[setting_up_and_managing_firebase_projects | Firebase]] project <a class="yt-timestamp" data-t="13:47:00">[13:47:00]</a>.
*   **Algolia**
    For full-text search capabilities, Algolia can be integrated into a [[setting_up_and_managing_firebase_projects | Firebase]] project <a class="yt-timestamp" data-t="13:52:00">[13:52:00]</a>.

## Framework and Library Integrations

Firebase provides specific libraries and recommendations for integration with popular front-end frameworks and development environments.

*   **Angular**
    [[deploying_angular_applications_using_firebase | Angular]] applications should use AngularFire, which integrates with Angular's change detection and router <a class="yt-timestamp" data-t="05:40:00">[05:40:00]</a>. [[deploying_and_hosting_applications_with_firebase | Firebase Hosting]] can also rewrite traffic to a [[cloud_functions_and_integration_with_firebase | Cloud Function]] or Cloud Run instance for server-side rendering (SSR) with frameworks like Angular Universal <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>.
*   **React**
    The ReactFire library, recently uncated, provides support for hooks and suspense when using React on the front-end <a class="yt-timestamp" data-t="05:45:00">[05:45:00]</a>.
*   **RxJS**
    RxFire integrates with RxJS, which works well with frameworks like Svelte <a class="yt-timestamp" data-t="05:50:00">[05:50:00]</a>.
*   **Next.js**
    [[deploying_and_hosting_applications_with_firebase | Firebase Hosting]] supports SSR for frameworks like Next.js by rewriting traffic to a [[cloud_functions_and_integration_with_firebase | Cloud Function]] or Cloud Run instance <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>.
*   **Flutter & Arduino**
    [[flutter_app_integration_with_firebase | Firebase]] Extended provides support for various other frameworks outside of the web, including [[flutter_app_integration_with_firebase | Flutter]] and Arduino <a class="yt-timestamp" data-t="05:56:00">[05:56:00]</a>.

## Other Enhancements

*   **Performance Monitoring**
    With a single line of code, performance monitoring can be implemented to gather metrics like first contentful paint across devices, providing insights into application performance in the wild <a class="yt-timestamp" data-t="06:06:00">[06:06:00]</a>.
*   **Crashlytics**
    For native mobile apps, Crashlytics offers easy setup for error and crash reporting, automatically opening issues for problems in the application <a class="yt-timestamp" data-t="06:17:00">[06:17:00]</a>.
*   **Machine Learning (ML)**
    [[setting_up_and_managing_firebase_projects | Firebase]] allows for leveraging machine learning within applications in multiple ways <a class="yt-timestamp" data-t="23:46:00">[23:46:00]</a>:
    *   **Predictions**: Guessing user behavior, such as purchase intent <a class="yt-timestamp" data-t="23:49:00">[23:49:00]</a>.
    *   **ML Kit**: Implementing AI-driven features like object detection and smart reply out-of-the-box <a class="yt-timestamp" data-t="23:53:00">[23:53:00]</a>.
    *   **AutoML**: Building custom image classification models <a class="yt-timestamp" data-t="24:00:00">[24:00:00]</a>.
    *   **TensorFlow**: Exporting [[setting_up_and_managing_firebase_projects | Firebase Analytics]] and [[working_with_firebase_firestore_and_realtime_updates | Firestore]] data to BigQuery for training custom TensorFlow models from scratch <a class="yt-timestamp" data-t="24:03:00">[24:03:00]</a>.