---
title: Building web apps with various programming languages
videoId: FQPlEnKav48
---

From: [[fireship]] <br/> 

Developing web applications involves using a variety of frameworks and programming languages. This exploration delves into the experience of building the same application multiple times across different technology stacks to identify strengths and weaknesses <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## What Web Frameworks Do

Web frameworks primarily perform three key functions <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>:
1.  **Database Abstraction**: They provide an abstraction layer over relational databases, often featuring a built-in Object Relational Mapper (ORM) that translates code from the programming language into SQL for database interaction <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
2.  **Routing**: Frameworks handle routing, mapping browser URLs to specific server-side code to be executed <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
3.  **Dynamic HTML**: They offer mechanisms to dynamically insert data from the database directly into HTML for the user interface <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

These three elements commonly form the Model-View-Controller (MVC) architecture, a prevalent approach for building full-stack web applications <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

## Framework Comparison

### Ruby on Rails
[[web_development_with_ruby_on_rails | Ruby on Rails]], built with Ruby, is known for simplifying web development and is used by major companies like Shopify, Airbnb, and GitHub <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. It remains popular in 2022 and takes an HTML-centric approach with libraries like Hotwire, Stimulus, and Turbo, contrasting with front-end frameworks like React, Angular, and Vue <a class="yt-timestamp" data-t="00:01:51">[00:02:06]</a>.

*   **Setup**: Requires Ruby and the Rails Gem. Initial setup on Debian Linux can be error-prone, but issues are typically solvable with a Google search <a class="yt-timestamp" data-t="00:02:06">[00:02:22]</a>.
*   **CLI**: The `rails` CLI is powerful, serving applications and generating code automatically with commands like `scaffold` <a class="yt-timestamp" data-t="00:02:24">[00:02:33]</a>.
*   **Architecture**: It's a "batteries included" framework, handling databases, testing, and logging <a class="yt-timestamp" data-t="00:02:37">[00:02:43]</a>. Main application code resides in the `app` directory, containing models, views, and controllers <a class="yt-timestamp" data-t="00:02:46">[00:02:50]</a>.
*   **Routing**: Defined in `routes.rb`, mapping URLs to controller actions. `resources` automatically create routes for basic CRUD features <a class="yt-timestamp" data-t="00:02:52">[00:03:01]</a>.
*   **Models**: Data logic is in models. Migrations sync model code with the database. Active Record serves as the Object Relational Mapper (ORM) <a class="yt-timestamp" data-t="00:03:13">[00:03:28]</a>.
*   **Views**: `html.erb` files (embedded Ruby) dynamically render data into HTML <a class="yt-timestamp" data-t="00:03:30">[00:03:37]</a>.
*   **Pros**: Strong separation of concerns, opinionated design allows significant functionality with minimal code, `scaffold` generates UI for data management <a class="yt-timestamp" data-t="00:03:39">[00:03:51]</a>.
*   **Cons**: The "magic" can be a drawback for some; Ruby is not the most popular language <a class="yt-timestamp" data-t="00:03:52">[00:03:57]</a>.

### Django
Django is a highly popular Python framework used by sites like Spotify and Bitbucket <a class="yt-timestamp" data-t="00:04:03">[00:04:08]</a>.

*   **Architecture**: Less overwhelming file structure than Rails but still "batteries included" <a class="yt-timestamp" data-t="00:04:09">[00:04:15]</a>. Code tends to be more explicit <a class="yt-timestamp" data-t="00:04:17">[00:04:19]</a>.
*   **CLI**: `manage.py` file provides CLI functionality for serving the app or generating new features <a class="yt-timestamp" data-t="00:04:21">[00:04:30]</a>.
*   **MVC**: Follows the MVC architecture. Routes are defined in `urls.py`, and controllers are Python functions in `views.py` <a class="yt-timestamp" data-t="00:04:32">[00:04:39]</a>.
*   **Models**: Python classes represent SQL database data, serving as the ORM <a class="yt-timestamp" data-t="00:04:44">[00:04:52]</a>.
*   **Templates**: HTML templates allow embedding Python directly <a class="yt-timestamp" data-t="00:04:53">[00:04:57]</a>.
*   **Superpower**: Built-in admin feature allows easy management of application data in the browser by registering models with the admin app <a class="yt-timestamp" data-t="00:04:59">[00:05:12]</a>.

