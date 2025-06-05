---
title: Ruby on Rails framework overview
videoId: FQPlEnKav48
---

From: [[fireship]] <br/> 

Ruby on Rails is a full-stack web development framework that gained prominence by simplifying web development significantly compared to earlier approaches <a class="yt-timestamp" data-t="01:46:27">[01:46:27]</a>. It remains popular in 2022 and is known for its "rebel" stance in the [[Introduction to web development | web development]] space <a class="yt-timestamp" data-t="01:52:03">[01:52:03]</a>.

## Key Characteristics

Ruby on Rails is renowned for building massive companies such as Shopify, Airbnb, and GitHub <a class="yt-timestamp" data-t="01:40:53">[01:40:53]</a>. It is considered a "batteries included" framework, meaning it comes with many built-in functionalities like handling relational databases, testing, and logging <a class="yt-timestamp" data-t="02:37:74">[02:37:74]</a>. This can make the initial project structure seem overwhelming <a class="yt-timestamp" data-t="02:43:24">[02:43:24]</a>.

The framework is highly opinionated, which allows for substantial functionality with minimal code <a class="yt-timestamp" data-t="03:41:89">[03:41:89]</a>. However, some developers might find this "magic" to be a drawback <a class="yt-timestamp" data-t="03:52:21">[03:52:21]</a>. Rails also adopts an HTML-centric approach to building web applications, differing from client-side frameworks like [[Reactjs overview and history | React]], Angular, and Vue, and utilizes adjacent libraries such as Hotwire, Stimulus, and Turbo <a class="yt-timestamp" data-t="01:55:67">[01:55:67]</a>.

## Architecture: Model-View-Controller (MVC)

Ruby on Rails adheres to the Model-View-Controller (MVC) architecture, which is the most common approach for building full-stack web applications <a class="yt-timestamp" data-t="01:33:04">[01:33:04]</a>.

*   **Models**: Contain the logic for data in the database <a class="yt-timestamp" data-t="03:15:02">[03:15:02]</a>.
*   **Views**: These are `html.erb` files (Embedded Ruby) that allow dynamic data rendering within HTML for the user interface <a class="yt-timestamp" data-t="03:29:43">[03:29:43]</a>.
*   **Controllers**: Map URLs to actions that run on the server, often retrieving data from the database <a class="yt-timestamp" data-t="02:54:21">[02:54:21]</a>.

## Core Features

### Setup and Development Experience

To start a new Rails project, you first need to install Ruby, then the Rails Gem, and finally run `rails new` <a class="yt-timestamp" data-t="02:06:56">[02:06:56]</a>. The initial setup can be prone to errors that usually require a Google search to resolve <a class="yt-timestamp" data-t="02:14:48">[02:14:48]</a>.

### Command Line Interface (CLI)

Once set up, the Rails CLI is very powerful <a class="yt-timestamp" data-t="02:23:44">[02:23:44]</a>. It can serve the application locally with `rails server` and automatically generate substantial code using commands like `scaffold` <a class="yt-timestamp" data-t="02:26:59">[02:26:59]</a>. The `scaffold` command can generate not only data retrieval logic but also UI for creating and updating data <a class="yt-timestamp" data-t="03:46:01">[03:46:01]</a>.

### Routing

Routing in Rails is managed in the `routes.rb` file, which maps URLs to controller actions <a class="yt-timestamp" data-t="02:52:03">[02:52:03]</a>. The `resources` keyword can automatically create all necessary routes for a basic CRUD (Create, Read, Update, Delete) feature <a class="yt-timestamp" data-t="02:58:30">[02:58:30]</a>.

### Database Integration

Rails provides an abstraction layer over relational databases, typically featuring a built-in Object-Relational Mapper (ORM) <a class="yt-timestamp" data-t="01:07:05">[01:07:05]</a>. This ORM, called Active Record, can migrate code from Ruby into SQL for database interaction <a class="yt-timestamp" data-t="03:25:70">[03:25:70]</a>. Before using data, a migration must be run to sync the model code with the database <a class="yt-timestamp" data-t="03:18:74">[03:18:74]</a>.

### Templating

Views are built using `html.erb` files, which allow embedding Ruby code directly into HTML to dynamically render data <a class="yt-timestamp" data-t="03:30:26">[03:30:26]</a>.

## Comparison and Verdict

Ruby on Rails is considered the "greatest of all time" [[Comparison of web development frameworks | full-stack framework]] by some <a class="yt-timestamp" data-t="01:12:12">[01:12:12]</a> <a class="yt-timestamp" data-t="14:14:03">[14:14:03]</a>. While Ruby isn't the most popular language globally <a class="yt-timestamp" data-t="03:54:99">[03:54:99]</a>, Rails offers a robust and opinionated approach to [[Backend development and serverside concepts | backend development]].