---
title: Evolution of AI models and their application
videoId: -rsTkYgnNzM
---

From: [[aidotengineer]] <br/> 

This article explores the [[evolution_and_history_of_ai_technology | evolution and history of AI technology]], particularly focusing on [[ai_models_and_training_methods | AI models and training methods]], challenges in their development, and future directions in application architecture.

## Early Experiences with LLMs
The speaker has been working with Large Language Models (LLMs) for four years, a significant duration given the rapid advancements in the field, especially since the emergence of ChatGPT <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. Initially, the goal was to build what would now be called an [[customization_and_scalability_in_ai_models | AI agent company]], focusing on customer support chatbots <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

Early LLMs, such as GPT-2 and GPT-3, presented significant [[challenges_in_building_ai_applications | challenges in building AI applications]] <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. They were described as "frustratingly stupid," had small context windows, and lacked sophisticated reasoning capabilities <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. This necessitated writing extensive code around these models to achieve even somewhat reliable performance <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. As models became smarter, less of this scaffolding code was needed, revealing patterns for building agents that scale with increasing intelligence <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

An example of early scaffolding was the JSONFormer library, designed for structured extraction when models were unable to reliably output JSON format <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

## The Bit or Lesson: Scaling with Compute
The core idea presented is that "systems that scale with compute beat systems that don't" <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. This means if a system can leverage more computational power to improve its performance without significant additional effort, it will outperform rigid, fixed, or deterministic systems <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. This principle is considered an obvious conclusion from the "Bit or Lesson" <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

Exponential trends, such as those seen in AI model capabilities, are rare, and when encountered, one should capitalize on them <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. Historical examples supporting this include:
*   **Chess and Go**: Early attempts involved writing extensive, clever software to synthesize human reasoning <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. While effective with fixed compute, scaling out computational search (e.g., Monte Carlo Tree Search) ultimately led to general methods winning <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
*   **Computer Vision and Atari Games**: Similar patterns where generalized, compute-intensive approaches surpassed rigid, hand-coded systems <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

## [[case_studies_and_practical_examples_of_ai_implementation | Case Study]]: Ramp's Switching Report Agent
Ramp, a finance platform, utilizes AI extensively to automate tasks like expense management, payments, and bookkeeping <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. A specific [[case_studies_and_practical_examples_of_ai_implementation | case study]] involves the "switching report" agent, designed to parse arbitrary CSV transaction formats from third-party card providers <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. The goal is to onboard users by helping them migrate transactions from other platforms <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

Three approaches to building this agent were explored:

### 1. Manual/Deterministic Approach
This involved manually writing code for the 50 most common third-party card vendors <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
*   **Pros**: Works reliably for known formats.
*   **Cons**: Requires significant manual effort to identify schemas and write specific parsing logic <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. Prone to breaking if vendor formats change <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>. Does not scale to arbitrary formats.

### 2. Hybrid (Classical + LLM) Approach
This approach combined classical scripting with LLMs. Each CSV column would be classified (e.g., date, transaction amount, merchant name) using an LLM or embedding model for semantic similarity, and then mapped to a desired schema <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
*   **Pros**: More general than manual coding <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.
*   **Cons**: Still primarily classical compute with some "fuzzy LLM land" integration <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.

### 3. LLM-Centric (Scaling with Compute) Approach
This radical approach involves giving the entire CSV to an LLM with a code interpreter (e.g., for Python/Pandas) <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. The LLM is instructed to output a CSV in a specific format, with unit tests and a verifier to check its work <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
*   **Initial Findings**: Running it once often doesn't work <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.
*   **Key Insight**: Running it 50 times in parallel significantly increases the likelihood of success and allows it to generalize across a vast range of formats <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
*   **Cost-Benefit**: Although this approach uses 10,000 times more compute than the first approach, it still costs less than a dollar per transaction <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. The true scarcity is engineer time, and a reliable, general system is more valuable than direct compute cost savings <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

## Generalizing [[the_evolution_and_current_state_of_ai_engineering | AI Engineering]] Architectures
The three approaches can be generalized to AI application architectures:

1.  **Classical-only**: Software engineered without AI.
2.  **Classical calls AI**: Traditional programming languages make calls to AI models (e.g., OpenAI APIs) for "fuzzy compute" <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
3.  **AI calls Classical**: The LLM itself decides when to use classical compute tools (e.g., running Python code), with most of the processing being "fuzzy" <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>.

Ramp is increasingly moving towards the third approach because the continuous improvements made by major AI labs to their models (the "blue arrows" or "fuzzy compute") directly benefit applications without additional internal effort <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>. This allows companies to "hitch the ride" on exponential AI trends <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.

## [[future_directions_in_ai_model_training_and_scaling | Future Directions]]: LLM as the Backend
A bold [[future_directions_in_ai_model_training_and_scaling | future direction]] proposes a shift in web application architecture.
*   **Traditional Web App**: Frontend (HTML/CSS/JS) makes requests to a classical backend, which interacts with a database <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>. Code generation tools might assist engineers, but the deployed system is purely classical <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>.
*   **LLM as Backend**: The LLM *is* the backend, performing execution <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>. It has access to tools like code interpreters, can make network requests, and interact with databases <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.

### Experimental LLM-Powered Mail Client
An experimental mail client was developed based on this principle <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>. When a user logs in, their Gmail token is sent to an LLM, which simulates a Gmail client <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>. The LLM has access to the user's emails and a code interpreter, and it renders the UI, for example, in Markdown <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>.

When a user interacts with the UI (e.g., clicking on an email), the LLM receives this information and decides how to render the next page, potentially making further requests to retrieve email content or perform actions like deleting an email <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>.

While currently slow and "barely works" due to the intense computational demands <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>, this concept highlights a potential [[future_directions_in_ai_model_training_and_scaling | future direction]] for software, where exponential improvements in AI capabilities could make such systems viable and efficient <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>.