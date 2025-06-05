---
title: Closures and recursion in JavaScript
videoId: gigtS_5KOqo
---

From: [[fireship]] <br/> 

[[javascript_function_basics_and_anatomy | Functions]] are considered the backbone of JavaScript development and mastering them is crucial for understanding the language <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. This article will delve into two advanced concepts: [[functions_and_closures_in_javascript | closures]] and recursion.

## [[functions_and_closures_in_javascript | Closures]]

A key concept in understanding [[functions_and_closures_in_javascript | closures]] is the **lexical environment** <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>. When a [[javascript_function_basics_and_anatomy | function]] is defined, it creates its own lexical environment <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>. Anything within curly braces (`{}`) represents its own lexical environment <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>. An inner [[javascript_function_basics_and_anatomy | function]]'s lexical environment includes its own local [[variables_and_scope_in_javascript | variables]] and a reference to the outer environment, which encompasses the outer [[javascript_function_basics_and_anatomy | function]] and the global script <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.

This means that an inner [[javascript_function_basics_and_anatomy | function]] can "remember" the local [[variables_and_scope_in_javascript | variables]] defined in its outer [[javascript_function_basics_and_anatomy | function]] <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>. Conversely, the outer [[javascript_function_basics_and_anatomy | function]] cannot access the local [[variables_and_scope_in_javascript | variables]] of the inner [[javascript_function_basics_and_anatomy | function]] <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.

Historically, before [[functions_closures_and_the_concept_of_this | arrow functions]], every new [[javascript_function_basics_and_anatomy | function]] had its own `this` context based on how it was called <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>. To consistently reference `this` inside nested [[javascript_function_basics_and_anatomy | functions]], older code might define a `self` variable equal to `this`, which JavaScript would then "close over" <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>. [[functions_closures_and_the_concept_of_this | Arrow functions]] remove this "ridiculousness" because they do not have their own `this` object <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>, inheriting `this` from their enclosing scope.

### Practical Example: `useCat` Hook

A practical example of a [[functions_and_closures_in_javascript | closure]] is a [[javascript_function_basics_and_anatomy | function]] like `useCat`, loosely inspired by React Hooks <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.

The outer [[javascript_function_basics_and_anatomy | function]] (`useCat`) establishes its own lexical environment and defines local [[variables_and_scope_in_javascript | variables]], such as a default name <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>. It then returns an array containing two different [[javascript_function_basics_and_anatomy | functions]] <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>:
1.  A getter [[javascript_function_basics_and_anatomy | function]] that retrieves the name and prefixes it <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.
2.  A setter [[javascript_function_basics_and_anatomy | function]] that takes a new name as an argument and updates the name in the outer [[javascript_function_basics_and_anatomy | function]]'s scope <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>.

```javascript
function useCat() {
  let name = 'Whiskers'; // Local variable in outer function
  return [
    function getName() {
      return `Meow, I'm ${name}`;
    },
    function setName(newName) {
      name = newName;
    }
  ];
}

const [getName, setName] = useCat();
console.log(getName()); // Meow, I'm Whiskers
setName('Mittens');
console.log(getName()); // Meow, I'm Mittens
```

The crucial aspect here is that the inner [[javascript_function_basics_and_anatomy | functions]] (the getter and setter) within the returned array retain access to and can manipulate the `name` [[variables_and_scope_in_javascript | variable]] from the outer `useCat` [[javascript_function_basics_and_anatomy | function]]'s lexical environment <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>. This demonstrates how [[functions_and_closures_in_javascript | closures]] allow inner [[javascript_function_basics_and_anatomy | functions]] to remember the state of their outer scope. [[functions_and_closures_in_javascript | Closures]] are frequently encountered in interview questions and real-world development <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.

## Recursion

Recursion in JavaScript involves defining a [[javascript_function_basics_and_anatomy | function]] that calls itself by name within its own [[javascript_function_basics_and_anatomy | function]] body <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>. When a recursive [[javascript_function_basics_and_anatomy | function]] encounters a call to itself, it pushes another instance of that [[javascript_function_basics_and_anatomy | function]] onto the call stack <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.

Without a defined **stopping condition**, a recursive [[javascript_function_basics_and_anatomy | function]] will run indefinitely, leading to an infinite loop and eventually a "Stack Overflow" error <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>.

### Practical Example: Filesystem Traversal

Recursive algorithms are highly efficient for traversing tree-like data structures <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>, such as a computer's filesystem.

Using Node.js, the `fs` (file system) module allows reading files on the local system <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>. Consider a `traverse` [[javascript_function_basics_and_anatomy | function]] that takes a directory path:

```javascript
const fs = require('fs');
const path = require('path');

function traverse(dirPath) {
  // Ensure it's a directory
  const stats = fs.statSync(dirPath);
  if (!stats.isDirectory()) {
    return; // Stopping condition: if it's not a directory, stop
  }

  // Read directory contents
  const items = fs.readdirSync(dirPath);

  // Stopping condition: if no subfolders exist
  if (!items || items.length === 0) {
    return;
  }

  // Loop over items and recursively call traverse for subfolders
  items.forEach(item => {
    const itemPath = path.join(dirPath, item);
    traverse(itemPath); // Recursive call
  });
}

// Start the traversal from the current working directory
traverse(process.cwd());
```

In this example:
*   The [[javascript_function_basics_and_anatomy | function]] checks if the given path is a directory and returns if not <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>.
*   It reads the contents of the directory, which provides an array of subfolders (or `undefined`) <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.
*   A crucial stopping condition is added: if no subfolders exist, the [[javascript_function_basics_and_anatomy | function]] stops recursing <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.
*   If subfolders are found, the [[javascript_function_basics_and_anatomy | function]] iterates over them using `forEach` and calls itself (`traverse`) for each subfolder <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>. This self-referential call makes it a recursive [[javascript_function_basics_and_anatomy | function]] <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.

To fully grasp these concepts, extensive practice is recommended <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>.