---
title: Pros and cons of different full stack frameworks
videoId: FQPlEnKav48
---

From: [[fireship]] <br/> 

This article explores various full stack web frameworks, each used to build the same web application to compare their developer experience, including setup, routing, database integration, and overall architecture <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a> <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. The choice of framework can significantly impact a startup's growth <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## What a Web Framework Does <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>

Web frameworks typically perform three main functions:
*   **Database Abstraction**: They provide an abstraction layer over relational databases, often featuring a built-in Object Relational Mapper (ORM) that can migrate code from a preferred programming language into SQL <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
*   **Routing**: They offer routing capabilities to map URLs in the browser to specific code that runs on the server <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
*   **Dynamic Data Insertion**: They provide a mechanism to dynamically insert data from the database directly into HTML for the user interface <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

These three elements commonly form the Model-View-Controller (MVC) architecture, a prevalent approach for building full stack web applications <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

## Framework Deep Dive

### Ruby on Rails (Ruby)
Ruby on Rails is known for simplifying web development compared to earlier approaches and has been used to build major companies like Shopify, Airbnb, and GitHub <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. It remains popular and adopts an HTML-centric approach with libraries like Hotwire, Stimulus, and Turbo, contrasting with front-end [[differences_and_similarities_among_frameworks_like_react_angular_and_vue | frameworks like React, Angular, and Vue]] <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

*   **Pros**:
    *   **Powerful CLI**: The Rails CLI can serve the application and automatically generate a significant amount of code, including using `scaffold` for basic CRUD features <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
    *   **Batteries-Included**: It manages the relational database, testing, logging, and other aspects, providing a comprehensive solution <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
    *   **Opinionated**: Rails' opinionated nature allows for achieving much functionality with minimal code <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
    *   **Clear Separation of Concerns**: It provides a good separation of concerns with distinct folders for models, views, and controllers within the `app` directory <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a> <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.
    *   **Active Record ORM**: Data is managed with the Active Record ORM <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
*   **Cons**:
    *   **Initial Setup Issues**: Initial setup can be error-prone <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
    *   **Overwhelming at First**: The extensive folder structure can seem overwhelming initially <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
    *   **"Magic"**: Its automated code generation can be seen as "too much magic" by some <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
    *   **Language Popularity**: Ruby is not the most popular language globally <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.

### Django (Python)
Django is a highly popular Python-based framework used for large sites like Spotify and Bitbucket <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

*   **Pros**:
    *   **Less Overwhelming File Structure**: The initial file structure is less overwhelming than Rails <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
    *   **Batteries-Included**: Still a comprehensive "batteries-included" framework <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
    *   **Explicit Code**: Code tends to be more explicit, with a `manage.py` file for CLI commands <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
    *   **Built-in Admin Feature**: A powerful built-in admin feature allows easy management of data directly in the browser <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.
    *   **ORM**: Models are Python classes representing data structure in SQL, acting as the ORM <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
    *   **Python Templating**: HTML templates allow direct embedding of Python <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

### Laravel (PHP)
Laravel is a popular PHP framework for web artisans <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

*   **Pros**:
    *   **Extensive Batteries-Included**: Even more comprehensive than Rails, handling web routes, API routes, and real-time communication with WebSockets <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.
    *   **Pre-configured Features**: Initial projects come configured with features like user authentication via providers <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
    *   **Eloquent ORM**: Uses Eloquent ORM, based on the Active Record pattern similar to Rails <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
    *   **Blade Templates**: Builds on PHP's native HTML integration with Blade templates for easier views <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.
    *   **Front-end Integration**: Thoughtful integration with front-end [[differences_and_similarities_among_frameworks_like_react_angular_and_vue | frameworks like React and Vue]] via tools like Inertia <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
*   **Cons**:
    *   **Long Initial Setup**: Initial app generation can take a long time and download many packages <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

### Next.js (JavaScript)
Next.js allows building full stack applications entirely with JavaScript <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. It's one of many options in the JavaScript world <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.

*   **Pros**:
    *   **Minimal Framework**: Starts as a very good minimal framework, allowing users to add desired database integrations (e.g., Prisma) <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
    *   **File System Routing**: Routing is handled conveniently with the file system, where each file in the `Pages` directory defines a URL <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
    *   **Integrated React**: Exports React components for UI/views, streamlining productivity by integrating a front-end framework fundamentally <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
    *   **Server-Side Code Execution**: Allows running server-side code (e.g., `getServerSideProps` with Node.js) for data fetching, tightly coupling server and client-side code effectively <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.
    *   **Simplifies Web Development Annoyances**: Handles many background tasks to simplify challenging aspects of web development <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.
*   **Cons**:
    *   **No Built-in Database Integration**: Does not provide out-of-the-box integration for databases, requiring external solutions like Prisma <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.

### Spring (Java)
The Spring Framework makes Java development enjoyable, despite Java being a "boilerplate driven language" <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>.

*   **Pros**:
    *   **Customizable Setup**: Features a generator that allows users to choose their framework and add various dependencies, including support for Kotlin or Groovy <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.
    *   **Robust Code**: Feels more robust compared to dynamic languages <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.
    *   **Metaprogramming**: Relies on metaprogramming to keep code simple <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.
    *   **MVC Pattern**: Follows the MVC pattern with controllers as classes and routes defined by decorators <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
    *   **Java Persistence API**: Database models are based on code using the Java Persistence API <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
*   **Cons**:
    *   **TimeLeaf templating**: The TimeLeaf templating engine was not found to be very user-friendly <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.

