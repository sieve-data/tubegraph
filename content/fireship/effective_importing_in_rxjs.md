---
title: Effective Importing in RxJS
videoId: ewcoEYS85Co
---

From: [[fireship]] <br/> 

When working with [[introduction_to_rxjs_and_observables | RxJS]], how the library is imported can significantly impact application bundle size <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

## Avoiding Large Bundle Sizes

A common pitfall is to import the entire [[introduction_to_rxjs_and_observables | RxJS]] library using `import star as RX` <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. While this makes all functionalities available, it causes the entire library to be bundled into the application's code, leading to a larger bundle size (e.g., 47 kilobytes) <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

## Tree-Shaking for Efficiency

[[introduction_to_rxjs_and_observables | RxJS]] is a "tree-shakable" library <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. This means that only the specific code that is actively used needs to be imported and bundled <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

To import [[introduction_to_rxjs_and_observables | RxJS]] effectively and leverage tree-shaking:
*   Only import the specific classes and [[rxjs_operators_and_their_usage | operators]] that are necessary for your source code <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   This practice can significantly reduce the bundle size (e.g., to less than 2 kilobytes) <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.