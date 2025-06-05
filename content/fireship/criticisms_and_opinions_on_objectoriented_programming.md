---
title: Criticisms and opinions on objectoriented programming
videoId: goy4lZfDtCE
---

From: [[fireship]] <br/> 

[[Objectoriented programming in Java|Object-oriented programming]] (OOP) is considered by some to be "absolutely the worst thing that's ever happened to the field of software engineering" <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This controversial opinion is echoed by many experienced developers <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>, with [[programmer_dissatisfaction|developers hating on OOP]] frequently in recent years <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

## Historical Perspective and Core Concepts

The concept behind OOP has existed since the 1960s <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. It allows developers to encapsulate data and logic within objects <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. The process typically begins with a class, which acts as a blueprint for creating multiple object instances <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. These classes can then inherit behaviors from one another, establishing a hierarchy of abstractions <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. OOP also incorporates various design patterns, such as singleton, factory, and dependency injection <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

## Criticisms of OOP

*   **Complexity and Perceived Productivity Gains**: The sophisticated features and design patterns in OOP can sometimes mislead developers into believing they are achieving productivity gains, even when a much simpler solution might exist <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
*   **Boilerplate Code**: A common complaint is that [[objectoriented_programming_in_java|object-oriented languages]] often demand significantly more boilerplate code compared to more functional programming approaches <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
*   **Mutable State Issues**: Applications built with OOP can accumulate a large amount of mutable state, making the code challenging to test, refactor, and comprehend <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   **Edgar Dijkstra's Quote**: Even legendary computer scientist Edgar Dijkstra is quoted as saying, "Object-oriented programs are offered as alternatives to correct ones" <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

## Balancing Perspectives

While acknowledging the validity of these criticisms, some developers believe they are "a bit overblown" <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

For instance, in JavaScript, many developers rarely implement their own classes or use inheritance <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. Instead, they prefer to create modules that export functions and plain objects <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. This approach offers benefits such as:
*   **Tree-shakeability**: Allows dead code to be eliminated when bundled <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
*   **Reduced Complexity**: Avoids concerns like constructors, getters, setters, and the often-confusing `this` keyword, which can add unnecessary complexity <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.

### When OOP Can Be Beneficial

Despite the criticisms, there are scenarios where classes and [[objectoriented_programming_in_java|object-oriented programming]] can be very effective:
*   **Encapsulation**: Classes can be a useful way to encapsulate specific functionalities <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
*   **Frameworks**: They work well in frameworks like Angular or Nest, which are designed with a predictable way of interacting with classes <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
*   **Specific Tools**: Other tools, such as Flutter or the Unity framework, are fundamentally [[objectoriented_programming_in_java|object-oriented]] and are highly regarded <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

Ultimately, when executed properly, [[objectoriented_programming_in_java|object-oriented programming]] can be intuitive and effective <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. However, it is not always the optimal solution, highlighting the importance of considering other [[programming_concepts_and_paradigms|programming concepts and paradigms]] like procedural or functional approaches with an open mind <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.