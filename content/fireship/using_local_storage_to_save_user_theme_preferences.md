---
title: Using local storage to save user theme preferences
videoId: rXuHGLzSmSE
---

From: [[fireship]] <br/> 

When a user selects a theme for a website, it's beneficial for that theme to persist even if the page is refreshed or the user navigates away and returns later <a class="yt-timestamp" data-t="01:07:07">[01:07:07]</a>. This persistence can be achieved by caching the user's selection in the browser's [[website_access_and_user_interactions | local storage]] <a class="yt-timestamp" data-t="01:10:10">[01:10:10]</a>.

## Caching User Selection with Local Storage
[[website_access_and_user_interactions | Local storage]] is a simple key-value store built directly into the browser <a class="yt-timestamp" data-t="01:10:10">[01:10:10]</a>. It can be accessed by calling `localStorage` in your script <a class="yt-timestamp" data-t="01:11:10">[01:11:10]</a>.

### Saving Theme Preferences
To save a theme preference, the `setItem` method is used <a class="yt-timestamp" data-t="01:12:20">[01:12:20]</a>. The first argument is the key (e.g., "theme") and the second is the value (e.g., "dark") <a class="yt-timestamp" data-t="01:12:20">[01:12:20]</a>.

*   **Saving Light/Dark Theme:** When switching to a light or dark theme, `localStorage.setItem('theme', 'dark')` or `localStorage.setItem('theme', 'light')` would be called respectively <a class="yt-timestamp" data-t="01:12:47">[01:12:47]</a>.
*   **Saving Solar Theme:** The solar theme works differently as it's applied *on top* of either the light or dark mode <a class="yt-timestamp" data-t="01:12:01">[01:12:01]</a>.
    *   If the user *is* using the solar theme, `localStorage.setItem('isSolar', true)` is called <a class="yt-timestamp" data-t="01:12:38">[01:12:38]</a>.
    *   If the user is *not* using solar, the `isSolar` property can simply be removed from local storage <a class="yt-timestamp" data-t="01:12:32">[01:12:32]</a>.

### Retrieving Saved Preferences
When the script runs (e.g., on page refresh or a new visit) <a class="yt-timestamp" data-t="01:12:12">[01:12:12]</a>:
1.  The user's existing theme and whether the solar theme is active are retrieved from [[website_access_and_user_interactions | local storage]] <a class="yt-timestamp" data-t="01:11:55">[01:11:55]</a>.
2.  If an existing theme is saved, that theme's class is added to the `<body>` element of the document <a class="yt-timestamp" data-t="01:12:01">[01:12:01]</a>.
3.  If a value for the solar theme is found, the `solar` class is also added to the `<body>` <a class="yt-timestamp" data-t="01:12:08">[01:12:08]</a>.

### Clearing Local Storage
To erase all key-value pairs saved in [[website_access_and_user_interactions | local storage]], `localStorage.clear()` can be called in the browser console <a class="yt-timestamp" data-t="01:12:53">[01:12:53]</a>. You can also inspect the currently saved key-value pairs by typing `localStorage` in the browser console <a class="yt-timestamp" data-t="01:12:47">[01:12:47]</a>.