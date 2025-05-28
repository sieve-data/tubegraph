---
title: Hilbert Hotel and Infinite Rooms
videoId: OxGsU8oIWjY
---

From: [[veritasium]] <br/> 

The Hilbert Hotel is a conceptual hotel featuring an infinite number of rooms, numbered sequentially from one onwards <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a> <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. As the manager of this hotel, one might initially assume it can always accommodate any number of guests <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. However, there are limits to even the [[mathematical_paradoxes_of_infinity | infinity]] of rooms available <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## Accommodating New Guests

### A Single New Guest
If the hotel is full with an infinite number of people, and one new guest arrives, they can still be accommodated <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a> <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. The solution is to announce to all existing guests to move down one room: the person in room one moves to room two, room two to room three, and so on <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a> <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. This frees up room one for the new guest <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

### A Finite Group of New Guests
Similarly, if a bus with a finite number of people, such as a hundred, arrives, the same principle applies <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. All existing guests move down a hundred rooms, vacating the first hundred rooms for the new arrivals <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

### An Infinitely Long Bus
When an infinitely long bus carrying an infinite number of people arrives, a different strategy is needed <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. Existing guests are instructed to move to the room with double their current room number (e.g., room one to room two, room two to room four) <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. This frees up all odd-numbered rooms <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. Since there are an infinite number of odd numbers, each person from the infinite bus can be assigned a unique odd-numbered room <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a> <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

### An Infinite Number of Infinite Buses
The hotel can even accommodate an infinite number of infinitely long buses <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. This is managed by conceptualizing an infinite spreadsheet <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>:
*   Rows represent the existing hotel guests and each incoming bus (Bus 1, Bus 2, etc.) <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
*   Columns represent the position of each person (Hotel Room 1, Bus 1 Seat 1, etc.) <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

Each person gets a unique identifier based on their vehicle and position <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. To assign rooms, a line is drawn that zigzags across the spreadsheet, touching every unique ID exactly once <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. This effectively transforms an infinite-by-infinite grid into a single infinite line, allowing each person to be matched with a unique room in the hotel <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a> <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

## The Limit: Uncountably Infinite Guests

Despite the hotel's ability to accommodate vast numbers of guests, there is a limit. This limit is demonstrated by a "big bus" where guests are identified by infinitely long names consisting only of the letters 'A' and 'B' <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a> <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. Every possible infinite sequence of these two letters is represented by a person on the bus <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

The challenge arises when trying to assign these guests to rooms using a spreadsheet <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. Even if an infinite list of room assignments is created, it's always possible to construct the name of a person who is not on that list <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>:
*   Take the first letter of the name in Room 1 and flip it (A to B, or B to A) <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
*   Take the second letter of the name in Room 2 and flip it <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.
*   Continue this process down the diagonal of the list, flipping the *n*th letter of the *n*th name <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

The resulting newly constructed name will differ from every name on the list by at least one character (the diagonal letter), proving it's not accounted for <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a> <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>.

### Countably vs. Uncountably Infinite

The Hilbert Hotel's rooms represent a [[concept_of_countably_vs_uncountably_infinite | countably infinite]] set, meaning there are as many rooms as there are positive integers (1, 2, 3...) <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a> <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>. In contrast, the number of people on the "big bus" is [[concept_of_countably_vs_uncountably_infinite | uncountably infinite]] <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. If one attempts to match each of these people with an integer (a room number), there will always be people left over <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. This illustrates that [[the_different_sizes_of_infinity | some infinities are bigger than others]] <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>, and represents a limit to the Hilbert Hotel's capacity <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

The [[implications_of_different_sized_infinities | discovery of different sized infinities]] profoundly influenced subsequent scientific inquiry, ultimately leading to the invention of modern computing devices <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a> <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.