### Laravel
Laravel is the most popular PHP framework, known for web artisans <a class="yt-timestamp" data-t="00:05:21">[00:05:25]</a>.

*   **Setup**: Requires PHP and Composer. Initial app generation can take time and download many packages <a class="yt-timestamp" data-t="00:05:26">[00:05:34]</a>.
*   **Architecture**: Very "batteries included," even more so than Rails <a class="yt-timestamp" data-t="00:05:34">[00:05:37]</a>.
*   **Routing**: Handles web routes, API routes, and real-time communication channels via WebSockets <a class="yt-timestamp" data-t="00:05:37">[00:05:45]</a>.
*   **Controllers**: Located in the `HTTP` directory, controllers are classes with methods that access data and render templates <a class="yt-timestamp" data-t="00:05:56">[00:06:04]</a>.
*   **Models**: Database models use Eloquent ORM, based on the Active Record pattern like Rails <a class="yt-timestamp" data-t="00:06:05">[00:06:10]</a>.
*   **Views**: Leverages Blade templates built on PHP to easily work with HTML <a class="yt-timestamp" data-t="00:06:11">[00:06:18]</a>.
*   **Ecosystem**: Integrates front-end frameworks like React and Vue well, with tools like Inertia bridging the gap between front-end and back-end <a class="yt-timestamp" data-t="00:06:21">[00:06:30]</a>.

### Next.js
Next.js allows building full-stack applications entirely with JavaScript <a class="yt-timestamp" data-t="00:06:31">[00:06:37]</a>.

*   **Setup**: Uses `npx create next app` for project generation <a class="yt-timestamp" data-t="00:06:48">[00:06:51]</a>.
*   **Database**: Does not provide built-in database integration; solutions like Prisma can be added <a class="yt-timestamp" data-t="00:06:53">[00:07:02]</a>. This modularity is considered a positive in the JavaScript ecosystem <a class="yt-timestamp" data-t="00:07:04">[00:07:13]</a>.
*   **Routing**: Handled by the file system; each file in the `Pages` directory defines a URL <a class="yt-timestamp" data-t="00:07:17">[00:07:25]</a>. Dynamic routes are created by wrapping file names in brackets <a class="yt-timestamp" data-t="00:07:26">[00:07:28]</a>.
*   **Views**: Files export React components for UI definition <a class="yt-timestamp" data-t="00:07:29">[00:07:32]</a>. Having React fundamentally integrated streamlines productivity <a class="yt-timestamp" data-t="00:07:38">[00:07:42]</a>.
*   **Data Fetching**: Supports server-side code execution with functions like `getServerSideProps` to fetch data (e.g., with Prisma) and deliver it as props to React components <a class="yt-timestamp" data-t="00:07:44">[00:08:05]</a>.
*   **Pros**: Minimal framework that simplifies complex parts of web development, client and server-side code are tightly coupled which works well in practice <a class="yt-timestamp" data-t="00:08:05">[00:08:21]</a>.

### Spring
The Spring framework, built with Java, aims to make Java web development enjoyable despite its boilerplate nature <a class="yt-timestamp" data-t="00:08:22">[00:08:30]</a>.

*   **Setup**: Features a generator for project creation, supporting Kotlin or Groovy, and allows choosing various dependencies <a class="yt-timestamp" data-t="00:08:32">[00:08:43]</a>.
*   **Code Quality**: Although verbose, the code "writes itself" and feels more robust than dynamic languages <a class="yt-timestamp" data-t="00:08:45">[00:08:52]</a>.
*   **MVC**: Follows the MVC pattern.## Building Web Apps with Various Programming Languages

Developing web applications involves using a variety of frameworks and programming languages. This exploration delves into the experience of building the same application multiple times across different technology stacks to identify strengths and weaknesses <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

