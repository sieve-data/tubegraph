---
title: Basic PHP syntax and usage
videoId: a7_WFUlFS94
---

From: [[fireship]] <br/> 

PHP is a dynamic, interpreted scripting language designed for building interactive websites on the server side <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Despite some "haters" declaring it dead, it remains a highly popular language for back-end web development <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## Role and Popularity
[[PHPs role in web development | PHP]] powers major Content Management Systems like WordPress, top-tier websites such as Wikipedia, and countless others using frameworks like Laravel and Symfony <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. Even Facebook utilizes PHP, though they developed a custom compiler to convert it to machine code on their servers <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. Statistically, there's a 78.5% chance that a client's website is running PHP <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

## History and Characteristics
[[History and origin of PHP | PHP]] was created in 1994 by Rasmus Lerdorf to manage his personal homepage <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. Originally an acronym for "Personal Home Page," its meaning was later updated to "Hypertext Preprocessor" <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. PHP holds a special place in history as it predates JavaScript and was among the first languages to be embedded directly within [[html_structure_and_syntax | HTML]], enabling dynamic website creation on a server <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. It is open-source and contributed to revolutionizing the web by making application development accessible <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. The PHP interpreter is implemented in C and features a syntax inspired by Perl <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## Basic Usage and Syntax

To get started with PHP:
1.  Create a PHP file, often with a `.php` extension <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
2.  Add [[html_structure_and_syntax | basic HTML]] structure to this file <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
3.  Enter "PHP mode" within the file by opening a `<?php` tag <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. Code placed between these tags will be rendered on the server <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

### Outputting Values
The `echo` statement is used to output a value at the location of the PHP tag <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

### Variables
To declare a variable, give it a name that starts with a dollar sign (`$`) followed by a value <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. PHP is a weakly typed language, so explicit type annotations are not required <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

```php
<?php
    $greeting = "Hello, World!";
    echo $greeting;
?>
```
When this code is rendered on a server, it outputs an [[html_structure_and_syntax | HTML]] string with the PHP tags replaced by the echoed content <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

PHP also includes a large number of predefined variables tailored for web development, such as `$_GET`, `$_POST`, and `$_COOKIE`, which contain information about the incoming HTTP request <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

### Functions and Paradigms
The language supports multiple [[PHPs programming paradigms and features | programming paradigms]] <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. It features first-class functions that can be assigned to variables or used anonymously as arguments <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. PHP has numerous built-in functions to facilitate various web development tasks <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. It also provides a complete object model, allowing for the definition of classes with inheritance to implement object-oriented patterns <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

### Current State
[[Current state and versions of PHP | PHP version 8]], the current major release, includes all the features expected from a modern, pragmatic language <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.