---
title: Symmetries and dihedral groups
videoId: mvmuCPvRoWQ
---

From: [[3blue1brown]] <br/> 

[[group_theory_and_symmetries | Group theory]] is primarily concerned with the study of symmetry <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

## Understanding Symmetry

When considering a symmetric shape like a square, its symmetry can be defined by all the actions that can be performed on it which leave it looking indistinguishable from its original state <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

Examples of such actions on a square include:
*   Rotating it 90 degrees counterclockwise <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
*   Flipping it around its vertical line of symmetry <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

Each of these actions is called a "symmetry" of the square <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

## Groups of Symmetries

All the symmetries of an object, when collected together, form a "group of symmetries" (or simply a "group") <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

The particular group of symmetries for a square consists of 8 distinct symmetries <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>:
*   The action of "doing nothing" (identity) <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.
*   Three different rotations (90°, 180°, 270°) <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.
*   Four different ways to flip the square over (reflections) <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

This group of 8 symmetries is specifically known as the **dihedral group of order 8** <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

### Finite vs. Infinite Groups

The dihedral group of order 8 is an example of a finite group, as it contains a limited number of actions (8 actions) <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

However, many other groups consist of infinitely many actions <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. For instance, the group of all possible rotations of a circle (of any angle) is an infinite group. This group captures all symmetries of the circle that do not involve flipping it <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. In this group, every action exists on an infinite continuum between 0 and 2π radians <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

### Group Arithmetic

A core aspect of [[group_theory_and_symmetries | group theory]] is understanding how symmetries interact with each other <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. This interaction forms a kind of arithmetic within the group:
*   On a square, rotating 90 degrees and then flipping it vertically results in the same overall effect as flipping it over a diagonal line <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.
*   On a circle, rotating 270 degrees followed by a 120-degree rotation is equivalent to a single 30-degree rotation <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.

In any group, two actions can be "added" or "multiplied" together by applying one after the other to produce a third action within the group <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. This collection of underlying relations, defining how pairs of actions compose to form a single equivalent action, is what fundamentally defines a group <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>. This organization of a collection of actions by their composition relation is crucial to much of modern mathematics <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.