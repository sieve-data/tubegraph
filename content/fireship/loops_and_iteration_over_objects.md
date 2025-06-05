---
title: Loops and iteration over objects
videoId: napDjGFjHR0
---

From: [[fireship]] <br/> 

An object is conceptually similar to a dictionary or map, defined as a collection of properties where each property associates a key to a value <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. While [[modern_javascript_array_methods|looping over an array]] is straightforward <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>, there are specific methods for iterating over the properties of an object <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.

## Methods for Iterating Objects

### The `for...in` Loop

One option for iterating over an object's properties is to use a `for...in` loop <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
*   This loop iterates over all enumerable properties in the object, as well as its prototypes <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.
*   However, this behavior can be confusing, so `for...in` loops are often avoided for general object iteration <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>.

### `Object.keys()` and `Object.values()`

A more common and recommended approach is to obtain the object's keys or values as an array <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.
*   **`Object.keys()`**: Returns an array containing the names of all the object's own enumerable string properties <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.
*   **`Object.values()`**: Returns an array containing the values of all the object's own enumerable string properties <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.

Once you have the keys or values in an array, you can loop over them using a regular `for` loop or any of the built-in [[modern_javascript_array_methods|array methods]], such as `forEach` <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.

### `Object.entries()`

If you need to iterate over both the keys and values simultaneously, `Object.entries()` is the solution <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.
*   This method returns an array of "tuples" (arrays where each inner array contains a `[key, value]` pair) <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
*   You can then use destructuring to easily access the key and value variables within your loop <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.