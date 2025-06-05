---
title: JavaScript template literals
videoId: Mus_vwhTCq0
---

From: [[fireship]] <br/> 

Template literals are a modern [[javascript_fundamentals_and_practical_concepts | JavaScript]] feature that offer an improved way to work with strings, solving issues commonly found with older string concatenation methods <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.

## String Interpolation

Before template literals, string concatenation often involved cumbersome syntax like `variable + "string" + expression + "other stuff"`, which required manual management of spaces and was annoying to deal with <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

Template literals allow for direct interpolation of values into a string <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. They are defined using backticks (`` ` ``) <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. Variables or expressions can be embedded within the string using the `${}` (dollar sign brackets) syntax <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.

For example, when combined with [[spread_syntax_in_javascript | object destructuring]], template literals can make strings much more readable and easier to maintain compared to repetitive property access <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

```javascript
// Old way (string concatenation)
const animal = { species: 'Horse', age: 7, name: 'Bojack' };
console.log("Feed " + animal.name + " the " + animal.species + " who is " + animal.age + " years old.");
// -> Feed Bojack the Horse who is 7 years old.

// Modern way (template literals with object destructuring)
function feedAnimal({ name, species, age }) {
  return `Feed ${name} the ${species} who is ${age} years old.`; <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>
}
console.log(feedAnimal(animal));
// -> Feed Bojack the Horse who is 7 years old.
```

## Tagged Templates

Template literals can also be used to build strings in a purely functional way through "tagged templates" <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. This involves attaching a function directly to a template literal, rather than passing a regular argument to the function <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

When a template literal is tagged with a function:
*   The function's first argument will be an array of string segments (the parts of the string *outside* the `${}` expressions) <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
*   Subsequent arguments will be the values or expressions from inside the `${}` in the order they appear <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

This allows for a single argument to compose multiple values in the return string <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>. It is considered a powerful concept for templating and is utilized in projects like Polymer via the lit-html library <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

```javascript
function horseAge(strings, age) {
  const isOld = age > 5 ? 'old' : 'young'; <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>
  return `${strings[0]}${isOld}${strings[1]}`; <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>
}

const animalAge = 7;
const status = horseAge`This animal is ${animalAge} and is `; <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>
console.log(status);
// -> This animal is old and is
```