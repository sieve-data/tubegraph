---
title: Building an Application with Apollo Client and Angular
videoId: 7wzR4Ig5pTI
---

From: [[fireship]] <br/> 

[[using_angular_components_and_component_architecture | Angular applications]] can leverage GraphQL and Apollo Client for efficient data communication with backend services <a class="yt-timestamp" data-t="00:36:22">[00:36:22]</a>. Apollo Client is a popular state management library that allows developers to write GraphQL queries and automatically update results in the UI <a class="yt-timestamp" data-t="06:31:02">[06:31:02]</a>. It provides integrations for major JavaScript frameworks, including Angular, React, Vue, vanilla web components, and native platforms like iOS and Android <a class="yt-timestamp" data-t="06:43:08">[06:43:08]</a>.

When combining Angular with GraphQL, an amazing developer experience is achieved through end-to-end type safety, especially when utilizing TypeScript <a class="yt-timestamp" data-t="07:13:00">[07:13:00]</a>. This integration allows for the automatic conversion of a GraphQL API into a series of interfaces directly usable in the frontend application <a class="yt-timestamp" data-t="07:16:00">[07:16:00]</a>.

## Setting Up an Angular Project with Apollo Client

To build a web application that fetches recent launches from the public SpaceX API using Apollo GraphQL and Angular, follow these steps:

### Initial Setup
1.  **Start with a new Angular application** <a class="yt-timestamp" data-t="07:29:56">[07:29:56]</a>.
2.  **Install the Apollo GraphQL extension for VS Code**: This provides syntax highlighting and other necessary features for working with GraphQL in the editor <a class="yt-timestamp" data-t="07:31:00">[07:31:00]</a>.
3.  **Create `apollo.config.ks`**: In the root of the project, create this file to tell Apollo where to find your backend API, pointing it to the public SpaceX API <a class="yt-timestamp" data-t="07:41:00">[07:41:00]</a>.

### Component and Routing Configuration
1.  **Generate Components**: Create two [[using_angular_components_and_component_architecture | Angular components]] using the Angular CLI:
    *   `ListView`: To display all recent launches <a class="yt-timestamp" data-t="07:52:00">[07:52:00]</a>.
    *   `DetailView`: To show specific launch details and pictures <a class="yt-timestamp" data-t="07:59:00">[07:59:00]</a>.
    *   Set the change detection to `OnPush` for performance optimization, as Apollo and GraphQL only require subscribing to observables for data <a class="yt-timestamp" data-t="08:05:00">[08:05:00]</a>.
2.  **Configure Routes**: In the `app-routing.module.ts`, set up routes for the generated components:
    *   The root route (`/`) should point to the `LaunchListComponent` as the default view <a class="yt-timestamp" data-t="08:20:00">[08:20:00]</a>.
    *   A dynamic route (e.g., `/launch/:id`) should point to the `LaunchDetailsComponent` to display details for a specific launch ID <a class="yt-timestamp" data-t="08:28:00">[08:28:00]</a>.
3.  **Clean `app.component.html`**: Remove boilerplate code, leaving only the `<router-outlet>` tag <a class="yt-timestamp" data-t="08:40:00">[08:40:00]</a>.

## Defining GraphQL Queries

GraphQL queries allow the frontend to specify the exact shape of the data it expects from the API <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>.

1.  **Launch List Query**:
    *   In `launch-list.graphql` (within the `launch-list` component directory), define a query named `pastLaunchesList` <a class="yt-timestamp" data-t="09:01:00">[09:01:00]</a>.
    *   This query can take an integer `limit` parameter (marked with `!` to make it required) <a class="yt-timestamp" data-t="09:12:00">[09:12:00]</a>.
    *   Specify the fields to be returned for each launch object, such as `id`, `mission_name`, and `links` to images <a class="yt-timestamp" data-t="09:30:00">[09:30:00]</a>.
    ```graphql
    query pastLaunchesList($limit: Int!) {
      launchesPast(limit: $limit) {
        id
        mission_name
        links {
          mission_patch_small
        }
        # ... other desired fields
      }
    }
    ```
2.  **Launch Details Query**:
    *   In `launch-details.graphql` (within the `launch-details` component directory), define a query for individual launch details <a class="yt-timestamp" data-t="09:43:00">[09:43:00]</a>.
    *   This query takes a required `ID` type argument <a class="yt-timestamp" data-t="09:49:00">[09:49:00]</a>.
    *   Filter by the desired fields from the API for a specific launch <a class="yt-timestamp" data-t="09:57:00">[09:57:00]</a>.
    ```graphql
    query launchDetails($id: ID!) {
      launch(id: $id) {
        id
        mission_name
        # ... more detailed fields
      }
    }
    ```

## Integrating Apollo Angular and Code Generation

