---
title: JavaScript debugging techniques
videoId: Mus_vwhTCq0
---

From: [[fireship]] <br/> 

[[JavaScript]] is a programming language that some people have historically "loved to hate" <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. While it was once considered a "toy" for web development <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>, modern tools like the cloud, Docker, and various APIs have abstracted away much of the complexity of backend development <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. Today, much development, especially [[JavaScript and Frontend Development | front-end development]], relies heavily on [[JavaScript]] <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

To write effective [[JavaScript]], it's essential to understand modern features and avoid less efficient practices <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. A fundamental skill for any [[JavaScript]] developer is debugging <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## Console Logging

The most common way to debug [[JavaScript]] is by using `console.log()` <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. While simple, there are both good and bad ways to utilize it <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

### Identifying Variables with Computed Property Names
When logging multiple variables, it can be difficult to know which variable corresponds to which output <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. A trick using *computed property names* involves adding variables to an object before logging <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. This approach reduces code footprint and clearly identifies the variable source of the data <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

```javascript
const obj1 = { id: 1 };
const obj2 = { name: 'test' };
const obj3 = { value: 100 };

// Bad way: Unclear output
console.log(obj1);
console.log(obj2);
console.log(obj3);

// Good way: Clear output using computed property names
console.log({ obj1, obj2, obj3 });
// Output: { obj1: { id: 1 }, obj2: { name: 'test' }, obj3: { value: 100 } }
```

### Customizing Console Output with CSS
For important data, you can make console logs stand out using custom CSS styling <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. This is achieved by using a `%c` placeholder in the string and providing the CSS style as a second argument <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

```javascript
console.log("%cThis is important data!", "color: orange; font-weight: bold;");
```

### Displaying Data as a Table with `console.table()`
When working with arrays of objects that share common properties, `console.table()` is highly useful <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. It displays the data in a clear, tabular format <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

```javascript
const animals = [
    { name: 'Lion', age: 5 },
    { name: 'Tiger', age: 3 },
    { name: 'Bear', age: 7 }
];
console.table(animals);
```

### Benchmarking Performance with `console.time()`
To benchmark the performance of code execution, you can use `console.time()` and `console.timeEnd()` <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. Start a timer with `console.time('timerName')` and end it with `console.timeEnd('timerName')` to log the elapsed time <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

```javascript
console.time('looper');
let i = 0;
while (i < 1000000) {
    i++;
}
console.timeEnd('looper'); // Logs the time taken for the loop to complete
```

### Tracing Function Calls with `console.trace()`
If you need to understand where a `console.log()` originated or how a specific function was called, `console.trace()` can provide a stack trace <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. This is particularly helpful for debugging unexpected function calls <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. It will show the call stack, indicating which lines defined and called the function <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

```javascript
function deleteItemFromDatabase() {
    console.trace('deleteItemFromDatabase was called!');
    // ... actual deletion logic
}

function processOrder() {
    deleteItemFromDatabase();
}

processOrder();
// console.trace will show the call stack leading to deleteItemFromDatabase
```