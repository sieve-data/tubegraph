---
title: Technology behind Notebook LM
videoId: sOyFpSW1Vls
---

From: [[lennyspodcast]] <br/> 

[[notebook_lm_development_and_origins | Notebook LM]] is an AI product that originated as a 20% project within [[Google Labs and product innovation | Google Labs]] <a class="yt-timestamp" data-t="01:06:03">[01:06:03]</a>. It began with a smaller Labs project called "talk to small Corpus," which explored using a Large Language Model (LLM) to interact with specific content <a class="yt-timestamp" data-t="01:06:36">[01:06:36]</a>. Risa Martin, the Product Lead for Notebook LM, observed this "nugget" and focused on making it truly useful <a class="yt-timestamp" data-t="01:06:45">[01:06:45]</a>.

The product's [[ai_product_development_and_challenges | development approach]] within Labs prioritizes starting with the technology and then discovering its practical applications <a class="yt-timestamp" data-t="01:10:07">[01:10:07]</a>.

## Core Technology and Models

Notebook LM is built upon powerful AI models:
*   **Gemini 1.5 Pro** This serves as the foundational LLM for Notebook LM <a class="yt-timestamp" data-t="01:18:18">[01:18:18]</a>.
*   **Powerful Voice Model / Audio Model** An advanced audio model operates on top of Gemini 1.5 Pro, specifically designed to enhance the quality of the generated audio <a class="yt-timestamp" data-t="01:23:24">[01:23:24]</a>. The audio feature was developed by a separate team within Google Labs specializing in powerful audio models <a class="yt-timestamp" data-t="01:09:03">[01:09:03]</a>.

## Content Studio: The Secret Sauce

The "real secret sauce" that makes Notebook LM's outputs, particularly the audio overviews, exceptionally good is an internal system called **Content Studio** <a class="yt-timestamp" data-t="01:29:29">[01:29:29]</a>. This system is designed to take an opinionated approach to the user's content, aiming for maximum helpfulness <a class="yt-timestamp" data-t="01:40:02">[01:40:02]</a>.

Content Studio determines the optimal format for the audio, such as the "Deep Dive" podcast style, which was the first format considered <a class="yt-timestamp" data-t="01:40:02">[01:40:02]</a>. The team, especially an engineer named Usama, focused on crafting Content Studio to make outputs relatable and engaging <a class="yt-timestamp" data-t="01:41:09">[01:41:09]</a>.

The audio model, combined with Content Studio, brings out the best in the generated speech, creating natural inflections, laughter, and interruptions, which required extensive listening and refinement during development <a class="yt-timestamp" data-t="01:51:00">[01:51:00]</a>.

## Audio Overview Feature

The audio overview allows users to upload any source (e.g., a URL, Google Doc, or PDF) and generates an AI-powered audio output <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>. This feature enables transformation of text into an auditory experience <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>. The initial idea behind the audio feature was to address the feedback that while interaction with text was possible, the output remained text <a class="yt-timestamp" data-t="01:40:02">[01:40:02]</a>.

## Future [[ai_product_development_and_challenges | Development]]

The long-term vision for [[applications_and_use_cases_of_notebook_lm | Notebook LM]] is to become an "AI editor surface" that is fully remixable, accepting any input (video, audio, emails, social media) and producing any output (blog posts, tutorial videos, chatbots) <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>. This aims to empower users to reshape information into new forms based on their needs <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>.

More tactically, the team is interested in bringing Notebook LM to mobile <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>. They are also experimenting with user control interfaces beyond simple "knobs" or "sliders" to maintain a magical and delightful experience <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>. Future improvements will focus on deepening the user experience <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>.