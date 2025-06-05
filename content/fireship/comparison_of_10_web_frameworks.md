---
title: Comparison of 10 web frameworks
videoId: FQPlEnKav48
---

From: [[fireship]] <br/> 

This article explores various web frameworks by detailing the experience of building the same application across ten different options, using distinct programming languages for each <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. The aim was to determine which [[pros_and_cons_of_different_full_stack_frameworks | full-stack framework]] is the most effective <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. The frameworks examined include: Rails, Django, Laravel, Spring, .NET, Next.js, Phoenix, Rocket, Gin, Vapor, and Ktor <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. The evaluation considered overall developer experience, setup, routing, database integration, and architecture <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

## What a Web Framework Does

A web framework primarily handles three core functions <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>:

*   **Database Abstraction**: Provides an abstraction over relational databases, often featuring a built-in Object-Relational Mapper (ORM) to migrate code from the programming language into SQL <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
*   **Routing**: Maps URLs in the browser to specific server-side code to be executed <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
*   **Dynamic HTML**: Offers a method to dynamically insert data from the database directly into HTML for the user interface (UI) <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

These three elements collectively form the Model-View-Controller (MVC) architecture, which is the most common approach for [[pros_and_cons_of_different_full_stack_frameworks | building full-stack web applications]] <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

## Framework Deep Dive

### Ruby on Rails

*   **Overview**: Built with Ruby, Rails was revolutionary for simplifying web development <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. It remains popular in 2022 and is known for its HTML-centric approach, contrasting with front-end [[differences_and_similarities_among_frameworks_like_react_angular_and_vue | frameworks like React, Angular, and Vue]] <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **Famous For**: Powering companies such as Shopify, Airbnb, and GitHub <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
*   **Setup**: Requires Ruby and the Rails Gem <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. Initial setup on Debian Linux encountered some solvable errors <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   **CLI**: Extremely powerful, capable of serving the application and generating significant code automatically with commands like `scaffold` <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
*   **Architecture**: A "batteries-included" framework handling relational databases, testing, and logging <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. Main application code is in the `app` directory, following an MVC pattern with models, views, and controllers <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
*   **Routing**: Defined in `routes.rb`, mapping URLs to controller actions <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. `resources` command automatically creates CRUD routes <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
*   **Database**: Managed by Active Record, an Object-Relational Mapper (ORM) <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. Models are synced with the database via migrations <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
*   **Views**: `html.erb` files (embedded Ruby) allow dynamic data rendering within HTML <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
*   **Pros**: Provides a good separation of concerns and is very opinionated, enabling significant functionality with minimal code <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. The `scaffold` feature generates UI for data management <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
*   **Cons**: Can be seen as "too much magic" by some, and Ruby is not the most popular language globally <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.

### Django

*   **Overview**: A Python-based framework, also extremely popular <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
*   **Famous For**: Used to build large sites like Spotify and Bitbucket <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
*   **Architecture**: Less overwhelming file structure than Rails but still a "batteries-included" framework <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. Code tends to be more explicit <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. Follows the MVC architecture <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
*   **CLI**: The `manage.py` file contains the command-line interface for serving the app or generating new features <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **Routing**: Defined in `urls.py` <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
*   **Controllers**: Represented by Python functions in `views.py` <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
*   **Database**: Models are Python classes representing SQL database data, functioning as the ORM <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
*   **Views**: HTML templates allow embedding Python code directly <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
*   **Notable Feature**: Includes a built-in admin feature to easily manage data in the browser <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.

### Laravel

*   **Overview**: The most popular PHP framework <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. PHP is the original server-side language of the web <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
*   **Setup**: Requires PHP and Composer <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. Initial app generation takes time and downloads many packages <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
*   **Architecture**: Even more "batteries-included" than Rails <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>. Includes user authentication via "providers" (shared services) <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
*   **Routing**: Handles web routes, API routes, and real-time communication channels (WebSockets) <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
*   **Controllers**: Found in the `HTTP` directory, containing methods to access data and render templates <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
*   **Database**: Uses Eloquent ORM, based on the same Active Record pattern as Rails <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.
*   **Views**: Leverages Blade templates, building on PHP's native integration with HTML <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.
*   **Ecosystem**: Offers adjacent tools like Inertia to bridge the gap between front-end [[javascript_trends_and_frameworks | frameworks like React and Vue]] and the backend <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

### Next.js

*   **Overview**: Allows [[building_a_todo_app_with_different_javascript_frameworks | full-stack application development]] entirely with JavaScript <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   **Setup**: Uses `npx create next app` to generate a starter project <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.
*   **Database**: Does not provide built-in database integration; Prisma is a popular choice to add manually <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. This minimal approach is favored in the JavaScript ecosystem <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   **Architecture**: Considered a minimal framework that simplifies complex web development aspects behind the scenes <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.
*   **Routing**: Handled by the file system, where each file in the `Pages` directory defines a URL <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. Dynamic routes are created by wrapping file names in brackets <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   **Views**: Each file exports a React component for the UI <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. Fundamental integration with React streamlines productivity <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.
*   **Data Fetching**: Supports server-side code execution with functions like `getServerSideProps` (running on Node.js) to fetch data (e.g., with Prisma) and deliver it as props to React components <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. Server-side and client-side code are tightly coupled <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

