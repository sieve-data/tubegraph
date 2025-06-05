---
title: Automating Real Estate Due Diligence with AI
videoId: Bf71xMwd-Y0
---

From: [[aidotengineer]] <br/> 

[[Automation of manual workflows with AI web agents | Automating real estate due diligence]] uses AI to streamline the process of reviewing properties before they are bought or sold <a class="yt-timestamp" data-t="02:01:58">[02:01:58]</a>. This approach aims to accelerate property transactions by tackling the traditionally manual and time-consuming task of legal due diligence <a class="yt-timestamp" data-t="02:02:44">[02:02:44]</a>.

## The Challenge of Traditional Due Diligence
Real estate due diligence often involves lawyers reading "mountains of paperwork" to find "needles in a haystack" for potential red flags before properties can be transacted <a class="yt-timestamp" data-t="02:17:34">[02:17:34]</a>. This process is slow and labor-intensive <a class="yt-timestamp" data-t="03:48:38">[03:48:38]</a>.

## Orbital Co-Pilot: An AI Solution
Orbital, a company with offices in New York and London, developed "Orbital Co-Pilot" to address this challenge <a class="yt-timestamp" data-t="01:56:07">[01:56:07]</a>. Its mission is to [[due_diligence_in_finance_workflows | automate real estate due diligence]] <a class="yt-timestamp" data-t="02:01:58">[02:01:58]</a>. Launched in January 2024, Orbital Co-Pilot is an agentic product designed to think like a real estate lawyer <a class="yt-timestamp" data-t="03:14:02">[03:14:02]</a>.

### How Orbital Co-Pilot Works
The system automates tasks typically performed manually by lawyers, such as reading paperwork and compiling extracted information <a class="yt-timestamp" data-t="03:45:00">[03:45:00]</a>.

A typical workflow involves:
1.  **Report Selection**: Users choose an appropriate report, such as an occupational lease report <a class="yt-timestamp" data-t="04:01:23">[04:01:23]</a>.
2.  **Document Upload**: Users upload legal documents, like deeds and leases, which can total hundreds of pages <a class="yt-timestamp" data-t="04:07:07">[04:07:07]</a>.
3.  **OCR and Structuring**: Documents are first processed using Optical Character Recognition (OCR) to structure handwritten and typed text <a class="yt-timestamp" data-t="04:16:38">[04:16:38]</a>.
4.  **Agentic Processing**: The [[building_agents_with_ai_sdk | agentic system]] creates a plan, breaking it down into multiple subtasks <a class="yt-timestamp" data-t="04:30:05">[04:30:05]</a>. Each subtask is its own agentic system with multiple LLM (Large Language Model) calls <a class="yt-timestamp" data-t="04:37:37">[04:37:37]</a>. The system is given objectives, such as finding the lease date or annual rent, and reads legal documents to find answers <a class="yt-timestamp" data-t="04:41:40">[04:41:40]</a>.
5.  **Report Generation**: Once tasks are completed, a final report is generated, which can be quickly reviewed by a lawyer <a class="yt-timestamp" data-t="04:56:00">[04:56:00]</a>. Citations within the report can be clicked to go back to the original source documents <a class="yt-timestamp" data-t="05:07:08">[05:07:08]</a>.
6.  **Export**: The report can be downloaded as a Word document for storage and client delivery <a class="yt-timestamp" data-t="05:16:04">[05:16:04]</a>.

### Impact and Scale
Orbital's agentic product has significantly scaled its operations:
*   **Token Consumption**: In 18 months, token consumption grew from less than a billion to almost 20 billion tokens per month, representing work previously done manually by lawyers <a class="yt-timestamp" data-t="05:34:00">[05:34:00]</a>.
*   **Revenue Growth**: The company scaled from zero revenue to multiple seven figures in annual recurring revenue within 18 months <a class="yt-timestamp" data-t="06:06:04">[06:06:04]</a>.

## Developing at the AI Frontier: Key Decisions

Orbital's development journey involved navigating the rapidly evolving AI landscape <a class="yt-timestamp" data-t="00:37:05">[00:37:05]</a>. They transitioned from System 1 models (like GPT-3.5 and GPT-4 32K) to System 2 models (like 01 preview and 04 mini) <a class="yt-timestamp" data-t="06:27:06">[06:27:06]</a>.

Key decisions made:
1.  **Optimizing for Prompting over Fine-tuning**: This allowed for maximum speed of development. Feedback from users could lead to prompt adjustments that were pulled in real-time, easily incorporating changes into the product <a class="yt-timestamp" data-t="07:00:23">[07:00:23]</a>.
2.  **Heavy Reliance on Domain Experts**: Private practice real estate lawyers, with decades of experience, were embedded in the team to write many of the prompts <a class="yt-timestamp" data-t="07:34:01">[07:34:01]</a>. They effectively teach the AI system their expertise <a class="yt-timestamp" data-t="07:49:10">[07:49:10]</a>.
3.  **"Vibes Over Evals"**: Instead of a rigorous, objective evaluation system, Orbital initially relied on human beings (often domain experts) testing the system subjectively <a class="yt-timestamp" data-t="07:57:33">[07:57:33]</a>. This approach, combined with user feedback and internal team testing, has contributed to significant growth <a class="yt-timestamp" data-t="08:12:08">[08:12:08]</a>.

