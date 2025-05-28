---
title: Concept of Countably vs Uncountably Infinite
videoId: OxGsU8oIWjY
---

From: [[veritasium]] <br/> 

The [[hilbert_hotel_and_infinite_rooms | Hilbert Hotel]] is a thought experiment designed to illustrate the nature of infinity. It features a hotel with an infinite number of rooms, numbered sequentially: one, two, three, four, and so on, forever <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. As the manager, one might assume that anyone could always be accommodated <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>, but there are limits to even this infinite capacity <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## Accommodating Countably Infinite Guests

Initially, imagine the [[hilbert_hotel_and_infinite_rooms | Hilbert Hotel]] is full, with one person in each of its infinite rooms <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

### One New Guest
If a single new guest arrives, the manager can ask everyone to move down one room (e.g., room one to room two, room two to room three) <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. This vacates room one for the new guest <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

### A Finite Busload of Guests
If a bus arrives with a finite number of people, such as a hundred, the same principle applies: all current guests move down by that number of rooms (e.g., 100 rooms), making the first 100 rooms available for the new arrivals <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

### An Infinitely Long Bus
When a bus carrying infinitely many people arrives, a more sophisticated solution is needed <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. The manager can tell each existing guest to move to the room with double their current room number (e.g., room one to room two, room two to room four, room three to room six) <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. This frees up all the odd-numbered rooms <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. Since there are an infinite number of odd numbers, each person from the infinite bus can be assigned a unique odd-numbered room <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

### An Infinite Number of Infinite Buses
The hotel can even accommodate an infinite number of infinite buses <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. This is achieved by creating an infinite grid or "spreadsheet" <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. One row represents the existing hotel guests, and subsequent rows represent each incoming infinite bus (bus 1, bus 2, bus 3, etc.) <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. Columns represent the position of each person (room number for existing guests, seat number for bus passengers) <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

Each person gets a unique identifier based on their vehicle and position <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. To assign rooms, one draws a line that zigzags across this infinite spreadsheet, visiting each unique ID exactly once <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>. By "straightening out" this zigzag line, an infinite-by-infinite grid is transformed into a single infinite line <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. Each person on this line can then be matched with a unique room in the hotel <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

## The Concept of Uncountably Infinite

Despite the hotel's remarkable capacity, there exists a type of infinity it cannot accommodate <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. Imagine an "infinite party bus" where each person is identified by a unique, infinitely long name consisting only of the letters 'A' and 'B' (e.g., A, B, B, A, A, A... or AB, AB, AB...) <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. This bus contains a person for every possible infinite sequence of these two letters <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

When attempting to assign rooms to these guests, the manager demonstrates that they cannot all fit <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. Even if an infinite spreadsheet is used to list every hotel room and its assigned infinitely long 'A'/'B' name, a name can always be created that is *not* on the list <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

### Cantor's Diagonalization Argument
This proof involves a process called **diagonalization**:
1.  Take the first letter of the name assigned to room one and flip it (A becomes B, B becomes A) <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
2.  Take the second letter of the name assigned to room two and flip it <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.
3.  Continue this process indefinitely, taking the Nth letter of the name assigned to room N and flipping it <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

The resulting infinitely long name is guaranteed not to appear anywhere on the list <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. It differs from the first name by its first letter, from the second name by its second letter, and so on, differing from every name on the list by at least one character—the letter on the diagonal <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.

## Countably vs. Uncountably Infinite
The number of rooms in the [[hilbert_hotel_and_infinite_rooms | Hilbert Hotel]] is **countably infinite** <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. This means there are as many rooms as there are positive integers (1, 2, 3, ...), allowing for a one-to-one correspondence <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.

By contrast, the number of people on the "party bus" is **uncountably infinite** <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. If one attempts to match each of these people with an integer, there will always be people left over <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.

This demonstrates that [[the_different_sizes_of_infinity | some infinities are bigger than others]] <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. The discovery of [[the_different_sizes_of_infinity | different sized infinities]] profoundly impacted mathematics, leading to a line of inquiry that influenced the development of modern computing devices <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.