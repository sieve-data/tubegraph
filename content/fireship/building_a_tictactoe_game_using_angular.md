---
title: Building a TicTacToe game using Angular
videoId: G0bBLvWXBvc
---

From: [[fireship]] <br/> 

This article provides a beginner-friendly guide to building a Tic-Tac-Toe game from scratch using Angular, demonstrating core concepts, deploying it, and making it installable as a Progressive Web App (PWA) <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. Despite its reputation, Angular is presented as an easy-to-use framework for rapid development <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## What is Angular?

Angular is a comprehensive framework encompassing multiple functionalities <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>:
*   A declarative UI framework <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
*   A code bundler <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
*   A tool for [[building_a_chatbot_with_angular | building progressive web apps]] <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
*   Handles server-side rendering <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.
*   Provides libraries for forms, [[writing_and_running_angular_component_tests | testing]], animation, and more <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

It offers many features out-of-the-box, anticipating the complexity that arises as an application grows, yet most features are optional and can be adopted as needed <a class="yt-timestamp" data-t="01:10:07">[01:10:07]</a>. At its core, Angular helps in building complex cross-platform applications using web technologies like JavaScript, HTML, and CSS <a class="yt-timestamp" data-t="01:22:04">[01:22:04]</a>.

## Getting Started with Angular

### Initial Setup
To begin, ensure Node.js is installed on your system <a class="yt-timestamp" data-t="02:00:01">[02:00:01]</a>.

1.  **Install Angular CLI**: Run `npm install -g @angular/cli` to gain access to the `ng` command in your terminal <a class="yt-timestamp" data-t="02:02:04">[02:02:04]</a>.
2.  **Generate a new Angular App**: Use `ng new [app-name]` <a class="yt-timestamp" data-t="02:11:06">[02:11:06]</a>. When prompted, select `yes` for routing and choose SCSS for styles <a class="yt-timestamp" data-t="02:17:09">[02:17:09]</a>.
3.  **Open in VS Code**: Useful extensions include the Angular Language Service (for syntax highlighting) <a class="yt-timestamp" data-t="02:26:01">[02:26:01]</a> and Angular Console (for point-and-click CLI commands) <a class="yt-timestamp" data-t="02:33:04">[02:33:04]</a>.

### Development Workflow
*   **Serving the App**: Use the `serve` command (or `ng serve`) to bundle code with webpack and live reload, reflecting changes in the browser at `localhost:4200` <a class="yt-timestamp" data-t="02:41:00">[02:41:00]</a>.
*   **Bundling and Deployment**: The `ng build` command automatically minifies and bundles your code, generating multiple bundles for differential loading to ensure the smallest JavaScript bundle is loaded based on browser features <a class="yt-timestamp" data-t="03:13:00">[03:13:00]</a>. The output is in the `dist` folder, ready for deployment <a class="yt-timestamp" data-t="03:31:00">[03:31:00]</a>.
*   **TypeScript**: Angular was a pioneer in encouraging TypeScript, which is now standard for large, complex projects <a class="yt-timestamp" data-t="03:44:00">[03:44:00]</a>.
*   **Testing**: The default Angular app comes with [[setting_up_angular_testing_environment | testing]] utilities like Karma and Jasmine, with options for other frameworks like Jest and Cypress via schematics <a class="yt-timestamp" data-t="04:01:00">[04:01:00]</a>.

## Angular UI Development - Core Concepts
Angular is a [[using_angular_components_and_component_architecture | component-based UI framework]] similar to React, Svelte, and Vue <a class="yt-timestamp" data-t="04:21:00">[04:21:00]</a>.

### Anatomy of a Component
Every component has three main pieces <a class="yt-timestamp" data-t="05:09:00">[05:09:00]</a>:
*   **Component TypeScript**: Defines custom JavaScript logic and internal state <a class="yt-timestamp" data-t="05:11:00">[05:11:00]</a>.
*   **HTML Template**: Contains the visual UI, allowing data binding from the TypeScript <a class="yt-timestamp" data-t="05:18:00">[05:18:00]</a>.
*   **Stylesheet**: Scoped to that component, preventing styles from affecting other components <a class="yt-timestamp" data-t="05:26:00">[05:26:00]</a>.

