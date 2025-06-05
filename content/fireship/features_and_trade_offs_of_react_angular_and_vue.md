---
title: Features and trade offs of React Angular and Vue
videoId: cuHDQhDhvPE
---

From: [[fireship]] <br/> 

Choosing a [[comparison_of_javascript_frameworks | JavaScript framework]] for frontend development can be a very difficult decision, whether you are a new developer or have 20 years of experience <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. There is no single "best" framework, and the optimal choice often depends on what makes you and your team happy <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. While some argue that a [[javascript framework | JavaScript framework]] isn't needed at all for web development, attempting to build a non-trivial application with vanilla JavaScript can lead to significant challenges, as it essentially forces developers to build their own custom framework to handle complex tasks <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

[[Frontend UI Libraries and Frameworks | Frontend UI Libraries and Frameworks]] provide solutions for key web development concepts like state management, data binding, events, and the application lifecycle <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. Unlike vanilla JavaScript, frameworks automatically bind HTML to JavaScript, making it easier to keep application data in sync with the user interface <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

## [[reactjs_overview_and_history | React]]

[[reactjs_overview_and_history | React]] is widely considered the most popular [[javascript framework | JavaScript framework]], although some refer to it as a library <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. It becomes the main driver of a project, requiring developers to adopt "the [[reactjs_overview_and_history | React]] way" <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.

### Features
*   **Origin**: Created by smart people at Facebook to build complex UIs like the Facebook UI <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.
*   **Design Philosophy**: Minimal by design, it relies on the open-source community for concerns like routing, animation, and state management <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
*   **Opinionatedness**: Not opinionated about how code is organized <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
*   **[[popularity_and_impact_of_reactjs_in_web_development | Popularity and Impact]]**: The most popular framework with over 10 million weekly downloads on npm and over 170,000 GitHub stars <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>. Its popularity makes it a valuable skill for employment and collaboration <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
*   **Tooling**: Has an official CLI called Create [[applications_of_react_including_react_native | React]] App <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>. Many developers also use tools like Next.js or Gatsby <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. It uses Webpack under the hood to bundle code <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
*   **Architecture**: Applications are organized as a tree of components that encapsulate parts of the UI and communicate with each other <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. This enables a declarative approach where the UI outcome is consistent for a given data set <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.
*   **Syntax**: Uses JSX, which looks like HTML but allows embedding JavaScript <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
*   **State Management**: Reactive state is defined with the `useState` hook <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.
*   **Event Handling**: Events can be bound directly to forms (e.g., `onSubmit`) <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>. HTML elements are descriptive, showing data and event bindings <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.
*   **Lifecycle Hooks**: The `useEffect` hook handles component lifecycle events, such as initial data loading <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.

### Trade-offs
*   **Decision Making**: Because it's not opinionated, developers must make many decisions about which libraries to use and how to ensure maintainability and scalability <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
*   **[[the_challenges_and_complexity_of_using_reactjs | Complexity of Hooks]]**: The `useEffect` hook can be confusing for new users, especially when needing to run it only once during initialization <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

## Angular

Angular, developed and maintained by Google, is seen as [[react_vs_angular_and_vue | React's]] "arch nemesis" <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.

### Features
*   **Developer**: Developed and maintained by Google <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
*   **Opinionatedness**: Very opinionated about how to organize and structure a project, leading to predictable conventions <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.
*   **[[comparison_of_web_development_frameworks | Ecosystem]]**: Comes with officially supported libraries for routing, animation, and server-side rendering <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
*   **[[popularity_and_impact_of_reactjs_in_web_development | Popularity]]**: Has 75,000 GitHub stars and is the second most downloaded framework on npm <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
*   **Tooling**: Features the most powerful CLI among frameworks <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>, used for generating new projects and components <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
*   **Language**: Requires the use of TypeScript <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
*   **Architecture**: Components are represented as TypeScript classes with a component decorator <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. Components are typically broken into three files: TypeScript, HTML, and CSS <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.
*   **State Management**: Reactive state is defined as a property on the component class <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
*   **Lifecycle Hooks**: Component lifecycle is managed by implementing special methods like `ngOnInit`, called when the component is initialized <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.
*   **Syntax**: Uses a special templating language to extend HTML, allowing for directives like `ngFor` to loop over items <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>. Unlike [[react_vs_angular_and_vue | React]], Angular brings JavaScript into the HTML <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.
*   **Data Binding**: Supports two-way data binding using the `ngModel` directive <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.

### Trade-offs
*   **Learning Curve**: Tends to have a much higher learning curve than other frameworks <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>, and can be overwhelming for beginners <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>.
*   **Project Size**: Generates a fairly large project structure from the start <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>.
*   **Module Imports**: Requires importing specific Angular modules (e.g., Forms module for `ngModel`) for certain directives to work <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.
*   **Suitability**: While powerful for big teams, it may be overwhelming if you're a beginner <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>. It is popular with enterprise applications due to its structured approach <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.

## Vue.js

Vue.js, independently developed by Evan You, offers a similar feel to Angular but in a package more approachable for independent developers <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.

### Features
*   **Developer**: Independently developed and maintained by Evan You <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.
*   **[[comparison_of_web_development_frameworks | Ecosystem]]**: Has official packages for routing and state management, plus a large ecosystem of third-party packages <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.
*   **[[popularity_and_impact_of_reactjs_in_web_development | Popularity]]**: Has the most GitHub stars at 187,000, and is roughly tied with Angular for second place in npm downloads <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.
*   **Tooling**: Features a powerful CLI, including a "Vue UI" command that provides a browser-based interface for generating apps with various dependencies and features <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.
*   **Architecture**: Components are defined in `.view` files and are organized into three parts: a template, a script, and styles <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>. The component itself is represented as a plain JavaScript object <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.
*   **State Management**: Reactive data or state is defined using the `data` property on the component object <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.
*   **Event Handling**: Methods to change state are defined in the `methods` property <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>. Directives like `v-on:submit` handle form submissions <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>, with modifiers like `.prevent` to automatically prevent default behavior <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>.
*   **Lifecycle Hooks**: Lifecycle methods, such as `mounted` (called when the component is initialized), can be used to tap into the component lifecycle <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.
*   **Syntax**: Uses directives similar to Angular, such as `v-for` to loop over items <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.
*   **Data Binding**: Employs the `v-model` directive for two-way data binding of form input values <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>.

### Trade-offs
*   **CLI Power**: While powerful, its CLI doesn't generate components and is not quite as powerful as the Angular CLI <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>.

## Conclusion

Ultimately, all modern [[comparison_of_javascript_frameworks | JavaScript frameworks]] like [[reactjs_overview_and_history | React]], Angular, and Vue can accomplish the same basic tasks in web development <a class="yt-timestamp" data-t="00:21:40">[00:21:40]</a>. The choice of framework often comes down to [[choosing_the_right_javascript_framework_for_your_project | personal preference]], team happiness, and the specific needs of a project, rather than one being definitively "the best" <a class="yt-timestamp" data-t="00:21:26">[00:21:26]</a>.