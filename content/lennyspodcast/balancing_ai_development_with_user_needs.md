---
title: Balancing AI development with user needs
videoId: En5cSXgGvZM
---

From: [[lennyspodcast]] <br/> 

The overarching goal with Cursor is to invent a new type of programming, a significantly different way to build software that moves towards a "world after code" <a class="yt-timestamp" data-t="00:00:00"></a>. This vision focuses on users specifying their intent for how they want everything to work, rather than painstakingly writing traditional code <a class="yt-timestamp" data-t="00:00:12"></a>.

## The Vision: Beyond Code
The future of software development, according to Cursor's co-founder and CEO Michael Tru, is one where programming is distilled down to describing intent to the computer in the most concise way possible <a class="yt-timestamp" data-t="00:04:56"></a>. This aims for a method of building software that is "legions higher level and more productive," and in some cases, more accessible <a class="yt-timestamp" data-t="00:05:15"></a>.

Michael Tru contrasts this vision with two common perspectives:
*   **Software building remains the same:** People continue text editing in formal programming languages like TypeScript, Go, C, and Rust <a class="yt-timestamp" data-t="00:05:50"></a>.
*   **Chatbot-style interaction:** Users type requests into a bot, asking it to build or change something, resembling a "chatbot Slackbot style where you're talking to your engineering department" <a class="yt-timestamp" data-t="00:06:07"></a>.

Both these visions are seen as problematic. The chatbot style lacks precision, as humans need more granular control to gesture at what they want to change, rather than simply typing in a text box removed from the actual application <a class="yt-timestamp" data-t="00:06:29"></a>. Conversely, the idea that nothing changes is considered incorrect, as technology will become much better <a class="yt-timestamp" data-t="00:06:51"></a>.

The "after code" world is envisioned as one where the logic of software is represented in a more human-readable form, akin to English or an evolution of programming language towards pseudocode <a class="yt-timestamp" data-t="00:07:01"></a>. This high-level, editable representation would be much terser and easier to navigate than millions of lines of impenetrable code <a class="yt-timestamp" data-t="00:07:18"></a>.