Orbital has a large and growing number of domain-specific prompts (over 1,000), which presents the challenge of "prompt tax" <a class="yt-timestamp" data-t="09:18:14">[09:18:14]</a>.

## The Concept of "Prompt Tax"
"Prompt tax" is the hidden cost incurred when integrating new AI model functionalities into applications <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>. It arises from the need to migrate existing prompts to new models and the inherent fear of unknown consequences or regressions <a class="yt-timestamp" data-t="10:04:12">[10:04:12]</a>. Unlike technical debt, prompt tax is driven by a desire to upgrade and unlock new capabilities now <a class="yt-timestamp" data-t="10:59:16">[10:59:16]</a>.

## Battle-Tested Tactics for AI Development

Orbital has developed several tactics to manage the challenges of rapid AI model evolution:

*   **Prompt Adaptation for System 2 Models**:
    *   **Specify *what* to do, not *how***: Unlike System 1 models requiring specific instructions, System 2 models need only a clear objective <a class="yt-timestamp" data-t="12:12:04">[12:12:04]</a>.
    *   **Leaner Prompts**: Repetitive instructions used for System 1 models can be removed <a class="yt-timestamp" data-t="12:26:01">[12:26:01]</a>.
    *   **Unblocking the Model**: Avoid too many constraints; allow System 2 models time to think and reason <a class="yt-timestamp" data-t="12:40:02">[12:40:02]</a>.
*   **Leveraging Thought Tokens**: System 1 models' thought tokens can be used for explainability for users (especially in complex legal matters) or for debugging when issues arise <a class="yt-timestamp" data-t="13:13:03">[13:13:03]</a>.
*   **Progressive Delivery with Feature Flags**: Similar to software development, new AI model upgrades can be rolled out progressively to mitigate risk <a class="yt-timestamp" data-t="13:46:04">[13:46:04]</a>.
*   **"Betting on the Model" Mantra**: The team operates on the principle that AI models will get smarter, cheaper, faster, and more capable in the future. This allows them to build features that will improve as models evolve <a class="yt-timestamp" data-t="14:55:03">[14:55:03]</a>.
*   **AI-Assisted Prompt Migration**: System 2 models can help migrate domain-specific prompts from older models, significantly reducing manual effort <a class="yt-timestamp" data-t="15:44:03">[15:44:03]</a>.
*   **Embracing Uncertainty and Shipping**: Given the probabilistic nature of AI models, teams must be brave enough to ship new models despite unknowns, and then deal with consequences by mitigating risks on the fly <a class="yt-timestamp" data-t="16:11:00">[16:11:00]</a>.
*   **Strong Feedback Loops**: Building systems to receive rapid user feedback (e.g., thumbs up/down) and deliver it immediately to AI engineers and domain experts allows for quick identification and fixing of issues <a class="yt-timestamp" data-t="17:09:08">[17:09:08]</a>. This enables fixes in minutes or hours, rather than days or weeks <a class="yt-timestamp" data-t="17:48:00">[17:48:00]</a>. This contributes to strong [[customer_success_with_ai_solutions | customer success]].

## The Future of AI Engineering

Deis Havaris, CEO of Google DeepMind, notes the unique challenge of the AI space: the underlying tech stack is evolving incredibly fast, making it difficult to bet on product features <a class="yt-timestamp" data-t="18:14:48">[18:14:48]</a>. This requires deeply technical product people who can anticipate where the technology will be in the future <a class="yt-timestamp" data-t="19:05:07">[19:05:07]</a>.

There is a growing opportunity for "product AI engineers" who understand both customer problems and model capabilities to turn them into valuable product features <a class="yt-timestamp" data-t="19:57:33">[19:57:33]</a>. This connective tissue, whether within a single AI engineer or a team, is a promising proposition for the future of the AI engineering community <a class="yt-timestamp" data-t="20:13:01">[20:13:01]</a>.

## Paying the Prompt Tax: Shipping with Confidence
As AI moves faster, and agentic product surface areas grow, having more confidence in shipping new models is crucial for continued innovation <a class="yt-timestamp" data-t="20:44:00">[20:44:00]</a>. While "vibes" have worked for Orbital thus far due to real-time user feedback and quick tooling, there's a question of whether this scales indefinitely <a class="yt-timestamp" data-t="21:06:00">[21:06:00]</a>.

The challenge of an objective evaluation system (eval system) for complex, probabilistic LLMs with many edge cases (correctness, style, conciseness, citations in legal documents) might be prohibitively expensive or slow to implement <a class="yt-timestamp" data-t="21:32:00">[21:32:00]</a>.

Progressive delivery—rolling out new models internally first, then to limited users, and gradually scaling—allows for fixing issues on the fly and calibrating rollout based on feedback volume <a class="yt-timestamp" data-t="22:30:00">[22:30:00]</a>. This strategy aims to maximize the benefits of new models while mitigating risks <a class="yt-timestamp" data-t="11:37:00">[11:37:00]</a>. The emphasis remains on "buy now" to stay on the edge of the AI frontier and maximize opportunity <a class="yt-timestamp" data-t="23:37:39">[23:37:39]</a>.