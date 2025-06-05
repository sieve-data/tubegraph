---
title: Comparison of web development frameworks
videoId: FQPlEnKav48
---

From: [[fireship]] <br/> 

A web application is a software application that runs on a web browser <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This article explores various full-stack web frameworks, examining their developer experience, setup process, routing mechanisms, database integration, and overall architecture <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. The choice of a framework can significantly impact a project's future development <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

## What a Web Framework Does
A web framework primarily handles three main functions <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>:
1.  **Database Abstraction**: Provides an abstraction layer over relational databases, often including a built-in Object Relational Mapper (ORM) to migrate code from the programming language into SQL <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
2.  **Routing**: Maps URLs in the browser to specific server-side code <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
3.  **Dynamic HTML**: Offers a way to dynamically insert data from the database directly into HTML for the user interface <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

These elements together form the Model-View-Controller (MVC) architecture, a common approach for building full-stack web applications <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

## Frameworks Overview

### Ruby on Rails
Ruby on Rails is a server-side framework known for building major companies like Shopify, Airbnb, and GitHub <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. It revolutionized [[introduction_to_web_development | web development]] by simplifying it significantly <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

*   **Language**: Ruby <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>
*   **Approach**: HTML-centric, using libraries like Hotwire, Stimulus, and Turbo, which contrasts with [[frontend_ui_libraries_and_frameworks | frontend frameworks]] like React, Angular, and Vue <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   **Setup**: Requires Ruby and the Rails Gem; initial setup can be error-prone <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
*   **CLI**: Extremely powerful, generating code automatically with commands like `scaffold` <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
*   **Architecture**: A "batteries-included" framework handling databases, testing, and logging <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. Main application code is in the `app` directory (models, views, controllers) <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
*   **Routing**: Defined in `routes.rb`, mapping URLs to controller actions. `resources` automatically create CRUD routes <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   **Database**: Managed by Active Record, an ORM that handles migrations and data <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
*   **Views**: `.html.erb` files (embedded Ruby) for dynamic data rendering <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
*   **Pros**: Opinionated, enabling a lot of functionality with minimal code <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

### [[django_framework_for_python_web_development | Django]]
[[django_framework_for_python_web_development | Django]] is a popular Python-based framework used for large sites like Spotify and Bitbucket <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

*   **Language**: Python <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>
*   **Architecture**: Less overwhelming file structure than Rails but still "batteries-included" <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. Code is more explicit <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. Follows MVC <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
*   **CLI**: `manage.py` file for CLI commands, serving the app, or generating features <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **Routing**: Defined in `urls.py` <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
*   **Controllers**: Python functions in `views.py` <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
*   **Database**: Models are Python classes representing SQL database structure (ORM) <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
*   **Views**: HTML templates allow embedding Python directly <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
*   **Special Feature**: Built-in admin feature for easily managing data in the browser <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.

### Laravel
Laravel is a [[popular_programming_languages_for_web_development | PHP framework]] for "web artisans" <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

*   **Language**: PHP <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>
*   **Setup**: Requires PHP and Composer; initial app generation can be lengthy <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
*   **Architecture**: Even more "batteries-included" than Rails <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
*   **Routing**: Handles web, API, and real-time communication (channels) routes <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
*   **Controllers**: Classes with methods for data access and template rendering <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
*   **Database**: Eloquent ORM, based on the Active Record pattern <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
*   **Views**: Blade templates build on PHP's native HTML integration <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
*   **Integration**: Strong emphasis on integrating [[frontend_ui_libraries_and_frameworks | frontend frameworks]] like React and Vue, with an adjacent tool called Inertia <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

### Next.js
Next.js allows building a full-stack application entirely with [[javascript_for_interactivity_and_frameworks | JavaScript]] <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

*   **Language**: [[javascript_for_interactivity_and_frameworks | JavaScript]] <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>
*   **Setup**: `npx create next app` to generate a starter project <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.
*   **Database**: Does not provide built-in database integration; allows developers to choose their preferred solution (e.g., Prisma) <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.
*   **Architecture**: Minimal framework <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.# [[comparison_of_javascript_frameworks | Comparison of Web Development Frameworks]]

A web application (web app) is a software application that runs in a web browser <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This article explores various full-stack web frameworks, examining their developer experience, setup process, routing mechanisms, database integration, and overall architecture <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. The choice of a framework can significantly impact a project's future development <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