### Spring

*   **Overview**: A Java framework that makes working with Java enjoyable, despite its boilerplate nature <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.
*   **Setup**: Offers a generator for a "create your own adventure" experience, allowing choice of language (Java, Kotlin, Groovy) and dependencies <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.
*   **Code Quality**: Code often feels more robust compared to dynamic languages <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.
*   **Architecture**: Follows the MVC pattern <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.
*   **Controllers**: Are classes where routes are defined using decorators on methods <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.
*   **Database**: Models are based on code using the Java Persistence API <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.
*   **Views**: Utilizes TimeLeaf templates, where attributes are added to HTML to define data insertion <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>. The presenter found TimeLeaf not very enjoyable to use <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.

### ASP.NET (.NET Framework)

*   **Overview**: An open-source framework maintained by Microsoft, known for being popular and reliable <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. It has evolved well, with modern supporting libraries like Blazer for client-side apps using WebAssembly and C# <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.
*   **Setup**: Install the .NET SDK and generate a new MVC application <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.
*   **Architecture**: Clear and not overwhelming initial project structure <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>. Offers excellent tooling and static typing <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
*   **Routing**: URLs are inferred from class names in controllers (e.g., `AnimalController` creates `/animals` URL) <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>. Methods within the class represent subsequent URL segments, and arguments can create dynamic URLs <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.
*   **Database**: Models are managed by the Entity Core framework ORM <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.
*   **Views**: Written in C# HTML (CSHTML) <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>. Allows accessing model data and declaring additional C# data within the view <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.
*   **Pros**: More verbose than other templating languages but offers full Intellisense <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>, which is very helpful <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.
*   **Cons**: Requires commitment to the Microsoft ecosystem <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.

### Phoenix

*   **Overview**: Built with Elixir, a functional language <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.
*   **Setup**: Has a powerful CLI similar to Ruby on Rails that can scaffold a full CRUD application <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
*   **Routing**: Similar to Rails, using `resources` to map necessary CRUD URLs to the controller <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.
*   **Controllers**: Functions namespaced under a module access data and render templates <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.
*   **Database**: Uses Ecto, an Object-Relational Mapper <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.
*   **Views**: Utilizes embedded Elixir, also similar to Rails <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>.
*   **Pros**: Offers a significant performance advantage because Elixir is a compiled language <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>. Includes a built-in live dashboard for performance monitoring <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.

### Gin

*   **Overview**: A high-performance HTTP framework based on the Go language <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>.
*   **Setup**: No fancy CLI; a Go project is created from scratch <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.
*   **Architecture**: Minimal HTTP framework that is not concerned with the MVC architecture <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. Developers must handle architectural decisions themselves <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>.
*   **Database**: Does not include an ORM; requires external packages like GORM <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.
*   **Pros**: Allows for a more focused code base tailored to specific business needs, potentially leading to a smaller code base with more low-level control <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.
*   **Views**: Uses Go's built-in templating language to interpolate values retrieved from the database <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.
*   **Cons**: As applications grow, managing complexity without a framework's conventions can become challenging, requiring experienced developers <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>.

### Rocket

*   **Overview**: A web framework based on the Rust programming language <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>.
*   **Architecture**: The Rust ecosystem does not have a full-blown MVC framework like Rails <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.
*   **Setup Difficulty**: Building a basic application proved very difficult <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.
*   **Approach**: The intended approach was to combine Rocket for HTTP and routing with Diesel (a Rust-based ORM) and the Askama templating language for HTML <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>.
*   **Outcome**: A full working demo could not be achieved with Rust <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
*   **Language Considerations**: Rust is a systems language offering low-level memory control, which is often unnecessary for typical web application developers <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>.

### Vapor

*   **Overview**: A framework based on the Swift programming language <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>. This app was built on a Mac, as Swift development tends to work better on that platform <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.
*   **Architecture**: Provides a well-organized project structure with clear controllers, models, and routes <a class="yt-timestamp" data-t="00:13:19">[00:13:19]</a>.
*   **Routing**: Routes point to controller methods that access data from models <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>.
*   **Database**: Uses Fluent, an ORM that models data using classes with decorators <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.
*   **Language Experience**: Swift is a well-designed language, enjoyable to work with <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>. Code is concise, readable, statically typed, and benefits from excellent tooling similar to Java or C# <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>. It embraces async/await for data fetching <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>.
*   **Views**: Features an engine called Leaf, which felt modern and practical <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>.

### Ktor

*   **Overview**: A Kotlin-based web application framework <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>. It is more minimal than frameworks like Spring <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>.

## Conclusion: The "Greatest of All Time"

While the journey explored a diverse range of [[comparison_of_popular_javascript_frameworks_in_2021 | JavaScript frameworks]] and others, the conclusion is that Ruby on Rails is "by far the best framework" <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>.