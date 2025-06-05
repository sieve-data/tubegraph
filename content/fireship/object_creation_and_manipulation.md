---
title: Object creation and manipulation
videoId: napDjGFjHR0
---

From: [[fireship]] <br/> 

In JavaScript, an object is a collection of properties, where each property associates a key with a value <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. Primitives in JavaScript represent a single value (like a number or a string), and anything that is not a primitive is considered an object <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. Most interesting functionalities in JavaScript are made possible by the object data type <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

An object is conceptually similar to a dictionary or a map found in other programming languages <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

## Creating Objects

There are several ways to create objects in JavaScript:

### Object Literal Syntax

The most straightforward way to create an object is by using the literal syntax <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. This involves defining a variable equal to curly braces `{}` <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. Inside the braces, you define properties separated by commas <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. A property is a key-value pair, with the property name on the left side and the property value on the right <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

The property name must be a unique value that can be coerced to a string <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. The value can be any data type, including a primitive, another object, or a function <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

### Constructor Syntax (`new Object()`)

Another way to create an object is using the constructor syntax with `new Object()` <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

### `Object.create()`

You can also use the static method `Object.create()` on the `Object` class <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. This method is particularly useful when you want an existing object to inherit properties from another object, effectively using the existing object as a [[prototypal_inheritance_in_javascript | prototype]] <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. When `Object.create()` is used to create a new object with a prototype, the new object initially appears blank, but it can access properties defined on its prototype <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. You can see the prototype an object inherits from by calling `Object.getPrototypeOf()` <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

### `Object.defineProperty()`

For more advanced control over property definition, you can use `Object.defineProperty()` <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. This method takes the object as its first argument, the key name as the second, and an object with options (known as a descriptor) as the third argument <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. It allows defining properties with specific characteristics, such as getters and setters <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. While not for regular use by most casual JavaScript users, it's crucial for a deeper [[javascript_fundamentals_and_practical_concepts | understanding of the language]] <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

### Constructor Functions and Classes

To customize how an object is created, you can write a constructor function <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>. By convention, constructor function names should be capitalized <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. Inside, `this` refers to the object being created, allowing you to define internal properties and methods <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. To initialize a new object with a constructor function, you use the `new` keyword <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>.

In modern JavaScript, the `class` keyword can be used instead of a constructor function, which is largely syntactic sugar for the same underlying process <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. This concept relates to [[understanding_creational_patterns | creational patterns]] in programming <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.

## Manipulating Object Properties

### Setting and Reading Properties

Properties can be set on an object after it's created, even if the object variable was defined with `const` <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

*   **Bracket Notation:** You can use bracket notation (`object['propertyName'] = value`) to set properties <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. This notation is also used to read or get property values <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
*   **Dot Notation:** Dot notation (`object.propertyName = value`) looks cleaner but requires property names to be a continuous string that does not start with a number <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. If property names contain spaces or start with numbers, dot notation will result in a syntax error <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

### Modern Property Assignment and Destructuring

*   **Property Shorthand:** If you want to set variables as properties on an object with the same name as the variable, you can simply add the variable directly to the object literal <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. JavaScript will coerce the variable name to the property name <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
*   **Destructuring:** This allows you to read an object's properties and set them as local variables <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. JavaScript will match variable names to property names on the object <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. You can also rename destructuring variables to avoid naming collisions by adding a colon after the property name (`{ propertyName: newVariableName }`) <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
*   **Overwriting Properties:** If you add another property with the same name, JavaScript will overwrite the value on the left with the value on the right without throwing an error <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
*   **Computed Property Names:** You can compute property names at runtime by wrapping an expression in brackets `[]` within the object literal <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

### Methods on Objects

[[JavaScript objects and their properties | Object properties]] can take [[javascript_function_basics_and_anatomy | functions]] as their values <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. When a function lives on an object, it's called a *method* <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

*   **Method Shorthand:** Methods can be defined using shorthand syntax, where you omit the `property: function` syntax and define a named function directly in the object literal <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Getters and Setters:** The `get` and `set` keywords can be used to define getters and setters on an object <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   **`this` Keyword:** When a method is defined on an object, `this` refers to that object <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. However, if an arrow function syntax is used for a method, `this` will refer to the global context instead of the object it's defined on <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
*   **[[method_chaining_and_object_references | Method Chaining]]:** To chain method calls together, a method must return `this` (a reference to the parent object) <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.

## Object References

[[JavaScript memory management and garbage collection | JavaScript objects]] are kept as references in the heap memory <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. This means when an object is assigned to another variable, both variables reference the *same* object in memory, rather than creating a copy of the object's value (as is the case with primitives) <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>. Consequently, if a property on the referenced object is updated through one variable, the change will be visible through the other variable as well <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.

## Combining and Cloning Objects

*   **`Object.assign()`:** To clone an object's properties into a new object and avoid direct referencing, `Object.assign()` can be used <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>. This method takes a target object (often a new empty object) and one or more source objects, assigning all enumerable properties from the source(s) to the target <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. It only copies own enumerable properties and does not recursively deep copy nested objects; nested objects will still be copied by reference <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.
*   **Spread Syntax (`...`):** A better alternative for cloning and combining objects is the spread syntax <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>. It offers similar functionality to `Object.assign()` in most cases and often looks cleaner, especially when combining multiple objects <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.

## [[loops_and_iteration_over_objects | Iterating Over Objects]]

While iterating over arrays is straightforward, iterating over objects requires specific methods:

*   **`for...in` loop:** This loop iterates over all enumerable properties of an object, including those inherited from its prototypes <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>. Due to its inclusion of prototype properties, it can be confusing and is often avoided for simple iteration <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>.
*   **`Object.keys()`:** Returns an array of an object's own enumerable property *names* <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.
*   **`Object.values()`:** Returns an array of an object's own enumerable property *values* <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.
*   **`Object.entries()`:** Returns an array of `[key, value]` pairs (tuples) for an object's own enumerable properties <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. These tuples can be destructured directly in a loop <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

[[JavaScript objects and their properties | JavaScript objects]] are a core building block of the language, offering great flexibility <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>. For further learning, consider exploring [[object_oriented_programming_with_typescript | Object Oriented Programming with TypeScript]] concepts.