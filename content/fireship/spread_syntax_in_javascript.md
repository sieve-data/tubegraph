---
title: Spread syntax in JavaScript
videoId: Mus_vwhTCq0
---

From: [[fireship]] <br/> 

The spread syntax (`...`) in [[JavaScript data types and control flow | JavaScript]] is a modern feature that enhances code conciseness, readability, and maintainability when working with objects and arrays <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. It allows you to expand an iterable (like an array) or an object into individual elements or properties.

## Spread Syntax with Objects

The spread syntax provides a more concise way to combine or update object properties compared to older methods <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.

### Prior Methods (and their drawbacks)

*   **Manual Property Assignment**: Traditionally, one might assign properties from one object to another one by one <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>. This approach is "ugly and verbose" <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a> and, more importantly, it **mutates** the original object, which can lead to unpredictable code <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.
*   **`Object.assign()`**: A better approach to merge objects immutably is `Object.assign()`, which takes the original object and merges it with other objects provided as arguments <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>. Properties are merged from left to right, meaning later arguments override earlier ones <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

### Using Spread Syntax for Objects

The spread syntax allows you to create a new object by placing existing objects within it using three dots (`...`) in front of them <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.

Similar to `Object.assign()`, when composing a new object, properties are merged from left to right, with properties farthest to the right having priority <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

<pre><code class="language-js">
const pokemon = { name: 'Pikachu', type: 'electric' };
const stats = { hp: 35, attack: 55, defense: 40 };

// Using spread syntax to create a new object with combined properties
const pikachuWithStats = { ...pokemon, ...stats };
console.log(pikachuWithStats);
// { name: 'Pikachu', type: 'electric', hp: 35, attack: 55, defense: 40 }

// Updating a single property while creating a new object
const leveledUpPikachu = { ...pikachuWithStats, hp: 45 };
console.log(leveledUpPikachu);
// { name: 'Pikachu', type: 'electric', hp: 45, attack: 55, defense: 40 }
</code></pre>

This method is largely "syntactic sugar" but significantly improves code readability and maintainability <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.

## Spread Syntax with Arrays

The spread syntax can also be used on arrays, providing a concise way to add, combine, or reorder elements <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.

### Prior Methods (and their drawbacks)

*   **`push()`**: Historically, new items would be added to an array one by one using the `push()` method <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

### Using Spread Syntax for Arrays

The spread syntax allows you to reduce multiple lines of code into one when adding items to an array <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.

*   **Appending Items (like `push`)**: By placing the spread array first (`...originalArray`), followed by the new items, you effectively append them to the end of the array <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.
*   **Prepending Items (like `unshift`)**: By placing the new items first, followed by the spread array, you add them to the beginning of the array <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.
*   **Inserting in the Middle**: The spread syntax offers even more flexibility, allowing you to splice values directly into the middle of an array <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.

<pre><code class="language-js">
let strings = ['apple', 'banana'];

// Appending items (like push)
strings = [...strings, 'cherry', 'date'];
console.log(strings); // ['apple', 'banana', 'cherry', 'date']

// Prepending items (like unshift)
strings = ['grape', ...strings];
console.log(strings); // ['grape', 'apple', 'banana', 'cherry', 'date']

// Inserting in the middle
strings = ['grape', 'fig', ...strings.slice(1)]; // Example: remove 'apple', add 'fig'
console.log(strings); // ['grape', 'fig', 'banana', 'cherry', 'date']
</code></pre>

### Trailing Commas

Modern [[JavaScript data types and control flow | JavaScript]] tolerates trailing commas in array and object literals, which used to cause errors <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. This is now considered good practice as it reduces the number of lines that appear to change in version control commits when adding or reordering elements <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.