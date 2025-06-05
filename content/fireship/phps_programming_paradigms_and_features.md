---
title: PHPs programming paradigms and features
videoId: a7_WFUlFS94
---

From: [[fireship]] <br/> 

PHP is a dynamic, interpreted scripting language designed for building interactive websites on the server side <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>, <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. Despite some criticisms, it remains one of the most popular languages for [[PHPs role in web development | back-end web development]] <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>, <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## Core Characteristics and Applications

PHP powers major platforms and websites, including:
*   Content Management Systems like WordPress <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.
*   Top-tier websites such as Wikipedia <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.
*   Numerous other sites utilizing frameworks like Laravel and Symphony <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.
*   Facebook, which developed a custom compiler to convert PHP to machine code on its servers <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>, <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

PHP is an open-source technology that revolutionized web development by making application creation accessible to a wider audience <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>, <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>, <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. Its interpreter is implemented in [[C influences on other programming languages | C]] <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. As of its version 8, PHP includes all the features expected from a modern, pragmatic language <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>, <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. Statistically, approximately 78.5% of client websites are currently running on PHP <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>, <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

## [[Programming Concepts and Paradigms | Programming Paradigms]]

PHP supports multiple [[Programming Concepts and Paradigms | programming paradigms]] <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>, <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>, including:

*   **[[Functional programming languages and their features | Functional Programming]]**: It provides first-class functions, which can be assigned to variables or used anonymously as arguments <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>, <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>, <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
*   **Object-Oriented Programming ([[Criticisms and opinions on objectoriented programming | OOP]]):** PHP has a complete object model that allows users to define classes with inheritance to implement [[Criticisms and opinions on objectoriented programming | object-oriented patterns]] <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>, <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>, <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

## Key Features

### Syntax and Embedding
PHP's syntax is inspired by Perl <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. It was one of the first languages to be embedded directly within HTML, enabling dynamic website construction on a server <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>, <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>, <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

To use [[Basic PHP syntax and usage | PHP]], a user can:
1.  Create a PHP file <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
2.  Add basic HTML to it <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
3.  Enter PHP mode by opening a `<?php` tag <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>, <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>, <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
4.  Code within these tags is processed and rendered on the server <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.
5.  The `echo` command is used to output a value in the location of the tag <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>, <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
6.  When the code is rendered, PHP tags are replaced by the echoed content <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>, <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>, <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

### Variables and Data Handling
*   Variables are declared by prefixing their name with a dollar sign (`$`) followed by a value <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>, <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
*   PHP is a weakly-typed language, meaning explicit type annotations are not required <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>, <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
*   It includes a large number of predefined variables (e.g., `$_GET`, `$_POST`, `$_COOKIE`) that are tailored for web development and contain information about incoming HTTP requests <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>, <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>, <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>, <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

### Built-in Functionality
PHP offers a vast array of built-in functions designed to handle almost any task a web developer might need <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>, <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>, <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.