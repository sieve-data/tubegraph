---
title: Progressive Web Application PWA features in Angular
videoId: G0bBLvWXBvc
---

From: [[fireship]] <br/> 

Angular is a powerful framework that simplifies the process of building and deploying Progressive Web Applications (PWAs). A PWA is an application that combines the best features of both web and mobile apps, offering an installable, offline-capable, and native-like experience <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## Why Angular for PWAs?

Despite its reputation as an enterprise-grade framework, Angular makes it easy for beginners to be productive and build complex products <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. Angular ships with many features out-of-the-box that anticipate the complexity an app might face as it grows, yet almost all its features are optional and can be adopted as needed <a class="yt-timestamp" data-t="01:10:07">[01:10:07]</a>.

Angular is a declarative UI framework, a code bundler, and a tool specifically designed for building progressive web apps <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. It handles server-side rendering and provides libraries for forms, testing, and animation <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. At its core, Angular helps in building complex cross-platform applications using web technologies like JavaScript, HTML, and CSS <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

> [!NOTE] Angular provides a highly performant package that reduces decision fatigue for web developers by offering a comprehensive solution instead of requiring them to choose from a vast number of open-source libraries <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

## Building and Deploying an Angular PWA

The [[Angular_7_virtual_scroll_feature_in_the_component_development_kit | Angular Command-Line Interface (CLI)]] is a powerful tool that leverages Angular's conventions to generate a lot of code automatically <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

### Initial Setup

1.  **Install Angular CLI**: Ensure Node.js is installed, then run `npm install -g @angular/cli` to get access to the `ng` command <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
2.  **Generate a New Angular App**: Use `ng new <app-name>` <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. The tutorial suggests enabling routing and choosing SCSS for styles <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
3.  **Development Workflow**: Run `ng serve` to bundle code with Webpack and live reload, reflecting changes in the browser at `localhost:4200` <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
4.  **Production Build**: Use `ng build` to automatically minify and bundle code, generating multiple bundles for differential loading, ensuring the smallest possible JavaScript bundle is loaded based on browser features <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. The output is placed in the `dist` folder, ready for deployment <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

### Core Angular Concepts for PWA Development

*   **TypeScript**: Angular encourages the use of TypeScript, which is now almost a standard for large, complex projects <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.
*   **Testing Utilities**: Angular sets up testing utilities out-of-the-box, such as Karma and Jasmine, with extensions available for Jest and Cypress <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
*   **[[using_angular_components_and_component_architecture | Component-based UI Architecture]]**: Angular, like React, Svelte, and Vue, uses a component-based UI architecture where data (properties) can be passed between components <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
    *   **Component Structure**: Each component consists of three main pieces:
        1.  **TypeScript**: Defines custom JavaScript logic and internal state <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
        2.  **HTML Template**: Contains the visual UI and allows data binding from TypeScript <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
        3.  **Stylesheet**: Scoped to the component, preventing styles from affecting other components <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
    *   **[[lifecycle_of_angular_components | Lifecycle Hooks]]**: Components have [[lifecycle_of_angular_components | lifecycle hooks]] like `ngOnInit` for initial setup <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.
*   **Routing**: Angular provides a powerful router for mapping components to URLs, supporting features like code splitting for lazy loading parts of the JavaScript bundle <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
*   **Data Binding and Change Detection**: Angular's templating language allows conditional expressions, loops, and direct data binding to HTML. It uses change detection to efficiently update the UI when component properties change <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.
*   **Third-party Component Libraries**: Angular's ecosystem offers libraries like Angular Material, [[hybrid_app_development_with_ionic_4 | Ionic]], and Nebular, which can be easily added with a single command (e.g., `ng add @nebular/theme`) to incorporate a consistent design system <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>.

### Making an Angular App a PWA

The easiest part of transforming an Angular app into a PWA is adding the PWA functionality <a class="yt-timestamp" data-t="00:18:15">[00:18:15]</a>.

1.  **Add PWA Schematic**: Run `ng add @angular/pwa` using the Angular CLI or console <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>.
2.  **Automatic PWA Configuration**: This command performs several crucial actions:
    *   Adds JavaScript code to load a service worker into the Angular app <a class="yt-timestamp" data-t="00:18:34">[00:18:34]</a>.
    *   Provides a configuration file to customize the service worker's behavior, primarily for offline functionality and caching <a class="yt-timestamp" data-t="00:18:39">[00:18:39]</a>.
    *   Adds a manifest file and icons necessary for the app's install button <a class="yt-timestamp" data-t="00:18:53">[00:18:53]</a>.

### Deploying the PWA

1.  **Build for Production**: First, build the app for production by running `ng build` <a class="yt-timestamp" data-t="00:19:04">[00:19:04]</a>. This compiles TypeScript to JavaScript in the `dist` folder <a class="yt-timestamp" data-t="00:19:09">[00:19:09]</a>.
2.  **Add Firebase Hosting**: Integrate [[deploying_angular_applications_using_firebase | Firebase]] into the project by running `ng add @angular/fire` <a class="yt-timestamp" data-t="00:19:18">[00:19:18]</a>. [[deploying_angular_applications_using_firebase | Firebase]] hosting can be used on the free tier <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>.
3.  **Deploy**: Execute `ng deploy` to automatically deploy the production app to the [[deploying_angular_applications_using_firebase | Firebase]] hosting account <a class="yt-timestamp" data-t="00:19:35">[00:19:35]</a>.

### Verifying and Using the PWA

After deployment, the app can be analyzed in Chrome DevTools' audits tab to determine if it's a valid PWA <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>. Achieving "green check marks" indicates the app is installable on user devices <a class="yt-timestamp" data-t="00:19:53">[00:19:53]</a>. PWAs are widely supported and can be installed on Windows desktops by hitting the install button in Chrome, adding a shortcut, and opening in a dedicated window, behaving like a traditional desktop app <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>. The same installability applies to mobile devices <a class="yt-timestamp" data-t="00:20:16">[00:20:16]</a>.

> [!INFO] **Summary**
> Angular's robust tooling and minimal configuration requirements enable developers to quickly build and deploy meaningful Progressive Web Applications that offer a native-like experience across platforms <a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a>.