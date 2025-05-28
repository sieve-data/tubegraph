---
title: Introduction to Programming for Beginners
videoId: Nxu6GlDleqA
---

From: [[jarvis]] <br/> 

Welcome to Tech Tuesday, where the aim is to provide a foundational understanding of programming for those with no prior experience <a class="yt-timestamp" data-t="00:39:00">[00:39:00]</a>. Even individuals familiar with programming concepts may find something new <a class="yt-timestamp" data-t="00:47:00">[00:47:00]</a>.

## What is Programming?

Coding, programming, and scripting are largely synonymous terms describing the act of giving a computer instructions, typically in a list <a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a>. This process can be compared to following a recipe, where each step has specific actions <a class="yt-timestamp" data-t="01:35:00">[01:35:00]</a>. Writing code is akin to reading a recipe and instructing a friend (in this case, a computer) on what to do <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>.

Knowing how to code is considered an invaluable skill across various professions <a class="yt-timestamp" data-t="02:06:00">[02:06:00]</a>.

## Practical Application: Ordering Pizza with Code

A common scenario for programmers is to [[Application of Programming in Everyday Tasks | build custom solutions to problems that have already been solved]] <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>. An example given is writing a script to order pizza programmatically, rather than using traditional methods like phone or internet <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>.

### Understanding APIs

To interact with services like Domino's programmatically, developers use an API (Application Programming Interface) <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>. An API can be thought of as a well-trained dog that understands specific commands to perform various tasks <a class="yt-timestamp" data-t="03:04:00">[03:04:00]</a>. The instructions given to an API must be very specific, similar to how one would teach a dog tricks <a class="yt-timestamp" data-t="03:17:00">[03:17:00]</a>.

### Choosing a Programming Language and Tools

[[Python Programming Basics | Python]] is recommended as an excellent language for learning programming due to its readability and versatility <a class="yt-timestamp" data-t="03:35:00">[03:35:00]</a>.

To interact with an API like Domino's using Python, one might use a "library" <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>. A library is helper code, often written by others, that translates Python instructions into commands the API can understand <a class="yt-timestamp" data-t="03:45:00">[03:45:00]</a>. An example library for Domino's is "pizza pie" <a class="yt-timestamp" data-t="04:05:00">[04:05:00]</a>. These libraries can be found on platforms like GitHub, where programmers share code <a class="yt-timestamp" data-t="04:15:00">[04:15:00]</a>.

A Python interpreter is a program that allows users to write and execute Python code and view its results <a class="yt-timestamp" data-t="03:57:00">[03:57:00]</a>.

## Core [[Understanding Programming Concepts Variables Classes Functions | Programming Concepts]] Illustrated

To order a pizza programmatically, several fundamental programming concepts come into play:

### 1. [[Understanding Programming Concepts Variables Classes Functions | Classes]]

A class serves as a template used to define objects <a class="yt-timestamp" data-t="04:58:00">[04:58:00]</a>. For example, in a pizza ordering system, a "Customer" class might define what information constitutes a customer (e.g., name, address) <a class="yt-timestamp" data-t="04:38:00">[04:38:00]</a>.

### 2. [[Understanding Programming Concepts Variables Classes Functions | Objects]]

An object is a specific instance of a class, with defined variables <a class="yt-timestamp" data-t="05:02:00">[05:02:00]</a>. If "Customer" is a class, then "Jarvis" (with a specific name and address) would be an object of that class <a class="yt-timestamp" data-t="05:05:00">[05:05:00]</a>.

### 3. [[Understanding Programming Concepts Variables Classes Functions | Variables]]

Variables are used to store objects or data for later use <a class="yt-timestamp" data-t="05:10:00">[05:10:00]</a>. For instance, the "Jarvis" customer object can be assigned to a variable named `Jarvis` <a class="yt-timestamp" data-t="05:17:00">[05:17:00]</a>. Similarly, menu item codes can be stored in variables like `Fanta` or `deluxe` <a class="yt-timestamp" data-t="06:42:00">[06:42:00]</a>.

