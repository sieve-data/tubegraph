---
title: Generational approaches to handling CSV data
videoId: -rsTkYgnNzM
---

From: [[aidotengineer]] <br/> 

The evolution of software development, particularly with the advent of Large Language Models (LLMs), has led to new approaches in building robust and scalable systems. A core idea influencing this shift is that "systems that scale with compute beat systems that don't" <a class="yt-timestamp" data-t="02:30:17">[02:30:17]</a>. This principle suggests that when building systems, it is advantageous to design them in a way that allows for improvement with increased computational resources <a class="yt-timestamp" data-t="02:51:24">[02:51:24]</a>. This concept, often called the "Bit or Lesson," highlights the rarity and power of exponential trends; when one is found, it should be leveraged <a class="yt-timestamp" data-t="03:01:46">[03:01:46]</a>. Historical examples, such as advancements in chess, Go, computer vision, and Atari games, demonstrate that while rigid, hand-coded systems might win with fixed compute, scaling search or general methods ultimately prevail <a class="yt-timestamp" data-t="03:17:15">[03:17:15]</a>.

## Ramp's Financial Platform and AI Integration

Ramp is a finance platform designed to help businesses manage expenses, payments, procurement, travel, and bookkeeping more efficiently <a class="yt-timestamp" data-t="03:59:16">[03:59:16]</a>. The company extensively integrates AI across its product to automate various tasks for finance teams and employees, such as submitting expense reports, booking flights, and handling reimbursements <a class="yt-timestamp" data-t="04:06:58">[04:06:58]</a>. Much of this work involves interacting with other systems, including legacy ones, to streamline workflows <a class="yt-timestamp" data-t="04:20:00">[04:20:00]</a>.

## The CSV Switching Report Problem

One specific challenge at Ramp involves a "switching report" agent, which processes CSV files from various third-party card providers <a class="yt-timestamp" data-t="04:38:07">[04:38:07]</a>. These CSVs can have arbitrary and diverse schemas from the internet <a class="yt-timestamp" data-t="04:42:07">[04:42:07]</a>. The goal is to parse these varied CSV formats into a standardized internal format, enabling Ramp to assist new users in onboarding their existing transaction data <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>.

## Generational Approaches to CSV Data Handling

Ramp's experience with the CSV switching report agent illustrates three distinct architectural approaches:

### 1. Manual/Rigid System (Classical Compute)

The simplest initial approach involved manually writing code for the 50 most common third-party card vendors <a class="yt-timestamp" data-t="05:32:04">[05:32:04]</a>. This method, while functional, required significant manual effort to understand each vendor's schema and write specific parsing logic <a class="yt-timestamp" data-t="05:47:04">[05:47:04]</a>. It also carried the risk of breaking if a vendor changed its format <a class="yt-timestamp" data-t="05:53:13">[05:53:13]</a>. In this model, all computation is classical, rigid, and deterministic <a class="yt-timestamp" data-t="03:40:47">[03:40:47]</a>.

### 2. Constrained Agent (Classical + Fuzzy Compute)