Crucially, this path is expected to go through existing professional engineers, evolving away from traditional code. The [[humanai_collaboration_in_product_development | human must remain in the driver's seat]], maintaining a high degree of control over all aspects of the software and having the ability to make changes very quickly through a fast iteration loop <a class="yt-timestamp" data-t="00:08:11"></a>.

### Evolving Roles: Logic Designers and Taste
In this future, skills like "taste" will become increasingly valuable <a class="yt-timestamp" data-t="00:08:52"></a>. While taste often relates to visual design, UI/UX, and smooth animations <a class="yt-timestamp" data-t="00:09:05"></a>, Michael Tru emphasizes its importance in defining the *logic* of how software works <a class="yt-timestamp" data-t="00:09:19"></a>. Being an engineer will shift to feeling more like being a "logic designer," specifying *what* is desired rather than painstakingly outlining *how* it's done under the hood <a class="yt-timestamp" data-t="00:09:41"></a>.

This implies a move away from the current need for extreme carefulness in software engineering, allowing for a more taste-driven approach once AI can mitigate glaring deficiencies and functionality issues <a class="yt-timestamp" data-t="00:10:24"></a>. While "vibe coding" currently describes generating code without fully understanding details, leading to limitations and unwieldy AI decisions, the goal is to enable continued human control over details even without deep code understanding <a class="yt-timestamp" data-t="00:11:00"></a>.

Taste, in this context, means "having the right idea for what should be built" and then experiencing an "effortless translation" of that vision—how it should work and look—into a functional computer application <a class="yt-timestamp" data-t="00:12:01"></a>. This eliminates the "painstakingly labor intensive" translation layer from a team's picture of a product to a computer-executable format <a class="yt-timestamp" data-t="00:12:21"></a>.

## Cursor's Origin and Product Philosophy
Cursor began as a solution search for a problem, deeply rooted in anticipating how AI would improve over the next decade <a class="yt-timestamp" data-t="00:13:06"></a>. Key inspirations were:
*   **GitHub Copilot:** The first beta version of Copilot was a truly useful AI product, standing out as one of the most useful dev tools ever adopted <a class="yt-timestamp" data-t="00:13:26"></a>.
*   **AI Scaling Papers:** Research from OpenAI and others showed that AI would improve simply by scaling models and data, even without new ideas <a class="yt-timestamp" data-t="00:13:56"></a>. This indicated the feasibility of AI products and future maturation of the technology <a class="yt-timestamp" data-t="00:14:15"></a>.

Initially, the team considered working on a "sleepy" and "uncompetitive" area like mechanical engineering automation <a class="yt-timestamp" data-t="00:15:21"></a>. However, they realized their lack of domain expertise and the difficulty of acquiring data for mechanical engineering models <a class="yt-timestamp" data-t="00:15:47"></a>. Eventually, they pivoted to programming, feeling that existing efforts in the space weren't sufficiently ambitious regarding how AI would transform software creation <a class="yt-timestamp" data-t="00:16:53"></a>.

### The IDE Path and Custom Models
Cursor's choice to build a new IDE (Integrated Development Environment) rather than a plugin or a standalone model was driven by a belief that the act of programming and its form factor would change significantly with AI <a class="yt-timestamp" data-t="00:20:49"></a>. Existing coding environments offer limited extensibility for such profound UI changes <a class="yt-timestamp" data-t="00:20:55"></a>, necessitating control over the entire application <a class="yt-timestamp" data-t="00:21:01"></a>.

A counterintuitive lesson in [[challenges_in_building_ai_products | building AI products]] for Cursor was the unexpected necessity of doing their *own* model development <a class="yt-timestamp" data-t="00:20:20"></a>. While they initially thought off-the-shelf models would suffice, "every magic moment in Kurser involves a custom model in some way" <a class="yt-timestamp" data-t="00:24:24"></a>. This approach focuses on complementing the weaknesses of large foundation models rather than reinventing the wheel <a class="yt-timestamp" data-t="00:34:02"></a>.

Cursor's technology stack combines:
*   **Large Generative Models:** Utilizing prominent models like Sonnet, Gemini, or GPT <a class="yt-timestamp" data-t="00:36:35"></a>.
*   **Custom Models:** Developed in-house for specific tasks where foundation models are too slow, costly, or lack specialization <a class="yt-timestamp" data-t="00:34:31"></a>. An example is their "souped-up autocomplete experience," which predicts the next 5-30 minutes of coding work across multiple files <a class="yt-timestamp" data-t="00:35:32"></a>. These models need to be incredibly fast (300ms completion) and cost-effective, specializing in predicting diffs (changes) within a codebase rather than generic text sequences <a class="yt-timestamp" data-t="00:35:45"></a>.
*   **Orchestration Models:** Custom models also assist the large foundation models by searching a codebase for relevant parts to show them (like a "mini Google search") and then filling in details from the large models' high-level change sketches into full code diffs <a class="yt-timestamp" data-t="00:36:46"></a>. This "ensemble of models" approach leverages the best features of each and gains cost advantages <a class="yt-timestamp" data-t="00:37:44"></a>.

## User Engagement and Growth
Cursor's rapid growth from $0 to $100 million ARR in 20 months, and then to $300 million ARR in 2 years, has been driven by a consistent exponential growth curve <a class="yt-timestamp" data-t="00:01:13"></a>. The success is attributed to a "sustained paranoia" about constant improvement, always feeling far from the end goal of a new form of programming <a class="yt-timestamp" data-t="00:27:16"></a>.

### Dogfooding and User Feedback
A core part of Cursor's product development process was "dogfooding," where the team intensely used the tool daily and refused to ship anything that wasn't useful to themselves <a class="yt-timestamp" data-t="00:20:03"></a>. The initial prototype was hand-rolled from scratch in about three months before switching to a VS Code base, driven by immediate user feedback and interest <a class="yt-timestamp" data-t="00:25:06"></a>. This "build in public quickly" approach, combined with adjusting based on early user feedback, was crucial <a class="yt-timestamp" data-t="00:26:15"></a>.

### Tips for New Users (and AI Adoption)
For new Cursor users, Michael Tru offers two main tips to develop a "taste" for what the models can do, their limitations, and how much specification they need:
1.  **Chop things up:** Instead of trying to specify a large task to the model in one go, break it into smaller bits. This allows for more frequent iteration and review of the AI's work <a class="yt-timestamp" data-t="00:24:08"></a>, <a class="yt-timestamp" data-t="00:47:28"></a>. This iterative approach is generally more successful than relying on the AI for an entire big task <a class="yt-timestamp" data-t="00:47:40"></a>.
2.  **Experiment in a safe environment:** Developers are encouraged to "explicitly try to fall on their face" and discover the limits of AI models in a safe context, such as a side project, rather than professional work <a class="yt-timestamp" data-t="00:48:05"></a>. Many users underestimate AI's capabilities, and this exploration helps build a gut feeling for what the model can achieve <a class="yt-timestamp" data-t="00:48:25"></a>. This "gut feeling" may need to be rebuilt with each new model launch <a class="yt-timestamp" data-t="00:48:56"></a>.

### Impact on Engineers: Junior vs. Senior
AI tools like Cursor benefit both junior and senior engineers, though in different ways:
*   **Junior Engineers:** Tend to "go a little too wholesale relying on AI for everything," which is not yet feasible for professional, collaborative work on large codebases <a class="yt-timestamp" data-t="00:49:55"></a>.
*   **Senior Engineers:** On average, senior engineers tend to "underrate what AI can do for them and stick to their existing workflows" <a class="yt-timestamp" data-t="00:50:48"></a>. However, some very senior individuals, particularly those on developer experience teams, are on the "front lines of really trying to adopt the technology as much as possible" <a class="yt-timestamp" data-t="00:50:35"></a>.

Ultimately, both cohorts receive "big benefits" from these tools, but they fall into different "anti-patterns" (expecting too much vs. expecting too little) <a class="yt-timestamp" data-t="00:50:56"></a>.

## [[the_future_of_ai_in_software_development | The Future of AI in Software Development]]
Despite the rapid advancements, Michael Tru believes that the current technological shift will be "incredibly consequential," more so than the internet or any shift since the advent of computers <a class="yt-timestamp" data-t="01:03:06"></a>. However, it will also be a "multi-decade thing," taking time to fully unfold <a class="yt-timestamp" data-t="01:03:18"></a>. There are still many independent problems to solve, both on the scientific side (making models faster, cheaper, smarter) and on the human experience side (how users interact with and control AI) <a class="yt-timestamp" data-t="01:03:30"></a>.

The demand for software is very lasting, and AI's ability to lower the "cost and demand" for building even simple applications, which currently can be as expensive as a "blockbuster movie," will lead to a massive increase in the amount of software built <a class="yt-timestamp" data-t="01:07:26"></a>. Therefore, there will likely be *more* demand for engineers in the long term, as they will be able to do "much more" <a class="yt-timestamp" data-t="01:08:49"></a>.

Companies that succeed will be those that "automating and augmenting a particular area of knowledge work," building both the underlying technology (integrating best parts from providers, sometimes in-house) and the product experience <a class="yt-timestamp" data-t="01:04:15"></a>. The most successful of these will build "very very big businesses" <a class="yt-timestamp" data-t="01:04:48"></a>.