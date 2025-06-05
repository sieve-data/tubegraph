---
title: Javas verbosity in code
videoId: m4-HM_sCvtQ
---

From: [[fireship]] <br/> 

Java is described as a [[java_as_a_boilerplate_driven_language | boilerplate driven language]] designed for writing verbose, [[Objectoriented programming in Java | object-oriented]] code <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Characteristics of Verbosity

The language was created to produce "instant legacy code" <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. Its verbosity is evident when compared to other languages like Python, where Java requires significantly more boilerplate <a class="yt-timestamp" data-t="01:47:48">[01:47:48]</a>. This extensive boilerplate is sarcastically presented as a "feature" rather than a "fundamental design flaw" <a class="yt-timestamp" data-t="01:49:50">[01:49:50]</a>.

## "Hello World" Example

To write a simple "Hello World" program in Java, a specific sequence of declarations is required:
1.  Before writing any code, one must declare `public static void main string args` <a class="yt-timestamp" data-t="01:25:57">[01:25:57]</a>.
2.  To print "Hello World", a class must be created <a class="yt-timestamp" data-t="01:32:00">[01:32:00]</a>. This is because Java enforces [[Objectoriented programming in Java | object-oriented programming]] principles <a class="yt-timestamp" data-t="01:33:00">[01:33:00]</a>.
3.  The `public static void main string args` declaration must then be included within the class <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>.
4.  Finally, the `system.out.printline` method is used to output "Hello World" <a class="yt-timestamp" data-t="01:44:00">[01:44:00]</a>.

This process demonstrates the significant amount of boilerplate code needed for even the most basic functionality in Java <a class="yt-timestamp" data-t="01:47:48">[01:47:48]</a>.

## Code Structure Implications

Users are advised to initially write one "giant bloated class" <a class="yt-timestamp" data-t="01:53:00">[01:53:00]</a>. When issues arise, this class is often broken down into a hierarchy of "deeply nested subclasses," which can make future refactoring impossible <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>.

> [!INFO]
> Despite its verbosity, Java is acknowledged as a language that "can get stuff done" and therefore "deserves our respect" <a class="yt-timestamp" data-t="02:14:00">[02:14:00]</a>.