Automatic code generation is a powerful feature when combining GraphQL with TypeScript.

1.  **Install Apollo Angular**: Run `ng add apollo-angular` from the command line. This installs Apollo dependencies and creates a `graphql.module.ts` file <a class="yt-timestamp" data-t="10:09:00">[10:09:00]</a>.
2.  **Configure GraphQL Module**: Open `graphql.module.ts` and set the `URI` variable to point to your GraphQL API endpoint (e.g., the SpaceX API) <a class="yt-timestamp" data-t="10:23:00">[10:23:00]</a>.
3.  **GraphQL Code Generator**:
    *   This tool automatically generates TypeScript interfaces and Angular services by analyzing your GraphQL schema and local queries <a class="yt-timestamp" data-t="10:37:00">[10:37:00]</a>.
    *   Install necessary packages (copy command from lesson repo) <a class="yt-timestamp" data-t="10:50:00">[10:50:00]</a>.
    *   Create a `codegen.yml` file in the project root to configure the generator, specifying where to find GraphQL files and what types of code to generate <a class="yt-timestamp" data-t="10:55:00">[10:55:00]</a>.
    *   Add a `codegen` script to your `package.json` (e.g., `"codegen": "graphql-codegen --config codegen.yml"`) <a class="yt-timestamp" data-t="11:07:00">[11:07:00]</a>.
    *   Run `npm run codegen` (or `yarn codegen`) in the terminal. This will create a `services` directory containing auto-generated Angular services with all necessary interfaces and methods to fetch data based on your queries <a class="yt-timestamp" data-t="11:19:00">[11:19:00]</a>.

## Building the User Interface Components

### Adding Angular Material
1.  **Install Angular Material**: Run `ng add @angular/material` to add a UI component library <a class="yt-timestamp" data-t="11:58:00">[11:58:00]</a>.
2.  **Import Modules**: Import necessary Material modules (e.g., `MatCardModule`) into your `app.module.ts` or a shared Material module <a class="yt-timestamp" data-t="12:04:00">[12:04:00]</a>.

### Launch List Component (`launch-list.component.ts`)
1.  **Inject Service**: In the constructor, inject the auto-generated `PastLaunchesService` <a class="yt-timestamp" data-t="12:11:00">[12:11:00]</a>.
2.  **Fetch Data**: Call the `fetch` method on the service, passing the `limit` argument (e.g., `30`). Pipe the response through the `map` operator to extract only the relevant `launchesPast` data <a class="yt-timestamp" data-t="12:20:00">[12:20:00]</a>.

### Launch List Template (`launch-list.component.html`)
1.  **Unwrap Observable**: Use Angular's `async` pipe to unwrap the `pastLaunches` observable, assigning the result to a template variable <a class="yt-timestamp" data-t="12:42:00">[12:42:00]</a>.
2.  **Loop and Display**: Use `*ngFor` to loop over the `pastLaunches` array and display each launch within an `mat-card`. Add a `routerLink` to each card to navigate to the detailed view with the launch ID <a class="yt-timestamp" data-t="12:51:00">[12:51:00]</a>.
3.  **Display Details**: Show `mission_name`, `links.mission_patch_small`, and other desired fields within the card <a class="yt-timestamp" data-t="13:11:00">[13:11:00]</a>.

### Launch Details Component (`launch-details.component.ts`)
1.  **Inject Dependencies**: Inject `ActivatedRoute` (from `@angular/router`) to access URL parameters and the auto-generated `LaunchDetailsService` <a class="yt-timestamp" data-t="13:35:00">[13:35:00]</a>.
2.  **Fetch Data by ID**:
    *   The `ActivatedRoute` provides URL parameters as an observable <a class="yt-timestamp" data-t="13:53:00">[13:53:00]</a>.
    *   Use the `rxjs switchMap` operator to switch from the ID parameter observable to the `launchDetailService.fetch` observable, passing the ID <a class="yt-timestamp" data-t="14:02:00">[14:02:00]</a>.
    *   Map the response down to the raw launch data <a class="yt-timestamp" data-t="14:21:00">[14:21:00]</a>.

### Launch Details Template (`launch-details.component.html`)
1.  **Unwrap Observable**: Use the `async` pipe to unwrap the `launchDetails` observable <a class="yt-timestamp" data-t="14:29:00">[14:29:00]</a>.
2.  **Display Details**: Add HTML to display the launch details (e.g., mission name, photos) by interpolating the values from the `launchDetails` object <a class="yt-timestamp" data-t="14:38:00">[14:38:00]</a>.

After these steps, running `ng serve` will allow you to view the list of SpaceX launches and click on individual items to see their details <a class="yt-timestamp" data-t="15:00:00">[15:00:00]</a>.