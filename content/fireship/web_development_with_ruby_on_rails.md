---
title: Web development with Ruby on Rails
videoId: FQPlEnKav48
---

From: [[fireship]] <br/> 

Ruby on Rails, often referred to as Rails, is a popular server-side framework for web development <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. It gained fame for its use in building major companies such as Shopify, Airbnb, and GitHub <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

## Historical Significance and Philosophy
Rails was revolutionary upon its release because it significantly simplified web development compared to existing methods <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. It remains popular in 2022 and is considered a "rebel" in the [[introduction_to_web_development | web development]] space <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. Rails, along with its adjacent libraries like Hotwire, Stimulus, and Turbo, adopts an HTML-centric approach to building web applications. This contrasts with the approaches seen in [[javascript_and_frontend_development | frontend development]] frameworks such as React, Angular, and Vue <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

## Setting up a Development Environment
To get started with Rails, you first need to install Ruby, then the Rails Gem, and finally run the `rails new` command <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. While the initial setup can sometimes be error-prone, requiring Google searches for solutions, the process is generally manageable <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

## Core Features and Architecture

### "Batteries Included" Framework
Rails is known as a "batteries included" framework, meaning it comes with comprehensive support for various aspects of web development, including relational databases, testing, and logging <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. While its extensive folder structure might appear overwhelming at first, the main application code is neatly contained within the `app` directory, which further organizes files into models, views, and controllers <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

### Command Line Interface (CLI)
The Rails CLI is exceptionally powerful <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. Beyond serving the application with `rails server` <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>, it can automatically generate a substantial amount of code using commands like `scaffold` <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

### Model-View-Controller (MVC) Architecture
Rails adheres strictly to the [[front_end_and_back_end_development | Model-View-Controller (MVC) architecture]] <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. This approach provides a clear separation of concerns in the application's design <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

#### Routing
Routing in Rails is defined in the `routes.rb` file <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. The `resources` keyword automatically generates all necessary [[framework_features_like_routing_and_database_integration | CRUD (Create, Read, Update, Delete) routes]] for a feature, mapping URLs in the browser to specific actions within a controller <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

#### Models and Database Integration
The logic for data interaction resides within the model <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>. Rails utilizes an Object-Relational Mapper (ORM) called Active Record, which translates Ruby code into SQL for database operations <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. Database migrations are used to synchronize the model code with the actual database schema <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.

#### Views
Views are typically `html.erb` files <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. ERB, standing for embedded Ruby, allows developers to dynamically insert data from the database directly into HTML for the user interface <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

## Pros and Cons
Rails is highly opinionated, which enables a lot of functionality to be achieved with very little code <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. For example, the `scaffold` command not only retrieves data but also provides UI for creating and updating it <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. However, this "magic" can sometimes be perceived as a drawback <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>, and Ruby is not the most widely adopted programming language <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.

Despite this, Ruby on Rails is highlighted as a top-tier framework <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>.