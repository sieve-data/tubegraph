---
title: C language characteristics and usage
videoId: U3aXWizDbQ4
---

From: [[fireship]] <br/> 
C is a statically typed, procedural programming language widely recognized for its foundational role in computing <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## [[History and origins of C programming language | History and Origins]]

The C programming language was developed in 1972 by Dennis Ritchie at Bell Labs <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. It was initially created to develop the Unix operating system <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. C is considered the "mother of all languages," having influenced the syntax of many subsequent programming languages, including C++, C#, Java, JavaScript, Perl, and PHP <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## [[Applications and usage of C | Applications and Usage]]

C is fundamental to many tools and systems that are commonly used today <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. Its applications include:
*   Operating system kernels for Windows, Linux, and Mac <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.
*   Databases like MySQL <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.
*   Interpreters for other languages, such as Python <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.
*   Tools like Vim and Git <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

## [[Key features of C | Key Features and Characteristics]]

### Compilation and Platform Dependency
C compiles directly to machine code, requiring minimal runtime support <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. However, it is platform-dependent, meaning an executable is specifically designed to run on a particular operating system <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

### Level of Control
Despite being a high-level language designed for human readability, C provides low-level control over memory and hardware <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

### Memory Management
C does not have a garbage collector, requiring the programmer to manage memory manually <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. When a variable is created, it is assigned an address in memory <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. This address can be stored in a special variable called a pointer <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. To prevent memory leaks, memory that is no longer needed must be explicitly freed <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. When memory allocated to the program is no longer required, the `free` function is used to release it back to the computer's RAM <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

### Data Types
C has a limited number of basic types <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. Variables are created by specifying a type, followed by a name and value <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.
*   **Characters**: There is no dedicated string type in C. Instead, `Char` represents a one-byte character stored as an integer <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
*   **Strings**: Strings are created as arrays of characters, with each letter having its own memory address and terminated by a null character <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. An alternative is to declare a pointer by adding a star `*` character in front of the type, allocate memory (e.g., four bytes), and then assign characters to each index, ending with a null character to form a string <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
*   **Complex Data Types**: While C is procedural and does not natively support [[Objectoriented programming in C | object-oriented features]], programmers can create their own complex data types using `structs` <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

## [[Getting started with C programming | Getting Started with C Programming]]

To begin programming in C:
1.  **Install a C Compiler**: A popular choice is the GNU C Compiler (GCC) <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.
2.  **Create a File**: Save your code in a file ending with the `.c` extension <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
3.  **Include Libraries**: Add any necessary libraries you plan to use <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
4.  **Main Function**: Include a `main` function, as this is where your program's execution begins <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. Note that there is no `function` keyword, and the `main` function typically returns an integer type <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. A return value of `0` indicates success, while `1` signifies failure <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
5.  **Print Output**: Use `printf` to print values to the standard output <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. To reference a variable's address in memory, place an ampersand `&` in front of it <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
6.  **Compile Code**: Compile your code into machine instructions for your operating system using the C compiler <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.