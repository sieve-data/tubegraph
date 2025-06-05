---
title: Numeral systems and base conversions
videoId: bOCHTHkBoAs
---

From: [[fireship]] <br/> 

While it's often said that extensive math knowledge isn't necessary for [[Programming Concepts and Paradigms | programming a computer]], understanding fundamental mathematical concepts, such as numeral systems, can demystify complex computing processes <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## How Humans Count: Base 10

Throughout history, most human counting systems have utilized base 10, which corresponds to the ten fingers on our hands <a class="yt-timestamp" data-t="01:34:00">[01:34:00]</a>. In a base 10 number like 423, the '4' is in the hundreds place (4 × 100), the '2' is in the tens place (2 × 10), and the '3' is in the ones place (3 × 1) <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>.

## How Computers Count: Base 2 (Binary)

Computers operate on a base 2 numeral system, also known as binary <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a>. Similar to base 10, each place in a base 2 number is multiplied by increasing powers of two, such as 2, 4, 8, 16, 32, 64, and 128 <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>. Understanding base 2 is foundational to grasping how other numeral bases function <a class="yt-timestamp" data-t="02:03:00">[02:03:00]</a>.

### Other Important Bases

*   **Base 16 (Hexadecimal)**: This system uses digits 0-9 and letters A-F <a class="yt-timestamp" data-t="02:08:00">[02:08:00]</a>. It is commonly used to represent binary values more concisely, as each hexadecimal digit can translate into four bits <a class="yt-timestamp" data-t="02:11:00">[02:11:00]</a>.
*   **Base 64**: This system introduces even more letters and symbols to encode binary values <a class="yt-timestamp" data-t="02:17:00">[02:17:00]</a>. It enables developers to represent binary data, such as an image, as a string of text <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>.

## Representing Decimal Numbers: Floating Point

While computers primarily use base 2 internally, they must represent base 10 numbers for human interaction <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>. The most common method for this is using floating-point numbers <a class="yt-timestamp" data-t="02:31:00">[02:31:00]</a>.

For example, if you execute `0.1 + 0.2` in a [[Programming Concepts and Paradigms | programming language]], the result might be `0.30000000000000004` <a class="yt-timestamp" data-t="02:34:00">[02:34:00]</a>. This occurs because computers use a similar approach to scientific notation to handle very large or very small numbers compactly <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>.

Computers have a limited amount of space for numbers (either 32 bits for single precision or 64 bits for double precision, which is the default in [[Programming Concepts and Paradigms | languages like Python and JavaScript]]) <a class="yt-timestamp" data-t="03:01:00">[03:01:00]</a>. A "floating point" means there's no fixed number of digits before or after the decimal point, allowing developers to balance range and precision <a class="yt-timestamp" data-t="03:09:00">[03:09:00]</a>. Certain numbers, like `0.01`, cannot be perfectly represented as a binary floating point, leading to minor rounding errors <a class="yt-timestamp" data-t="03:17:00">[03:17:00]</a>.