---
title: Object destructuring and template literals
videoId: Mus_vwhTCq0
---

From: [[fireship]] <br/> 

Modern JavaScript offers features like object destructuring and template literals to make code more concise and efficient <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

## Object Destructuring

Object destructuring is a technique used to eliminate repetition when working with object properties <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. Instead of repeatedly referencing an object to access its properties (e.g., `animal.name`, `animal.age`), you can destructure the object to pull out specific properties into their own variables <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

### Destructuring in Function Arguments

If a function takes an object as an argument but only needs a few of its properties, those properties can be destructured directly in the function's argument list <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. This involves wrapping the desired property names in curly braces `{}` within the argument signature <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

```javascript
function feedAnimal({ name, type, diet }) {
  // Now name, type, and diet can be used directly
  return `${name} the ${type} eats ${diet}.`;
}
```
This approach makes the code more readable and easier to maintain, especially when dealing with large objects that have many properties <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

### Alternative Destructuring

Another way to destructure an object is to pass the entire object as an argument and then use a `const` variable within the function to destructure the properties <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

```javascript
function feedAnimal(animal) {
  const { name, type, diet } = animal; // Destructure properties
  return `${name} the ${type} eats ${diet}.`;
}
```
This method can be preferable if you need to destructure multiple objects within a single [[functions_and_closures_in_javascript | function]] <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.

## Template Literals

Template literals are a feature in modern JavaScript that provide a more flexible and readable way to work with strings compared to older string concatenation methods <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.

### Basic Interpolation

Historically, building strings in JavaScript often involved cumbersome string concatenation using the `+` operator, requiring careful management of spaces and variables <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>. Template literals solve this by allowing values to be interpolated directly into the string <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

Template literals are defined using backticks (`` ` ``) instead of single or double quotes <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. Variables or expressions can be embedded within the string using the `${expression}` syntax <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.

```javascript
const name = "Pikachu";
const type = "Electric";
const diet = "berries";

// Using object destructuring and template literals together
function feedAnimal({ name, type, diet }) {
  return `${name} the ${type} eats ${diet}.`;
}

console.log(feedAnimal({ name: "Pikachu", type: "Electric", diet: "berries" }));
// Output: Pikachu the Electric eats berries.
```
This makes strings significantly more readable and easier to maintain <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.

### Tagged Template Literals

Template literals can also be "tagged," allowing for strings to be built in a purely functional way <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. A tagged template literal involves placing a [[functions_and_closures_in_javascript | function]] name directly before the backtick-enclosed string <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

When a template literal is tagged with a function, the function receives the string segments as its first argument (an array of strings) and then any interpolated expressions as subsequent arguments <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.

```javascript
function horseAge(strings, age) {
  const ageCategory = age > 5 ? "old" : "young";
  return `${strings[0]}${ageCategory}${strings[1]}`;
}

const horse = { age: 7 };
const description = horseAge`This horse is an ${horse.age} animal.`;
console.log(description);
// Output: This horse is an old animal.
```
This powerful concept is used for advanced templating, such as in the Polymer project via the lit-HTML library <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.