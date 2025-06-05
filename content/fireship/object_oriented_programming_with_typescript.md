---
title: Object Oriented Programming with TypeScript
videoId: fsVL_xrYO0w
---

From: [[fireship]] <br/> 

Object-Oriented Programming (OOP) in TypeScript is an imperative approach to software development, providing a clear set of statements to follow to achieve a desired final state for an application <a class="yt-timestamp" data-t="04:07:22">[04:07:22]</a>. This contrasts with a functional or declarative approach, which focuses more on describing the state and logic rather than the explicit control flow <a class="yt-timestamp" data-t="04:12:28">[04:12:28]</a>.

While there is no single "correct" way to write code, and debating programming paradigms is like debating art with no absolutes, OOP offers a structured way to manage complexity, especially in larger applications <a class="yt-timestamp" data-t="01:12:35">[01:12:35]</a>.

## [[classes_and_inheritance_in_typescript | Classes in TypeScript]]

A class in TypeScript serves as a blueprint for instantiating objects <a class="yt-timestamp" data-t="04:22:15">[04:22:15]</a>. An instance of a class is an object with defined properties and methods <a class="yt-timestamp" data-t="04:29:43">[04:29:43]</a>.

### Constructor

The `constructor` is a special method within a class that runs once when an object is instantiated <a class="yt-timestamp" data-t="04:34:56">[04:34:56]</a>. Arguments passed to the constructor initialize the object's properties <a class="yt-timestamp" data-t="04:38:39">[04:38:39]</a>. To create an instance of a class, the `new` keyword is used before the class name <a class="yt-timestamp" data-t="04:48:08">[04:48:08]</a>.

### Public and Private Members

TypeScript introduces access modifiers like `public` and `private` for class members (properties and methods) <a class="yt-timestamp" data-t="04:58:39">[04:58:39]</a>:

*   **Public Members**: When using the `public` keyword in front of an argument in the constructor, TypeScript automatically sets that argument as a public property on each object instance <a class="yt-timestamp" data-t="05:01:21">[05:01:21]</a>. Public members are accessible both within the class and from any instances of the class <a class="yt-timestamp" data-t="05:09:59">[05:09:59]</a>. While convenient for directly mutating values on an object, excessive direct mutation of public properties can make code difficult to track and test <a class="yt-timestamp" data-t="05:17:41">[05:17:41]</a>.
*   **Private Members**: Members marked as `private` can only be used internally within the class definition <a class="yt-timestamp" data-t="05:54:11">[05:54:11]</a>. This allows for separation between a class's public API and its internal logic <a class="yt-timestamp" data-t="05:59:08">[05:59:08]</a>. For example, a value can be made immutable by making it private and providing a getter method for reading, but not changing, its value <a class="yt-timestamp" data-t="06:04:44">[06:04:44]</a>.

### Internal State

Class instances can maintain their own internal state <a class="yt-timestamp" data-t="06:14:14">[06:14:14]</a>. Methods can be defined to mutate these internal state values. This encapsulation of logic and state within a class provides a structured approach to managing data and behavior <a class="yt-timestamp" data-t="06:56:06">[06:56:06]</a>. TypeScript also automatically provides an interface and documentation for the class <a class="yt-timestamp" data-t="07:00:19">[07:00:19]</a>.

### Static Methods

Classes can define `static` methods, which are unique because they belong to the class itself, not to an instance of the class <a class="yt-timestamp" data-t="07:07:08">[07:07:08]</a>. Static methods can function as pure functions, meaning their output depends only on their inputs, and the class can be used as a namespace to run these functions <a class="yt-timestamp" data-t="07:17:09">[07:17:09]</a>.

### [[prototypal_inheritance_in_javascript | Prototypal Inheritance in JavaScript]]

It's important to note that classes in JavaScript are essentially syntactic sugar for functions and [[prototypal_inheritance_in_javascript | prototypal inheritance]] <a class="yt-timestamp" data-t="05:31:07">[05:31:07]</a>. When compiled to ES3, JavaScript classes are shown to be functions with a closure that prevents local variables from "bleeding out" into the global scope <a class="yt-timestamp" data-t="05:38:52">[05:38:52]</a>.

## [[classes_and_inheritance_in_typescript | Inheritance]] vs. Composition

For code reusability, a common debate in OOP is between [[classes_and_inheritance_in_typescript | inheritance]] and composition <a class="yt-timestamp" data-t="07:29:05">[07:29:05]</a>.

### [[classes_and_inheritance_in_typescript | Inheritance]]

With [[classes_and_inheritance_in_typescript | inheritance]], you start with a larger base class, and then child classes inherit all its functionality, overriding or extending it with custom behaviors <a class="yt-timestamp" data-t="07:41:26">[07:41:26]</a>. In TypeScript, this is achieved with the `extends` keyword (e.g., `SuperHuman extends Human`) <a class="yt-timestamp" data-t="08:24:26">[08:24:26]</a>. The child class's constructor will often call `super()` to execute the parent class's constructor <a class="yt-timestamp" data-t="08:31:08">[08:31:08]</a>. While powerful, deeply nested class hierarchies can make debugging difficult <a class="yt-timestamp" data-t="09:02:40">[09:02:40]</a>.

### Composition

Composition, on the other hand, breaks down interfaces and logic into smaller, independent pieces, and then builds up larger functions or objects by combining these pieces <a class="yt-timestamp" data-t="07:51:30">[07:51:30]</a>. This can be achieved in various ways:

*   **Concatenating Objects / Mixins**: This involves decoupling properties or behaviors into objects or functions that return objects, then merging these objects to create a final function or object <a class="yt-timestamp" data-t="09:28:44">[09:28:44]</a>. This is often referred to as a mixin pattern, a type of multiple [[classes_and_inheritance_in_typescript | inheritance]] <a class="yt-timestamp" data-t="09:44:59">[09:44:59]</a>. While powerful, this approach might lose some of the ergonomics of class-based OOP <a class="yt-timestamp" data-t="09:56:07">[09:56:07]</a>.
*   **Class-based Mixins in TypeScript**: TypeScript offers the flexibility to use mixins in a class-based format <a class="yt-timestamp" data-t="10:05:31">[10:05:31]</a>. This involves creating small "behavior" classes that define individual functionalities, focusing on "what something does" rather than "what something is" <a class="yt-timestamp" data-t="10:16:03">[10:16:03]</a>. Instead of `extends`, a class can `implement` multiple classes. Implementing a class means being concerned only with its interface, not its underlying code <a class="yt-timestamp" data-t="10:33:04">[10:33:04]</a>. A helper function (like `applyMixins` from TypeScript Docs) is then used to apply the code from the implemented classes to the base class <a class="yt-timestamp" data-t="10:43:08">[10:43:08]</a>. This approach often requires explicit type annotations for return values on methods <a class="yt-timestamp" data-t="10:51:02">[10:51:02]</a>.