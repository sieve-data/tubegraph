---
title: Hilbert Hotel paradox
videoId: OxGsU8oIWjY
---

From: [[veritasium]] <br/> 

The Hilbert Hotel is a conceptual hotel with an infinite number of rooms, numbered one, two, three, four, and so on forever <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. Despite its infinite capacity, there's a limit to how many guests it can accommodate, demonstrating that some infinities are larger than others <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## Accommodating Guests

When managing the Hilbert Hotel, certain strategies allow for accommodating new guests even when all infinite rooms are already occupied by an infinite number of people <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

### A Single New Guest

If a new guest arrives and all rooms are full, the manager can simply tell all existing guests to move down one room (guest in room one moves to room two, guest in room two moves to room three, and so on) <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. This frees up room one for the new arrival <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

### A Finite Number of New Guests

For a finite group of new guests, such as a bus with a hundred people, the process is similar: everyone moves down a corresponding number of rooms (e.g., 100 rooms), and the new guests occupy the newly vacated rooms <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

### An Infinite Number of New Guests

When an infinitely long bus carrying infinitely many people arrives, a more sophisticated method is required <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. Existing guests are asked to move to the room with double their current room number (e.g., room one to room two, room two to room four, room three to room six) <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. This frees up all odd-numbered rooms, of which there are an infinite number <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. Each person from the infinite bus can then be assigned a unique odd-numbered room <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

### An Infinite Number of Infinite Buses

If an infinite number of infinite buses arrive, all carrying an infinite number of people, a spreadsheet approach can be used <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. Each row represents a bus (or the existing hotel guests), and columns represent positions within the vehicle <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. By drawing a zigzag line from the top-left corner across the spreadsheet, every unique ID (combination of vehicle and position) can be covered exactly once <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. This effectively transforms an infinite-by-infinite grid into a single infinite line, allowing each person to be assigned a unique room <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

## The Uncountably Infinite Challenge

Despite these creative solutions, there is a class of infinities that the Hilbert Hotel cannot accommodate <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

### The Infinite Party Bus

Imagine an "infinite party bus" where each person is identified by a unique, infinitely long name consisting only of the letters 'A' and 'B' <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>. On this bus, every possible infinite sequence of 'A's and 'B's exists <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

### The Paradox: Uncountable Infinity

When attempting to assign rooms to these guests, it becomes impossible to list every single name, even with an infinite number of rooms <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. This is demonstrated using a method similar to [[cantors_diagonalization_proof | Cantor's Diagonalization Proof]] <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>:

1.  Create an infinite list, assigning a room number to each infinite 'A'/'B' name from the bus <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
2.  To create a new name not on the list, take the first letter of the first name and flip it (A to B, B to A) <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
3.  Then, take the second letter of the second name and flip it <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.
4.  Continue this process down the diagonal of the list <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

The resulting name will be different from every name on the list by at least one character (the diagonal letter) <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. This proves that no matter how long the list is, there will always be a name that isn't on it, meaning the set of names is larger than the set of natural numbers.

## Countable vs. Uncountable Infinity

The Hilbert Hotel has a *countably infinite* number of rooms, meaning there are as many rooms as there are positive integers <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. However, the number of people on the "party bus" is *uncountably infinite* <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. If you try to match each uncountably infinite person with an integer (room), there will always be people left over <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

> [!INFO] Key Takeaway
> This demonstrates that "some infinities are bigger than others" <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>, and there is a limit to the number of people that can fit into the Hilbert Hotel <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

The discovery of different-sized infinities sparked a line of inquiry that led directly to the invention of modern computing devices <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.