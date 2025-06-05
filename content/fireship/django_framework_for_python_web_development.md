---
title: Django framework for Python web development
videoId: FQPlEnKav48
---

From: [[fireship]] <br/> 

Django is a popular [[Python Applications and Frameworks | Python]]-based [[comparison_of_web_development_frameworks | web framework]] designed for building [[Introduction to web development | web app]]s <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It is described as a "batteries included" framework, meaning it provides many components and tools necessary for [[Introduction to web development | web development]] out of the box <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

## Prominence and Use Cases
Django is extremely popular and has been used to build massive sites such as Spotify and Bitbucket <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. It enables the creation of [[Introduction to web development | web app]]s using the [[Popular programming languages for web development | Python]] language <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

## Core Functionality of a Web Framework
Like other [[comparison_of_web_development_frameworks | web Frameworks]], Django performs three main functions <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>:
1.  **Database Abstraction**: It provides an abstraction over relational databases, typically with a built-in Object Relational Mapper (ORM) that translates [[Popular programming languages for web development | Python]] code into SQL queries <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
2.  **Routing**: It maps URLs in the browser to specific code that runs on the [[Frontend and backend development layers | server]] <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
3.  **Dynamic Data Insertion**: It offers a way to dynamically insert data from the database directly into HTML for the user interface (UI) <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

These elements collectively form the Model-View-Controller (MVC) architecture, a common approach for building full-stack [[Introduction to web development | web app]]s <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

## Developer Experience
The [[comparison_of_web_development_frameworks | developer experience]] with Django includes aspects like setup, routing, database integration, and overall architecture <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

### Project Structure
When generating a new Django app, the file structure is less overwhelming compared to [[Ruby on Rails framework overview | Rails]], yet it remains a "batteries included" framework <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. Code in Django tends to be more explicit <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. For example, the `manage.py` file contains the code for the [[web_application_tools_for_developers | command line interface]] (CLI), used to serve the app locally or generate new features as "apps" within the project <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

### MVC Architecture in Django
Django adheres to the MVC architecture <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>:
*   **Routing**: Routes are defined in the `urls.py` file <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
*   **Controllers**: Controllers are represented as [[Popular programming languages for web development | Python]] functions in the `views.py` file <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>. A route points to one of these functions <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.
*   **Models**: Models are [[Popular programming languages for web development | Python]] classes that define the structure of data in an SQL database, serving as the Object Relational Mapper <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>. The controller functions might access data from these models <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
*   **Views**: HTML templates allow embedding [[Popular programming languages for web development | Python]] directly into the code <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

### Built-in Admin Feature
A significant advantage of Django is its built-in admin feature <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. Developers can register models with the admin app to easily manage all application data directly in the browser <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>. This feature is highly useful and avoids the need for custom development <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.