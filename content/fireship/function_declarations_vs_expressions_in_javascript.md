---
title: Function declarations vs expressions in JavaScript
videoId: gigtS_5KOqo
---

From: [[fireship]] <br/> 

[[Functions and closures in JavaScript | Functions]] are fundamental to JavaScript development, often considered the backbone of the language <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. Mastering them can make understanding other concepts in the language relatively easy <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Function Anatomy
Whether using a declaration or an expression, the core anatomy of a [[JavaScript function basics and anatomy | JavaScript function]] remains similar:
*   **`function` keyword**: Used to declare a function <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   **Name**: A readable name should be chosen for the function <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. Naming things in computer science is notoriously difficult <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
*   **Parentheses `()`**: Used to define any [[Variables and scope in JavaScript | parameters]] (inputs) the function will take <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
    *   A [[Variables and scope in JavaScript | parameter]] acts as a [[Variables and scope in JavaScript | variable]] that the function can access when called <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   **Curly braces `{}`**: Enclose the function body, where all the logic is defined <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
    *   The function body typically either performs a task (e.g., `console.log`) or returns a value <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
    *   If no `return` statement is present, a function implicitly returns `undefined` <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
    *   A `return` statement allows a value calculated inside the function to be used elsewhere, potentially assigned to a [[Variables and scope in JavaScript | variable]] <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

### Calling a Function
To execute a declared function, it must be called <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. This is done by referencing its name followed by parentheses, passing actual values as [[Variables and scope in JavaScript | arguments]] for its [[Variables and scope in JavaScript | parameters]] <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

**Parameters vs. Arguments**
*   **[[Variables and scope in JavaScript | Parameters]]**: The [[Variables and scope in JavaScript | variable]] inputs defined in the function definition <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **[[Variables and scope in JavaScript | Arguments]]**: The actual values or expressions used when calling the function <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

## Function Declaration
A function declaration (also known as a function definition or statement) is the standard way to define a named function <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

```javascript
function greet(name) { // 'function' keyword, name, parameters
  console.log(`Hello, ${name}!`); // function body
}

greet("World"); // Calling the function with an argument
```

### Hoisting
A key characteristic of function declarations is that they are **hoisted** <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. This means the function declaration is moved to the top of its scope by the JavaScript engine before code execution <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>. Consequently, you can call a function declaration *before* it is defined in the code <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

```javascript
sayHi("Alice"); // This works because sayHi is hoisted
function sayHi(person) {
  console.log(`Hi, ${person}!`);
}
```

## Function Expression
A function expression involves using a function as a value <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. This typically means assigning an anonymous function (a function without a name) to a [[Variables and scope in JavaScript | variable]] <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

```javascript
const greetExpression = function(name) { // Assigning an anonymous function to a variable
  console.log(`Hello from expression, ${name}!`);
};

greetExpression("Bob"); // Calling the function via the variable name
```

### No Hoisting
Unlike declarations, function expressions are **not hoisted** <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. The function is not created until that specific line of code is reached during script execution <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. Attempting to call a function expression before its definition will result in an error <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

```javascript
// greetExpressionBefore("Charlie"); // This would cause an error: ReferenceError: Cannot access 'greetExpressionBefore' before initialization

const greetExpressionBefore = function(person) {
  console.log(`Hi from expression, ${person}!`);
};
greetExpressionBefore("Charlie"); // This works
```

### Immediately Invoked Function Expression (IIFE)
A special type of function expression is an Immediately Invoked Function Expression (IIFE) <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. This involves wrapping an anonymous function in parentheses and then calling it immediately with another set of parentheses <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.

```javascript
(function() {
  console.log("This function runs immediately!");
})(); // The outer parentheses make it an expression, the inner ones call it
```

This pattern is useful for creating a private scope for [[Variables and scope in JavaScript | variables]], preventing them from polluting the global namespace <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. The suggested best practice for IIFE syntax is to wrap the *entire invocation* in parentheses, like `(function() { /* ... */ })();` <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

## Arrow Functions
Arrow functions, introduced in ES6, provide a more compact and concise way to write [[JavaScript function basics and anatomy | functions]] <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. They are a type of function expression.

```javascript
const greetArrow = (name) => { // Variable, parameters in parentheses, arrow, function body
  console.log(`Hello from arrow, ${name}!`);
};

greetArrow("David");
```

### Implicit Return
If an arrow function's body consists of a single expression, you can omit the curly braces, and it will implicitly return the result of that expression <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. This can reduce multiple lines of code to a single line <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

```javascript
const add = (a, b) => a + b; // Implicitly returns a + b
console.log(add(2, 3)); // 5
```

If the function body requires multiple statements, curly braces are necessary, and an explicit `return` statement will be needed to return a value <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

### Key Characteristics of Arrow Functions
*   **Always Expressions**: Arrow functions are always function expressions; you cannot simply declare an arrow function without assigning it to a [[Variables and scope in JavaScript | variable]] <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
*   **No `this` Binding**: Arrow functions do not have their own `this` object <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>. Instead, they inherit `this` from the enclosing lexical context. This is a significant difference from traditional `function` declarations/expressions, where `this` binding depends on how the function is called <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>. This eliminates the need for patterns like `const self = this;` in older code to maintain `this` context <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.

## Best Practices
While there's no universal "best practice" for choosing between function declarations and expressions <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>, many developers today lean towards function expressions, especially arrow functions <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

*   **Predictability**: Because function expressions are not hoisted, it can make it easier to understand their place in the application's context and their dependencies <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
*   **Global Namespace**: Function expressions are less likely to accidentally pollute the global namespace <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.
*   **Conciseness**: Arrow functions offer a more concise syntax, especially for simple [[JavaScript function basics and anatomy | functions]] <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.
*   **`this` Context**: Arrow functions' lexical `this` binding can simplify code by avoiding unexpected `this` context issues <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.

For modern JavaScript, preferring arrow function syntax when possible is a common recommendation <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.