### What Web Frameworks Do

Web frameworks primarily perform three key functions <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>:
1.  **Database Abstraction**: They provide an abstraction layer over relational databases, often featuring a built-in Object Relational Mapper (ORM) that translates code from the programming language into SQL for database interaction <a class="yt-timestamp" data-t="00:01:07">[00:01:18]</a>.
2.  **Routing**: Frameworks handle routing, mapping browser URLs to specific server-side code to be executed <a class="yt-timestamp" data-t="00:01:18">[00:01:25]</a>.
3.  **Dynamic HTML**: They offer mechanisms to dynamically insert data from the database directly into HTML for the user interface <a class="yt-timestamp" data-t="00:01:25">[00:01:31]</a>.

These three elements commonly form the Model-View-Controller (MVC) architecture, a prevalent approach for building a full-stack web app <a class="yt-timestamp" data-t="00:01:31">[00:01:39]</a>.

### Framework Comparison

#### Ruby on Rails
[[web_development_with_ruby_on_rails | Ruby on Rails]], built with Ruby, is known for simplifying web development and is used by major companies like Shopify, Airbnb, and GitHub <a class="yt-timestamp" data-t="00:01:40">[00:01:46]</a>. It remains popular in 2022 and takes an HTML-centric approach with libraries like Hotwire, Stimulus, and Turbo, contrasting with front-end frameworks like React, Angular, and View <a class="yt-timestamp" data-t="00:01:51">[00:02:06]</a>.

*   **Setup**: Requires Ruby and the Rails Gem. Initial setup on Debian Linux can be error-prone, but issues are typically solvable with a Google search <a class="yt-timestamp" data-t="00:02:06">[00:02:22]</a>.
*   **CLI**: The `rails` CLI is powerful, serving applications and generating code automatically with commands like `scaffold` <a class="yt-timestamp" data-t="00:02:24">[00:02:33]</a>.
*   **Architecture**: It's a "batteries included" framework, handling relational databases, testing, and logging <a class="yt-timestamp" data-t="00:02:37">[00:02:43]</a>. Main application code resides in the `app` directory, containing models, views, and controllers <a class="yt-timestamp" data-t="00:02:46">[00:02:50]</a>.
*   **Routing**: Defined in `routes.rb`, mapping URLs to controller actions. `resources` automatically create routes for basic CRUD features <a class="yt-timestamp" data-t="00:02:52">[00:03:01]</a>.
*   **Models**: Data logic is in models. Migrations sync model code with the database. Active Record serves as the Object Relational Mapper (ORM) <a class="yt-timestamp" data-t="00:03:13">[00:03:28]</a>.
*   **Views**: `html.erb` files (embedded Ruby) dynamically render data into HTML <a class="yt-timestamp" data-t="00:03:30">[00:03:37]</a>.
*   **Pros**: Strong separation of concerns, opinionated design allows significant functionality with minimal code, `scaffold` generates UI for data management <a class="yt-timestamp" data-t="00:03:39">[00:03:51]</a>.
*   **Cons**: The "magic" can be a drawback for some; Ruby is not the most popular language <a class="yt-timestamp" data-t="00:03:52">[00:03:57]</a>.

#### Django
Django is a highly popular Python framework used by sites like Spotify and Bitbucket <a class="yt-timestamp" data-t="00:04:03">[00:04:08]</a>.

*   **Architecture**: Less overwhelming file structure than Rails but still "batteries included" <a class="yt-timestamp" data-t="00:04:09">[00:04:15]</a>. Code tends to be more explicit <a class="yt-timestamp" data-t="00:04:17">[00:04:19]</a>.
*   **CLI**: `manage.py` file provides CLI functionality for serving the app or generating new features <a class="yt-timestamp" data-t="00:04:21">[00:04:30]</a>.
*   **MVC**: Follows the MVC architecture. Routes are defined in `urls.py`, and controllers are Python functions in `views.py` <a class="yt-timestamp" data-t="00:04:32">[00:04:39]</a>.
*   **Models**: Python classes represent SQL database data, serving as the ORM <a class="yt-timestamp" data-t="00:04:44">[00:04:52]</a>.
*   **Templates**: HTML templates allow embedding Python directly <a class="yt-timestamp" data-t="00:04:53">[00:04:57]</a>.
*   **Superpower**: Built-in admin feature allows easy management of application data in the browser by registering models with the admin app <a class="yt-timestamp" data-t="00:04:59">[00:05:12]</a>.

