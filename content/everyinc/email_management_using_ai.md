---
title: Email management using AI
videoId: MhKKKBG28a4
---

From: [[everyinc]] <br/> 

Kora is a product designed to solve the common dread associated with email by reducing the stress of managing an inbox [02:34:00]. It aims to provide a better way to handle the overwhelming volume of messages [03:15:00].

## What Kora Does

Kora helps users by taking away approximately 90% of emails from their inbox and presenting them in a brief format twice a day [03:46:00]. This allows users to read through essential information and bottom lines quickly, focusing only on important items [03:57:00].

Instead of manually archiving and reading emails one by one, Kora enables users to scroll through summaries of various emails, such as partnership updates, legal agreements, spending reports, newsletters, and promotions [00:04:00]. Once reviewed, the user is done, without needing to press archive [00:30:00]. Users can still return any email to their inbox or read the full message if desired [05:36:00]. This process saves a significant amount of time daily and transforms email management into a more pleasant experience [05:47:00].

## The Rapid Development of Kora

Kora's initial version (V1) was developed rapidly, with a functioning prototype created in a single day [00:40:00]. The entire product was built end-to-end in about three months [06:03:00]. This speed was made possible by leveraging AI tools, which can write a significant portion of the code [09:27:00]. The developer, Kieran, estimates that 80% to 90% of Kora's code was written by AI, while 100% of the thought process behind it came from him [11:41:00]. This demonstrates how AI acts as a collaborator, accelerating tedious tasks [11:55:00].

## Kora's Product Evolution

Initially, Kora began as an email assistant focused on drafting emails, similar to many other products available [06:40:00]. However, the team realized that even the best Large Language Models (LLMs) couldn't fully replicate human context [06:59:00]. About 50% of emails requiring responses need additional context that an LLM lacks [07:12:00].

The key insight was that the primary cognitive load of email is the stress of managing the inbox, not necessarily responding to emails [07:33:00]. Responding to emails can actually be a pleasurable part of progressing work [07:42:00]. The true burden was the "managing and cleaning" of the inbox [07:50:00]. This realization led Kora to shift its focus from drafting emails to automating inbox management through daily briefs [08:02:00].

## AI's Impact on Software Development

The advent of AI has dramatically reduced the cost and time required to build software [08:27:00]. This shift makes the "what to build" question far more crucial than the "how to build" [08:32:00]. A rough version of almost any software can be built in a few days [08:36:00].

### Software as Content, Writing as Coding
With AI, software is becoming more akin to content, as it's easier to write and can go viral [13:50:00]. Conversely, writing is becoming more like coding, as written instructions can directly build functional products [14:07:00]. This merging highlights a move from software engineering as purely "problem-solving" to creating experiences that evoke feelings [15:00:00]. In a world where AI can solve many problems, the software that makes users "feel great" is likely to succeed [15:24:00].

This new paradigm emphasizes:
*   **Good taste and style**: Products with a strong perspective stand out [15:42:00].
*   **Experience**: The designer's vision and intuition become paramount [15:47:00].
*   **Strong perspectives/methodologies**: AI allows developers to enforce specific methodologies, like Kora dictating email review times, which was previously a manual discipline [17:26:00].

## Kieran's AI-Powered Development Process

Kieran's process for rapidly building with AI involves:
1.  **Problem Definition**: Deeply understanding the problem to be solved [09:39:00].
2.  **Idea Generation (Walking & Talking)**: Taking a walk to enter a flow state and building a detailed prompt mentally [19:52:00]. He visualizes the app and talks through its elements, including details like background colors, textures, and button styles, using descriptive words like "fancy" or "Apple design" [20:05:00].
3.  **Transcribing the Prompt**: Recording the spoken prompt (e.g., using voice memos or Mech Whisper) and converting it to text [10:07:00].
4.  **LLM Interaction**: Taking the transcribed text to a chosen LLM (currently O1 Pro for its deep thinking capabilities) to develop a Product Requirements Document (PRD) [23:52:00]. This involves grounding the model by specifying its role (e.g., "you are a very good iOS engineer") [20:26:00].
5.  **Coding and Iteration**: Using coding assistants like Cursor Composer or Wind Surf [26:25:00]. These tools can set up environments, install dependencies, and automatically fix errors, saving significant time otherwise spent debugging [31:11:00].

### Prompt Engineering in Practice
The ability to articulate a detailed vision, such as describing an app's functionality, background appearance, and button style, is a crucial aspect of prompt engineering that is "not going away" [22:42:00].

### Managing Context in AI Coding
To prevent AI from forgetting previous decisions or making unwanted changes (e.g., deleting old code), a `.cursor_rules` file can be used in Cursor Composer [38:46:00]. This file allows users to define rules and preferred behaviors for the AI, such as specifying helper functions or coding conventions [39:09:00]. These rules are often added reactively when the AI deviates from expectations [39:34:00]. For specific cases, notepads can be used to inject prompts or PRDs into the composer for one-off tasks [47:05:00].

## Challenges and Future Outlook

### Product-Market Fit
Kora currently has 7,000 people on its waitlist [52:28:00]. The current challenge is onboarding these users and understanding their real concerns, especially since allowing an app access to email can be high-pressure [52:51:00]. Manual onboarding is used to identify and fix problems early [53:14:00]. A significant question is whether Kora's unique approach to email management will resonate with a broader audience beyond its initial users [58:17:00].

### Navigating "Mushy" Problems
Unlike traditional software problems that are binary (it works or it doesn't), problems in product development are often "mushy" and subjective [01:01:29]. Solving these requires:
*   **Perspective**: Having a clear vision for the product [01:01:37].
*   **Iteration**: Continuously trying new things, getting data, and refining ideas [01:01:39].
*   **Prioritization**: Deciding which problems to solve or which successful aspects to enhance [01:02:04]. Focusing on one area of excellence can make users more forgiving of other limitations [01:02:00].
*   **Embracing the Messiness**: Accepting that there isn't a "completion state" for a company or product, and enjoying the continuous journey of improvement [01:04:33].

### The Unending Frontier of AI
The ongoing advancements in AI, such as the potential for Artificial General Intelligence (AGI) in the near future, present an "unending frontier" [01:03:07]. While AI labs focus on solving "provable" step-by-step problems (like coding or math), many real-world problems are "squishy" and cannot be reduced to such verifiable steps [01:03:30]. These "squishy" problems rely on taste, intuition, and pattern matching [01:03:49]. AI can assist with these, but the feedback loop is iterative and observational rather than provable [01:04:02].

> "It's important to just remember that whatever we're learning right now, it's I just it's easier to have a it's easy to have a Doomer mindset that like AGI is just going to take over like everything and we won't have jobs anymore and we won't be able to be creative but the reality is the human reality is it will just open the door to something else" <a class="yt-timestamp" data-t="01:12:12">[01:12:12]</a>

Kora exemplifies this outlook: instead of AI making email obsolete, it redefines the human interaction with it. By summarizing automated or less important messages, Kora allows users to focus their attention solely on emails from other humans who matter [01:12:53]. This makes email a more "human way to email" [01:13:33].