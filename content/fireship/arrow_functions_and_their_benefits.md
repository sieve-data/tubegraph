---
title: Arrow functions and their benefits
videoId: gigtS_5KOqo
---

From: [[fireship]] <br/> 

[[javascript_function_basics_and_anatomy | Functions]] are fundamental to [[javascript_fundamentals_and_practical_concepts | JavaScript]] development <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. Among the ways to define functions, the arrow syntax provides a compact and concise alternative, offering more than just [[new_javascript_features_in_2020 | syntactic sugar]] <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>, <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.

## Arrow Function Syntax

To define an arrow function, you start with a variable to name it, followed by parentheses for parameters, and then an arrow (`=>`) pointing to the function body <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

```javascript
const myFunction = (parameter1, parameter2) => {
  // Function body
};
```

## Implicit Return

One notable feature of arrow functions is the implicit return <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. If the function body consists of a single expression, you can omit the curly braces, and the result of that expression will be automatically returned <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. This can reduce multiple lines of code to a single line <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

```javascript
// Before
const add = (a, b) => {
  return a + b;
};

// After (Implicit Return)
const add = (a, b) => a + b;
```

If the function requires additional logic or multiple statements, curly braces can still be used, but a `return` statement will then be necessary to return a value <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>, <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

## Arrow Functions as Expressions

Arrow functions are always expressions <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. This means they cannot be simply declared like a traditional [[function_declarations_vs_expressions_in_javascript | function declaration]] <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>. They must be assigned to a variable or used where a value is expected.

## Lexical `this` Binding

A significant characteristic of arrow functions is that they do not have their own `this` object <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

Before arrow functions, every new function created its own `this` context based on how it was called <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>. This often led to patterns where developers would define a variable, typically named `self` or `_this`, and assign `this` to it to maintain context consistently across nested functions, leveraging [[functions_and_closures_in_javascript | JavaScript's closure]] mechanism <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>, <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.

```javascript
// Old pattern before arrow functions
function MyObject() {
  this.value = 10;
  const self = this; // Capture 'this'
  setTimeout(function() {
    console.log(self.value); // Uses captured 'self'
  }, 1000);
}
```

With arrow functions, this "ridiculousness" is no longer needed <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. Arrow functions inherit the `this` value from their enclosing lexical context <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.

```javascript
// Modern pattern with arrow functions
function MyObject() {
  this.value = 10;
  setTimeout(() => {
    console.log(this.value); // 'this' refers to MyObject
  }, 1000);
}
```

This behavior simplifies code, especially in object-oriented programming or when dealing with [[rxjs_operators_and_their_usage | callbacks]].

## Preferred Usage

In modern [[javascript_fundamentals_and_practical_concepts | JavaScript]], it's generally preferred to use arrow functions when possible <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>. They combine well with [[modern_javascript_array_methods | array methods]] like `map`, allowing for powerful operations in a single line of code <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>, <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>. While functional techniques using arrow functions may be less performant than traditional `for` loops in some cases, this difference is often negligible in most applications <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>, <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.