#### Laravel
Laravel is the most popular PHP framework, known for web artisans <a class="yt-timestamp" data-t="00:05:21">[00:05:25]</a>.

*   **Setup**: Requires PHP and Composer. Initial app generation can take time and download many packages <a class="yt-timestamp" data-t="00:05:26">[00:05:34]</a>.
*   **Architecture**: Very "batteries included," even more so than Rails <a class="yt-timestamp" data-t="00:05:34">[00:05:37]</a>.
*   **Routing**: Handles web routes, API routes, and real-time communication channels via WebSockets <a class="yt-timestamp" data-t="00:05:37">[00:05:45]</a>.
*   **Controllers**: Located in the `HTTP` directory, controllers are classes with methods that access data and render templates <a class="yt-timestamp" data-t="00:05:56">[00:06:04]</a>.
*   **Models**: Database models use Eloquent ORM, based on the Active Record pattern like Rails <a class="yt-timestamp" data-t="00:06:05">[00:06:10]</a>.
*   **Views**: Leverages Blade templates built on PHP to easily work with HTML <a class="yt-timestamp" data-t="00:06:11">[00:06:18]</a>.
*   **Ecosystem**: Integrates front-end frameworks like React and Vue well, with tools like Inertia bridging the gap between front-end and back-end <a class="yt-timestamp" data-t="00:06:21">[00:06:30]</a>.

#### Next.js
Next.js allows building a full-stack application entirely with JavaScript <a class="yt-timestamp" data-t="00:06:31">[00:06:37]</a>. Other JavaScript options include Express, Angular Universal, SvelteKit, NestJS, and Adonis <a class="yt-timestamp" data-t="00:06:40">[00:06:45]</a>.

*   **Setup**: Uses `npx create next app` for project generation <a class="yt-timestamp" data-t="00:06:48">[00:06:51]</a>.
*   **Database**: Does not provide built-in database integration; solutions like Prisma can be added <a class="yt-timestamp" data-t="00:06:53">[00:07:02]</a>. This modularity is considered a positive in the JavaScript ecosystem <a class="yt-timestamp" data-t="00:07:04">[00:07:13]</a>.
*   **Routing**: Handled by the file system; each file in the `Pages` directory defines a URL <a class="yt-timestamp" data-t="00:07:17">[00:07:25]</a>. Dynamic routes are created by wrapping file names in brackets <a class="yt-timestamp" data-t="00:07:26">[00:07:28]</a>.
*   **Views**: Files export React components for UI definition <a class="yt-timestamp" data-t="00:07:29">[00:07:32]</a>. Having React fundamentally integrated into the framework can streamline productivity <a class="yt-timestamp" data-t="00:07:38">[00:07:42]</a>.
*   **Data Fetching**: Supports server-side code execution with functions like `getServerSideProps` to fetch data (e.g., with Prisma) and deliver it as props to React components <a class="yt-timestamp" data-t="00:07:44">[00:08:05]</a>.
*   **Pros**: Minimal framework that simplifies complex parts of web development, client and server-side code are tightly coupled, which generally works very well <a class="yt-timestamp" data-t="00:08:05">[00:08:21]</a>.

#### Spring
The Spring framework, built with Java, aims to make Java web development enjoyable despite its boilerplate nature <a class="yt-timestamp" data-t="00:08:22">[00:08:30]</a>.

