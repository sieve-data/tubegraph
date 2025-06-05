---
title: Applications of React including React Native
videoId: Tn6-PIqc4UM
---

From: [[fireship]] <br/> 

[[react_introduction_and_history | React]], a JavaScript library developed at Facebook and released in 2013, is primarily used for [[building_components_with_react | building user interfaces]] <a class="yt-timestamp" data-t="00:00:00"></a>. It is considered the most influential UI library of recent memory <a class="yt-timestamp" data-t="00:00:06"></a>.

## Core UI Development with React
[[building_components_with_react | React]] is used to build components, which are logical, reusable parts of a user interface <a class="yt-timestamp" data-t="00:00:10"></a>. The process of [[building_components_with_react | building a component]] is simplified to its theoretical minimum: it is merely a JavaScript function <a class="yt-timestamp" data-t="00:00:15"></a>.

### Component Structure and Data Flow
The return value of a [[building_components_with_react | React]] component function is its HTML or UI, written using a special syntax called JSX <a class="yt-timestamp" data-t="00:00:23"></a>. JSX allows for the easy combination of JavaScript with HTML markup <a class="yt-timestamp" data-t="00:00:29"></a>.

To pass data into a component, a `props` argument is used <a class="yt-timestamp" data-t="00:00:33"></a>. This data can be referenced within the function body or UI using braces <a class="yt-timestamp" data-t="00:00:37"></a>. [[building_components_with_react | React]] will automatically update the UI when the `props` value changes <a class="yt-timestamp" data-t="00:00:41"></a>.

For internal state management within a component, the `state` hook can be employed <a class="yt-timestamp" data-t="00:00:44"></a>. A hook is a function that returns a value and a function to change that value <a class="yt-timestamp" data-t="00:00:48"></a>. For example, `count` could be a reactive state variable, and `setcount` would be the function to modify it <a class="yt-timestamp" data-t="00:00:53"></a>. When used in the template, the `count` will always display its most recent value <a class="yt-timestamp" data-t="00:00:58"></a>. This state can be dynamically changed by user interaction, such as binding `setcount` to a button click event <a class="yt-timestamp" data-t="00:01:01"></a>. [[building_components_with_react | React]] also provides various other built-in hooks for common use cases <a class="yt-timestamp" data-t="00:01:05"></a>.

## The Broader [[ecosystem_and_development_philosophy_of_react_native_and_flutter | React Ecosystem]]
A significant reason for [[popularity_and_impact_of_reactjs_in_web_development | React's widespread adoption]] and application is the massive [[ecosystem_and_development_philosophy_of_react_native_and_flutter | ecosystem]] that surrounds it <a class="yt-timestamp" data-t="00:01:09"></a>. [[building_components_with_react | React]] itself does not directly handle concerns like routing, state management, or animation <a class="yt-timestamp" data-t="00:01:14"></a>. Instead, it allows these functionalities to evolve naturally within the open-source community <a class="yt-timestamp" data-t="00:01:17"></a>. This means there is typically a well-supported library available for almost any development task <a class="yt-timestamp" data-t="00:01:21"></a>.

Examples of applications and supporting libraries within the [[ecosystem_and_development_philosophy_of_react_native_and_flutter | React ecosystem]] include:
*   **Static Sites**: Gatsby <a class="yt-timestamp" data-t="00:01:26"></a>
*   **Server-Side Rendering**: Next.js <a class="yt-timestamp" data-t="00:01:28"></a>
*   **Animation**: React Spring <a class="yt-timestamp" data-t="00:01:30"></a>
*   **Forms**: Formik <a class="yt-timestamp" data-t="00:01:31"></a>
*   **State Management**: Redux, MobX, Flux, Recoil, XState, and many more <a class="yt-timestamp" data-t="00:01:32"></a>

This extensive selection provides developers with endless choices to accomplish tasks in their preferred manner <a class="yt-timestamp" data-t="00:01:36"></a>.

## React Native for Mobile Applications
A significant advantage of learning [[building_components_with_react | React]] is the ease with which developers can transition to [[comparison_of_react_native_and_flutter_for_cross_platform_app_development | React Native]] to build mobile applications <a class="yt-timestamp" data-t="00:01:40"></a>. The core concepts of [[building_components_with_react | React]] directly transfer to mobile app development using [[comparison_of_react_native_and_flutter_for_cross_platform_app_development | React Native]] <a class="yt-timestamp" data-t="00:01:42"></a>. This versatility makes knowing [[building_components_with_react | React]] one of the most in-demand skills for front-end developers today <a class="yt-timestamp" data-t="00:01:45"></a>.