### Application Structure
*   **`index.html`**: A plain HTML file containing `<app-root>`, which is replaced by the Angular JavaScript application during bootstrapping <a class="yt-timestamp" data-t="04:48:00">[04:48:00]</a>.
*   **`src/app` directory**: Where the actual UI code is written <a class="yt-timestamp" data-t="04:38:00">[04:38:00]</a>.
*   **`app.component`**: The default generated component, serving as the entry point <a class="yt-timestamp" data-t="04:40:00">[04:40:00]</a>.
*   **`router-outlet`**: Angular provides a powerful router for mapping components to URLs, capable of code splitting for lazy loading parts of the JavaScript bundle <a class="yt-timestamp" data-t="05:37:00">[05:37:00]</a>.

## Building the Tic-Tac-Toe Game

The Tic-Tac-Toe game involves a `Square` component and a `Board` component.

### Square Component (`src/app/square`)
The `Square` component represents an individual square on the game board <a class="yt-timestamp" data-t="06:16:00">[06:16:00]</a>.

1.  **Generation**: Use `ng generate component Square --inlineTemplate --inlineStyles` to create it with inline template and styles <a class="yt-timestamp" data-t="06:18:00">[06:18:00]</a>.
2.  **`@Component` Decorator**: Every component starts with `@Component`, which configures its behavior, including the `selector` (the name used in HTML) <a class="yt-timestamp" data-t="07:00:00">[07:00:00]</a>.
3.  **Data Binding and Interpolation**:
    *   Properties added to the component class can be interpolated in the template using double braces `{{ propertyName }}` <a class="yt-timestamp" data-t="08:11:00">[08:11:00]</a>.
    *   Angular's change detection updates the UI performantly when properties change <a class="yt-timestamp" data-t="08:24:00">[08:24:00]</a>.
4.  **`@Input()` Decorator**: Used to define properties that can be passed in from a parent component <a class="yt-timestamp" data-t="08:58:00">[08:58:00]</a>. This allows the `Square` component to receive its value (X or O) from the `Board` component <a class="yt-timestamp" data-t="09:19:00">[09:19:00]</a>.
5.  **UI (Dumb) Component**: The `Square` component is considered a "dump component" because it only has an input and doesn't modify its own state, making it easy to test <a class="yt-timestamp" data-t="09:36:00">[09:36:00]</a>.

### Board Component (`src/app/board`)
The `Board` component is a "smart component" responsible for managing the game's state <a class="yt-timestamp" data-t="09:58:00">[09:58:00]</a>.

1.  **Generation**: Generate with default options <a class="yt-timestamp" data-t="10:04:00">[10:04:00]</a>.
2.  **Internal State**:
    *   `squares`: An array representing the nine game board moves <a class="yt-timestamp" data-t="10:14:00">[10:14:00]</a>.
    *   `xIsNext`: A boolean to determine the current player <a class="yt-timestamp" data-t="10:20:00">[10:20:00]</a>.
    *   `winner`: Stores 'X' or 'O' if a winner exists <a class="yt-timestamp" data-t="10:26:00">[10:26:00]</a>.
3.  **Lifecycle Hooks**: `ngOnInit` is used for initial setup work in a component <a class="yt-timestamp" data-t="10:45:00">[10:45:00]</a>.
4.  **`newGame()` Method**: Initializes the `squares` array with null values, sets `winner` to null, and `xIsNext` to true <a class="yt-timestamp" data-t="10:50:00">[10:50:00]</a>.
5.  **Computed Property (`player`)**: A TypeScript getter to compute `player` ('X' or 'O') based on `xIsNext` <a class="yt-timestamp" data-t="11:30:00">[11:30:00]</a>.
6.  **`makeMove(idx: number)` Method**: An event handler for user clicks <a class="yt-timestamp" data-t="11:50:00">[11:50:00]</a>. It checks if the square is empty, splices in the current player's mark, and toggles `xIsNext` <a class="yt-timestamp" data-t="12:03:00">[12:03:00]</a>.
7.  **`calculateWinner()` Method**: An algorithm to determine if a player has won the game <a class="yt-timestamp" data-t="12:22:00">[12:22:00]</a>.
8.  **HTML Template**:
    *   Displays the current player and winner using interpolation <a class="yt-timestamp" data-t="12:45:00">[12:45:00]</a>.
    *   **Event Binding**: Uses parentheses `()` to bind to events like `(click)` <a class="yt-timestamp" data-t="13:06:00">[13:06:00]</a>.
    *   **Structural Directives**:
        *   `*ngIf`: Conditionally renders HTML based on a true/false evaluation, e.g., to display the winner <a class="yt-timestamp" data-t="13:30:00">[13:30:00]</a>.
        *   `*ngFor`: Renders a component multiple times based on an array, iterating over `squares` to create each `app-square` <a class="yt-timestamp" data-t="14:02:00">[14:02:00]</a>. It can also access the current item (`val`) and its index (`i`) <a class="yt-timestamp" data-t="14:16:00">[14:16:00]</a>.
    *   **CSS Styling**: Uses CSS Grid for a 3x3 grid layout <a class="yt-timestamp" data-t="14:45:00">[14:45:00]</a>.

