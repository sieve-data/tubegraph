---
title: Java as a boilerplate driven language
videoId: m4-HM_sCvtQ
---

From: [[fireship]] <br/> 

Java is described as a boilerplate-driven language, intended for writing verbose, [[Objectoriented programming in Java | object-oriented]] code that can become instant legacy code <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Characteristics
Java is known for its verbosity <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. The extensive boilerplate is humorously presented as a "feature" rather than a "fundamental design flaw" <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

## Setting Up and Running Java
Before writing any code, it is necessary to install the JDK, [[Java runtime environment and just in time compilation | JRE]], and [[Java virtual machine and platform independence | JVM]] on a machine, which might take a few days <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. Reading error logs is also a common task, and a vertical monitor is recommended for this purpose <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

### Core Boilerplate Phrases
A common phrase developers learn is "public static void main string args" <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. This specific line is essential for the entry point of many Java applications.

### Creating a Basic Program
To write a "Hello World" program, Java requires creating a class <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. This is because Java "forces" developers into [[Objectoriented programming in Java | object-oriented programming]] <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. Before proceeding, it's suggested that one might need to read "design patterns cover to cover" <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

The structure for a "Hello World" program includes:
*   The `public static void main string args` method <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   A `System.out.println` statement for the output <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

This results in significantly more boilerplate compared to languages like Python for a simple task <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

## Design Practices
Initially, developers might write "one giant bloated class" <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. When issues arise, this might be broken down into a "hierarchy of deeply nested subclasses" <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>, which can make future refactoring impossible <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.