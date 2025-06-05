---
title: Console logging techniques in JavaScript
videoId: Mus_vwhTCq0
---

From: [[fireship]] <br/> 

[[javascript_basics_and_history | JavaScript]] is a programming language that has evolved significantly over time. Once considered a "toy" for front-end web development, [[javascript_basics_and_history | JavaScript]] in 2019 has become central, especially for startups doing the majority of their development on the front end, due to tools like the cloud, Docker, and various [[api_debugging_tools | APIs]] that abstract away back-end complexities <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. A fundamental skill for writing effective [[state_of_javascript_in_modern_development | modern JavaScript]] is knowing how to debug like a pro <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## Debugging with Console.log

The most common way to debug in [[javascript_basics_and_history | JavaScript]] is by using `console.log` <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. While simple, there are both good and bad ways to utilize it <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

### Displaying Multiple Variables Clearly

When logging multiple variables, simply logging them one after the other makes it difficult to know which variable corresponds to which output <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. A trick using *computed property names* allows you to add variables to an object and log them simultaneously. This not only reduces code but clearly labels the data with its variable name in the console <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

### Customizing Console Output with CSS

For important data, you can make console output stand out with custom CSS styling <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. By using `%c` in the string argument, you can substitute data and apply CSS styles defined in a subsequent argument <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. This allows for visually distinct messages, such as bold orange text <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

### Console.table for Tabular Data

If you have objects that share common properties, especially an array of objects, `console.table()` is highly useful for displaying them in a structured table format <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

### Benchmarking Performance with Console.time

To benchmark code performance, `console.time()` allows you to track execution time <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. You define a timer with a unique name using `console.time("name")`, execute the code you want to measure, and then call `console.timeEnd("name")` to display the elapsed time <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

### Tracing Function Calls with Console.trace

When you need to understand where a `console.log` (or any code within a function) originated, `console.trace()` can provide a stack trace <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. Adding `console.trace()` inside a function will log where that function was called from and what defined it, showing the call stack <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. This is useful for preventing accidental duplicate calls or understanding execution flow <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.