## Enhancing the UI with a Design System (Nebular)
Angular's ecosystem offers various third-party component libraries that can be easily added to projects.

1.  **Adding Nebular**: Run `ng add @nebular/theme` <a class="yt-timestamp" data-t="15:48:00">[15:48:00]</a>. Choose a theme (e.g., Cosmic) and enable customization and animation <a class="yt-timestamp" data-t="15:59:00">[15:59:00]</a>.
2.  **Configuration**: This command updates `themes.scss` for variable customization <a class="yt-timestamp" data-t="16:07:00">[16:07:00]</a> and imports Nebular modules into `app.module` <a class="yt-timestamp" data-t="16:14:00">[16:14:00]</a>. It's possible to import only specific modules (e.g., `NbButtonModule`) to keep bundle sizes small <a class="yt-timestamp" data-t="16:31:00">[16:31:00]</a>.
3.  **Applying Styles**: Use directives like `nbButton` on HTML elements (e.g., `button`) to apply Nebular button themes and behaviors <a class="yt-timestamp" data-t="16:58:00">[16:58:00]</a>. Conditional rendering (`*ngIf`) can be used to display different button styles based on the square's state (empty, 'X', or 'O') <a class="yt-timestamp" data-t="17:34:00">[17:34:00]</a>.

## Making it a Progressive Web App (PWA)
Transforming the game into a PWA is a straightforward process in Angular.

1.  **Add PWA Schematic**: Run `ng add @angular/pwa` <a class="yt-timestamp" data-t="18:25:00">[18:25:00]</a>.
2.  **PWA Features**: This command adds <a class="yt-timestamp" data-t="18:30:00">[18:30:00]</a>:
    *   JavaScript code to load a service worker <a class="yt-timestamp" data-t="18:35:00">[18:35:00]</a>.
    *   A configuration file for customizing service worker behavior (e.g., offline caching) <a class="yt-timestamp" data-t="18:39:00">[18:39:00]</a>.
    *   A manifest file and icons for the app's install button <a class="yt-timestamp" data-t="18:53:00">[18:53:00]</a>.
3.  **Deployment**:
    *   Build for production: `ng build` <a class="yt-timestamp" data-t="19:06:00">[19:06:00]</a>.
    *   Add Firebase (optional, for hosting): `ng add @angular/fire`. This integrates Firebase hosting (which can be used on the free tier) <a class="yt-timestamp" data-t="19:18:00">[19:18:00]</a>.
    *   Deploy: `ng deploy` automatically deploys the production app to Firebase hosting <a class="yt-timestamp" data-t="19:35:00">[19:35:00]</a>.
4.  **Testing PWA**: Use Chrome DevTools' audits tab to verify PWA compliance <a class="yt-timestamp" data-t="19:48:00">[19:48:00]</a>. A compliant PWA can be installed on devices (e.g., Windows desktop, mobile) as if it were a native application <a class="yt-timestamp" data-t="19:57:00">[19:57:00]</a>.

Angular's powerful tooling and conventions make it highly efficient for building and deploying robust web applications quickly <a class="yt-timestamp" data-t="18:02:00">[18:02:00]</a>.