To create a more general system, LLMs were introduced into the deterministic flow <a class="yt-timestamp" data-t="06:09:12">[06:09:12]</a>. This approach involved using an LLM to classify each column in an incoming CSV (e.g., date, transaction amount, merchant name, user's name) and then mapping it to a desired schema <a class="yt-timestamp" data-t="06:29:05">[06:29:05]</a>. In this architecture, most of the compute still occurs in "classical land," with a portion delegated to the "fuzzy LLM land" for tasks like semantic similarity or classification <a class="yt-timestamp" data-t="06:47:03">[06:47:03]</a>. This is represented by a classical system calling into a fuzzy LLM system <a class="yt-timestamp" data-t="08:44:48">[08:44:48]</a>.

### 3. LLM-Driven Agent (Fuzzy + Classical Compute)

The most advanced approach involves giving the LLM direct control over the CSV parsing process <a class="yt-timestamp" data-t="07:01:21">[07:01:21]</a>. The LLM is provided with a code interpreter (e.g., Pandas, Rust-based ones), access to the CSV's head or tail, and a target format with a unit test or verifier <a class="yt-timestamp" data-t="07:03:09">[07:03:09]</a>. While a single execution of this approach might not work, running it 50 times in parallel significantly increases its success rate and generalization across diverse formats <a class="yt-timestamp" data-t="07:31:07">[07:31:07]</a>.

Although this approach might use 10,000 times more compute than the first method, the cost is still minimal (less than a dollar per transaction) <a class="yt-timestamp" data-t="07:58:30">[07:58:30]</a>. The primary scarce resource is engineer time, and a system that works reliably, even with higher compute, is more valuable than one requiring constant manual intervention <a class="yt-timestamp" data-t="07:50:06">[07:50:06]</a>. This architecture flips the control, with the LLM deciding when to break into classical compute (e.g., writing Python code), meaning most of the compute is "fuzzy" <a class="yt-timestamp" data-t="08:54:02">[08:54:02]</a>.

## Generalization to Backend Systems

These three architectural patterns — purely classical, classical calling fuzzy, and fuzzy calling classical — can be generalized to almost all backend request-response systems <a class="yt-timestamp" data-t="09:17:35">[09:17:35]</a>. Historically, most systems built by humanity resemble the purely classical model <a class="yt-timestamp" data-t="09:37:37">[09:37:37]</a>. With the rise of services like OpenAI, many systems now fall into the second category, where traditional programming languages call into LLM servers for fuzzy compute <a class="yt-timestamp" data-t="09:42:37">[09:42:37]</a>.

However, Ramp is increasingly moving towards the third approach (LLM-driven) because it leverages the continuous improvements made by large labs to LLMs <a class="yt-timestamp" data-t="09:58:08">[09:58:08]</a>. By relying more on LLMs, a company's codebase can directly benefit from these advancements without much internal effort, demonstrating the power of "hitching a ride" on exponential trends <a class="yt-timestamp" data-t="10:07:44">[10:07:44]</a>.

## The Future of Software: LLM as the Backend

A more radical future vision proposes the LLM itself as the backend of a web application <a class="yt-timestamp" data-t="11:37:57">[11:37:57]</a>.

### Traditional Web App Model
In a traditional web application (e.g., Gmail), a static file server sends JavaScript, HTML, and CSS to the browser <a class="yt-timestamp" data-t="10:49:10">[10:49:10]</a>. The browser renders the UI, and user interactions trigger requests from the frontend to the backend <a class="yt-timestamp" data-t="11:06:29">[11:06:29]</a>. The backend then queries a database and returns results <a class="yt-timestamp" data-t="11:10:06">[11:10:06]</a>. While code generation tools might assist engineers in writing the code, the deployed software is purely classical compute <a class="yt-timestamp" data-t="11:20:20">[11:20:20]</a>.

### LLM as Backend Model
The proposed alternative model positions the LLM as the backend, responsible for execution <a class="yt-timestamp" data-t="11:40:02">[11:40:02]</a>. This LLM has access to tools like a code interpreter and can make network requests and interact with a database <a class="yt-timestamp" data-t="11:46:42">[11:46:42]</a>.

A demonstration of this concept involved a mail client:
*   When a user logs in, their Gmail token is sent to an LLM, initiating a chat session <a class="yt-timestamp" data-t="14:03:00">[14:03:00]</a>.
*   The LLM, instructed to simulate a Gmail client with access to the user's token and a code interpreter, renders the UI (in markdown format) <a class="yt-timestamp" data-t="14:11:07">[14:11:07]</a>.
*   When the user clicks on an email, the LLM receives this information and renders the appropriate page, potentially by making a `GET` request for the email's body <a class="yt-timestamp" data-t="14:45:00">[14:45:00]</a>.
*   The LLM also determines and renders additional features, such as options to mark an email as unread or delete it <a class="yt-timestamp" data-t="15:17:10">[15:17:10]</a>.

While such software currently works slowly and "barely works" <a class="yt-timestamp" data-t="15:34:00">[15:34:00]</a>, the speaker suggests that with exponential trends in LLM development, this type of software could significantly improve in the future <a class="yt-timestamp" data-t="15:56:06">[15:56:06]</a>. This approach encourages developers to consider how more software might eventually resemble these LLM-centric architectures <a class="yt-timestamp" data-t="16:07:07">[16:07:07]</a>.