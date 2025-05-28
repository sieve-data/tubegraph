---
title: Python Programming Basics
videoId: Nxu6GlDleqA
---

From: [[jarvis]] <br/> 

This article provides an [[introduction_to_programming_for_beginners | introduction to programming]] concepts, using [[introduction_to_programming_and_python | Python]] as the language of choice, and demonstrates an [[application_of_programming_in_everyday_tasks | application of programming]] through a pizza ordering script.

## What is Programming?
Coding, programming, and scripting are all terms that describe the act of giving a computer instructions, typically in a list format, similar to a recipe [01:27:00]. Writing code is like cooking with a friend: you read the recipe steps and tell your friend (the computer) what to do [01:41:00]. Learning to code is considered an invaluable skill regardless of one's profession [02:06:00].

## Key Programming Concepts
### Application Programming Interface (API)
An API (Application Programming Interface) can be thought of as a well-trained dog [03:00:00]. Just as you teach a dog specific tricks (like fetch), an API performs a variety of actions, but requires very specific instructions to do so [03:22:00]. For example, the Domino's Pizza API allows programmatic ordering of pizzas [02:45:00].

### Python as a Programming Language
[[introduction_to_programming_and_python | Python]] is considered an excellent language for learning programming due to its ease of understanding [03:35:00].

### Libraries
A library is helper code written by someone else that translates your code into instructions a specific API can understand [03:44:00]. For instance, `pizzapy` is a Python library that allows users to interact with the Domino's API [04:03:00]. These libraries are often shared on platforms like GitHub [04:13:00].

### Python Interpreter
A Python interpreter is a program that allows you to write Python code and immediately see the results [03:56:00].

### [[understanding_programming_concepts_variables_classes_functions | Classes]] and [[understanding_programming_concepts_variables_classes_functions | Objects]]
A [[understanding_programming_concepts_variables_classes_functions | class]] defines a template that is used to create [[understanding_programming_concepts_variables_classes_functions | objects]] [04:58:00]. An [[understanding_programming_concepts_variables_classes_functions | object]] is an instance of a [[understanding_programming_concepts_variables_classes_functions | class]] with defined [[understanding_programming_concepts_variables_classes_functions | variables]] [05:02:00].
*   **Example**: The `pizzapy` library defines a `Customer` [[understanding_programming_concepts_variables_classes_functions | class]] which takes a name and address as data. When you input your specific name and address, you create a "customer" [[understanding_programming_concepts_variables_classes_functions | object]] [04:39:00]. Similarly, a `CreditCard` [[understanding_programming_concepts_variables_classes_functions | class]] holds payment information [07:13:00].

### [[understanding_programming_concepts_variables_classes_functions | Variables]]
[[understanding_programming_concepts_variables_classes_functions | Variables]] are nicknames or containers used to hold onto [[understanding_programming_concepts_variables_classes_functions | objects]] or data for later use [05:10:00].
*   **Example**: After creating a customer [[understanding_programming_concepts_variables_classes_functions | object]], you can assign it to a [[understanding_programming_concepts_variables_classes_functions | variable]] named `Jarvis` so you can easily refer to that specific customer later [05:14:00].

### [[understanding_programming_concepts_variables_classes_functions | Functions]]
A [[understanding_programming_concepts_variables_classes_functions | function]] is like a special trick or action that an API or an [[understanding_programming_concepts_variables_classes_functions | object]] can perform [05:25:00]. [[understanding_programming_concepts_variables_classes_functions | Functions]] often require additional input to perform their calculations [06:10:00].
*   **Example**: The `StoreLocator` [[understanding_programming_concepts_variables_classes_functions | class]] contains [[understanding_programming_concepts_variables_classes_functions | functions]] to find a Domino's location. Specifically, `storelocator.findClosestStore(customer)` is a [[understanding_programming_concepts_variables_classes_functions | function]] that takes a customer [[understanding_programming_concepts_variables_classes_functions | object]] as input to find the nearest store [05:27:00]. Other [[understanding_programming_concepts_variables_classes_functions | functions]] include `addItem` to add items to an order [07:01:00], and `placeOrder` to finalize a pizza order [07:29:00].

## Practical Application: Ordering Pizza with Python
To demonstrate these concepts, a script to order pizza from Domino's using the `pizzapy` library was created [02:26:00].

The process involves:
1.  **Defining the Customer**: Create a `Customer` [[understanding_programming_concepts_variables_classes_functions | object]] by providing a name and address [04:37:00].
2.  **Finding the Store**: Use the `StoreLocator.findClosestStore()` [[understanding_programming_concepts_variables_classes_functions | function]], passing the customer [[understanding_programming_concepts_variables_classes_functions | object]] as input, to find the nearest Domino's [05:22:00].
3.  **Building the Order**:
    *   Store specific menu item codes (e.g., for Deluxe pizza and Fanta) in [[understanding_programming_concepts_variables_classes_functions | variables]] [06:36:00].
    *   Create an `Order` [[understanding_programming_concepts_variables_classes_functions | object]] [06:47:00].
    *   Call `beginCustomerOrder()` with the customer and store [[understanding_programming_concepts_variables_classes_functions | objects]] [06:56:00].
    *   Use the `addItem()` [[understanding_programming_concepts_variables_classes_functions | function]] to add selected items to the order [07:01:00].
4.  **Adding Payment Information**: Create a `CreditCard` [[understanding_programming_concepts_variables_classes_functions | object]] with payment details and save it to a [[understanding_programming_concepts_variables_classes_functions | variable]] [07:10:00].
5.  **Placing the Order**: Call the `placeOrder()` [[understanding_programming_concepts_variables_classes_functions | function]] on the store [[understanding_programming_concepts_variables_classes_functions | object]], providing the order and credit card [[understanding_programming_concepts_variables_classes_functions | objects]] as arguments [07:25:00].

This example demonstrates [[understanding_programming_concepts_variables_classes_functions | variables]], [[understanding_programming_concepts_variables_classes_functions | classes]], [[understanding_programming_concepts_variables_classes_functions | objects]], [[understanding_programming_concepts_variables_classes_functions | functions]], and the concept of procedural programming [08:09:00].

> [!NOTE]
> Programming, while sometimes held up as difficult, is often made more challenging by available resources rather than its inherent complexity [07:54:00]. Good code aims to be as easy to understand as a clear instruction [08:05:00].

The code for this example is available on GitHub, encouraging users to experiment and build upon it [08:22:00].