---
title: GraphQL Query Language and Schema
videoId: 7wzR4Ig5pTI
---

From: [[fireship]] <br/> 

[[introduction_to_graphql | GraphQL]] is a powerful query language for Application Programming Interfaces (APIs) and a runtime for executing queries [00:00:00]. It provides a consistent way for front-end applications to communicate with back-end applications, acting as a "Rosetta Stone" to request data, regardless of underlying programming language differences [00:00:36].

At its core, [[introduction_to_graphql | GraphQL]] requires you to define a schema for your data, which then tells [[introduction_to_graphql | GraphQL]] how to fetch and supply that data [00:00:03].

## Key Concepts

### Schema and Types
On the server, [[introduction_to_graphql | GraphQL]] defines **types** for the data that is available [00:01:11]. This strong typing allows for robust tooling and predictable data shapes [00:01:19]. For example, when querying data, hovering over a field in a [[introduction_to_graphql | GraphQL]] query will display its type, which can be a built-in type like `String` or `Integer`, or a custom type defined by the server [00:02:01]. This ensures that front-end developers always know the exact shape of the data to expect from the server [00:02:14].

### Resolvers
The server also defines **resolvers**, which are functions responsible for actually fetching the data from a database or other data source [00:01:13].

### Queries
[[introduction_to_graphql | GraphQL]] queries are used by front-end applications to request data. The query itself has the same shape as the JSON payload you expect to receive back from the API [00:00:58].

Queries can be customized in several ways:
*   **Arguments**: Queries can take arguments, such as a `limit` to specify the number of items or an `offset` for pagination [00:04:45]. For individual items, an `ID` argument is often used, signalling a unique value [00:05:01].
*   **Variables**: Values can be reused throughout queries by using variables, which are prefixed with a dollar sign (`$`) [00:05:16].
*   **Directives**: Queries can be conditionally changed based on variable values using directives like `@skip` or `@include`. For instance, the `@skip` directive can exclude a field if a boolean variable is true [00:05:21].
*   **Union Types**: If a property in the [[introduction_to_graphql | GraphQL]] schema returns multiple types (a union type), you can specify which fields to return based on the specific type received [00:05:44].

### Mutations
While queries are for reading data, **mutations** are used to write or modify data on the server [00:06:13]. A mutation works similarly to a query but serves as a convention to signal that data will be modified on the server [00:06:19].

## [[differences_between_rest_and_graphql | GraphQL vs. REST]]

[[differences_between_rest_and_graphql | REST]] (Representational State Transfer) has been the standard for API design for about 20 years [00:02:25]. However, there are significant [[differences_between_rest_and_graphql | differences between REST and GraphQL]] APIs:

| Feature      | REST API                                                                                             | [[introduction_to_graphql | GraphQL]] API                                                                                         |
| :----------- | :--------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------- |
| **Endpoints**| Multiple URL endpoints, each request mapped to its own unique URL (e.g., `/bread`, `/ham`, `/cheese`) [00:02:39]. | Single entry point into the API [00:03:01].                                                                                  |
| **Data Fetch**| Often requires multiple requests to retrieve related data (e.g., three requests for bread, ham, and cheese for a sandwich) [00:02:35]. | A single query can retrieve complex, related data (e.g., a full sandwich with all its ingredients) [00:03:18].            |
| **Data Return**| Returns the full JSON payload for each request, potentially including data not needed by the front-end (e.g., a full loaf of bread, which the front-end then filters) [00:02:44]. | Returns only the actual fields that were requested by the query, reducing over-fetching [00:03:14].                        |
| **Flexibility**| Adding more data fields (e.g., side salad, drink) often requires additional requests to new URLs [00:03:26]. | Updating the query to include more fields is a simple matter of modifying the query itself [00:03:26].                     |
| **Simplification**| Can lead to more complex front-end code to manage multiple requests and filter data [00:02:55].    | Simplifies the way data is requested from front-end code [00:03:35].                                                        |

## Advantages and Disadvantages of [[introduction_to_graphql | GraphQL]]

### Advantages
*   **Reduced Over-fetching**: Only the requested fields are returned, optimizing data transfer [00:03:14].
*   **Simplified Client-side Data Retrieval**: A single query can fetch all necessary data, reducing the need for multiple API calls [00:03:35].
*   **Strongly Typed System**: Provides excellent tooling and predictability for data shapes [00:01:19].
*   **Introspection**: Allows API consumers to explore the available data and queries directly from the backend [00:01:32].
*   **Improved Developer Experience**: Especially when combined with technologies like TypeScript, it offers end-to-end type safety and an amazing developer experience [00:07:24].
*   **Scalability for Complex APIs**: Benefits truly shine for large APIs with multiple developers and numerous back-end data sources that need to be mapped together [00:04:06].

