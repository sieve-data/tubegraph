---
title: JavaScript objects and their properties
videoId: napDjGFjHR0
---

From: [[fireship]] <br/> 

## Introduction to JavaScript Objects

In JavaScript, an object is a collection of properties, where each property associates a key to a value <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. If you have previously learned about [[javascript_data_types_and_control_flow | JavaScript data types and control flow]], you know there are seven primitive data types, which represent a single value like a number or a string <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. Anything that is not a primitive is considered an object <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. The object data type makes everything "interesting" possible in JavaScript <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

Conceptually, a JavaScript object is similar to a dictionary or a map found in other programming languages <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

## Creating Objects

There are several ways to create objects in JavaScript:

### Object Literal Syntax

The most straightforward way to create an object is by using the literal syntax <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. This involves defining a variable equal to curly braces `{}` <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. Inside the braces, you define properties separated by commas <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. A property is a key-value pair, where the left side is the property name and the right side is the property value <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. The property name must be a unique value that can be coerced to a string <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>, while the value can be any data type, including a primitive, another object, or a function <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

Even if an object is defined with `const`, you can still set properties on it after creation <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

### Constructor Syntax

Another way to create an object is using the constructor syntax, for example, `new Object()` <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

### `Object.create()`

A static method on the `Object` class called `create` can be used <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. While not typically used for empty objects, it is most useful when you want a new object to inherit properties from an existing object, using it as a prototype <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. When a new object is created using `Object.create()` with an existing object as a prototype, properties of the prototype are accessible on the new object even if they don't appear directly on it <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. This means the property exists on the new object's prototype <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. You can see this by calling `Object.getPrototypeOf()`, which returns the original prototype object <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

### `Object.defineProperty()`

You can add a property to an object using `Object.defineProperty()` <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. This method takes three arguments: the object itself, the name of the key (property name), and a descriptor object with options <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. The `value` option in the descriptor can create a property identical to those created with literal syntax <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. This method also allows for advanced features like defining getters <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. While not for casual use, understanding it is important for a deep comprehension of the language <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

## Property Access and Manipulation

### Bracket Notation

Properties can be set on an object after it's created using bracket notation, followed by the property name in quotes, and then assigned a value <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. Properties can also be read or retrieved using the same bracket notation <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

### Dot Notation

Properties can also be set and accessed using dot notation <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. Dot notation looks cleaner, but property names must be a continuous string and cannot start with a number <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. Using dot notation with property names containing spaces or starting with numbers will result in a syntax error <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

### Modern Syntax for Property Management

#### Shorthand Property Names

In [[javascript_highlevel_features | modern JavaScript]], if you want to set variables on an object with the same property names as the variable names, you can simply add the variable directly to the object literal <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. JavaScript will coerce the variable name to the property name <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

#### Destructuring

Object destructuring allows you to read an object's properties and set them as local variables in a single line of code <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. JavaScript matches the variable names to the property names on the object <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

If you need to give the destructured variable a different name (e.g., to avoid a name collision), you can add a colon after the property name in the destructuring assignment, followed by your desired variable name <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

#### Overwriting Properties

If you add another property with the same name to an object, the new value will overwrite the existing one without throwing an error <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

#### Computed Property Names

You can compute property names by wrapping them in brackets `[]` and placing an expression inside <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. The expression's value will be computed when the object is created to generate the key for that property <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

## Object Methods

Object properties can also take functions as their value <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. When a function lives on an object, it is called a method <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

### Shorthand Method Syntax

You can define a method using shorthand syntax by omitting the property name and defining a named function directly in the object literal <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

### Getters and Setters

The `get` and `set` keywords can be used to define getters and setters on an object <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.

### The `this` Keyword

When you define a method on an object, the `this` keyword refers to that specific object <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>. However, if you use arrow function syntax for a method, `this` will refer to the global `this` context, not the object itself <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

### Method Chaining

To chain methods together (as seen in libraries like jQuery), a method must return `this` <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. Since `this` refers to the parent object when defined in a named function, returning `this` ensures that subsequent method calls continue to reference the original object <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

## Object References

[[javascript_fundamentals_and_practical_concepts | Previously]], you may have learned the difference between the call stack and the heap memory <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. Primitive values are typically short-lived in the call stack <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>, while JavaScript objects are kept as references in the heap <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.

When you assign a primitive value to another variable, a copy of the value is made <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>. Changes to one variable do not affect the other <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.

However, when you assign an object to another variable, it creates a reference to the same object in the heap <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>. Both variables reference the identical object <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. Therefore, if a property on the object is updated through one variable, the change will be reflected when accessing the object through the other variable, because they share the same reference <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.

## Combining and Cloning Objects

Due to the nature of object references, updating the same object in multiple places can be difficult <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. Often, you want to clone an object's properties into a new, distinct object.

### `Object.assign()`

One way to clone an object's properties into a new object is with `Object.assign()` <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>. This method takes a target object (often a brand new empty object) and assigns enumerable properties from one or more source objects to it <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>.

It's important to note that `Object.assign()` only copies internal enumerable properties <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. You can see which properties will be copied using `Object.getOwnPropertyNames()`, which returns an array of all property names owned directly by the object <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>. Properties inherited higher up the prototype chain are *not* copied <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. Additionally, `Object.assign()` performs a *shallow copy*; if an object's properties themselves reference other objects, those nested objects are still copied by reference, not deep-copied by value <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

### Spread Syntax (`...`)

A better alternative for cloning and combining objects is the spread syntax (`...`) <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>. While there are minor differences, the spread syntax can often be used interchangeably with `Object.assign()` and looks cleaner when combining many objects <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.

## Iterating Over Objects

While [[modern_javascript_array_methods | looping over an array]] is straightforward, iterating over an object requires specific methods:

### `for...in` Loop

The `for...in` loop can iterate over all enumerable properties in an object, including those inherited from its prototypes <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>. However, this can be confusing, so it is often avoided for simple iteration <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>.

### `Object.keys()`, `Object.values()`, `Object.entries()`

A better alternative is to get the keys or values as an array using `Object.keys()` or `Object.values()` <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>. Once you have an array, you can use a regular `for` loop or [[loops_and_iteration_over_objects | built-in array methods]] like `forEach` <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.

To loop over both keys and values together, `Object.entries()` returns an array of tuples (key-value pairs) <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. You can then destructure the key and value variables directly within the loop <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.

## Constructor Functions and Classes

### Constructor Functions

You can customize the way an object is created by writing a constructor function <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. By convention, constructor function names should always be capitalized <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. Inside the function, you define properties and methods using the `this` keyword to reference internal properties on the object when it's created or instantiated <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. This is similar to a class in other object-oriented programming languages <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.

To initialize a new object using a constructor function, use the `new` keyword in front of the function call <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>.

### Classes

In [[javascript_highlevel_features | modern JavaScript]], you can use the `class` keyword instead of a constructor function to achieve similar results <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. The `class` keyword is mostly just syntactic sugar for the underlying constructor function process <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.

JavaScript objects are a fundamental and flexible building block of the language <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.