*   **Setup**: Features a generator for project creation, supporting Kotlin or Groovy, and allows choosing various dependencies <a class="yt-timestamp" data-t="00:08:32">[00:08:43]</a>.
*   **Code Quality**: Although verbose, the code "writes itself" and feels more robust compared to dynamic languages <a class="yt-timestamp" data-t="00:08:45">[00:08:52]</a>.
*   **MVC**: Follows the MVC pattern. Controllers are classes with routes defined using decorators on methods <a class="yt-timestamp" data-t="00:08:56">[00:09:02]</a>. Spring relies heavily on metaprogramming <a class="yt-timestamp" data-t="00:09:04">[00:09:06]</a>.
*   **Models**: Database models are based on code using the Java Persistence API <a class="yt-timestamp" data-t="00:09:10">[00:09:12]</a>.
*   **Views**: Data is used in templates via TimeLeaf, where attributes are added to HTML to define data placement <a class="yt-timestamp" data-t="00:09:14">[00:09:20]</a>.
*   **Cons**: TimeLeaf templating experience was not good <a class="yt-timestamp" data-t="00:09:20">[00:09:23]</a>.

#### ASP.NET
ASP.NET, based on C#, is an open-source project maintained by Microsoft, known for its popularity and reliability <a class="yt-timestamp" data-t="00:09:24">[00:09:34]</a>. It has evolved with modern libraries like Blazer for client-side apps using WebAssembly and C# <a class="yt-timestamp" data-t="00:09:34">[00:09:41]</a>.

*   **Setup**: Requires the .NET SDK to generate a new MVC application <a class="yt-timestamp" data-t="00:09:41">[00:09:46]</a>.
*   **Architecture**: Good initial project structure with clear naming, not too overwhelming, and benefits from static typing and tooling like Java <a class="yt-timestamp" data-t="00:09:47">[00:09:53]</a>.
*   **Routing**: URLs are inferred from class names in controllers, with methods representing URL segments and arguments for dynamic URLs <a class="yt-timestamp" data-t="00:09:54">[00:10:08]</a>.
*   **Models**: Data is represented by a model managed by Entity Framework Core ORM <a class="yt-timestamp" data-t="00:10:08">[00:10:12]</a>.
*   **Views**: Written in C# HTML (Razor), allowing access to model data and declaration of additional C# data within the file <a class="yt-timestamp" data-t="00:10:13">[00:10:22]</a>. It's more verbose but provides full IntelliSense <a class="yt-timestamp" data-t="00:10:24">[00:10:27]</a>.
*   **Pros**: Really impressive overall <a class="yt-timestamp" data-t="00:10:29">[00:10:30]</a>.
*   **Cons**: Requires allegiance to Microsoft <a class="yt-timestamp" data-t="00:10:31">[00:10:34]</a>.

#### Phoenix
Phoenix is an Elixir-based framework, a functional language that differs from most object-oriented languages <a class="yt-timestamp" data-t="00:10:36">[00:10:44]</a>.

*   **Setup**: After installation, a new project can be generated, similar to Ruby on Rails <a class="yt-timestamp" data-t="00:10:48">[00:10:51]</a>.
*   **CLI**: Very powerful, capable of automatically scaffolding an entire CRUD application <a class="yt-timestamp" data-t="00:10:51">[00:10:56]</a>.
*   **Routing**: Similar to Rails, with resources mapping necessary CRUD URLs to controllers <a class="yt-timestamp" data-t="00:10:57">[00:11:02]</a>.
*   **Controllers**: Functions namespaced under a module access data and render templates <a class="yt-timestamp" data-t="00:11:02">[00:11:07]</a>.
*   **Models**: Uses Ecto as its ORM <a class="yt-timestamp" data-t="00:11:07">[00:11:11]</a>.
*   **Templates**: Uses embedded Elixir, which feels very similar to Rails <a class="yt-timestamp" data-t="00:11:11">[00:11:14]</a>.
*   **Pros**: Huge advantage in performance because Elixir is a compiled language <a class="yt-timestamp" data-t="00:11:14">[00:11:18]</a>. Every app includes a built-in live dashboard for performance monitoring <a class="yt-timestamp" data-t="00:11:19">[00:11:22]</a>.

