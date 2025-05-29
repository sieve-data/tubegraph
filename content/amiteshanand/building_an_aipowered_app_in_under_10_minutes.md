---
title: Building an AIpowered app in under 10 minutes
videoId: UGbePdInPVc
---

From: [[amiteshanand]] <br/> 

An AI-powered application called "Do You Know" (named *Jaan-Pehechan* in Hindi) was developed in just 10 minutes without writing a single line of code <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. This app allows users to upload or click pictures of objects, which then provides interesting facts about them <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. For example, uploading an image of a red fort led to information about its history and UNESCO World Heritage status <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.

## Tools Used

The rapid development was made possible by leveraging two key platforms:

### [[using_lovable_ai_app_builder | Lovable AI App Builder]]
Lovable is an AI app builder that can create applications from a simple prompt <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
It offers:
*   Basic CRUD (Create, Read, Update, Delete) functionality <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
*   Connectivity with Supabase for database integration <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
*   Full functionality generated with a single command <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
*   Export projects via GitHub, publish, and deploy <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
*   A free plan offering five messaging credits daily, with paid plans available at $20 <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

### Nvus AI Studio
Nvus AI Studio serves as an inference provider for AI models <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>. It provides a full-stack platform to utilize various open LLMs (Large Language Models) such as Quin DC 5, Mistral, and Meta Llama <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. The "Do You Know" app specifically used Quin Vision models from Nvus AI Studio for its AI features <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

Nvus offers:
*   A playground to test and compare models <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. Users can compare performance, add system prompts, and set parameters <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.
    *   For example, testing image generation with prompts like "Eiffel Tower on Mars" or "a boy dancing underwater" <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
    *   Comparing text-to-text models like Meta Llama 3.18B Instruct and 2.5 Coder 7B for explaining JavaScript code <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   Access to multiple open LLM models at a cheaper rate compared to other AI providers <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.
*   API keys for integration via Python, Curl, or JavaScript, adhering to OpenAI formatting <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.
*   Free credits upon sign-up for trial and testing <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.

## Building the "Do You Know" App

The app was initiated with a single prompt to Lovable: "Build an app like [current app] features lot of potential features to add" and instructions to use the Vision model via Nvus API <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.

### Development Timeline
The process was remarkably quick:
*   The initial prompt was given at 11:42 p.m. <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
*   The app was almost ready by 11:50 p.m., taking under 10 minutes for the core functionality <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
*   Lovable even suggested refactoring the code due to its length <a class="yt-timestamp" data-t="00:07:55">[00:07:55]</a>.

### Post-Generation Modifications
After the initial generation, further enhancements were added:
*   Integration of image analysis using the Nvus Vision API <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.
*   Improvements to the UI and features <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.
*   Setup of Supabase to store the five most recent searches <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>. This required connecting Supabase projects and providing Nvus API keys <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.

## Future Enhancements
The creator plans to add more features to the "Do You Know" app, including:
*   OAuth (authentication) <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
*   A streak feature to track what users learned daily, similar to Duolingo or Snapchat streaks <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.