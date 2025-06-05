---
title: Introduction to Angular CommandLine Interface CLI
videoId: G0bBLvWXBvc
---

From: [[fireship]] <br/> 

The Angular Command Line Interface (CLI) is a powerful "superpower" for developers, distinguishing itself from typical CLIs <a class="yt-timestamp" data-t="01:49:10">[01:49:10]</a> <a class="yt-timestamp" data-t="01:53:11">[01:53:11]</a>. Its strength lies in Angular's conventions, enabling automatic code generation and reducing "decision fatigue" for web developers faced with numerous open-source libraries <a class="yt-timestamp" data-t="01:55:09">[01:55:09]</a> <a class="yt-timestamp" data-t="00:51:04">[00:51:04]</a> <a class="yt-timestamp" data-t="00:53:03">[00:53:03]</a>. It provides many features out of the box, anticipating complexity as an application grows, yet almost all features are optional and can be adopted as needed <a class="yt-timestamp" data-t="01:10:04">[01:10:04]</a> <a class="yt-timestamp" data-t="01:16:04">[01:16:04]</a>.

The Angular CLI helps developers quickly build complex, cross-platform applications using web technologies like JavaScript, HTML, and CSS <a class="yt-timestamp" data-t="01:21:05">[01:21:05]</a> <a class="yt-timestamp" data-t="01:25:06">[01:25:06]</a>.

## Installation and Initial Setup

To install the Angular CLI, you need Node.js installed on your system <a class="yt-timestamp" data-t="01:59:08">[01:59:08]</a>. Once Node.js is ready, run the following npm command globally:

`npm install -g @angular/cli` <a class="yt-timestamp" data-t="02:03:00">[02:03:00]</a>

This command provides access to the `ng` command in your terminal <a class="yt-timestamp" data-t="02:07:07">[02:07:07]</a>.

## Core Commands and Functionality

### `ng new` - Generating a New Application

The first step is to generate a new Angular application using `ng new` followed by the app's name <a class="yt-timestamp" data-t="02:10:04">[02:10:04]</a> <a class="yt-timestamp" data-t="02:12:06">[02:12:06]</a>. The CLI will prompt you for configuration options, such as adding routing and choosing a stylesheet format (e.g., SCSS) <a class="yt-timestamp" data-t="02:17:01">[02:17:01]</a> <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>.

### `ng serve` - Serving the Application

The `serve` command bundles code with Webpack and uses live reload, allowing changes to be reflected immediately in the browser on `localhost:4200` <a class="yt-timestamp" data-t="02:41:04">[02:41:04]</a> <a class="yt-timestamp" data-t="02:45:00">[02:45:00]</a> <a class="yt-timestamp" data-t="02:51:08">[02:51:08]</a>.

### `ng build` - Building for Production

The `build` command automatically minifies and bundles your code <a class="yt-timestamp" data-t="03:13:08">[03:13:08]</a> <a class="yt-timestamp" data-t="03:17:03">[03:17:03]</a>. It also generates multiple bundles for differential loading, ensuring the browser loads the smallest possible JavaScript bundle based on its features <a class="yt-timestamp" data-t="03:20:03">[03:20:03]</a> <a class="yt-timestamp" data-t="03:21:05">[03:21:05]</a>. The resulting raw JavaScript code is placed in the `dist` folder, which is ready for deployment to a production hosting account or server <a class="yt-timestamp" data-t="03:29:00">[03:29:00]</a> <a class="yt-timestamp" data-t="03:31:07">[03:31:07]</a> <a class="yt-timestamp" data-t="03:33:04">[03:33:04]</a>.

### `ng generate` - Generating Components and Other Schematics

The `generate` command is crucial for creating various parts of an Angular application, such as [[basics_of_angular_components|components]] <a class="yt-timestamp" data-t="06:14:00">[06:14:00]</a> <a class="yt-timestamp" data-t="06:16:00">[06:16:00]</a>. When generating a component, you can choose options like `inline template` and `inline styles` to keep the component's HTML and CSS within its TypeScript file if separation isn't needed <a class="yt-timestamp" data-t="06:27:07">[06:27:07]</a> <a class="yt-timestamp" data-t="06:31:01">[06:31:01]</a>.

### `ng add` - Adding Functionality and Libraries

The `ng add` command allows you to easily add third-party libraries and functionality to your project. This command automatically installs and configures the added package within your Angular application <a class="yt-timestamp" data-t="01:50:09">[01:50:09]</a>.

Examples:
*   `ng add @angular/pwa`: Adds progressive web app capabilities, including JavaScript for service workers, a configuration file for service worker behavior, a manifest file, and icons for the install button <a class="yt-timestamp" data-t="01:26:00">[01:26:00]</a> <a class="yt-timestamp" data-t="01:28:00">[01:28:00]</a> <a class="yt-timestamp" data-t="01:30:00">[01:30:00]</a> <a class="yt-timestamp" data-t="01:33:00">[01:33:00]</a> <a class="yt-timestamp" data-t="01:34:00">[01:34:00]</a>.
*   `ng add @nebular/theme`: Installs and configures the Nebular UI theme, often with options for theme choice, customization, and animation <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a> <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>.
*   `ng add @angular/fire`: Integrates Firebase into an Angular project, prompting for a Firebase project ID <a class="yt-timestamp" data-t="01:42:00">[01:42:00]</a> <a class="yt-timestamp" data-t="01:44:00">[01:44:00]</a>.

### `ng deploy` - Deploying Applications

The `ng deploy` command automatically deploys your production application, for example, to a Firebase hosting account, providing the hosting URL upon completion <a class="yt-timestamp" data-t="01:46:00">[01:46:00]</a> <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a>.

## Tooling and Support

The Angular CLI works hand-in-hand with tools like the Angular Language Service for syntax highlighting in HTML templates <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a> <a class="yt-timestamp" data-t="02:28:00">[02:28:00]</a>. Additionally, the Angular Console provides a graphical interface to point and click on CLI commands, removing the need for manual typing <a class="yt-timestamp" data-t="02:33:04">[02:33:04]</a> <a class="yt-timestamp" data-t="02:37:09">[02:37:09]</a>.

The CLI also automatically sets up testing utilities (e.g., Karma and Jasmine), reducing the need for manual configuration <a class="yt-timestamp" data-t="04:11:04">[04:11:04]</a> <a class="yt-timestamp" data-t="04:15:00">[04:15:00]</a>. It supports other [[setting_up_angular_testing_environment|testing frameworks]] like Jest and Cypress via schematics or extensions <a class="yt-timestamp" data-t="04:01:06">[04:01:06]</a> <a class="yt-timestamp" data-t="04:07:00">[04:07:00]</a>.