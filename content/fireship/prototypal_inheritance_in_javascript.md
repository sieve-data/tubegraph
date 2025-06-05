---
title: Prototypal inheritance in JavaScript
videoId: napDjGFjHR0
---

From: [[fireship]] <br/> 

In JavaScript, objects are fundamental, with anything that is not a [[javascript_objects_and_their_properties | primitive data type]] being an object <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. Objects are collections of properties, where each property associates a key to a value <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. Understanding how objects inherit properties is crucial for deeper comprehension of the language <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

## Object Creation with Prototypes

While objects can be created using literal syntax (`{}`) <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a> or constructor syntax (`new Object()`) <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>, the `Object.create()` static method allows for explicit prototypal inheritance <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. This method is most useful when you want a new object to inherit properties from an existing object, using the existing object as its prototype <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

```javascript
const organism = {
  dna: Math.random() // Contains a DNA property of a random number
};

// Create a new object using organism as the prototype
const newObject = Object.create(organism);

console.log(newObject); // {} - appears blank initially
console.log(newObject.dna); // Accesses the DNA property from the prototype
```
<a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>
When `newObject` is created with `Object.create(organism)`, it appears to be a blank object if simply logged <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. However, if you attempt to access a property like `dna` on `newObject`, it successfully retrieves the value from the `organism` prototype <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. This demonstrates that the property is "invisible" on the new object itself but exists on its prototype <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

### Checking the Prototype

To confirm where a property lives, you can use `Object.getPrototypeOf()` which returns the original prototype object <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

```javascript
Object.getPrototypeOf(newObject); // Returns the 'organism' object
```
<a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>

> [!NOTE]
> This behavior of prototypal inheritance is described as one of the "weirder parts of JavaScript" <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

## Property Descriptors and Inheritance

While not commonly used by casual users, `Object.defineProperty()` allows for advanced control over object properties through a descriptor object <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. This method can define properties with specific attributes like `value`, `writable`, `enumerable`, and `configurable`, influencing how they behave and are inherited or copied <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. Understanding it is important for a deep understanding of the language <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

## Cloning Objects and Inheritance

When combining or cloning objects, it's crucial to understand how references and inheritance interact.

### Object References vs. Values
[[javascript_objects_and_their_properties | JavaScript objects]] are stored as references in the heap, unlike [[variable_declaration_and_scope_in_javascript | primitive values]] which are typically short-lived in the call stack <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. This means that if you assign one object variable to another, both variables reference the *same* underlying object in memory <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>. Changes made through one variable will be reflected in the other <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.

### Object.assign()
To clone an object's properties into a new object, `Object.assign()` can be used <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. It copies only the *own enumerable properties* of a source object to a target object <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.

*   `Object.assign()` does **not** copy properties inherited from higher up in the prototype chain <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
*   It performs a shallow copy: if an object's property references another object, that nested object is still copied by reference, not recursively deep-copied <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

You can inspect which properties would be copied using `Object.getOwnPropertyNames()`, which returns an array of all property names directly owned by an object <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.

### Spread Syntax
The spread syntax (`...`) offers a cleaner alternative to `Object.assign()` for combining or cloning objects, with very minor differences in most cases <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>. It also performs a shallow copy.

## Looping Over Object Properties

When iterating over an object's properties, it's important to consider inheritance:

*   **`for...in` loop:** This loop iterates over all *enumerable properties* of an object, including those inherited from its prototypes <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>. This behavior can be confusing and is often avoided <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>.
*   **`Object.keys()` and `Object.values()`:** These methods return an array of an object's *own enumerable property names* or *values*, respectively <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>. These arrays can then be iterated using standard array methods like `forEach` <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.
*   **`Object.entries()`:** This method returns an array of key-value pairs (tuples) for an object's *own enumerable properties*, which can be destructured in a loop <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.

## Constructor Functions and Classes

Historically, JavaScript objects were instantiated using **constructor functions** <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>. By convention, constructor functions are capitalized <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. Inside a constructor function, `this` refers to the new object being created <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>, allowing properties and methods to be defined on it <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.

```javascript
function Zombie(name) {
  this.name = name;
  this.created = new Date();
  this.bite = function() {
    console.log(`${this.name} bites!`);
    return this; // Allows method chaining
  };
}

const myZombie = new Zombie('Braindead');
myZombie.bite();
```
<a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>

A constructor function is similar to a class in [[Object Oriented Programming with TypeScript | object-oriented programming languages]] <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>. In modern JavaScript, the `class` keyword is syntactic sugar over these underlying constructor functions, simplifying the process of creating and instantiating new objects <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>. The core concept remains that a function instantiates or creates a new object <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.