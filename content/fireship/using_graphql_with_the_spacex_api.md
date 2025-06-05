---
title: Using GraphQL with the SpaceX API
videoId: 7wzR4Ig5pTI
---

From: [[fireship]] <br/> 

[[introduction_to_graphql|GraphQL]] is a query language for APIs that allows you to define a schema for your data and then specify how to fetch and supply that schema. This approach can lead to significant benefits in data interaction <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This article will explore the fundamental concepts of [[introduction_to_graphql|GraphQL]] by interacting with the public SpaceX API <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## What is [[introduction_to_graphql|GraphQL]]?

At its most basic, [[introduction_to_graphql|GraphQL]] is a language that enables front-end applications to communicate with back-end applications <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. It provides a consistent method for your front-end to request data from your back-end, regardless of underlying programming language differences <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

When a front-end application sends a [[graphql_query_language_and_schema|GraphQL Query]], the query's shape is identical to the JSON data it expects to receive back from the API <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. On the server side, [[introduction_to_graphql|GraphQL]] functions as a runtime for executing these queries <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. The server defines types for available data and resolvers to fetch that data from a database or other sources <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

A significant advantage of [[introduction_to_graphql|GraphQL]] is its strong typing on the server, which enables amazing tooling <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. As a consumer of the API, you can perform introspection to see what data is available <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. When you execute a [[graphql_query_language_and_schema|GraphQL Query]], the JSON payload returned will have properties identical to the structure defined in your query <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. Hovering over a field in a [[graphql_query_language_and_schema|GraphQL Query]] reveals its type (e.g., string, integer, or custom types defined by the server) <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. This ensures that as a front-end developer, you always know the exact shape of the data you expect <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

## [[differences_between_rest_and_graphql|Differences Between REST and GraphQL APIs]]

[[differences_between_rest_and_graphql|REST]] (Representational State Transfer) has been the standard for API design for about 20 years <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

### [[differences_between_rest_and_graphql|REST]] API Characteristics:
*   **Multiple Requests:** To get different pieces of data, you often make separate requests, each mapped to its unique URL <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
*   **Full Payloads:** Each response from the server typically contains the full JSON payload, even if your front-end application only needs a subset of that data <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>. The unused data must then be filtered out on the front end <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
*   **Adding Data:** Adding more data to a request often requires making additional requests to different URLs <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.

### [[introduction_to_graphql|GraphQL]] API Characteristics:
*   **Single Entry Point:** Instead of multiple URL endpoints, [[introduction_to_graphql|GraphQL]] typically has a single entry point into the API <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
*   **Query-Driven Data Return:** The actual [[graphql_query_language_and_schema|query]] sent from the front end determines what the back end will return; it's not based on a URL <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
*   **Precise Data Fetching:** The [[introduction_to_graphql|GraphQL]] API only returns the exact fields that were requested <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
*   **Simplified Data Requests:** Adding more data (e.g., a side salad and a drink) is a simple matter of updating the [[graphql_query_language_and_schema|query]] <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

### Advantages and Disadvantages:
While [[introduction_to_graphql|GraphQL]] simplifies how you request data from your front-end code <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>, it's not always a superior alternative to [[differences_between_rest_and_graphql|REST]] <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.
*   **Added Complexity:** A significant disadvantage is the initial added complexity <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. Building a [[differences_between_rest_and_graphql|RESTful]] service with [[creating_api_endpoints_with_express|Express.js]] can be done with minimal code, but [[introduction_to_graphql|GraphQL]] requires additional dependencies and a type system <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
*   **Scaling Benefits:** The benefits of [[introduction_to_graphql|GraphQL]] become substantial when working with multiple developers on a large API that integrates various back-end data sources <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. For small teams or simple APIs, the benefits might not outweigh the upfront complexity <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

## Exploring the SpaceX API with [[graphql_query_language_and_schema|GraphQL Queries]]

The public SpaceX API provides an interactive [[introduction_to_graphql|GraphQL]] Explorer for experimentation <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

### Basic Queries
1.  **Listing Rockets:** To query all rockets, you can select the "Rockets" field. Introspection will show that this returns an array of "Rocket" objects, which is a custom type defined by the server <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. You can then select specific properties like `id`, `name`, `type`, `country`, and `active` <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.
2.  **Query Arguments:** [[graphql_query_language_and_schema|Queries]] can take arguments. For instance, the `rockets` query can use a `limit` argument to specify the number of rockets returned or an `offset` for pagination <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
3.  **Individual Item Queries:** To request a specific rocket, you can use the `rocket` query, passing an `ID` as an argument <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.

### Advanced [[graphql_query_language_and_schema|GraphQL]] Concepts
*   **Variables:** You can reuse values in your [[graphql_query_language_and_schema|queries]] using variables, prefixed with a dollar sign (`$`) <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
*   **Directives:** Directives allow you to change the [[graphql_query_language_and_schema|query]] based on a variable's value. For example, the `@skip` directive can exclude a field if a condition is true <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
*   **Union Types:** Your [[graphql_query_language_and_schema|GraphQL]] schema might have properties that return multiple types, known as union types. For example, a `side` might be `FrenchFries` or a `Salad`, and you can query different fields based on the resolved type <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.

