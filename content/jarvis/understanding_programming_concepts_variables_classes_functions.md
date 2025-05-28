---
title: Understanding Programming Concepts Variables Classes Functions
videoId: Nxu6GlDleqA
---

From: [[jarvis]] <br/> 

This article provides an [[introduction_to_programming_for_beginners | introduction to programming]] concepts, using the example of ordering pizza programmatically to illustrate key ideas like variables, classes, and functions <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

## What is Programming?

[[introduction_to_programming_for_beginners | Coding]], [[introduction_to_programming_for_beginners | programming]], and scripting are essentially the same act: giving a computer instructions, typically in a list <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. This process is likened to a recipe with a list of steps <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. Writing code is like cooking with a friend, where you read the recipe and tell the computer (your "friend") what to do <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. Knowing how to [[introduction_to_programming_for_beginners | code]] is considered an invaluable skill across professions <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

### Application of Programming: Ordering Pizza
A practical [[application_of_programming_in_everyday_tasks | application of programming in everyday tasks]] is writing a script to order pizza <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. This demonstrates how software engineers build custom solutions even for problems that might already have simpler solutions <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

## Key Programming Concepts

The example of ordering pizza programmatically introduces several fundamental concepts of [[python_programming_basics | programming basics]]:

### Application Programming Interface (API)
An API (Application Programming Interface) allows interaction with a service, like Domino's Pizza, programmatically <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. Think of an API as a "well-trained dog" that can do specific tricks when given very specific instructions, as dogs don't understand general English commands <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

### Programming Language: Python
The demonstration uses [[introduction_to_programming_and_python | Python]], described as an excellent language for learning programming <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.

### Libraries and Interpreters
To interact with the Domino's API using [[introduction_to_programming_and_python | Python]], a "helper code" written by someone else on the internet is used <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. This helper code, called `pizza-pie`, is a **library** that translates Python code into instructions Domino's can understand <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. The code is accessed and run through a **Python interpreter**, a program that allows writing Python code and seeing immediate results <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. Libraries like `pizza-pie` can be downloaded from platforms like GitHub <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

### Classes and Objects
To place an order, the code needs to know:
*   The delivery address <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>
*   The nearest Domino's location <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>
*   The order details <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>
*   Payment information <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>

These pieces of information are handled using **classes** and **objects**:

*   **Class:** A class serves as a template to define objects <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>. For example, `pizza-pie` defines a `Customer` class as someone with a name and address <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. Other classes include `Order`, `CreditCard`, and `StoreLocator` <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a><a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a><a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
*   **Object:** An object is an instance of a class with defined variables <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. When specific name and address data are plugged into the `Customer` template, an object is defined <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. For instance, "Jarvis" is an object of the `Customer` class <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

### Variables
**Variables** are used to hold onto objects or data for later use <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. In the example, the customer object is assigned to a variable named `Jarvis` <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. Similarly, product codes for Fanta and Deluxe pizza are stored in variables named `Fanta` and `deluxe` <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

### Functions
**Functions** are "special tricks" that an API can perform <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. They often require additional input to perform their calculations <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
Examples of functions used:
*   `store_locator.find_closest_store(customer)`: A function within the `StoreLocator` class that finds the nearest Domino's location based on customer information <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. The `.` (dot) notation is how you ask an object to perform a specific action <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.
*   `begin_customer_order(customer, store)`: A function that initiates an order, taking both customer and store information <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.
*   `add_item()`: A function used to add items to an order <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
*   `place_order(order, card)`: A function of the `Store` class that finalizes the order using the order object and credit card information <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.

This example also touched upon the concept of **procedural programming** <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

## Conclusion and Further Learning
While [[introduction_to_programming_for_beginners | programming]] can seem difficult, the inherent complexity is often exaggerated by the [[critical_commentary_on_video_tutorials | available resources]] rather than the task itself <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>. Good code should be as easy to understand as a written instruction <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>. The discussed example covered variables, classes, objects, and functions <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. The code used in the demonstration is available on GitHub <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

Jarvis also encourages users to listen to his [[role_of_podcasts_and_hobbies_in_developing_programming_skills | podcast]], "A Boys," which discusses feelings and has a video version on self-esteem <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. He also mentions attending VidCon, where previous talks inspired him to restart his YouTube channel <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.