---
title: Method chaining and object references
videoId: napDjGFjHR0
---

From: [[fireship]] <br/> 

[[JavaScript objects and their properties | JavaScript objects]] are collections of key-value pairs, acting conceptually like dictionaries or maps in other programming languages <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a> <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. Anything that is not a [[JavaScript fundamentals and practical concepts | primitive data type]] in JavaScript is considered an object <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Object References

[[JavaScript fundamentals and practical concepts | JavaScript objects]] are stored as references in the heap memory, unlike [[JavaScript fundamentals and practical concepts | primitive values]] which are typically short-lived in the call stack <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a> <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. This distinction has significant implications:

*   **Primitives**: When one primitive variable is set equal to another, they each point to their own distinct primitive value. Changing one does not affect the other <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a> <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
*   **Objects**: When one object variable is set equal to another, they both reference the *same* object in heap memory <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a> <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. This means if a property of the object is updated through one variable, the change will be visible through the other variable as they are both sharing the same reference <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a> <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

Even if an [[Object creation and manipulation | object]] is defined with a `const` variable, its properties can still be modified after creation, as `const` prevents reassignment of the variable itself, not mutation of the object it references <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a> <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

### Cloning Objects

To avoid issues with shared references when updating objects in multiple places, you can clone an object's properties into a new object <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a> <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.

*   **`Object.assign()`**: This method can be used to copy the enumerable properties from one or more source objects to a target object <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a> <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>. It's important to note that `Object.assign()` only copies properties owned directly by the object and performs a shallow copy, meaning nested objects are still copied by reference <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a> <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.
*   **Spread Syntax (`...`)**: For cloning objects, the spread syntax offers a more concise and often preferred alternative to `Object.assign()` <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a> <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. It also performs a shallow copy <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

## Methods on Objects

When a [[JavaScript function basics and anatomy | function]] is a property of an [[JavaScript objects and their properties | object]], it is called a "method" <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a> <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>. You can define methods using a shorthand syntax within an [[Object creation and manipulation | object literal]], omitting the property name and directly defining a named function <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a> <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.

### The `this` Keyword in Methods

When a method is defined on an [[JavaScript objects and their properties | object]] using regular [[JavaScript function basics and anatomy | function]] syntax, the `this` keyword inside that method refers to the object it lives on <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a> <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.

However, if an [[JavaScript function basics and anatomy | arrow function]] syntax is used for a method, `this` will refer to the global context (e.g., `window` in a browser) rather than the parent object <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a> <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.

## Method Chaining

Method chaining is a technique where multiple methods are called sequentially on the same [[JavaScript objects and their properties | object]], often seen in libraries like jQuery <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a> <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>. To enable method chaining, a method must return a reference to the [[JavaScript objects and their properties | object]] itself <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. This is achieved by returning `this` from the method <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. By returning `this`, each method call returns the original object, allowing the next method in the chain to be called on it <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.