### 4. [[Understanding Programming Concepts Variables Classes Functions | Functions]]

A function is a specific action or "trick" that an API or object can perform <a class="yt-timestamp" data-t="05:27:00">[05:27:00]</a>. Functions often require additional input to perform their calculations <a class="yt-timestamp" data-t="06:10:00">[06:10:00]</a>.

*   **Example**: `store_locator.find_closest_store(customer)` is a function that finds the nearest store by taking a `customer` object as input <a class="yt-timestamp" data-t="05:39:00">[05:39:00]</a>.
*   **Accessing Functions**: The "dot" notation (`object.function()`) is used to ask an object to perform a specific function <a class="yt-timestamp" data-t="05:46:00">[05:46:00]</a>.

## Building the Pizza Order Program

The steps to programmatically order a pizza involve:

1.  **Defining the Customer**: Create a customer object with name and address using the `Customer` class <a class="yt-timestamp" data-t="04:35:00">[04:35:00]</a>.
2.  **Finding the Nearest Store**: Use a function (e.g., `store_locator.find_closest_store`) to locate the closest Domino's based on the customer's information <a class="yt-timestamp" data-t="05:22:00">[05:22:00]</a>.
3.  **Creating the Order**: Use an `Order` class to create a custom order object, specifying the customer and store <a class="yt-timestamp" data-t="06:47:00">[06:47:00]</a>.
4.  **Adding Items**: Use a function like `add_item` to add specific menu items (identified by unique codes) to the order <a class="yt-timestamp" data-t="07:01:00">[07:01:00]</a>.
5.  **Adding Payment Information**: Create a credit card object using a `CreditCard` class, providing necessary payment details <a class="yt-timestamp" data-t="07:12:00">[07:12:00]</a>.
6.  **Placing the Order**: Call a function (e.g., `place_order`) on the store object, passing in the completed order and credit card information <a class="yt-timestamp" data-t="07:25:00">[07:25:00]</a>.

## Conclusion

Programming, despite its perceived difficulty, is not inherently complex <a class="yt-timestamp" data-t="07:54:00">[07:54:00]</a>. Challenges often stem from the quality of available learning resources rather than the task itself <a class="yt-timestamp" data-t="07:58:00">[07:58:00]</a>. Good code should be as understandable as a written recipe <a class="yt-timestamp" data-t="08:05:00">[08:05:00]</a>.

This example demonstrated core [[Understanding Programming Concepts Variables Classes Functions | programming concepts]] including:
*   [[Understanding Programming Concepts Variables Classes Functions | Variables]] <a class="yt-timestamp" data-t="08:10:00">[08:10:00]</a>
*   [[Understanding Programming Concepts Variables Classes Functions | Classes]] <a class="yt-timestamp" data-t="08:11:00">[08:11:00]</a>
*   [[Understanding Programming Concepts Variables Classes Functions | Objects]] <a class="yt-timestamp" data-t="08:12:00">[08:12:00]</a>
*   [[Understanding Programming Concepts Variables Classes Functions | Functions]] <a class="yt-timestamp" data-t="08:13:00">[08:13:00]</a>
*   Procedural programming <a class="yt-timestamp" data-t="08:14:00">[08:14:00]</a>

The code for this example, modified from an existing library for clarity, is available on GitHub to encourage experimentation <a class="yt-timestamp" data-t="08:22:00">[08:22:00]</a>.

***

### Announcements

The author hosts a comedy [[role_of_podcasts_and_hobbies_in_developing_programming_skills | podcast]] about feelings called "A Boys" <a class="yt-timestamp" data-t="00:56:00">[00:56:00]</a>. Recent topics include career and self-esteem <a class="yt-timestamp" data-t="00:58:00">[00:58:00]</a>. The author also attended VidCon, where inspiration from talks led to restarting a YouTube channel after an eight-year hiatus <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>.