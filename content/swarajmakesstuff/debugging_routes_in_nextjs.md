---
title: Debugging Routes in Nextjs
videoId: 9AMlt2ThybU
---

From: [[swarajmakesstuff]] <br/> 

When implementing [[Nextjs Parallel Routes | parallel]] and [[Nextjs Intercepting Routes | intercepting routes]] in Next.js, developers may encounter errors if certain routing conventions are not followed <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.

## Importance of `default.js`

A common issue arises when the `default.js` file is not included in the application <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. If `default.js` is removed, the application may return a 404 "could not be found" error, even though the page content might still render visibly <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>. This error is particularly prevalent when working with TypeScript <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.

### Why `default.js` is Crucial

Next.js defines `default.js` to handle fallback scenarios <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. When a user tries to reload a page, Next.js may not be able to immediately recover the active state of the current URL <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>. In such cases, `default.js` is loaded temporarily until the complete page state can be recovered and rendered <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.

If `default.js` is absent, Next.js skips this recovery step, leading to a redirection to a 404 error page <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. Therefore, it is essential to always include a `default.js` page, especially when using TypeScript <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.