### Disadvantages
*   **Upfront Complexity**: Setting up a [[introduction_to_graphql | GraphQL]] service can be more complex than a simple RESTful service, requiring additional dependencies and a type system [00:03:51].
*   **Overkill for Simple APIs**: For small teams or relatively simple APIs, the benefits of [[introduction_to_graphql | GraphQL]] might not be substantial enough to justify the added initial complexity [00:04:02].
*   **Backend Resolution Complexity**: While [[introduction_to_graphql | GraphQL]] offers front-end flexibility, writing the code to resolve queries on the backend tends to be the more difficult part [00:06:06].

## Practical Application and Tooling

### [[using_graphql_with_the_spacex_api | SpaceX API]] Example
The public [[using_graphql_with_the_spacex_api | SpaceX API]] can be used to demonstrate [[introduction_to_graphql | GraphQL]] concepts. Its [[introduction_to_graphql | GraphQL]] Explorer allows users to interact with the API, see available queries via introspection, and execute example queries to view the JSON payloads [00:01:25]. For example, one can query for all rockets or an individual rocket by its ID [00:04:22].

### Front-end Integration with Apollo Client
The most popular way to work with [[introduction_to_graphql | GraphQL]] from a front-end application is by using the **Apollo Client** [00:06:30]. Apollo Client is a state management library that allows writing [[introduction_to_graphql | GraphQL]] queries and seeing the results automatically update in the UI [00:06:36]. It offers integrations for major JavaScript frameworks (Angular, React, Vue), vanilla web components, and native platforms (iOS, Android) [00:06:42].

### Code Generation with TypeScript
When combined with TypeScript, [[introduction_to_graphql | GraphQL]] offers exceptional tooling [00:07:11]. The **[[introduction_to_graphql | GraphQL]] Code Generator** is a tool that can analyze a [[introduction_to_graphql | GraphQL]] schema and automatically generate TypeScript interfaces and services for fetching data [00:10:37]. This means a [[introduction_to_graphql | GraphQL]] API can be converted into a series of interfaces directly usable in a front-end application, providing end-to-end type safety and an improved developer experience [00:07:16].

### Example: Angular with Apollo Client
Building a web application to fetch recent launches from [[using_graphql_with_the_spacex_api | SpaceX]] and display launch details can illustrate the integration:
1.  **Project Setup**: Install the Apollo [[introduction_to_graphql | GraphQL]] extension for VS Code for syntax highlighting [00:07:31].
2.  **Apollo Configuration**: Create an `apollo.config.ks` file to point to the backend API (e.g., the public [[using_graphql_with_the_spacex_api | SpaceX API]]) [00:07:43].
3.  **Component Generation**: Generate Angular components for a launch list and launch details using the Angular CLI [00:07:52].
4.  **Routing**: Set up routes for these components using Angular's routing module [00:08:20].
5.  **[[introduction_to_graphql | GraphQL]] Query Definition**: Define [[introduction_to_graphql | GraphQL]] queries (e.g., `pastLaunchesList`, `launchDetails`) in dedicated files, specifying required fields and arguments [00:09:01].
6.  **Apollo Integration**: Integrate Apollo into the Angular project using `ng add apollo-angular`, which installs dependencies and creates a [[introduction_to_graphql | GraphQL]] module [00:10:09].
7.  **Code Generation Setup**: Configure the [[introduction_to_graphql | GraphQL]] Code Generator with a `codegen.yaml` file to specify where to find [[introduction_to_graphql | GraphQL]] files and what to generate (e.g., Angular services with interfaces) [00:10:55].
8.  **Run Code Generator**: Execute the generator command (`cogent`) to create a `services` directory containing automatically generated services and interfaces based on the [[using_graphql_with_the_spacex_api | SpaceX API]] schema and local [[introduction_to_graphql | GraphQL]] queries [00:11:14].
9.  **Component Implementation**: Inject the generated services (e.g., `PastLaunchesService`, `LaunchDetailsService`) into the Angular components [00:12:12]. Use methods like `fetch` with arguments (e.g., `limit: 30`) [00:12:22]. Use RxJS operators like `map` to transform responses and `switchMap` to handle chained observables (e.g., getting an ID from the URL and then fetching data) [00:13:14].
10. **Template Binding**: Unpack observables in the template using Angular's `async` pipe and loop over data with `ngFor` [00:12:44]. Bind data to UI elements like material cards and router links [00:12:58].

This setup allows developers to focus on writing components and [[introduction_to_graphql | GraphQL]] queries, while the underlying code for data fetching and typing is automatically generated [00:11:51].