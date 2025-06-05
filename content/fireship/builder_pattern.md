---
title: Builder pattern
videoId: tv-_1er1mWI
---

From: [[fireship]] <br/> 

The Builder pattern is a [[software_design_patterns | software design pattern]] that allows for the step-by-step construction of a complex object <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. Instead of using a single constructor to define all properties at once, the Builder pattern employs methods to add components of the object incrementally <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

## How it Works
With the Builder pattern, an object is created method by method, rather than solely through its constructor <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. This approach makes it easier to manage many configuration options for an object <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. The logic for building the object can even be delegated to an entirely separate class <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

### Method Chaining
In languages like JavaScript, each building method typically returns `this` (a reference to the current object instance) <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. This enables "method chaining," where multiple builder methods can be called sequentially on the same object instance, with the object being returned after each step <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

### Analogy: The Hot Dog Stand
Imagine running a hot dog stand <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. When a customer orders, instead of listing all ingredients at once to a constructor, they specify each desired topping using separate methods (e.g., `addMustard()`, `addKetchup()`) <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. This makes it easier to track and defer each step of the order <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

## Usage and Trends
The Builder pattern is frequently encountered in libraries, such as jQuery <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>. However, in recent years, its popularity has somewhat declined <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.