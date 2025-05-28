---
title: Conways Game of Life and Undecidability
videoId: HeQX2HjkcNo
---

From: [[veritasium]] <br/> 

The Game of Life, created in 1970 by mathematician John Conway, is a "zero-player game" played on an infinite grid of square cells, each of which is either live or dead <a class="yt-timestamp" data-t="01:07:00">[01:07:00]</a>. John Conway sadly passed away in 2020 from COVID-19 <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>.

## Rules and Behavior
The game operates based on only two simple rules, which are applied to create successive generations after an initial arrangement of cells is set up <a class="yt-timestamp" data-t="01:35:00">[01:35:00]</a>:
1.  Any dead cell with exactly three living neighbors comes to life <a class="yt-timestamp" data-t="01:28:00">[01:28:00]</a>.
2.  Any living cell with less than two or more than three living neighbors dies <a class="yt-timestamp" data-t="01:35:00">[01:35:00]</a>.

Despite these simple rules, the game can generate a wide variety of behaviors <a class="yt-timestamp" data-t="01:53:00">[01:53:00]</a>:
*   Some patterns are stable and never change once they arise <a class="yt-timestamp" data-t="01:59:00">[01:59:00]</a>.
*   Others oscillate back and forth in a loop <a class="yt-timestamp" data-t="02:05:00">[02:05:00]</a>.
*   A few patterns, like the "glider," can travel across the grid forever <a class="yt-timestamp" data-t="02:05:00">[02:05:00]</a>.
*   Many patterns simply "fizzle out" <a class="yt-timestamp" data-t="02:18:00">[02:18:00]</a>.
*   A few patterns keep growing forever, generating new cells <a class="yt-timestamp" data-t="02:18:00">[02:18:00]</a>.

## Undecidability in the Game of Life
Given the simple rules, one might expect to be able to predict the ultimate fate of any pattern: will it reach a steady state, or will it keep growing without limit <a class="yt-timestamp" data-t="02:25:00">[02:25:00]</a>? However, it turns out that this question is impossible to answer <a class="yt-timestamp" data-t="02:34:00">[02:34:00]</a>.

The ultimate fate of a pattern in Conway's Game of Life is **undecidable** <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>. This means there is no possible algorithm guaranteed to answer the question in a finite amount of time <a class="yt-timestamp" data-t="02:48:00">[02:48:00]</a>. Even running the pattern for millions or billions of generations doesn't guarantee a definitive answer about its long-term behavior <a class="yt-timestamp" data-t="03:04:00">[03:04:00]</a>.

### Connection to Turing Completeness
The Game of Life is a [[The Halting Problem and Turing Machines | Turing complete]] system <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>. This means it is powerful enough to simulate any computable algorithm, just like a modern computer <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>, <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>. All [[The Halting Problem and Turing Machines | Turing complete]] systems come with an "analog of the [[The Halting Problem and Turing Machines | Halting Problem]]" – some undecidable property <a class="yt-timestamp" data-t="02:43:00">[02:43:00]</a>. In the case of Conway's Game of Life, its halting problem is literally whether or not a pattern eventually "halts" (i.e., reaches a stable state or disappears) <a class="yt-timestamp" data-t="02:48:00">[02:48:00]</a>, <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>.

Because the Game of Life is [[The Halting Problem and Turing Machines | Turing complete]], it is capable of simulating itself <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>. This means it's possible to create a Game of Life pattern that runs another Game of Life pattern <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>.

Many other systems are also [[The Halting Problem and Turing Machines | Turing complete]] and thus exhibit undecidability, including Wang tiles, quantum physics, airline ticketing systems, and even games like Magic: The Gathering <a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a>, <a class="yt-timestamp" data-t="03:21:00">[03:21:00]</a>.