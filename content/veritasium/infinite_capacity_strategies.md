---
title: Infinite capacity strategies
videoId: OxGsU8oIWjY
---

From: [[veritasium]] <br/> 

The Hilbert Hotel is a conceptual hotel featuring an infinite number of rooms, numbered one, two, three, four, and so on forever <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. While it might seem capable of accommodating anyone, there are limits to its capacity, demonstrating fascinating concepts about [[Infinity in mathematics | infinity]] <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## Accommodating New Guests

Assuming all rooms are full with an infinite number of people <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>:

### One New Guest

When a single new guest arrives, the manager can accommodate them by asking every existing guest to move down one room (e.g., room one to room two, room two to room three) <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. This frees up room one for the new arrival <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

### A Finite Busload of Guests

If a bus arrives with a finite number of people, such as one hundred, the same principle applies <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. All existing guests move down a hundred rooms, and the new guests occupy the newly vacated rooms <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

### An Infinite Busload of Guests

For an infinitely long bus carrying infinitely many people <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>, a different [[Strategies for complex problem solving | strategy]] is employed. Existing guests are instructed to move to the room number that is double their current room number (e.g., room one to room two, room two to room four, room three to room six) <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. This action makes all odd-numbered rooms available <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. Since there are an infinite number of odd numbers, each person from the infinite bus can be given a unique, odd-numbered room <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

### An Infinite Number of Infinite Buses

Even when an infinite number of infinite buses arrive <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>, the hotel can still accommodate everyone. This involves creating an infinite spreadsheet <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>:
*   Rows represent each bus (Bus 1, Bus 2, Bus 3, etc.), plus a row for existing hotel guests <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
*   Columns represent positions (Room 1, Room 2; Bus 1 Seat 1, Bus 1 Seat 2, etc.) <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
*   Each person receives a unique identifier based on their vehicle and position <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

To assign rooms, a line is drawn that zigzags across the spreadsheet, starting from the top-left corner and covering each unique ID exactly once <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. Straightening this line transforms the infinite-by-infinite grid into a single infinite line <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. Each person on this line can then be matched with a unique room in the hotel, ensuring everyone fits <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

## The Limits of Infinite Capacity

### The Uncountable Party Bus

A major challenge arises with a "big bus" where everyone is identified by an infinitely long name consisting only of two letters, 'A' and 'B' (e.g., "A, B, B, A, A..." or "AB, AB, AB...") <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. This bus contains a person for every possible infinite sequence of these two letters <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. The hotel cannot accommodate this group <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

### Cantor's Diagonalization Argument

To explain why these guests cannot fit, the manager demonstrates by attempting to list them in the infinite spreadsheet <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. Even with a complete infinite list of names assigned to rooms, it is possible to write down the name of a person who is *not* on the list <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.

This is done by taking the first letter of the first name on the list and flipping it (A to B, or B to A), then taking the second letter of the second name and flipping it, and so on, all the way down the list <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. The resulting new name is guaranteed to not appear anywhere on the list because it differs from every name on the list by at least one character – specifically, the character on the diagonal position <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

### Countable vs. Uncountable Infinities

The Hilbert Hotel's rooms represent a [[Countable vs uncountable infinity | countably infinite]] set, meaning there are as many rooms as there are positive integers (1, 2, 3, ...) <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. In contrast, the number of people on the "party bus" is [[Countable vs uncountable infinity | uncountably infinite]] <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. If one attempts to match each of these people with an integer, there will always be people left over <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. This demonstrates that some [[Infinity in mathematics | infinities]] are larger than others <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.

## Implications

The discovery of different sized [[Infinity in mathematics | infinities]] sparked a line of inquiry that directly led to the invention of modern computing devices <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>, a connection explored further in the [[History of infinite sets and technology | history of infinite sets and technology]].