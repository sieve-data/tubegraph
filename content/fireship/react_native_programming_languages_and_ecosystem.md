---
title: React Native programming languages and ecosystem
videoId: X8ipUgXH6jw
---

From: [[fireship]] <br/> 

[[react_native_vs_flutter_comparison | React Native]], developed by Facebook, is a prominent framework for building cross-platform mobile applications <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. It allows developers to create applications for multiple platforms like iOS, Android, and the web from a single codebase <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. The video demonstrates its capabilities by building a chat app using [[react_native_vs_flutter_comparison | React Native]] with Firebase as the backend <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

## Programming Languages

[[react_native_vs_flutter_comparison | React Native]] applications are primarily coded in [[popular_dynamic_and_highlevel_programming_languages | JavaScript]], with [[using_react_and_ethers_for_web3_apps | React]] serving as a required UI library <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. [[using_react_and_ethers_for_web3_apps | React]] can be seen as an extension of the [[popular_dynamic_and_highlevel_programming_languages | JavaScript]] language <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. For developers seeking a type system, [[react_native_vs_flutter_comparison | React Native]] also supports TypeScript <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. While [[popular_dynamic_and_highlevel_programming_languages | JavaScript]] was not originally designed for mobile app development, it has become a widely used language in the ecosystem <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Ecosystem

The [[react_native_vs_flutter_comparison | React Native]] ecosystem is characterized by its origins at Facebook and its active development on GitHub <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a> <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

### Development Philosophy

[[react_native_vs_flutter_comparison | React Native]], similar to [[using_react_and_ethers_for_web3_apps | React]] for the web, is designed to be minimal <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. It provides a set of base components, but largely relies on the open-source community for additional functionalities <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>. Consequently, a complete [[react_native_vs_flutter_comparison | React Native]] project often necessitates a significant number of third-party dependencies depending on the required features <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

Despite this, [[react_native_vs_flutter_comparison | React Native]] benefits from a large and active community, enabling developers to find solutions for a wide range of needs <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

### Limitations

A notable challenge with [[react_native_vs_flutter_comparison | React Native]] is that many [[using_react_and_ethers_for_web3_apps | React]] web libraries are not compatible with it <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>. For example, libraries for advanced animations like Framer Motion are not directly usable in [[react_native_vs_flutter_comparison | React Native]] <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.

## Architecture

Under the hood, [[react_native_vs_flutter_comparison | React Native]] operates by running two separate [[popular_dynamic_and_highlevel_programming_languages | JavaScript]] threads <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>. One thread manages the app's execution on the native platform, while the other handles the application's business logic <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. These threads are isolated but communicate through a "bridge" where they exchange serialized messages <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>. This system allows a [[popular_dynamic_and_highlevel_programming_languages | JavaScript]] app to interact with the native platform, ensuring that when [[react_native_vs_flutter_comparison | React Native]] renders a component, it's a true native component on the corresponding platform <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. This means the UI will consistently reflect the intended appearance of native components <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.

## [[performance_and_developer_experience_in_react_native_and_flutter | Developer Experience]]: Setup and Tooling

### Initial Setup

To begin a new [[react_native_vs_flutter_comparison | React Native]] project, developers can run `npx react-native init` from the command line <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. A template like `native-base` can optionally be passed to provide a pre-built UI <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. Alternatively, `expo` can be used instead of the default [[react_native_vs_flutter_comparison | React Native]] CLI to offer a more comprehensive starting point <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

Upon opening a new project, developers will find several configuration files in the root directory, including:
*   **Metro:** For hot reloading <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   **Watchman:** Also for hot reloading <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
*   **Buck:** The build tool <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
*   **Babel:** For transpiling [[popular_dynamic_and_highlevel_programming_languages | JavaScript]] <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
*   Flow: Ships by default, giving the project a "very Facebooky" feel <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.

The application's source code is typically contained within a single `app.js` file <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. This file contains familiar [[using_react_and_ethers_for_web3_apps | React]] code for web developers, with the main difference being the use of special components imported from [[react_native_vs_flutter_comparison | React Native]] in JSX instead of standard HTML elements <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.

### Development Workflow

To serve a [[react_native_vs_flutter_comparison | React Native]] app locally:
1.  Connect to an Android emulator using an `adb` command <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.
2.  Run `npm start` to initiate Metro, which watches for code changes <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
3.  In a separate terminal, run `npm run android` to build and install the app on the emulator <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
4.  The app will automatically update in the background when code changes are detected <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
5.  Typing 'r' into the Watchman terminal performs a hot reload, which is crucial for preserving application state while reflecting code changes during design iterations <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.

### Tooling Philosophy

The tooling within [[react_native_vs_flutter_comparison | React Native]] is described as a "create your own adventure story" <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>. Being a [[popular_dynamic_and_highlevel_programming_languages | JavaScript]] project, developers have the flexibility to integrate tools like TypeScript for better type checking <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>. Other options include using the Ignite CLI to auto-generate boilerplate code or Expo to quickly launch the app on a device <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.

While this variety offers many options, it can also lead to decision fatigue and increased reliance on third-party solutions <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. Adding TypeScript to [[react_native_vs_flutter_comparison | React Native]] can provide similar tooling benefits to [[flutter_programming_languages_and_ecosystem | Dart]] (used in [[flutter_programming_languages_and_ecosystem | Flutter]]), such as immediate feedback on code errors <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.

### Component Structure

Both [[react_native_vs_flutter_comparison | React Native]] and [[flutter_programming_languages_and_ecosystem | Flutter]] utilize a tree structure of components or widgets <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. In [[react_native_vs_flutter_comparison | React Native]], this resembles HTML or JSX, where components like `View` tags can contain nested components <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>. Components can have state that changes during the app's lifecycle, and [[react_native_vs_flutter_comparison | React Native]] automatically re-renders the UI when the state changes <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.

[[react_native_vs_flutter_comparison | React Native]] often presents a challenge where there isn't a pre-built component for every desired functionality <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>. This requires developers to either customize a base component or install a third-party package <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. In [[using_react_and_ethers_for_web3_apps | React]], creating a new function for each UI component makes the process of extracting logic into custom components more intuitive <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.