### .NET / ASP.NET (C#)
ASP.NET is an open-source project maintained by Microsoft, known for its popularity and reliability <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.

*   **Pros**:
    *   **Well-Evolved**: Has evolved nicely over the years with modern supporting libraries like Blazor for client-side apps with Web Assembly and C# <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.
    *   **Clear Project Structure**: The initial project structure is well-organized and not overwhelming <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>.
    *   **Awesome Tooling & Static Typing**: Offers excellent tooling and static typing similar to Java <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.
    *   **Inferred Routing**: URLs are inferred from class names in controllers, with methods representing URL segments and supporting dynamic URLs <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>.
    *   **Entity Framework Core ORM**: Models are managed by the Entity Framework Core ORM <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.
    *   **CSHTML Views**: Views are written in CSHTML, providing full IntelliSense <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.
*   **Cons**:
    *   **Microsoft Association**: "You have to sell your soul to the big giant Tech Corporation" <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.

### Phoenix (Elixir)
Phoenix is an excellent framework based on the Elixir functional programming language <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.

*   **Pros**:
    *   **Powerful CLI**: Similar to Ruby on Rails, it has a powerful CLI capable of scaffolding an entire CRUD application <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.
    *   **Rails-like Routing**: Routing is similar to Rails, mapping CRUD URLs to controllers <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
    *   **Ecto ORM**: Uses an ORM called Ecto <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.
    *   **Embedded Elixir Templates**: Templates use embedded Elixir, similar to Rails <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.
    *   **High Performance**: Elixir is a compiled language, giving Phoenix a significant performance advantage <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.
    *   **Live Dashboard**: Every app includes a built-in live dashboard for performance monitoring <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.
*   **Cons**:
    *   **Functional Language**: Elixir's functional nature feels different from common object-oriented languages <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.

### Gin (Go)
Gin is a high-performance framework powered by the Go language <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>.

*   **Pros**:
    *   **Minimal HTTP Framework**: Focuses on HTTP and is not concerned with MVC, allowing for more low-level control <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.
    *   **Flexible Structure**: No need to follow strict MVC conventions, enabling highly focused functions tailored to business needs <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>.
    *   **Smaller Codebase**: Results in a smaller codebase with more granular control <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>.
    *   **GORM ORM**: Can integrate with an ORM like GORM for database management <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.
    *   **Built-in Templating**: Go has its own built-in templating language for views <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.
*   **Cons**:
    *   **No CLI**: Does not use a fancy CLI; projects are created from scratch <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.
    *   **No Built-in ORM**: Does not contain an ORM by default <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.
    *   **Complexity with Growth**: Can become harder to manage as the application scales without explicit conventions <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>.
    *   **Requires More Knowledge**: Users need to understand more about structuring applications themselves <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.

### Rocket (Rust)
Rocket is a web framework for Rust, a systems language <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>.

*   **Pros**:
    *   **Potential for Performance**: As a Rust-based framework, it offers low-level control over memory <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.
    *   **Component-based UI with Yew**: The Rust ecosystem includes component-based frameworks like Yew for web apps with WebAssembly <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.
*   **Cons**:
    *   **No Full MVC Framework**: The Rust ecosystem currently lacks a full-blown MVC framework similar to Rails <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.
    *   **Difficult to Build Basic Apps**: Building a basic application can be very difficult <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.
    *   **Low-Level Control**: Rust provides low-level control over memory, which is often not needed by average web application developers <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.
    *   **Time-Consuming**: Requires significant time and dedication to develop with <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>.

### Vapor (Swift)
Vapor is a framework based on the Swift programming language <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.

*   **Pros**:
    *   **Well-Organized Structure**: Provides a well-organized project structure with clear controllers, models, and routes <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>.
    *   **Enjoyable Language**: Swift is a well-designed language that is enjoyable to work with <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.
    *   **Concise, Readable, Statically Typed**: Code is concise, readable, and statically typed with excellent tooling similar to Java or C# <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>.
    *   **Async/Await Embrace**: Embraces async/await for data fetching from models <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>.
    *   **Fluent ORM**: Uses an ORM called Fluent, which models data with classes and decorators <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.
    *   **Modern Templating**: Has a modern and practical templating engine called Leaf <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>.
*   **Cons**:
    *   **Mac Dependency**: Building apps with Swift works better on a Mac <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.

### Ktor (Kotlin)
Ktor is a Kotlin-based web application framework <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.

*   **Pros**:
    *   **Minimal**: It is a more minimal option compared to Spring <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>.

## Conclusion

After reviewing multiple full stack frameworks, the "greatest of all time" is ultimately revealed to be **Ruby on Rails** <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a> <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>. It is considered "by far the best framework" and is likened to "the magic Jordan of web Frameworks" <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>.

For more information on [[comparison_of_10_web_frameworks | web framework comparisons]], [[tradeoffs_of_javascript_frameworks | tradeoffs of JavaScript frameworks]], [[comparison_of_popular_javascript_frameworks_in_2021 | popular JavaScript frameworks in 2021]], [[choosing_the_best_javascript_framework | choosing the best JavaScript framework]], [[comparison_with_other_javascript_frameworks | comparisons with other JavaScript frameworks]], [[differences_and_similarities_among_frameworks_like_react_angular_and_vue | differences and similarities among frameworks like React, Angular, and Vue]], [[introduction_to_tech_stacks | introduction to tech stacks]], [[building_a_todo_app_with_different_javascript_frameworks | building a todo app with different JavaScript frameworks]], and [[javascript_frameworks_and_their_updates | JavaScript frameworks and their updates]], see the related articles.