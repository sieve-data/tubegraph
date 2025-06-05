---
title: Building applications with vanilla JavaScript
videoId: cuHDQhDhvPE
---

From: [[fireship]] <br/> 

While the landscape of web development is dominated by modern [[comparison_of_javascript_frameworks | JavaScript frameworks]], understanding and utilizing [[javascript_basics_and_history | vanilla JavaScript]]—plain, unadulterated [[javascript_basics_and_history | JavaScript]] without libraries or frameworks—remains a fundamental skill for any expert web developer <a class="yt-timestamp" data-t="01:02:02">[01:02:02]</a>.

## The Role of Vanilla JavaScript in Modern Development

Although some "hot takes" occasionally suggest that a [[javascript_for_interactivity_and_frameworks | JavaScript framework]] isn't necessary <a class="yt-timestamp" data-t="00:58:00">[00:58:00]</a>, attempting to build a non-trivial application solely with [[javascript_basics_and_history | vanilla JavaScript]] can lead to significant challenges <a class="yt-timestamp" data-t="01:07:08">[01:07:08]</a>. Developers often end up inadvertently building their own rudimentary [[javascript_for_interactivity_and_frameworks | JavaScript framework]] in the process <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>. This highlights why the vast majority of developers opt to build their applications using established frameworks <a class="yt-timestamp" data-t="04:17:00">[04:17:00]</a>.

## Core Concepts in Vanilla JavaScript Application Development

When building an application with [[javascript_basics_and_history | vanilla JavaScript]], several key concepts must be manually managed:

*   **State Management**: Keeping track of the application's data <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>.
*   **Data Binding**: Connecting the HTML elements to the [[javascript_basics_and_history | JavaScript]] data <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>.
*   **Events**: Handling user interactions and other application events <a class="yt-timestamp" data-t="01:44:00">[01:44:00]</a>.
*   **Application Lifecycle**: Managing what happens when the application loads, updates, or unloads <a class="yt-timestamp" data-t="01:45:00">[01:45:00]</a>.

Unlike modern frameworks, [[javascript_basics_and_history | vanilla JavaScript]] does not automatically bind HTML to [[javascript_basics_and_history | JavaScript]] <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a>. This requires developers to imperatively select HTML elements from the DOM (Document Object Model) <a class="yt-timestamp" data-t="01:55:00">[01:55:00]</a>, which can become tedious and annoying in complex applications <a class="yt-timestamp" data-t="02:01:00">[02:01:00]</a>.

## Example: Building a Basic To-Do Application

A basic to-do application, allowing users to add and save items to local storage, illustrates the manual effort involved in [[javascript_basics_and_history | vanilla JavaScript]] <a class="yt-timestamp" data-t="01:23:00">[01:23:00]</a>.

To set up a simple [[javascript_basics_and_history | vanilla JavaScript]] application, you create an HTML file and add a script tag to its body <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>.

### Manual DOM Manipulation and State Management

In [[javascript_basics_and_history | vanilla JavaScript]], you must manually obtain references to HTML elements using methods like `document.querySelector` <a class="yt-timestamp" data-t="02:17:00">[02:17:00]</a>. Application data, such as a list of to-do items, is typically stored in a [[javascript_basics_and_history | JavaScript]] array <a class="yt-timestamp" data-t="02:24:00">[02:24:00]</a>.

Updating the UI when data changes is a manual process <a class="yt-timestamp" data-t="02:31:00">[02:31:00]</a>. For instance, to add a new to-do item:
1.  You create a new HTML element using `document.createElement` <a class="yt-timestamp" data-t="02:43:00">[02:43:00]</a>.
2.  You imperatively update its `innerHTML` with the desired content <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>.
3.  You append the new element to the existing list in the DOM <a class="yt-timestamp" data-t="02:53:00">[02:53:00]</a>.

This approach makes it challenging to keep the application's data (state) synchronized with the user interface <a class="yt-timestamp" data-t="03:03:00">[03:03:00]</a>.

### Event Handling

To react to user interactions, such as form submissions, you register event listeners on the relevant HTML elements <a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a>. For a form submission, the `preventDefault` method is typically called to stop the page from refreshing <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>.

One notable drawback is that HTML markup in [[javascript_basics_and_history | vanilla JavaScript]] doesn't inherently indicate the presence of event listeners; one must search through the [[javascript_basics_and_history | JavaScript]] code to understand these connections, which becomes "extremely difficult in a complex application" <a class="yt-timestamp" data-t="03:35:00">[03:35:00]</a>.

### Application Lifecycle

Managing the application's lifecycle, like loading existing data when the page first loads, involves manually retrieving data (e.g., from local storage) and then iterating through it to render items in the UI <a class="yt-timestamp" data-t="03:47:00">[03:47:00]</a>.

## Conclusion

While building a to-do application with [[javascript_basics_and_history | vanilla JavaScript]] is achievable, this approach does not scale well with increasing complexity <a class="yt-timestamp" data-t="04:09:00">[04:09:00]</a>. Features like routing or animations would need to be implemented from scratch <a class="yt-timestamp" data-t="04:13:00">[04:13:00]</a>. This is why the vast majority of developers choose to build their applications with a [[javascript_for_interactivity_and_frameworks | framework]] <a class="yt-timestamp" data-t="04:17:00">[04:17:00]</a>, which provide standardized ways to handle state, data binding, events, and the application lifecycle.