---
title: Framework features like routing and database integration
videoId: FQPlEnKav48
---

From: [[fireship]] <br/> 

Web applications, at their core, handle requests from users, process data, and present information back to them <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Web frameworks are essential tools that streamline this process by providing abstractions and structures for common tasks. This article focuses on two key features that nearly all web frameworks provide: routing and database integration.

## [[Core Features and Capabilities | Core Features and Capabilities]] of a Web Framework

A web framework primarily focuses on three main functionalities <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>:

1.  **Database Abstraction (ORM)**: Frameworks typically provide an abstraction layer over relational databases. This often comes in the form of an Object-Relational Mapper (ORM), which translates code from a preferred programming language into SQL code for database interaction <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
2.  **Routing**: They provide mechanisms to map a URL from a browser to specific code that needs to be executed on the server <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
3.  **Dynamic Data Insertion (Templating)**: Frameworks offer ways to dynamically insert data, often retrieved from a database, directly into HTML for the user interface <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

These three elements together commonly form the Model-View-Controller (MVC) architecture, a prevalent approach for building full-stack web applications <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

## Framework-Specific Implementations

Different frameworks implement these core features in various ways, influencing the overall developer experience and the specific architectural patterns they encourage.

### [[Web development with Ruby on Rails | Ruby on Rails]]

Rails is known for simplifying web development <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a> and is a "batteries included" framework, handling relational databases, testing, logging, and more <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

*   **Routing**: Defined in the `routes.rb` file, where URLs are mapped to actions within a controller <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. The `resources` keyword can automatically generate all necessary routes for basic CRUD (Create, Read, Update, Delete) features <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
*   **Database Integration**: Manages data with `Active Record`, its built-in ORM <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. Models contain the logic for data, and migrations are used to sync the code with the actual database <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
*   **Views**: Uses `html.erb` files (Embedded Ruby) to dynamically render data inside HTML <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

Rails is highly opinionated, allowing significant functionality with minimal code through features like scaffolding <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

### Django

Django is another popular "batteries included" framework, known for its use in large sites like Spotify <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. It follows the MVC architecture and offers more explicit code than Rails <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

*   **Routing**: Routes are defined in the `urls.py` file <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
*   **Database Integration**: Models are Python classes that represent the structure of data in an SQL database, acting as the ORM <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
*   **Views**: Uses HTML templates that allow embedding Python directly into the code <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
*   **Unique Feature**: Django includes a powerful built-in admin feature that allows easy management of data in the browser after defining models <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.

### Laravel

Laravel, a PHP framework, is also a "batteries included" solution <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

*   **Routing**: Handles not only web routes but also API routes and channels for real-time communication via WebSockets <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
*   **Database Integration**: Its database models use `Eloquent ORM`, which is based on the same Active Record pattern as Rails <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
*   **Views**: Builds on PHP's native ability to work with HTML using `Blade templates` <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.
*   **Front-End Integration**: Laravel has considered integration with [[building_interactive_websites_with_spalike_features | front-end frameworks]] like React and Vue, offering tools like Inertia to bridge the gap between front-end and back-end <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

### Next.js

Next.js allows [[Front End and Back End Development | full-stack applications]] to be built entirely with JavaScript <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

*   **Database Integration**: It does not provide built-in database integration, allowing developers to choose external solutions like Prisma <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.
*   **Routing**: Handled by the file system; each file in the `Pages` directory defines a different URL <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. Dynamic routes are created by wrapping the file name in brackets <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
*   **Views**: Each file exports a React component for the UI (view) <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
*   **Data Fetching**: Supports server-side code execution with functions like `getServerSideProps`, enabling data fetching (e.g., using Prisma) on the server and delivering it as props to React components <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.

### Spring Framework

Spring is a Java-based framework that emphasizes a modular approach <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.

*   **Routing**: Routes are defined using decorators on controller methods <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
*   **Database Integration**: Database models are based on code using the Java Persistence API <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
*   **Views**: Uses `TimeLeaf` templates, where attributes are added to HTML to define data placement <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.

### .NET Framework (ASP.NET)

ASP.NET is an open-source framework maintained by Microsoft, known for its reliability and modern supporting libraries like Blazor <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.

*   **Routing**: URLs are inferred from class names in controllers, and methods within those classes represent subsequent URL segments <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>. Dynamic URLs can be created by taking arguments in methods <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.
*   **Database Integration**: Data models are managed by an ORM called `The Entity Core Framework` <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.
*   **Views**: Written in `CSHTML`, which allows accessing data models and declaring additional C# data within the template <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.

### Phoenix

Phoenix is based on the Elixir programming language, a functional language that offers high performance <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.

*   **Routing**: Very similar to Ruby on Rails, using `sources` to map CRUD URLs to controllers <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
*   **Database Integration**: Uses an ORM called `Ecto` <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.
*   **Views**: Templates use `embedded Elixir`, similar to Rails <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.
*   **Performance**: Phoenix is known for its performance due to Elixir being a compiled language, and every app includes a built-in live dashboard for performance monitoring <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.

### Gin

Gin is a minimal HTTP framework powered by the Go language <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>. It does not enforce the MVC architecture <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.

*   **Database Integration**: It does not contain a built-in ORM; external packages like `Gorm` are used <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.
*   **Routing**: The framework focuses on very focused functions rather than strict MVC conventions <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>.
*   **Views**: Go has its own built-in templating language to interpolate values retrieved from the database <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.

Gin offers a smaller codebase and more low-level control, but requires more developer expertise as the application grows <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>.

### Rocket

Rocket is a web framework for Rust, a systems language <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>. The Rust ecosystem does not have a full-blown MVC framework like Rails <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>.

*   **Routing**: Rocket is used for HTTP and routing <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.
*   **Database Integration**: Requires combining with a Rust-based ORM like `Diesel` <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>.
*   **Views**: Uses templating languages like `Askama` to integrate data into HTML <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>.

Building with Rust can be challenging for typical web application development due to its low-level memory control <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>.

### Vapor

Vapor is a web framework based on the Swift programming language <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>. It offers a well-organized project structure with clear separation of controllers, models, and routes <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>.

*   **Routing**: Routes point to methods in the controller <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>.
*   **Database Integration**: Uses an ORM called `Fluent`, which models data using classes and decorators <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>. It embraces async/await for data fetching <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>.
*   **Views**: Features a templating engine called `Leaf`, described as modern and practical <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>.

Swift provides a statically typed language with good tooling, making it enjoyable to work with <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.

### Ktor

Ktor is a Kotlin-based web application framework, noted as a more minimal alternative to Spring <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.

---

The choice of framework significantly impacts a startup's trajectory for the next decade <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. While the "best" framework is debatable, some, like Ruby on Rails, are considered highly effective due to their "magic" and opinionated nature <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>. Ultimately, the developer's skill and understanding are paramount, as "without you, the framework would be nothing" <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.