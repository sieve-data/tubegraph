---
title: Development of open source web browsers
videoId: p572p-irRaU
---

From: [[fireship]] <br/> 

The World Wide Web is considered a critical pillar of human civilization, once called "cyberspace" by John Perry Barlow, who envisioned a world where anyone could express beliefs without fear of coercion or silence <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This freedom has had significant impacts, from influencing governments to generating wealth and enabling widespread sharing of content <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## The Threat to Web Openness
An [[importance_and_impact_of_browser_competition | existential threat]] to this openness exists in the form of browser consolidation <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. Browsers like Chrome, Safari, Edge, and Firefox account for over [[browser_market_share_and_dominance | 90% of the market share]] <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. Most of these browsers either share technology or receive funding controlled by Google <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. This concentration of power means that whoever controls the browser ultimately controls the Internet <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

> "He who controls the spice controls the universe, but he who controls the browser controls the Internet." <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>

## The Browser Wars and New Entrants
The browser wars are currently ongoing <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. While Firefox recently launched new features like sidebar-managed tabs, which were already present in Arc Browser <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>, new open-source browsers are emerging. Two notable examples built in Rust that are currently trending are Verso, which uses the Servo engine, and Blitz, a highly minimal web renderer <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

## Ladybird: A Futuristic Open-Source Browser
An even more ambitious project is Ladybird, a futuristic open-source browser <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

### Origins with SerenityOS
Ladybird's origins trace back to Andreas Kling, a software engineer who previously worked on WebKit at Apple and Nokia <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. In October 2018, while unemployed and bored, Kling embarked on an extreme project: building his own operating system, SerenityOS <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. This OS, intended for daily use, featured a 1990s graphical user interface (GUI) and a late 2000s Unix command-line interface (CLI) <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. Every component, from the kernel to the web browser, had to be built from scratch for SerenityOS <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. The name "SerenityOS" is inspired by the Serenity Prayer <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

### Evolution into Ladybird
On July 4th, 2022, the browser engine developed for SerenityOS declared its independence as a cross-platform project and a full web browser <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. It was renamed Ladybird <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. Two years later, with over a thousand contributors and half a million lines of C++ code, Andreas Kling partnered with a GitHub co-founder to establish a non-profit organization to manage the browser <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

### Project Philosophy
The Ladybird project operates on the principle of having "no incentives" to avoid negative influences <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. It is funded entirely through sponsorships and donations <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>. Crucially, its code is completely free and does not borrow from other browsers <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. This contrasts with privacy-focused browsers like Brave, which is a for-profit entity built on Google's Chromium engine <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

### Development Challenges
[[challenges_in_creating_a_new_web_browser | Building a web browser from scratch]] is incredibly complex and generally considered impossible <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. For [[introduction_to_web_development | web developers]] to create websites using HTML, CSS, and JavaScript <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>, browser engines must adhere to the W3C specification, which contains over 1.4 million words and constantly evolves with new features, raising the barrier to entry <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

The Ladybird developers have already built their own HTML and JavaScript engines, creatively named libHTML and libJS <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. They also leverage established [[web_application_tools_for_developers | tools]] like FFmpeg for video support <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. In software development, the process typically follows phases: "make it work," "make it good," and "make it faster" <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. Ladybird is currently in the first phase: "make it work" <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.

The first alpha version for Linux and macOS is not expected until the summer of 2026, with a Windows version coming even later <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. However, the code is available on GitHub for those who wish to experiment by building it from source <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.

### Related Open-Source Tools
Speaking of free and open-source [[web_application_tools_for_developers | tools]], Convex is highlighted as an alternative to Firebase for app developers <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. It simplifies backend development by providing scheduled jobs, server functions, database queries, and file storage using pure [[state_of_javascript_in_modern_development | TypeScript]] <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. This enables tRPC-style autocomplete and type safety throughout the stack <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. Convex also offers an ACID-compliant database with optimized caching and optional schema enforcement, avoiding the complexities of SQL migrations and ORMs, and features automatic real-time subscriptions on all database queries <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

## Benefits of Competition
Regardless of the [[browser_market_share_and_dominance | market share]] Ladybird achieves, its development benefits everyone by challenging the increasing consolidation of power on the Internet <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.