## What a Web Framework Does
A web framework primarily handles three main functions <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>:
1.  **Database Abstraction**: Provides an abstraction layer over relational databases, typically with a built-in Object Relational Mapper (ORM) to translate code from the programming language into SQL <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
2.  **Routing**: Maps a URL in the browser to specific server-side code that should be executed <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
3.  **Dynamic HTML**: Offers a method to dynamically insert data from the database directly into HTML for the user interface <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

Together, these elements often form the Model-View-Controller (MVC) architecture, which is the most common approach when building a full-stack web app <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

## Frameworks Overview

### Ruby on Rails
Ruby on Rails is a server-side framework famously used to build companies like Shopify, Airbnb, and GitHub <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. It revolutionized [[introduction_to_web_development | web development]] by dramatically simplifying it <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

*   **Language**: Ruby <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>
*   **Approach**: HTML-centric, using adjacent libraries like Hotwire, Stimulus, and Turbo, which contrasts with [[frontend_ui_libraries_and_frameworks | frontend frameworks]] like React, Angular, and Vue <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   **Setup**: Requires Ruby and the Rails Gem; initial setup can be error-prone <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
*   **CLI**: Extremely powerful, generating code automatically with commands like `scaffold` <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
*   **Architecture**: A "batteries-included" framework handling relational databases, testing, logging, and more <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. The main application code resides in the `app` directory (models, views, controllers) <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
*   **Routing**: Defined in `routes.rb`, mapping URLs to controller actions. `resources` automatically create all necessary CRUD routes <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   **Database**: Managed by Active Record, an ORM <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
*   **Views**: `.html.erb` files (embedded Ruby) allow dynamic data rendering within HTML <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
*   **Pros**: Very opinionated, enabling significant functionality with minimal code <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

### [[django_framework_for_python_web_development | Django]]
[[django_framework_for_python_web_development | Django]] is an extremely popular Python-based framework used for massive sites like Spotify and Bitbucket <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

*   **Language**: Python <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>
*   **Architecture**: Less overwhelming file structure than Rails but still "batteries-included" <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. Code tends to be more explicit <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. Follows the MVC architecture <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
*   **CLI**: Uses a `manage.py` file for CLI commands, including serving the app locally or generating features <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **Routing**: Defined in the `urls.py` file <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
*   **Controllers**: Represented as Python functions in the `views.py` file <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
*   **Database**: Models are Python classes representing the structure of data in an SQL database (ORM) <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
*   **Views**: HTML templates allow embedding Python directly <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
*   **Special Feature**: Includes a built-in admin feature for easily managing data in the browser <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.

### Laravel
Laravel is a [[popular_programming_languages_for_web_development | PHP framework]] dubbed "the PHP framework for web Artisans" <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

*   **Language**: PHP <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>
*   **Setup**: Requires PHP and Composer; initial app generation can be time-consuming due to many package downloads <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
*   **Architecture**: Even more "batteries-included" than Rails <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
*   **Routing**: Handles not only web routes but also API routes and channels for real-time communication via websockets <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
*   **Controllers**: Classes containing methods that access data and render specific templates <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
*   **Database**: Eloquent ORM, based on the same Active Record pattern as Rails <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
*   **Views**: Blade templates build on PHP's native ability to work with HTML <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
*   **Integration**: Strong focus on integrating [[frontend_ui_libraries_and_frameworks | front-end frameworks]] like React and Vue, with an adjacent tool called Inertia to bridge the gap between front-end and backend frameworks <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

### Next.js
Next.js enables building a full-stack application entirely with [[javascript_for_interactivity_and_frameworks | JavaScript]] <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

*   **Language**: [[javascript_for_interactivity_and_frameworks | JavaScript]] <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>
*   **Setup**: `npx create next app` generates a starter project <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.
*   **Database**: Does not provide built-in database integration, allowing developers to choose their preferred solution (e.g., Prisma) <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.
*   **Architecture**: Minimal framework that simplifies annoying parts of [[introduction_to_web_development | web development]] <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.
*   **Routing**: Handled by the file system; each file in the `Pages` directory defines a different URL <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. Dynamic routes use brackets in the file name <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
*   **Views**: Each file exports a React component to define the UI <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
*   **Data Fetching**: Supports server-side code execution with functions like `getServerSideProps` to fetch data (e.g., using Prisma) and deliver it as props to the React component <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.

### Spring
Spring is a Java framework that makes working with Java enjoyable, despite Java being known for boilerplate code <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.

