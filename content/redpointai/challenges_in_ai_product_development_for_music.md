---
title: Challenges in AI product development for music
videoId: 11RVpiQzviQ
---

From: [[redpointai]] <br/> 

The development and scaling of AI products, particularly in the music industry, present a unique set of [[challenges_in_ai_product_development | challenges]]. Mikey Shulman, CEO of Suno, highlights several key areas where product development and underlying infrastructure face hurdles as they scale to a massive user base <a class="yt-timestamp" data-t="00:36:00">[00:36:00]</a>.

## The "Blank Canvas" Problem

A significant hurdle for many AI products, including Suno, is the "blank canvas" problem, where users are presented with an empty input field and don't know where to begin <a class="yt-timestamp" data-t="08:14:00">[08:14:00]</a>. While Suno offers suggestions, the ideal solution involves more intuitive prompts that don't require users to "expressly describ[e] the thing you want to make a song about" <a class="yt-timestamp" data-t="11:31:00">[11:31:00]</a>. Future improvements could include:
*   Guiding users through a creative process, as seen in a Valentine's Day experience where the reason for making a song was obvious <a class="yt-timestamp" data-t="09:03:00">[09:03:00]</a>.
*   Allowing non-text-based inputs, such as describing a mood <a class="yt-timestamp" data-t="11:41:00">[11:41:00]</a>, using visuals, humming melodies <a class="yt-timestamp" data-t="10:01:00">[10:01:00]</a>, tapping beats, or incorporating everyday sounds <a class="yt-timestamp" data-t="11:47:00">[11:47:00]</a>.
*   Moving beyond text-driven interfaces, which are seen as a sign of how early the field still is <a class="yt-timestamp" data-t="10:35:00">[10:35:00]</a>.

Shulman notes that while large language models (LLMs) help with writer's block in text, a musical equivalent for overcoming creative stagnation isn't fully developed <a class="yt-timestamp" data-t="09:53:00">[09:53:00]</a>. The goal is to make music creation feel more like a natural form of communication and storytelling <a class="yt-timestamp" data-t="09:30:00">[09:30:00]</a>.

## Subjective Model Evaluation

Evaluating AI music models is inherently more complex than text models due to the subjective nature of music. Unlike text, where benchmarks often relate to reasoning and factual correctness, music "does not have a correct answer" <a class="yt-timestamp" data-t="21:06:00">[21:06:00]</a>.
*   **Aesthetics matter:** While automatic metrics for audio quality exist, they are often flawed. The ultimate test of quality is how much users love the music produced, which depends on song quality (moving, touching) and user control over the output <a class="yt-timestamp" data-t="21:11:00">[21:11:00]</a>.
*   **Human evaluation:** A significant amount of human evaluation is required because subjective judgments are crucial <a class="yt-timestamp" data-t="20:41:00">[20:41:00]</a>.
*   **User feedback:** Direct and implicit user feedback, such as usage patterns, model choices, and community input (e.g., Discord), are vital for identifying issues and guiding improvements <a class="yt-timestamp" data-t="22:20:00">[22:20:00]</a>.

Fixing model issues is often case-dependent and requires deep understanding of the data, as there are no straightforward universal rules <a class="yt-timestamp" data-t="23:05:00">[23:05:00]</a>.

## Iterative Control and Precision

Users often know exactly how a generated song is wrong, but there isn't a direct way to express iterative changes like "do that but change X" <a class="yt-timestamp" data-t="23:55:00">[23:55:00]</a>. The models currently offer loose guidelines rather than precise control over specific elements like BPM (beats per minute), which has an objective answer <a class="yt-timestamp" data-t="24:14:00">[24:14:10]</a>.

The goal is to allow users to "pour their heart out" into the creation process, whether by singing, using image montages, or "mood boarding" sounds, rather than relying on a "sterile" text box <a class="yt-timestamp" data-t="13:06:00">[13:06:00]</a>.

## Business Model and Pricing Strategy

The current business models for AI products often adapt traditional SaaS pricing, which may not be suitable for generative AI where marginal costs per generation are significant <a class="yt-timestamp" data-t="18:50:00">[18:50:00]</a>.
*   **Early stage:** The industry is still very early, and the ways people will enjoy AI music are expected to evolve, so Suno is "actively not trying to innovate on the business model" yet <a class="yt-timestamp" data-t="18:34:00">[18:34:00]</a>.
*   **Product- and use-case dependent:** The optimal pricing model will likely vary significantly across different AI domains (music, text, video) and specific use cases <a class="yt-timestamp" data-t="19:37:00">[19:37:00]</a>.

## Infrastructure Scaling

Rapid user growth, like Suno's 10 million users <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>, puts immense pressure on infrastructure.
*   **Tool chain evolution:** The tool chain for deploying AI models is still evolving <a class="yt-timestamp" data-t="27:32:00">[27:32:00]</a>.
*   **Build vs. buy:** Companies need to be deliberate about where to innovate (build) and where to leverage existing solutions (buy). Suno benefits from services like Modal for easy GPU job deployment <a class="yt-timestamp" data-t="27:37:00">[27:37:00]</a>.
*   **Leveraging other domains:** The audio and music AI space often benefits from problems already solved by the more advanced image and text communities, such as continuous batching infrastructure <a class="yt-timestamp" data-t="28:15:00">[28:15:00]</a>.
*   **Speed is critical:** Delivering a magical experience quickly is paramount. Users expect instant results (like Spotify) and will click away if generation takes too long <a class="yt-timestamp" data-t="25:46:00">[25:46:00]</a>. Suno uses auto-regressive Transformers to stream songs while they are still being made <a class="yt-timestamp" data-t="26:34:00">[26:34:00]</a>.

## Intellectual Property and Partnerships

The AI music industry is very early in defining [[ai_transformation_in_the_music_industry | IP partnerships]] and dealing with copyright.
*   **Spotify vs. Napster analogy:** Shulman draws an analogy to Spotify and Napster, suggesting there will be companies that work with the industry and those that work against it <a class="yt-timestamp" data-t="41:48:00">[41:48:00]</a>. Suno is "very excited to work with the industry" <a class="yt-timestamp" data-t="42:05:00">[42:05:00]</a>.
*   **Artist impersonation:** Suno avoids creating new songs "by" specific artists without their express consent, viewing it as a "flash in the pan" viral moment rather than a sustainable future for music creation <a class="yt-timestamp" data-t="42:20:00">[42:20:00]</a>. The focus is on empowering users to create content relevant to their own lives and experiences <a class="yt-timestamp" data-t="43:27:00">[43:27:00]</a>.