### Mutations
In addition to reading data with [[graphql_query_language_and_schema|queries]], you can also modify or write data on the server using a **mutation** <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>. A mutation functions similarly to a [[graphql_query_language_and_schema|query]] but serves as a convention to signal that data on the server will be altered <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

## [[building_an_application_with_apollo_client_and_angular|Building an Application with Apollo Client and Angular]]

To use [[introduction_to_graphql|GraphQL]] in a front-end application, the [[building_an_application_with_apollo_client_and_angular|Apollo Client]] is a popular choice <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>. It's a state management library that allows you to write [[graphql_query_language_and_schema|GraphQL Queries]] and see the results automatically update in your UI <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. [[building_an_application_with_apollo_client_and_angular|Apollo]] offers integrations for major JavaScript frameworks (Angular, React, Vue), vanilla web components, and native platforms (iOS, Android) <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

### Project Goal
Create a simple web application that fetches recent launches from SpaceX. Clicking a launch will display its details and associated pictures <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. The combination of [[introduction_to_graphql|GraphQL]] with TypeScript provides end-to-end type safety, enhancing the developer experience <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.

### Setup Steps
1.  **VS Code Extension:** Install the [[building_an_application_with_apollo_client_and_angular|Apollo GraphQL]] extension for VS Code for syntax highlighting <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
2.  **Apollo Configuration:** Create an `Apollo config KS` file at the root of your project, pointing to the public SpaceX API as your back-end <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.
3.  **Angular Components:** Generate Angular components for the list view (`ListView`) and detail view (`DetailView`) using the Angular CLI <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>.
4.  **Routing Configuration:** Set up routes in `app-routing.module.ts`:
    *   The default route (`/`) goes to the launch list component.
    *   A route with a URL parameter (`/launch/:id`) goes to the launch details component <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.

### Writing [[graphql_query_language_and_schema|GraphQL Queries]]
Before generating code, define your [[graphql_query_language_and_schema|GraphQL Queries]]:
1.  **Launch List Query (`launchListGraphQL`):**
    *   Define a [[graphql_query_language_and_schema|query]] named `pastLaunchesList` that takes a required `limit` integer parameter <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.
    *   Inside, reference the `launchesPast` query from SpaceX and pass the `limit` argument <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.
    *   Specify desired fields for each launch object, such as `id`, `mission_name`, and `links` to images <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.
2.  **Launch Details Query (`launchDetailsGraphQL`):**
    *   This [[graphql_query_language_and_schema|query]] takes a required `ID` type argument <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.
    *   Pass this `ID` to the `launch` query and filter by the desired fields for a single launch object <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.

### Automated Code Generation
[[introduction_to_graphql|GraphQL]] code generation is a powerful feature:
1.  **Integrate Apollo Angular:** Run `ng add apollo-angular` to install dependencies and create a [[introduction_to_graphql|GraphQL]] module <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. Configure this module to find the [[introduction_to_graphql|GraphQL]] API URI <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>.
2.  **[[graphql_query_language_and_schema|GraphQL Code Generator]]:** This tool can examine your [[graphql_query_language_and_schema|GraphQL]] schema and generate TypeScript interfaces and Angular services <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.
    *   Install the necessary packages <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.
    *   Create a `codegen.yaml` file in the project root to tell the generator where to find your [[graphql_query_language_and_schema|GraphQL]] files and what to generate <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.
    *   Add a `codegen` script to your `package.json` <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.
    *   Run the command (`npm run codegen`) to generate a `services` directory containing an Angular service with interfaces and methods to fetch data from the SpaceX API, based on your local [[graphql_query_language_and_schema|GraphQL Queries]] <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.

### Building UI Components
1.  **Angular Material:** Add Angular Material for styling <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.
2.  **Launch List Component:**
    *   Inject the auto-generated `PastLaunchesService` into the component's constructor <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.
    *   Use the `fetch` method from the service, passing a `limit` (e.g., 30) <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>.
    *   Use the `pipe` and `map` operators to extract `response.data.launchesPast` <a class="yt-timestamp" data-t="00:12:32">[00:12:32]</a>.
    *   In the template, unwrap the observable using the `async` pipe and loop over the `pastLaunches` array with `ngFor` to display material cards <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>.
    *   Add a `routerLink` to each card that points to the specific launch ID for navigation to the details page <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.
3.  **Launch Details Component:**
    *   Import `ActivatedRoute` from `@angular/router` and the `LaunchDetailsGraphQLService` <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>.
    *   Inject both into the constructor <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.
    *   Obtain the launch `ID` from the URL parameters using `activatedRoute.paramMap` <a class="yt-timestamp" data-t="00:13:47">[00:13:47]</a>.
    *   Use the `rxjs switchMap` operator to switch from the ID observable to an observable of the actual data from the `launchDetailService.fetch` method, passing the ID <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.
    *   Map the response to extract the raw launch data <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.
    *   In the template, unwrap the observable with the `async` pipe and display the launch details and photos <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>.

By following these steps, you will have a full-stack [[building_an_application_with_apollo_client_and_angular|Apollo GraphQL]]-powered Angular application <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>. For additional challenges, consider building an Angular pipe to format launch dates in relative time <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>.