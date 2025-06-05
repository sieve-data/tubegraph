---
title: Using Angular components and component architecture
videoId: G0bBLvWXBvc
---

From: [[fireship]] <br/> 

Angular is a declarative UI framework that facilitates building complex cross-platform applications using web technologies like JavaScript, HTML, and CSS <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. At its core, Angular enables the creation of user interfaces by building and composing components together <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

## What is an Angular Component?

An Angular component is a fundamental building block of an Angular application, acting as a custom HTML element <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. Every component starts with a `@Component` decorator, which allows configuration via an object <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.

Each component typically consists of three main pieces <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>:

1.  **Component TypeScript (`.ts` file)**: This file defines the custom JavaScript logic and the internal state of the component <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
2.  **HTML Template (`.html` file)**: This contains the actual visual UI of the component, allowing data to be bound from the TypeScript file <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>. Angular provides a special templating language to empower HTML with JavaScript-like logic, enabling conditional expressions, loops, and direct data binding <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.
3.  **Style Sheet (`.css` or `.scss` file)**: Styles defined here are scoped specifically to that component, preventing them from affecting other components <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.

## Component Architecture and Communication

Angular utilizes a component-based UI architecture, similar to other UI frameworks like React, Svelte, and Vue <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. This architecture allows for:

*   **Data Passing**: Properties or data can be passed from one component to another <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
*   **Reactivity**: Declarative UI frameworks like Angular make it easy to keep application data in sync with the visual UI for the end user <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>. Angular employs "change detection" to look for changes in properties and update the UI performantly <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>.

### Component Selectors and Bootstrapping

The `selector` option within the `@Component` decorator defines the name of the component as it will be used in HTML <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. For example, `app-root` is the entry point into an Angular application, and this element is replaced with the actual Angular JavaScript application <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. This initial parsing of JavaScript is called bootstrapping <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

### Data Binding and Input Properties

Data can be bound to a template by adding it as a property to the component class <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. This data can then be interpolated in the template using double curly braces (`{{ }}`) <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>.

To pass data from a parent component to a child component, the `@Input` decorator is used <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>. This allows properties to be "input" into the component <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>. TypeScript can be used to type-check these input values <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.

### Event Handling

Angular allows binding to events using parentheses syntax, for example, `(click)`. This provides a way to execute methods in the component's TypeScript file in response to user interactions <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.

### [[Smart Components vs Dumb Components in Angular | Smart Components vs Dumb Components]]

*   **UI Component (Dumb Component)**: A component that only has inputs and does not modify its own state. It relies entirely on data passed from a parent component. These components are typically easy to test and focused solely on UI rendering <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>. An example is the `SquareComponent` in a tic-tac-toe game <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.
*   **Smart Component**: A component that manages its own internal state or data and orchestrates interactions between other components <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>. The `BoardComponent` in a tic-tac-toe game is an example, managing the game's state (squares, current player, winner) <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.

## Component Lifecycle

Components have a lifecycle, including a `constructor` that runs immediately when the class is created <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>. For initial setup work in a component, the [[Lifecycle of Angular Components | `ngOnInit` lifecycle hook]] is commonly used <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>. This hook is part of the `OnInit` interface from `@angular/core` <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

## Working with Directives

Angular templates leverage [[Angular Directives and Usage | directives]] to extend HTML with more dynamic behavior:

*   **Structural Directives**: These modify the DOM structure, adding or removing elements. Common examples include `*ngIf` for conditional rendering <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a> and `*ngFor` for looping over collections to render components multiple times <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.
*   **Attribute Directives**: These change the appearance or behavior of a DOM element or component. An example is `nbButton` from the Nebular theme, which applies button styling and behaviors to any HTML element <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>.

## Generating Components with Angular CLI

The Angular Command Line Interface (CLI) is a powerful tool that helps automate code generation based on Angular's conventions <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. To generate a new component, you can use the `ng generate component` command (or `ng g c` for short) <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>. Options like `inline-template` and `inline-styles` can be used to keep a component's HTML and CSS directly within its TypeScript file if preferred <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.

## Tooling for Components

Angular offers extensive tooling to enhance developer productivity:

*   **Angular Language Service**: Provides syntax highlighting and autocompletion for HTML templates <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
*   **Angular Console**: A graphical user interface (GUI) for the Angular CLI, allowing developers to point and click on CLI commands instead of typing them manually <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
*   **TypeScript**: Angular strongly encourages the use of TypeScript, which is now almost a standard for large, complex projects <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

## Integrating Component Libraries

Angular's ecosystem includes a variety of third-party component libraries like Angular Material, Ionic, and Nebular, which can be easily added to a project with a single CLI command (`ng add`) <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>. These libraries provide pre-built, themeable UI components, significantly reducing the effort required to achieve a consistent and visually appealing UI <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>.