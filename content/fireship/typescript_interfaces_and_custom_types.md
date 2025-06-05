---
title: TypeScript interfaces and custom types
videoId: ahCwqrYpIuM
---

From: [[fireship]] <br/> 

[[type_annotations_and_error_checking_in_typescript | TypeScript]] allows developers to create custom types and interfaces, providing powerful ways to define the shape of data and improve code reliability.

## Custom Types

You can create your own types from scratch <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>. When creating a custom type, it's typical to name it using Pascal case <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

Initially, a custom type can be arbitrarily assigned to a primitive type like a string <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>. When a variable is then annotated with this custom type, you receive specific feedback related to that type, rather than just the underlying primitive type <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.

### Union Types

A custom type can be restricted to specific values, such as "bold" or "italic" <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. This is achieved by creating a union type, where the allowed values are separated by a pipe (`|`) <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. This ensures that the variable can only be assigned to these specific values <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. Union types are versatile and not limited to strings; they can also include numbers <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.

## Interfaces

Interfaces are frequently used to strong type objects that have multiple properties with varying types <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. They help enforce a specific object shape, which is crucial for preventing bugs that can arise from using objects or class instances with incorrect structures <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

To define an interface, you specify the types for each property within the object <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. Once defined, this interface can be used to strong type objects directly, as a return value from a function, or as an argument to a function <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.

### Flexible Interfaces

In scenarios where an interface might be too restrictive, you can maintain required properties while allowing for additional properties <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>. This is done by creating an index signature, such as `[key: string]: any`, which means any additional string key can have a value of any type <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. This allows for flexibility while still requiring specific core properties <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.