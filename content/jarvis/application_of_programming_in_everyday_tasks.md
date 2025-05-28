---
title: Application of Programming in Everyday Tasks
videoId: Nxu6GlDleqA
---

From: [[jarvis]] <br/> 

Programming, coding, and scripting are terms that generally describe the act of giving a computer instructions, usually in a list format, much like a recipe <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. This process involves the programmer reading the steps and instructing the computer, which acts as a "friend" or assistant <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

Knowing how to code is an invaluable skill regardless of one's profession <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

## Why Program for Simple Tasks?

While many everyday problems have already been solved by existing solutions (e.g., ordering pizza online), a software engineer's career often involves building custom solutions to these problems <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. This approach demonstrates how programming can automate tasks that might otherwise be done manually, like ordering pizza using a script <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

## Understanding Key Programming Concepts Through a Practical Example

The following example demonstrates how to programmatically order a pizza, illustrating several core [[understanding_programming_concepts_variables_classes_functions | programming concepts]]:

### Application Programming Interfaces (APIs)

An [[using_apis_to_automate_tasks | API (Application Programming Interface)]] allows different software systems to communicate and interact <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. It can be thought of as a "well-trained dog" that performs specific tricks (actions) when given precise instructions <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>. For instance, Domino's Pizza exposes an API that enables ordering pizzas programmatically <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

### Libraries

A library is a collection of pre-written code that provides helper functions and classes, making it easier to interact with APIs or perform common tasks <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. In the pizza ordering example, a [[python_programming_basics | Python]] library named "pizza-pie," written by someone else, translates Python code into instructions that Domino's API can understand <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. These libraries are often shared on platforms like GitHub <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

### Python Interpreter

To write and execute [[python_programming_basics | Python]] code, a Python interpreter is used <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. This program allows users to write code and immediately see the results <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. [[introduction_to_programming_and_python | Python]] is considered an excellent language for learning programming due to its readability and versatility <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.

### Classes and Objects

*   **Classes** provide a template or blueprint for creating objects <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>. For example, the `Customer` class defines what information is needed to represent a customer (e.g., name, address) <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. Similarly, `Order` and `CreditCard` can be defined as classes <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
*   **Objects** are instances of a class with defined values for their variables <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. For instance, "Jarvis" becomes a `Customer` object when specific name and address data are plugged into the `Customer` template <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.

### Variables

[[understanding_programming_concepts_variables_classes_functions | Variables]] are used to store data or objects for later use <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. For example, the `Customer` object is assigned to a variable named "Jarvis" <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>. Menu item codes (e.g., for Deluxe pizza or Fanta) can also be stored in variables <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

### Functions

A [[understanding_programming_concepts_variables_classes_functions | function]] is like a special "trick" or action that an object or API can perform <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. Functions often require additional input (parameters) to perform their calculations <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. Examples include:
*   `storelocator.findcloseststore(customer)`: A function within the `storelocator` class that finds the nearest Domino's location based on customer information <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
*   `begin_customer_order(customer, store)`: A function to initiate an order, taking customer and store details as input <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
*   `add_item()`: A function to add items to an order <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
*   `place_order(order, card)`: A function of the `Store` class that sends the order and credit card information to the local Domino's <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.

## Steps to Order Pizza Programmatically (Procedural Programming)

The process of ordering a pizza programmatically follows a procedural sequence:

1.  **Define the Customer:** Create a `Customer` object with a name and address <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
2.  **Find the Nearest Store:** Use the `storelocator.findcloseststore()` function, providing the `Customer` object as input, to find the closest Domino's <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
3.  **Create the Order:**
    *   Initiate an `Order` object using `begin_customer_order()` with the customer and store information <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.
    *   Add desired menu items (e.g., Deluxe pizza, Fanta) to the order using the `add_item()` function, referring to them by their specific Domino's codes <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
4.  **Add Payment Information:** Create a `CreditCard` object with the necessary payment details <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.
5.  **Place the Order:** Call the `place_order()` function on the `Store` object, passing in the prepared `Order` and `CreditCard` objects <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.

## Conclusion

Despite popular perception, [[introduction_to_programming_for_beginners | programming]] is not inherently difficult to understand <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>. Good code should be as easy to comprehend as plain text <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>. The example of programmatically ordering pizza demonstrates practical applications of fundamental [[understanding_programming_concepts_variables_classes_functions | programming concepts]] such as variables, classes, objects, and functions, all within a context that illustrates procedural programming <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>. Experimentation is encouraged, with code often available on platforms like GitHub for others to learn from and modify <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.

> [!NOTE]
> The speaker also mentions their podcast "A Boys" which discusses feelings and careers, and their attendance at VidCon, which inspired them to restart their YouTube channel. These personal anecdotes highlight the [[role_of_podcasts_and_hobbies_in_developing_programming_skills | role of podcasts and hobbies in developing programming skills]] and personal growth <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.