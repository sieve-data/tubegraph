---
title: Advanced animation techniques with Framer Motion
videoId: SuqU904ZHA4
---

From: [[fireship]] <br/> 

Animation is a powerful tool for developers, capable of transforming standard features into something unique and engaging <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This article explores how to implement declarative animations in React using the [[using_framer_motion_for_animations_in_react | Framer Motion]] library, covering topics from basic styling and state management to complex, physics-based animations <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

## Introduction to [[using_framer_motion_for_animations_in_react | Framer Motion]]

[[using_framer_motion_for_animations_in_react | Framer Motion]] is a well-maintained and polished library for implementing animations in React, developed by the team behind the Framer design tool <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. It offers an intuitive approach to animation, simplifying code compared to traditional CSS animations <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. Beyond ease of use, [[using_framer_motion_for_animations_in_react | Framer Motion]] can integrate with React application state and listen to various browser events, which is not possible with CSS alone <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.

## Getting Started

To begin, a React project is initialized using `create-react-app` <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. The only dependency required is `framer-motion`, installed via npm <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. After removing boilerplate code and importing `normalize.css` for a clean slate, custom CSS for the project can be added <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

## Basic Animation: Animated Button

A basic animation can be implemented by animating a button:
1.  Import the `motion` component from [[using_framer_motion_for_animations_in_react | Framer Motion]] <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
2.  Replace a regular HTML `button` tag with a `motion.button` component <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
3.  Utilize props like `whileHover` to make the button grow on hover and `whileTap` to make it shrink on tap, simulating a push <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

This demonstrates how [[using_framer_motion_for_animations_in_react | Framer Motion]] simplifies animation by wrapping HTML elements and providing direct animation props <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

## Building an Animated Modal Window

A common UI feature, the modal window, can be built with animations using [[using_framer_motion_for_animations_in_react | Framer Motion]] <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. It consists of two main components: a `Backdrop` and the `Modal` window itself <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

### Backdrop Component

The `Backdrop` is an overlay that darkens the screen and sits behind the modal window <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   It's defined as a `motion.div` <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
*   It takes `children` to embed other components (like the modal) and an `onClick` handler to manage global state (e.g., closing the modal) <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
*   CSS positions it absolutely, covers the screen, and uses an opacity in its hex color for a semi-transparent black background <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
*   Animation states for the backdrop:
    *   `initial`: `opacity: 0` (invisible) <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.
    *   `animate`: `opacity: 1` (visible) <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.
    *   `exit`: `opacity: 0` (fade out) <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.

### Modal Component

The `Modal` component is the window that appears on top of the backdrop <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.
*   It's nested inside the `Backdrop` component <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
*   An `onClick` handler on the modal's `motion.div` calls `event.stopPropagation()` to prevent clicks inside the modal from triggering the backdrop's close function <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.
*   CSS uses `clamp()` and `min()` functions for responsive width and height without media queries <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.

## Advanced Animation Concepts

### Variants for Complex Animation Sequences

[[using_framer_motion_for_animations_in_react | Framer Motion]]'s `variants` property allows defining multiple custom animation states within an object <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. This enables creating complex sequences of animations based on user interaction or application state <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

For the modal, `variants` defines three states:
*   `hidden`: `translateY: -100vh` (starts off-screen above) <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
*   `visible`: `translateY: 0` (drops into natural position) <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
*   `exit`: `translateY: 100vh` (drops off-screen below) <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

### Spring Animations and Physics

The `transition` property can be tweaked to add dynamic effects. For the modal, a `type: 'spring'` animation can be applied for a bouncy effect <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.

Spring animations involve two key physics parameters:
*   **Damping**: A decrease in the amplitude of an oscillation due to energy being drained from the system <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. Lower damping results in more bouncing, while higher damping reduces the bounce <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.
*   **Stiffness**: Affects how slowly or quickly the spring reacts <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>. Lower stiffness makes the spring react slowly, higher stiffness makes it react quickly <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.

> [!TIP]
> Understanding the relationship between damping and stiffness can significantly enhance the visual quality of spring animations <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

### `AnimatePresence` for Exit Animations

A common challenge is animating components as they are removed from the DOM, as simply unmounting them causes them to disappear instantly <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>. [[using_framer_motion_for_animations_in_react | Framer Motion]]'s `AnimatePresence` component solves this problem <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.

By wrapping the `Modal` component with `AnimatePresence`:
*   The modal remains visible temporarily even after its state changes and it's conceptually "removed" from the DOM, allowing its `exit` animation to complete <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.
*   `initial={false}` disables any initial animations when `AnimatePresence` first renders <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
*   `exitBeforeEnter` (set to `true`) ensures that all nodes finish their exit animation before new ones enter <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.

### Draggable Components

One of the simplest yet powerful advanced features is making a component draggable. By simply adding the `drag` prop to a `motion.div` component, it becomes freely draggable around the screen <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>. This immediately adds interactive functionality without complex event handling.