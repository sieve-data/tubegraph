---
title: Using APIs to Automate Tasks
videoId: Nxu6GlDleqA
---

From: [[jarvis]] <br/> 

[[Application of Programming in Everyday Tasks | Automating tasks]] involves giving a computer a list of instructions, similar to a recipe, to perform specific actions <a class="yt-timestamp" data-t="01:27:17">[01:27:17]</a>. This process is often referred to as coding, programming, or scripting <a class="yt-timestamp" data-t="01:27:17">[01:27:17]</a>. Knowing how to code is considered an invaluable skill regardless of one's profession <a class="yt-timestamp" data-t="02:06:06">[02:06:06]</a>.

## What is an API?

An API, or **Application Programming Interface**, acts as a specific set of instructions that allows you to interact with a service or system programmatically <a class="yt-timestamp" data-t="03:00:23">[03:00:23]</a>.

> "We can think of it like a well-trained dog. You can teach dogs tricks like fetch or like handshakes and stuff but dogs don't really understand English... so those instructions have to be very specific. API's are essentially the same way they do a bunch of things but the way you ask it to do those things is very specific." <a class="yt-timestamp" data-t="03:04:46">[03:04:46]</a>

## Automating Pizza Ordering: A Practical Example

A practical demonstration of [[Application of Programming in Everyday Tasks | automation]] using an API involves writing a script to order pizza <a class="yt-timestamp" data-t="02:22:30">[02:22:30]</a>. This illustrates how a software engineer might build a custom solution to a problem that already has existing solutions <a class="yt-timestamp" data-t="02:35:10">[02:35:10]</a>. Domino's Pizza, for instance, exposes an API that allows for programmatic pizza orders <a class="yt-timestamp" data-t="02:45:51">[02:45:51]</a>.

The process of ordering pizza programmatically requires the code to:
*   Know the delivery address <a class="yt-timestamp" data-t="04:27:46">[04:27:46]</a>
*   Know the nearest Domino's location <a class="yt-timestamp" data-t="04:29:21">[04:29:21]</a>
*   Provide the order details <a class="yt-timestamp" data-t="04:30:31">[04:30:31]</a>
*   Handle payment for the order <a class="yt-timestamp" data-t="04:31:52">[04:31:52]</a>

To achieve this, developers can use a "library," which is helper code written by others that translates your code into instructions the API can understand <a class="yt-timestamp" data-t="03:44:31">[03:44:31]</a>. For Python, a library named "pizza pie" can be used for the Domino's API <a class="yt-timestamp" data-t="04:02:40">[04:02:40]</a>.

### Key Programming Concepts in Automation

To execute the pizza ordering script, several fundamental programming concepts are utilized:

*   **Python Interpreter:** A program that allows you to write Python code and see the immediate result <a class="yt-timestamp" data-t="03:56:07">[03:56:07]</a>.
*   **Libraries:** Collections of pre-written helper code that simplify interactions with APIs <a class="yt-timestamp" data-t="03:52:41">[03:52:41]</a>. For example, "pizza pie" is a library that simplifies interaction with the Domino's API <a class="yt-timestamp" data-t="04:02:40">[04:02:40]</a>. These can often be found on platforms like GitHub <a class="yt-timestamp" data-t="04:14:48">[04:14:48]</a>.
*   **Classes:** Act as templates used to define "objects" <a class="yt-timestamp" data-t="04:56:29">[04:56:29]</a>. Examples include a `Customer` class (defining a customer with a name and address) <a class="yt-timestamp" data-t="04:38:09">[04:38:09]</a>, an `Order` class to create a custom order object <a class="yt-timestamp" data-t="06:47:04">[06:47:04]</a>, and a `Credit Card` class for payment information <a class="yt-timestamp" data-t="07:12:12">[07:12:12]</a>.
*   **Objects:** An instance of a class with defined variables <a class="yt-timestamp" data-t="05:01:29">[05:01:29]</a>. For instance, a specific customer with a given name and address is an object created from the `Customer` class <a class="yt-timestamp" data-t="05:05:46">[05:05:46]</a>.
*   **Variables:** Nicknames or labels used to hold onto objects or data for later use <a class="yt-timestamp" data-t="05:11:00">[05:11:00]</a>. For example, `Jarvis` could be a variable holding the customer object <a class="yt-timestamp" data-t="05:15:37">[05:15:37]</a>.
*   **Functions:** Special "tricks" or actions that an API, class, or object can perform <a class="yt-timestamp" data-t="05:25:01">[05:25:01]</a>. Examples include `store locator.find closest storage.customer` to find the nearest Domino's <a class="yt-timestamp" data-t="05:37:57">[05:37:57]</a>, `begin customer order` to start an order <a class="yt-timestamp" data-t="06:55:28">[06:55:28]</a>, and `add item` to add items to an order <a class="yt-timestamp" data-t="07:01:14">[07:01:14]</a>. Functions often require additional input to perform their calculations <a class="yt-timestamp" data-t="06:10:48">[06:10:48]</a>.
*   **Procedural Programming:** The overall concept of giving step-by-step instructions for a computer to follow <a class="yt-timestamp" data-t="08:14:15">[08:14:15]</a>.

### Steps to Order Pizza Programmatically:

1.  **Import the Library:** Bring the "pizza pie" library into the Python interpreter <a class="yt-timestamp" data-t="04:05:00">[04:05:00]</a>.
2.  **Define the Customer:** Create a `Customer` object with a name and address, assigning it to a variable (e.g., `Jarvis`) <a class="yt-timestamp" data-t="04:35:10">[04:35:10]</a>.
3.  **Find the Nearest Store:** Use the `store locator.find closest storage.customer` function, providing the customer object as input, and assign the result to a variable (e.g., `my local Domino's`) <a class="yt-timestamp" data-t="05:22:07">[05:22:07]</a>.
4.  **Create the Order:** Define specific menu items using their codes and use the `Order` class to create an order object <a class="yt-timestamp" data-t="06:25:21">[06:25:21]</a>.
    *   Call `begin customer order`, providing the customer and store <a class="yt-timestamp" data-t="06:55:28">[06:55:28]</a>.
    *   Call `add item` repeatedly to add desired items to the order <a class="yt-timestamp" data-t="07:01:14">[07:01:14]</a>.
5.  **Add Payment Information:** Use the `Credit Card` class to input credit card details and save it to a variable <a class="yt-timestamp" data-t="07:11:50">[07:11:50]</a>.
6.  **Place the Order:** Call the `place order` function on the `my local Domino's` object, providing the created order and credit card information <a class="yt-timestamp" data-t="07:29:10">[07:29:10]</a>.

## Broader Implications

Programming, though sometimes perceived as difficult, is fundamentally about giving instructions <a class="yt-timestamp" data-t="07:54:33">[07:54:33]</a>. The speaker suggests that good code is relatively straightforward to understand <a class="yt-timestamp" data-t="08:05:00">[08:05:00]</a>. The demonstration of ordering pizza programmatically serves as an encouraging example of doing "something cool" with code <a class="yt-timestamp" data-t="08:18:04">[08:18:04]</a>. [[Role of podcasts and hobbies in developing programming skills | Experimentation with code and existing libraries]] is encouraged for further learning <a class="yt-timestamp" data-t="08:27:00">[08:27:00]</a>.