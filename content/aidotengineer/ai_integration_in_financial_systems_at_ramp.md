---
title: AI integration in financial systems at Ramp
videoId: -rsTkYgnNzM
---

From: [[aidotengineer]] <br/> 

The speaker, head of AI at Ramp, has been working with LLMs for four years, starting before the widespread adoption of models like ChatGPT <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. Early efforts involved building what are now called [[knowledge_agents_in_finance_workflows|AI agents]] for customer support, aiming to make chatbots smarter <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. Initial experiences with models like GPT-2 were "frustratingly stupid" due to small context windows and poor reasoning capabilities, requiring extensive custom code to achieve even "somewhat reliably" working systems <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. Over time, as models improved, much of this scaffolding code could be removed, revealing patterns in how to build scalable agents <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. The speaker also developed `Jsonformer`, a structured extraction library for JSON, as early models struggled with structured output <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

## The Bit or Lesson: Scaling with Compute

A core philosophy for [[ai_implementation_and_best_practices|AI implementation]] is that "systems that scale with compute beat systems that don't" <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. This idea is rooted in the rarity of exponential trends; when one is found, it should be leveraged <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. Historically, in fields like chess, Go, computer vision, and Atari games, efforts to build rigid, deterministic systems with extensive, clever human-written code were eventually surpassed by general methods that scaled with increased computational search <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

## Ramp's [[ai_strategies_in_financial_technology_companies|AI Strategies]]

Ramp is a finance platform that helps businesses manage expenses, payments, procurement, travel, and bookkeeping more efficiently <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>. The company extensively uses [[ai_tools_in_financial_research_and_due_diligence|AI]] across its product to automate "boring stuff" for finance teams and employees, such as submitting expense reports, booking flights, and handling reimbursements <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. This often involves interacting with other legacy systems <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

### Case Study: The "Switching Report" Agent

A practical example of [[ai_integration_and_tool_calling|AI integration]] at Ramp is the "Switching Report" agent, designed to parse transaction data from third-party card providers <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. The challenge is that CSV files from different providers have arbitrary and varying schemas <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. The goal is to ingest these CSVs into a format Ramp understands, facilitating customer onboarding <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

Three approaches to building this system were discussed:

1.  **Classical/Rigid Approach:**
    *   Involves manually writing code for the 50 most common third-party card vendors <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
    *   This approach is effective but requires manual effort to understand each schema and maintenance if formats change <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
    *   Predominantly uses "classical compute" (traditional programming) <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.

2.  **Hybrid Approach (Constrained Agent):**
    *   Introduces LLMs to enhance the system <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
    *   For each column in the CSV, an LLM classifies its type (e.g., date, transaction amount, merchant name) using semantic similarity <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.
    *   The classified columns are then mapped to Ramp's desired schema <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.
    *   Most compute remains classical, with some "fuzzy LLM land" computation <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
    *   Represents a transition where classical code calls into fuzzy LLM operations <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

3.  **LLM-Centric Approach (General Agent):**
    *   The CSV is directly given to an LLM with a "code interpreter" (e.g., Python/Pandas) <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
    *   The LLM is instructed to output a CSV in a specific format and is given a unit test/verifier to check its work <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
    *   Running this approach once typically fails <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.
    *   However, running it 50 times in parallel drastically increases the likelihood of success and generalization across various formats <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
    *   This method uses significantly more compute (10,000 times more than the first approach) but is still cost-effective given the value of engineer time and successful transactions <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.
    *   In this setup, the LLM decides when to execute classical code (e.g., Python scripts) and most of the compute is "fuzzy" <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.

The speaker notes that Ramp is increasingly moving towards the third approach because the "blue arrows" (LLM capabilities) are continuously improved by major labs, providing direct benefits to the company without significant internal effort <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>. This aligns with [[leveraging_existing_infrastructure_for_ai_integration|leveraging existing infrastructure for AI integration]] and the [[integration_of_mcp_with_ai_applications|integration of mCP with AI applications]].

## Future Vision: The LLM as the Backend

The traditional web application model involves a frontend sending requests to a backend, which interacts with a database and returns data, with [[openais_approach_to_integrating_ai_in_enterprises|AI]] typically used during code generation or by engineers <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.

The proposed future model suggests the **backend *is* the LLM** <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>. In this model, the LLM has direct access to tools like code interpreters, can make network requests, and interact with databases <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.

The speaker demonstrated a proof-of-concept email client built on this principle <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>. When logging in, the Gmail token is sent to an LLM, which simulates a Gmail client, accessing emails via the token and a code interpreter <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>. The LLM then renders the UI (e.g., markdown for the homepage) <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>. User interactions, like clicking on an email, are also passed directly to the LLM, which then decides how to render the next page or perform actions (e.g., delete an email) <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>.

While this kind of software is currently slow and "barely works," the speaker believes that given exponential trends in AI, it could take off in the future, prompting a shift in how software and backends are conceived <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>.