---
title: Integrating thirdparty libraries with TypeScript
videoId: ahCwqrYpIuM
---

From: [[fireship]] <br/> 

When working with [[introduction_to_typescript | TypeScript]] projects, integrating third-party [[javascript_package_management_and_libraries | JavaScript package management and libraries | libraries]] is a common task <a class="yt-timestamp" data-t="04:31">[04:31]</a>. [[introduction_to_typescript | TypeScript]] provides mechanisms to ensure these [[javascript_package_management_and_libraries | JavaScript package management and libraries | libraries]] are type-checked, offering better developer tooling and bug detection <a class="yt-timestamp" data-t="04:56">[04:56]</a>.

## Type Declarations for Libraries

Many mainstream [[javascript_package_management_and_libraries | JavaScript package management and libraries | libraries]], such as Firebase, automatically ship with their type declarations <a class="yt-timestamp" data-t="04:40">[04:40]</a>. This means that when you install these [[javascript_package_management_and_libraries | JavaScript package management and libraries | libraries]], [[introduction_to_typescript | TypeScript]] can immediately understand their structure and provide [[type_annotations_and_strong_typing_in_typescript | strong typing]], autocomplete, and IntelliSense <a class="yt-timestamp" data-t="04:56">[04:56]</a>.

However, not all [[javascript_package_management_and_libraries | JavaScript package management and libraries | libraries]] include type declarations by default <a class="yt-timestamp" data-t="04:44">[04:44]</a>. For example, if you install a library like Lodash using [[installing_and_setting_up_typescript_with_NPM | NPM]] and try to import it into a [[introduction_to_typescript | TypeScript]] file, you might receive a warning from [[introduction_to_typescript | TypeScript]] indicating that no declarations were found <a class="yt-timestamp" data-t="04:46">[04:46]</a>. This absence means you won't get any auto-complete or IntelliSense in the IDE for that specific library <a class="yt-timestamp" data-t="04:54">[04:54]</a>.

### Installing Community-Maintained Types

For [[javascript_package_management_and_libraries | JavaScript package management and libraries | libraries]] that do not ship with their own type declarations, there is a large mono-repository of community-maintained types available <a class="yt-timestamp" data-t="04:58">[04:58]</a>. These types are typically installed as development dependencies.

To install types for a library (e.g., Lodash), you would use [[installing_and_setting_up_typescript_with_NPM | NPM]] to install the corresponding `@types` package <a class="yt-timestamp" data-t="05:02">[05:02]</a>. For Lodash, this would be `@types/lodash` <a class="yt-timestamp" data-t="05:02">[05:02]</a>.

```bash
npm install lodash
npm install --save-dev @types/lodash
```
Once installed, your development environment will have autocomplete and IntelliSense for every function provided by that library <a class="yt-timestamp" data-t="05:05">[05:05]</a>.