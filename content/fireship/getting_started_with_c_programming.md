---
title: Getting started with C programming
videoId: U3aXWizDbQ4
---

From: [[fireship]] <br/> 

C is a statically typed, procedural programming language <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It is known for its role in creating foundational software and systems <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

It was created in 1972 by Dennis Ritchie at Bell Labs <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>, where it was initially used to develop the Unix operating system <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. C is considered the "mother of all languages" due to its influence on the syntax of other languages like C++, C#, Java, JavaScript, Perl, and PHP <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

## [[c_language_characteristics_and_usage | Key Characteristics of C]]

C compiles directly to machine code and requires minimal runtime support <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. However, it is platform-dependent, meaning an executable is designed to run on a specific operating system <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. While considered a high-level language designed for humans, C also provides low-level control over memory and hardware <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

### Memory Management
Unlike some other languages, C does not have a garbage collector <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>; instead, your code must manage its own memory <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

*   When a variable is created, it's assigned an address in memory <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
*   This memory address can be stored in another variable called a pointer <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
*   To avoid memory leaks, you must explicitly free the memory when the variable is no longer needed <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. This is done using the `free` function to release allocated memory back to the computer's RAM <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

## Getting Started with C

### 1. Install a C Compiler
To begin, you'll need to install a C compiler <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. A popular choice is the GNU C Compiler (GCC) <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

### 2. Create Your First C File
Create a file that ends with the `.c` extension <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

### 3. Basic Program Structure
Every C program needs to include any libraries you plan to use and contain a `main` function <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. The program begins execution from this `main` function <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.
*   There is no `function` keyword <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   The `main` function typically returns an integer type <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
*   A return value of `0` signifies success, while `1` indicates failure <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

### 4. Basic Data Types and Variables
C has only a few basic data types <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
To create a variable, start with its type, followed by a name and a value <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.
*   **Printing to output**: Use `print F` to print a value to the standard output <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
*   **Referencing memory address**: Put an ampersand (`&`) in front of a variable to reference its address in memory <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

#### Strings in C
There is no dedicated `string` type in C <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
*   A `char` represents a one-byte character stored as an integer <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
*   A string can be created as an array of characters <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. Each letter will have its own memory address and the string must be terminated by a null character <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
*   Another approach is to use a pointer, by adding a star (`*`) character in front of the type <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. You can then allocate memory (e.g., four bytes) and assign a character to each index, ending with the null character to form a string <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

### 5. Complex Data Types
C is a procedural language and does not support object-oriented features <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. However, you can create your own complex data types using `structs` <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

### 6. Compile Your Code
After writing your code, you compile it into machine instructions for your specific operating system using the C compiler <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.