*   **Language**: Java (can also use Kotlin or Groovy) <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>
*   **Setup**: Features a generator to customize the framework with desired dependencies <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.
*   **Architecture**: Follows the MVC pattern <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>. Code feels robust compared to dynamic languages <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
*   **Controllers**: Classes where routes are defined using decorators on methods <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>. Relies on metaprogramming to keep code simple <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.
*   **Database**: Models are based on code using the Java Persistence API <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
*   **Views**: Thymeleaf templates use attributes in HTML to define data placement <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.

### .NET (ASP.NET)
ASP.NET is an open-source project maintained by Microsoft, known for being popular and reliable <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.

*   **Language**: C# <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>
*   **Evolution**: Has evolved well, with modern supporting libraries like Blazor for building client-side apps with WebAssembly and C# <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.
*   **Setup**: Install the .NET SDK, then generate a new MVC application <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.
*   **Project Structure**: Initial project structure is clear and organized <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>.
*   **Features**: Provides excellent tooling and static typing <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.
*   **Routing**: URLs are inferred from class names in controllers, with methods representing next URL segments <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>.
*   **Database**: Models are managed by the Entity Core framework (ORM) <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.
*   **Views**: Written in C# HTML, allowing data access and C# declarations within templates, with full IntelliSense <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.

### Phoenix
Phoenix is a framework based on the Elixir functional programming language <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.

*   **Language**: Elixir <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>
*   **Setup**: Powerful CLI similar to Ruby on Rails, capable of scaffolding an entire CRUD application automatically <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
*   **Routing**: Similar to Rails, using resources to map CRUD URLs to controllers <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
*   **Controllers**: Functions namespaced under a module that access data and render templates <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.
*   **Database**: Uses an ORM called Ecto <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.
*   **Views**: Templates use embedded Elixir, similar to Rails' ERB <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.
*   **Performance**: Huge advantage in performance because Elixir is a compiled language <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>.
*   **Special Feature**: Every app includes a built-in live dashboard for monitoring performance <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.

### Gin
Gin is a high-performance framework powered by the Go language <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.

*   **Language**: Go <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>
*   **Setup**: No fancy CLI; Go projects are created from scratch <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.
*   **Architecture**: A minimal HTTP framework not concerned with MVC <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>; developers must handle architectural decisions <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.
*   **Database**: Does not contain a built-in ORM; external packages like GORM are used <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>.
*   **Flexibility**: Allows for smaller codebases and more low-level control, writing focused functions <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
*   **Views**: Go has its own built-in templating language to interpolate values from the database <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.
*   **Consideration**: Can become harder to manage as the application grows <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>.

### Rocket
Rocket is a web framework for the Rust programming language <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.

*   **Language**: Rust <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>
*   **Ecosystem**: The Rust ecosystem currently lacks a full-blown MVC framework like Rails <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.
*   **Approach**: Combines Rocket for HTTP and routing with Diesel (a Rust-based ORM) and Askama (a templating language) <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>.
*   **Difficulty**: Can be challenging to build a basic application due to Rust being a systems language that provides low-level control over memory, which most web application developers may not need <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>.
*   **Related Tool**: `Yew` is a component-based framework for building web apps with WebAssembly in Rust <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.

### Vapor
Vapor is a framework based on the Swift programming language <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.

*   **Language**: Swift <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>
*   **Setup**: Typically built on macOS, as Swift integration often works better there <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.
*   **Project Structure**: Well-organized with clear directories for controllers, models, and routes <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>.
*   **Controllers**: Routes point to methods in the controller which access data from a model <a class="yt-timestamp" data-t="00:13:24">[00:13:24]</a>.
*   **Database**: Uses an ORM called Fluent, which models data using classes and decorators <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.
*   **Language Features**: Swift is a well-designed language, offering concise, readable, statically typed code with excellent tooling <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>. It embraces async/await for data fetching <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>.
*   **Views**: Employs a modern and practical templating engine called Leaf <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>.

### Ktor
Ktor is a Kotlin-based web application framework <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.

*   **Language**: Kotlin <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>
*   **Architecture**: More minimal than Spring <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>.

## Conclusion
After reviewing various full-stack frameworks, Ruby on Rails is highlighted as a top contender due to its comprehensive features and developer experience <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.

> [!NOTE] Disclaimer
> The speaker jokingly states that the best framework is "your own reflection in the mirror" before declaring Ruby on Rails as "by far the best framework" <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.