---
title: Criticism and practical use of design patterns
videoId: tv-_1er1mWI
---

From: [[fireship]] <br/> 

Initially, a junior developer's code might resemble "Play-Doh snakes" <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. As they become a senior developer and learn about [[overview_of_software_design_patterns | software design patterns]], their code can become as intricate as the Sistine Chapel <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. However, a principal engineer might realize that maintaining such complex code for a simple website is unnecessary and return to simpler "Play-Doh snakes" <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. This highlights the subjective and sometimes controversial nature of using design patterns <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## The Gang of Four Book

A highly influential book in programming history, "Design Patterns" by four C++ engineers known as The Gang of Four, outlines 23 different approaches to address recurring [[problemsolving_skills_in_software_development | problems]] programmers face <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. These patterns are categorized into three main types:
*   [[understanding_creational_patterns | Creational patterns]]: How objects are created <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.
*   [[structural_patterns_in_software_design | Structural patterns]]: How objects relate to each other <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
*   [[behavioral_patterns_in_programming | Behavioral patterns]]: How objects communicate with each other <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

Becoming a proficient software engineer involves the ability to [[problemsolving_skills_in_software_development | solve problems]] with a programming language, rather than just memorizing its syntax <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. Understanding a variety of patterns can help with [[problemsolving_skills_in_software_development | solving problems]] relevant to modern [[design_techniques_in_app_development | app developers]] <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## Practical Use and Considerations

[[overview_of_software_design_patterns | Design patterns]] are not simply algorithms that can be copied and pasted; they require careful thought and implementation <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. Knowing how to write recognized [[overview_of_software_design_patterns | design patterns]] can help a programmer level up <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

### Potential Pitfalls and Criticisms

Despite their benefits, [[overview_of_software_design_patterns | design patterns]] can also add unnecessary complexity and boilerplate to a codebase if used improperly <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. The Gang of Four book itself has received many criticisms <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. A key moral is to leverage a language's built-in features before implementing a complex [[overview_of_software_design_patterns | design pattern]] <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

Specific criticisms and nuances for patterns mentioned include:
*   **Singleton**: In JavaScript, this pattern can often be replaced by simply creating a global object due to how objects are passed by reference and the concept of global data, making the pattern itself extra boilerplate <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. It's an "entirely different story" in C++ <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **Prototype**: While an alternative to class inheritance, extending a class with additional functions via its prototype in JavaScript is generally considered a bad practice <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.
*   **Builder**: This pattern, while useful for step-by-step object creation and method chaining, has "gone a bit out of style in recent years" <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
*   **State**: Relying on conditional logic or switch statements to handle different possibilities based on application state generally "doesn't scale very well" <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.

## Examples of Patterns and Their Utility

The video introduces various [[overview_of_software_design_patterns | design patterns]] with practical examples:

### Creational Patterns
*   **Singleton**: Ensures that an object can only be instantiated once <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. Example: A `Settings` class for global app settings <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
*   **Prototype**: A way to implement inheritance by cloning an already created object, leading to a flatter prototype chain in dynamic languages like JavaScript <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. Example: Cloning a "zombie" object with `Object.create` <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
*   **Builder**: Creates an object step-by-step using methods rather than a single constructor, allowing for method chaining <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. Example: Building a hot dog by chaining methods for ingredients <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
*   **Factory**: Uses a function or method to instantiate an object instead of the `new` keyword, useful for determining which object to create based on conditions <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>. Example: Creating platform-specific buttons for iOS or Android without repetitive conditional logic <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.

### Structural Patterns
*   **Facade**: Provides a simplified API to hide complex low-level details of a codebase <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. Example: A `Facade` class to simplify complex plumbing and electrical systems for a house occupant <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. Libraries like jQuery are good examples of facades <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.
*   **Proxy**: Replaces a target object with a substitute that can intercept operations like getting or setting properties <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. Example: Vue.js uses proxies for its reactivity system to update the UI when data changes <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. Also useful for large objects that are expensive to duplicate in memory <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.

### Behavioral Patterns
*   **Iterator**: Allows traversal through a collection of objects <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. Modern languages provide abstractions like the `for` loop <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. Example: Implementing a custom range function in JavaScript that iterates through a series of values <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>. It's a "pull-based system" <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.
*   **Observer**: Allows many objects to subscribe to events broadcast by another object, creating a one-to-many relationship <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. Example: Firebase client apps subscribing to server data changes <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. It's a "push-based system" <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.
*   **Mediator**: Acts as a middleman or broker to coordinate communication between multiple objects, preventing a dangerous many-to-many relationship <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>. Example: An air traffic controller mediating between airplanes and runways <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>, or middleware in Express.js intercepting requests <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>. It provides separation of concerns and eliminates code duplication <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.
*   **State**: Allows an object to behave differently based on a finite number of internal states, making an object's behavior predictable <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>. Example: A `Human` class whose "think" method behaves differently based on its `mood` state, achieved by delegating to separate state classes <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>. This avoids extensive conditional logic and doesn't require changing the API when the state changes <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.