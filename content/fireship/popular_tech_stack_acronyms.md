---
title: Popular Tech Stack Acronyms
videoId: Sxxw3qtb3_g
---

From: [[fireship]] <br/> 

When learning to code for a startup idea, choosing a tech stack is a critical decision that is difficult to change later <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. An application can be thought of as a "technology sandwich" <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>, comprising various layers of technology. While there's no official definition for a tech stack, it generally consists of three main parts <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>:

*   **Front End**: Tools for building the user interface that the end-user interacts with <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. This often includes a [[popular_dynamic_and_highlevel_programming_languages | JavaScript]] framework for the web, or tools like iOS, Android, or Flutter for mobile <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
*   **Back End**: Comprises a server-side runtime (e.g., Node.js or Python) and a database to store user-generated data <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. Infrastructure for this layer is typically purchased from large cloud providers like [[aws_computer_services_and_tools | Amazon Web Services (AWS)]] <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
*   **APIs (Application Programming Interfaces)**: These are the tools that connect the front end to the back end, such as REST or GraphQL <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. They also include essential third-party services (e.g., Stripe for payments, Twilio for text messaging, SendGrid for email) that perform functions spanning both front-end and back-end categories <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

Many popular tech stacks are known by catchy acronyms, which can help convey expertise in the tech industry <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

## Historic Tech Stack: LAMP

The original tech stack, LAMP, emerged in the late 1990s <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. It is an acronym for:
*   **L**inux
*   **A**pache
*   **M**ySQL
*   **P**HP

At a time when building web applications often required expensive commercial software, LAMP provided a free and open-source alternative <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. It eventually paved the way for web frameworks like WordPress and Joomla <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

## Modern JavaScript-Based Stacks

In modern times, while building web applications is easier, tech stacks have become more complex due to the abundance of available tools and services <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

### MEAN Stack

One of the most popular modern stacks is MEAN <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>, an acronym for:
*   **M**ongoDB (a NoSQL database) <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>
*   **E**xpress.js (a backend web application framework for Node.js) <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>
*   **A**ngular (a front-end [[popular_dynamic_and_highlevel_programming_languages | JavaScript]] framework) <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>
*   **N**ode.js (a server-side [[popular_dynamic_and_highlevel_programming_languages | JavaScript]] runtime) <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>

The MEAN stack gained popularity largely due to its memorable acronym <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

### Variations: MERN and MEVN

Variations of the MEAN stack emerged as other front-end frameworks gained prominence. These include:
*   **MERN**: Replaces Angular with [[comparison_of_popular_javascript_frameworks_in_2021 | React]] <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.
*   **MEVN**: Replaces Angular with [[comparison_of_popular_javascript_frameworks_in_2021 | Vue]] <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

### Custom Acronyms: FANCY

Developers and companies sometimes create their own acronyms to describe their specific tech stacks. An example is "FANCY," used by Fireship.io, which stands for:
*   **F**irebase
*   **H**ugo
*   **A**ngular
*   **N**ode
*   **S**tripe
*   **E**xpress <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>

While catchy, choosing a tech stack purely for its acronym can sometimes lead to regrets <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. These acronyms often do not fully capture the complete set of tools and services required in a real-world tech stack <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. For insight into what successful companies use, resources like `stackshare.io` can be helpful <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

## Simplified Tech Stacks: Petite Fire Stack

Despite the complexity of many modern tech stacks, it's important to remember that end-users do not care about the underlying technology; they only want a good experience <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. Over-engineering a tech stack can lead to unnecessary complexity and cost <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

A simplified approach, such as the "Petite Fire Stack," focuses on core functionality without excessive components:
*   **Front End**: A lightweight [[comparison_of_popular_javascript_frameworks_in_2021 | JavaScript]] framework like Petite Vue, which can be dropped in with a script tag, eliminating the need for a module bundler like Webpack <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>. For styling, Bootstrap offers a quick way to achieve a decent UI <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>. For mobile, Ionic can wrap the web application in a web view for [[building_a_todo_app_with_different_javascript_frameworks | iOS]] and Android deployment <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.
*   **Back End**: Firebase provides a document database that scales without a dedicated backend server, and also handles user authentication <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>. Server-side code can be handled by Firebase Cloud Functions, a serverless option that scales automatically without concerns about Docker, Kubernetes, or Terraform <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.
*   **APIs**: Complex API solutions like GraphQL might be unnecessary for simpler applications <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.

This simplified [[introduction_to_tech_stacks | introduction_to_tech_stacks]] can be the easiest way to [[pros_and_cons_of_different_full_stack_frameworks | build a full stack web application]] <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.