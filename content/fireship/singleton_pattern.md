---
title: Singleton pattern
videoId: tv-_1er1mWI
---

From: [[fireship]] <br/> 

The Singleton pattern is a [[software_design_patterns | software design pattern]] that ensures an object can only be instantiated once <a class="yt-timestamp" data-t="01:33:00">[01:33:00]</a>. It is considered one of the easier patterns to understand <a class="yt-timestamp" data-t="01:33:00">[01:33:00]</a>.

## Implementation Details

### In TypeScript

In TypeScript, a Singleton class can be implemented by:
*   Giving it a static instance property <a class="yt-timestamp" data-t="01:45:00">[01:45:00]</a>.
*   Making its constructor private to prevent direct instantiation with the `new` keyword <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>.
*   Creating a static `getInstance` method that checks if an instance already exists <a class="yt-timestamp" data-t="01:50:00">[01:50:00]</a>. If an instance does not exist, it creates a new one, ensuring only one object is ever created <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>.

For example, a `Settings` class could be implemented as a Singleton to represent global application settings data <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>.

### In JavaScript

In JavaScript, the concept of a Singleton can be achieved more simply due to its built-in features <a class="yt-timestamp" data-t="02:02:00">[02:02:00]</a>. JavaScript has object literals and the concept of global data, and objects are passed by reference <a class="yt-timestamp" data-t="02:02:00">[02:02:00]</a>. The same basic characteristics as the Singleton pattern can be obtained by simply creating a global object <a class="yt-timestamp" data-t="02:08:00">[02:08:00]</a>. In this context, implementing the pattern with explicit boilerplate might be unnecessary <a class="yt-timestamp" data-t="02:13:00">[02:13:00]</a>.

## Considerations

The applicability and necessity of the Singleton pattern can be subjective and controversial <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>. While useful in some languages like C++ <a class="yt-timestamp" data-t="02:17:00">[02:17:00]</a>, it's advisable to leverage a language's built-in features before opting for a complex [[software_design_patterns | design pattern]] <a class="yt-timestamp" data-t="02:19:00">[02:19:00]</a>. Improper use of [[software_design_patterns | design patterns]] can introduce unnecessary complexity and boilerplate code <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>.