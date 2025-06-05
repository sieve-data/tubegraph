---
title: Technical details of the websites tech stack
videoId: xR5d4Ba4FZg
---

From: [[fireship]] <br/> 

The website "The Real World," formerly known as Andrew Tate's Hustler's University, was described by hackers as "hilariously insecure" <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. Through private research, its [[understanding_and_choosing_a_tech_stack | tech stack]] was reverse-engineered <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## Overall [[understanding_and_choosing_a_tech_stack | Stack]] Overview

A job listing for a full-stack developer within the platform's chat rooms provided key insights into the [[understanding_and_choosing_a_tech_stack | stack]] <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. The primary components identified include:
*   [[trends_in_programming_languages_and_web_development | TypeScript]] <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>
*   Tailwind CSS <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>
*   [[Networking and Web Technologies | Websockets]] <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>
*   REST <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>

## [[Frontend and backend development layers | Frontend]] Technologies

The website utilizes several modern [[Frontend and backend development layers | frontend]] technologies:
*   The main signup page for the platform uses [[comparison_of_web_development_frameworks | Next.js]] <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
*   However, the main application is built with Vite <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
*   It includes [[features_and_trade_offs_of_React_Angular_and_Vue | React.js]] <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
*   A significant security vulnerability found was that the [[Frontend and backend development layers | frontend]] JavaScript bundle was not obfuscated and contained all code comments, making it much easier to reverse engineer <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

## [[Backend development and serverside concepts | Backend]] Technologies

Investigation into DNS prefetch links in the document's head, likely pointing to [[Backend development and serverside concepts | backend]] services, revealed more details <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>:
*   The server hosting the API URL is Cloudflare <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
*   The presence of the text "rocket" on a 404 page indicates the use of the Rust Rocket framework <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>, confirmed as `rust rocket` <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>.
*   The use of Rust Rocket suggests a connection to Revolt chat, an open-source chat platform <a class="yt-timestamp" data-t="00:02:59">[00:03:01]</a>.
    *   In 2022, the developer of Revolt accused "Hustler's University" of stealing their software by violating the AGPL license <a class="yt-timestamp" data-t="00:03:03">[00:03:10]</a>.
    *   It appears they are still using a closed-source fork of Revolt <a class="yt-timestamp" data-t="00:03:21">[00:03:23]</a>.
*   The hackers were able to break authentication on the API <a class="yt-timestamp" data-t="00:03:28">[00:03:29]</a>.

## Mobile Development

The platform includes mobile applications:
*   It has a desktop wrapper <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   It uses Capacitor for iOS and Android <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
*   Capacitor is a tool designed to run web applications in a web view on iOS or Android, allowing for quick mobile app development from a web app <a class="yt-timestamp" data-t="00:02:16">[00:02:21]</a>.