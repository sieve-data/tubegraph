---
title: Definition and exploration of distance in mathematics
videoId: XFDM1ip5HdU
---

From: [[3blue1brown]] <br/> 

The concept of distance plays a fundamental role in mathematics, particularly in understanding how numbers relate to each other and how [[teaching_and_understanding_mathematical_concepts | mathematical concepts]] are defined and expanded <a class="yt-timestamp" data-t="03:53:00">[03:53:00]</a>. While intuitively understood as "how far apart" two objects or numbers are, its formal definition allows for diverse interpretations that can lead to new forms of mathematics <a class="yt-timestamp" data-t="00:36:00">[00:36:00]</a>.

## Intuitive and Formal Understanding of Distance

Early [[conceptualizing_mathematical_problems | mathematical conceptualization]] of distance often begins with a paradoxical feeling: no matter how close two things are, they can always be brought a little bit closer together without touching <a class="yt-timestamp" data-t="01:18:00">[01:18:00]</a>. This can be visualized by placing two objects on a number line, for instance, one at 0 and the other at 1 <a class="yt-timestamp" data-t="01:29:00">[01:29:00]</a>. If the first object marches towards the second, cutting the distance between them in half with each step, the points it touches form a sequence: ½, ½ + ¼, ½ + ¼ + ⅛, and so on <a class="yt-timestamp" data-t="01:35:00">[01:35:00]</a>. Geometrically, these numbers clearly approach 1 <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>.

The definition of "approach" is crucial here <a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a>. It's not merely that the distance between each number in a sequence and a target value (e.g., 1) gets smaller <a class="yt-timestamp" data-t="03:20:00">[03:20:00]</a>. What makes the target value special is that the numbers can get *arbitrarily close* to it <a class="yt-timestamp" data-t="03:29:00">[03:29:00]</a>. This means that no matter how small a desired distance is chosen (e.g., one hundredth, one millionth), if one goes far enough down the list of numbers, they will eventually fall within that tiny distance of the target value <a class="yt-timestamp" data-t="03:36:00">[03:36:00]</a>. This precise understanding allows for the formal definition of [[convergent_infinite_sums | infinite sums]] <a class="yt-timestamp" data-t="04:01:00">[04:01:00]</a>.

## Properties of a Distance Function (Metric)

A mathematical notion of distance is essentially a function that takes two numbers and outputs a number indicating how far apart they are <a class="yt-timestamp" data-t="09:15:00">[09:15:00]</a>. For a distance function to be genuinely useful, it must share certain properties with the familiar concept of distance <a class="yt-timestamp" data-t="09:33:00">[09:33:00]</a>:

*   **Shift Invariance:** The distance between two numbers should not change if both numbers are shifted by the same amount <a class="yt-timestamp" data-t="09:42:00">[09:42:00]</a>. For example, the distance between 0 and 4 should be the same as between 1 and 5, or 2 and 6 <a class="yt-timestamp" data-t="09:48:00">[09:48:00]</a>.
*   **Triangle Inequality:** Although not explicitly elaborated on in the transcript, this property ensures that the direct path between two points is always the shortest <a class="yt-timestamp" data-t="10:14:00">[10:14:00]</a>. This property is also satisfied by legitimate distance functions <a class="yt-timestamp" data-t="13:26:00">[13:26:00]</a>.

## The 2-adic Metric: An Alternative Notion of Distance

The standard number line is not the only reasonable way to organize numbers <a class="yt-timestamp" data-t="09:05:00">[09:05:00]</a>. Mathematicians in the 20th century discovered alternative ways to define distance between rational numbers, leading to profound insights <a class="yt-timestamp" data-t="08:51:00">[08:51:00]</a>. One such alternative is the **2-adic metric** <a class="yt-timestamp" data-t="13:35:00">[13:35:00]</a>.

This metric organizes numbers into a hierarchy of "rooms," "sub-rooms," and "sub-sub-rooms," based on divisibility by powers of 2 <a class="yt-timestamp" data-t="10:34:00">[10:34:00]</a>. For instance:
*   Numbers in different large "yellow rooms" are a distance of 1 from each other <a class="yt-timestamp" data-t="12:43:00">[12:43:00]</a>.
*   Numbers in the same large room but different "orange sub-rooms" are a distance of ½ from each other <a class="yt-timestamp" data-t="12:50:00">[12:50:00]</a>.
*   Numbers in the same orange sub-room but different "sub-sub-rooms" are a distance of ¼ from each other <a class="yt-timestamp" data-t="12:59:00">[12:59:00]</a>.
*   This continues, using reciprocals of increasingly larger powers of 2 to indicate closeness <a class="yt-timestamp" data-t="13:09:00">[13:09:00]</a>.

Under the 2-adic metric, numbers like 1, 3, 7, 15, 31, and so on (which are all one less than a power of 2) genuinely approach negative 1 <a class="yt-timestamp" data-t="14:02:00">[14:02:00]</a>. This notion of distance makes certain seemingly nonsensical [[convergent_infinite_sums | infinite sums]], like 1 + 2 + 4 + 8 + ... = -1, mathematically consistent <a class="yt-timestamp" data-t="07:07:00">[07:07:00]</a>, <a class="yt-timestamp" data-t="13:58:00">[13:58:00]</a>.

The 2-adic metric is part of a broader family of distance functions called **p-adic metrics**, where 'p' represents any prime number <a class="yt-timestamp" data-t="13:40:00">[13:40:00]</a>. These metrics give rise to entirely new types of numbers, distinct from real or complex numbers, and have become central to modern number theory <a class="yt-timestamp" data-t="13:48:00">[13:48:00]</a>.

This exploration of distance highlights a recurring pattern in [[the_relationship_between_mathematical_invention_and_discovery | the discovery of math]]: a seemingly ill-defined or nonsensical observation from "nature" prompts the definition of new concepts, which in turn yield genuinely useful mathematics and broaden traditional notions <a class="yt-timestamp" data-t="14:22:00">[14:22:00]</a>.