#### Gin
Gin is a high-performance HTTP framework powered by the Go language <a class="yt-timestamp" data-t="00:11:24">[00:11:28]</a>.

*   **Setup**: No fancy CLI; a Go project is created from scratch <a class="yt-timestamp" data-t="00:11:30">[00:11:34]</a>.
*   **Architecture**: Minimal HTTP framework, not concerned with MVC architecture, requiring developers to manage it themselves <a class="yt-timestamp" data-t="00:11:36">[00:11:41]</a>. It also lacks a built-in ORM, so external packages like GORM are used <a class="yt-timestamp" data-t="00:11:41">[00:11:47]</a>.
*   **Pros**: Allows for more focused functions and flexibility, avoiding framework conventions, suitable for simpler applications <a class="yt-timestamp" data-t="00:11:47">[00:11:59]</a>. Leads to a smaller codebase with more low-level control <a class="yt-timestamp" data-t="00:12:15">[00:12:17]</a>.
*   **Templates**: Go has its own built-in templating language for interpolating database values into template files <a class="yt-timestamp" data-t="00:12:06">[00:12:13]</a>.
*   **Cons**: As applications grow, it becomes harder to manage without framework conventions, requiring more developer expertise <a class="yt-timestamp" data-t="00:12:18">[00:12:23]</a>.

#### Rocket
Rocket is a web framework for Rust <a class="yt-timestamp" data-t="00:12:24">[00:12:26]</a>. The Rust ecosystem currently lacks a full-blown MVC framework like Rails <a class="yt-timestamp" data-t="00:12:27">[00:12:31]</a>.

*   **Approach**: Building a basic application proved difficult. A common approach involves using Rocket for HTTP and routing, combined with Diesel (a Rust-based ORM) and a templating language like Askama <a class="yt-timestamp" data-t="00:12:31">[00:12:45]</a>.
*   **Challenges**: A full working demo was not achieved with Rust due to its nature as a systems language, offering low-level memory control not typically needed by average web developers <a class="yt-timestamp" data-t="00:12:48">[00:12:55]</a>. It requires more time and dedication <a class="yt-timestamp" data-t="00:12:56">[00:13:00]</a>.
*   **Related Tool**: Yew is a component-based framework for [[using_web_components_in_modern_web_development | building web apps]] with WebAssembly in Rust <a class="yt-timestamp" data-t="00:13:01">[00:13:07]</a>.

#### Vapor
Vapor is a framework based on the Swift programming language <a class="yt-timestamp" data-t="00:13:11">[00:13:14]</a>. It generally works better on a Mac <a class="yt-timestamp" data-t="00:13:15">[00:13:19]</a>.

*   **Architecture**: Provides a well-organized project structure with controllers, models, and routes <a class="yt-timestamp" data-t="00:13:20">[00:13:24]</a>. Routes point to methods in controllers, which access data from models <a class="yt-timestamp" data-t="00:13:24">[00:13:28]</a>.
*   **Models**: Uses Fluent ORM, which employs classes and decorators to model data <a class="yt-timestamp" data-t="00:13:28">[00:13:34]</a>.
*   **Language Benefits**: Swift is a well-designed language, making it enjoyable to work with; it's concise, readable, statically typed, and offers excellent tooling <a class="yt-timestamp" data-t="00:13:34">[00:13:43]</a>. It embraces `async/await` for data fetching <a class="yt-timestamp" data-t="00:13:43">[00:13:46]</a>.
*   **Templating**: Features a modern and practical templating engine called Leaf <a class="yt-timestamp" data-t="00:13:48">[00:13:51]</a>.

#### Ktor
Ktor is a Kotlin-based web application framework, considered more minimal than Spring <a class="yt-timestamp" data-t="00:13:53">[00:13:58]</a>.

### Conclusion

After exploring various full-stack frameworks, [[web_development_with_ruby_on_rails | Ruby on Rails]] is regarded as the best framework due to its efficiency and "magic" <a class="yt-timestamp" data-t="00:14:14">[00:14:18]</a>.