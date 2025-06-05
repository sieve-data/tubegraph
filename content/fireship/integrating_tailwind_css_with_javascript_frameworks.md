---
title: Integrating Tailwind CSS with JavaScript frameworks
videoId: pfaSUYaSgRo
---

From: [[fireship]] <br/> 

[[introduction_to_tailwind_css | Tailwind CSS]] is a highly disruptive web technology that promotes a [[functional_utility_class_approach_in_tailwind_css | functional utility class approach]] to CSS [00:00:08] to enable faster UI development and customization [00:00:16]. One of the primary reasons for its popularity is its seamless integration with component-based [[javascript_trends_and_frameworks | JavaScript frameworks]] [01:55:00].

## Compatibility and General Approach
Tailwind CSS is designed to work effectively with various [[javascript_trends_and_frameworks | JavaScript frameworks]] such as React, Vue, Angular, and Svelte [01:50:00]. The core principles of integrating Tailwind remain consistent across different frameworks [02:02:00], with detailed setup instructions available in the official Tailwind documentation [02:05:00].

## Example Setup with React (Create React App)
For a project initialized with Create React App, integrating Tailwind involves several steps:
1.  **Install Dependencies**: Begin by installing the necessary dependencies [02:12:00].
2.  **Override PostCSS Configuration**: Install `craco`, a package used to override the native PostCSS configuration [02:15:00].
3.  **Modify `package.json`**: Replace `react-scripts` with `craco` in your `package.json` file [02:18:00].
4.  **Create `craco.config.js`**: Create a `craco.config.js` file to apply the Tailwind plugin [02:22:00].
5.  **Generate Tailwind Config**: Use `npx tailwindcss init` to generate a `tailwind.config.js` file in the project's root directory [02:27:00].
6.  **Include Tailwind Styles**: In your `index.css` file, use the Tailwind directive to include the actual Tailwind styles [02:34:00].
7.  **Run the Project**: Start the project locally by running `npm start` [02:41:00].

## Benefits of Component-Based Integration
Integrating Tailwind with component-based [[javascript_trends_and_frameworks | JavaScript frameworks]] offers several advantages:
*   **IntelliSense**: When adding CSS classes to a React component (or other framework components), developers benefit from excellent IntelliSense support in editors like VS Code, which displays all available Tailwind utility classes and their underlying CSS properties [02:23:00].
*   **Organized UI**: The ability to break down a UI into smaller, manageable components (e.g., `sidebar.js`) helps keep the codebase organized and easier to maintain, even when applying many classes to an element [04:40:00].
*   **Custom Classes with Utilities**: Custom CSS classes can be built using Tailwind utilities within the `index.css` file via the `@apply` directive, allowing for reusability of common utility combinations [08:51:00].
*   **Responsive and Interactive UI**: Tailwind's utility classes and variants (like `hover`, `focus`, `group-hover`, `md`, `lg`) simplify the creation of responsive layouts and interactive elements with animations and transitions [09:37:00].
*   **Dark Mode Integration**: [[customizing_themes_and_enabling_dark_mode_in_tailwind_css | Dark mode]] can be easily implemented by configuring the `darkMode` option in `tailwind.config.js` (either `media` or `class` strategy) and using the `dark:` variant on elements. Custom React hooks can manage user preferences for dark mode in local storage [11:56:00].

This integration approach allows developers to design highly customized UIs more quickly while leveraging the tooling and maintainability benefits of [[javascript_trends_and_frameworks | JavaScript frameworks]] [01:37:00]. An example project showcased in this context involves [[building_a_discordinspired_animated_navbar_with_tailwind_css | building a Discord-inspired dashboard]] with animated sidebar icons and tooltips [00:30:00].