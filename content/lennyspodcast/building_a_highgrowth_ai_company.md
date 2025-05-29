---
title: Building a highgrowth AI company
videoId: En5cSXgGvZM
---

From: [[lennyspodcast]] <br/> 

Cursor, developed by Any Sphere, is an AI code editor that aims to change how engineers and product teams build software <a class="yt-timestamp" data-t="01:04:47">[01:04:47]</a>. It is recognized as one of the fastest-growing products ever, reaching $100 million ARR just 20 months after launch and $300 million ARR within two years <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>. Michael Tru, co-founder and CEO of Any Sphere, shares insights into building Cursor and the future of software development <a class="yt-timestamp" data-t="00:56:00">[00:56:00]</a>.

## Vision: The Future of Programming "After Code"

Cursor's goal is to invent a new type of programming, a world "after code" <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. This vision involves a significantly different way to [[ai_and_software_development | build software]] that focuses on describing intent to the computer in the most concise way possible <a class="yt-timestamp" data-t="00:46:00">[00:46:00]</a>.

### Beyond Traditional Coding
Michael Tru predicts that being an engineer will increasingly feel like being a "logic designer" <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. The focus will shift from the "how" (writing in formal programming languages like TypeScript or Go) to the "what" (specifying intent for how everything should work) <a class="yt-timestamp" data-t="00:51:00">[00:51:00]</a>. The representation of software logic will evolve to resemble English, appearing more like pseudo-code that is terse and easy to navigate <a class="yt-timestamp" data-t="07:01:00">[07:01:00]</a>.

### Beyond Chatbot Interaction
Cursor's vision differs from simply typing commands into a bot. While chatbot-style interaction lacks the precision needed for complete human control over software <a class="yt-timestamp" data-t="06:27:00">[06:27:00]</a>, the future requires humans to remain in the driver's seat, maintaining control over all aspects of the software with the ability to make changes quickly <a class="yt-timestamp" data-t="08:11:00">[08:11:00]</a>.

### The Role of "Taste"
In this future, "taste" will be increasingly valuable <a class="yt-timestamp" data-t="08:52:00">[08:52:00]</a>. This refers to having the right idea for what should be built, rather than just visual design <a class="yt-timestamp" data-t="09:05:00">[09:05:00]</a>. The process will become an effortless translation of intent (what you want built, how it should work, how it should look) onto a computer <a class="yt-timestamp" data-t="12:07:00">[12:07:00]</a>. As AI gets better, engineers will need to be less careful and more focused on this higher-level taste <a class="yt-timestamp" data-t="10:27:00">[10:27:00]</a>.

> [!info] Vibe Coding
> "Vibe coding," where developers generate code without fully understanding the details, currently leads to problems like limited scalability and lack of control <a class="yt-timestamp" data-t="11:00:00">[11:00:00]</a>. However, future solutions aim to give users continued control over details even when they don't fully understand the underlying code <a class="yt-timestamp" data-t="11:20:00">[11:20:00]</a>.

## The Origin Story of Cursor

Cursor began as a solution in search of a problem, stemming from reflections on how AI would improve over the next decade <a class="yt-timestamp" data-t="13:06:00">[13:06:00]</a>.

### Initial Excitement
Two key moments sparked the idea:
1.  **Using GitHub Copilot:** The first beta version of GitHub Copilot was a truly useful AI product and one of the most useful dev tools adopted by the founders <a class="yt-timestamp" data-t="13:23:00">[13:23:00]</a>.
2.  **OpenAI's Scaling Papers:** These papers showed that AI would improve simply by scaling models and data, even without new ideas <a class="yt-timestamp" data-t="13:56:00">[13:56:00]</a>.

By late 2021/early 2022, it became clear that [[role_of_ai_in_startups_and_entrepreneurship | AI products]] were possible and the technology would mature <a class="yt-timestamp" data-t="14:13:00">[14:13:00]</a>. Many were focused on making models, but few were deeply considering how knowledge work would change as AI improved <a class="yt-timestamp" data-t="14:24:00">[14:24:00]</a>.

### The Mechanical Engineering Detour
Initially, the team made a "misstep" by deciding to work on automating mechanical engineering, believing it would be an uncompetitive and sleepy area <a class="yt-timestamp" data-t="15:10:00">[15:10:00]</a>. This endeavor lasted about four months <a class="yt-timestamp" data-t="15:33:00">[15:33:00]</a>. Challenges included the founders' lack of familiarity with mechanical engineering, and the need to develop custom models due to a scarcity of relevant 3D model data <a class="yt-timestamp" data-t="15:47:00">[15:47:00]</a>. They eventually realized they weren't passionate about the field <a class="yt-timestamp" data-t="16:34:00">[16:34:00]</a>.

### The Pivot to AI Code Editor
Observing that the programming space hadn't changed much despite time passing, and sensing a lack of ambition from existing players, the team pivoted <a class="yt-timestamp" data-t="16:40:00">[16:40:00]</a>. They felt that existing solutions weren't sufficiently ambitious about how AI would transform software creation <a class="yt-timestamp" data-t="16:53:00">[16:53:00]</a>. This insight led them to [[ai_and_software_development | build Cursor]] <a class="yt-timestamp" data-t="17:00:00">[17:00:00]</a>.

> [!tip] Opportunity in Ambition Gaps
> Even if a market seems saturated (e.g., AI coding apps), there's still a big opportunity if existing players lack ambition or have flaws in their approach <a class="yt-timestamp" data-t="17:24:00">[17:24:00]</a>. The ceiling for what AI can achieve is exceptionally high, allowing for significant leaps <a class="yt-timestamp" data-t="17:51:00">[17:51:00]</a>.

### Why an IDE, Not a Plugin or Pure Model?
The decision to build a full Integrated Development Environment (IDE) stemmed from core beliefs:
*   **Human Control:** Unlike those focusing on full automation, Cursor prioritized giving humans control over all decisions in the end product <a class="yt-timestamp" data-t="19:08:00">[19:08:00]</a>.
*   **Realism about AI Capabilities:** While excited about AI's long-term maturity, the team maintained a "realism" that AI cannot yet do everything and humans need to remain in the driver's seat <a class="yt-timestamp" data-t="19:33:00">[19:33:00]</a>.
*   **Evolving Programming:** The act of programming is expected to change significantly, requiring control over the entire application, which existing plugin-based environments lack due to limited extensibility <a class="yt-timestamp" data-t="20:46:00">[20:46:00]</a>.

## Key Elements of Cursor's High Growth

Cursor's rapid growth from $0 to $100 million ARR in a year and a half <a class="yt-timestamp" data-t="26:51:00">[26:51:00]</a> was driven by several factors. The growth has been a consistent exponential <a class="yt-timestamp" data-t="28:10:00">[28:10:00]</a>.

### Product-Led Growth & Dogfooding
A core strategy was "dogfooding" – intensely using the tool internally every day <a class="yt-timestamp" data-t="20:03:00">[20:03:00]</a>. The team never wanted to ship anything that wasn't useful to themselves <a class="yt-timestamp" data-t="20:09:00">[20:09:00]</a>. Cursor's first prototype was hand-rolled from scratch in about three months, and they started using it full-time after five weeks, throwing away their previous editor <a class="yt-timestamp" data-t="25:40:00">[25:40:00]</a>. This internal usage instilled realism about the technology <a class="yt-timestamp" data-t="20:17:00">[20:17:00]</a>.

> [!info] Initial Release
> The initial release of Cursor was rushed, within a couple of months from the first line of code, aiming to build in public and gather feedback <a class="yt-timestamp" data-t="26:05:00">[26:05:00]</a>. This early user feedback led to key changes, like switching to a VS Code base instead of a custom build <a class="yt-timestamp" data-t="26:31:00">[26:31:00]</a>.

### Sustained Iteration & Paranoia
The initial three-month version "wasn't very good" <a class="yt-timestamp" data-t="27:11:00">[27:11:00]</a>. Success came from a "sustained paranoia" about how the product could get better <a class="yt-timestamp" data-t="27:16:00">[27:16:00]</a>. The team focused on the "continued evolution of the tool and just making the tool consistently better," rather than just the initial push <a class="yt-timestamp" data-t="27:43:00">[27:43:00]</a>. They intentionally "let fires burn" on traditional sales and marketing to prioritize product development <a class="yt-timestamp" data-t="29:10:00">[29:10:00]</a>.

### Model Development: A Counterintuitive Necessity
Initially, Cursor did not expect to do its own model development, believing existing large models were sufficient <a class="yt-timestamp" data-t="32:15:00">[32:15:00]</a>. However, every "magic moment" in Cursor now involves a custom model <a class="yt-timestamp" data-t="33:22:00">[33:22:00]</a>. This custom model work is a major focus for hiring and has significantly improved product quality <a class="yt-timestamp" data-t="33:14:00">[33:14:00]</a>.

Custom models are used for:
*   **Autocomplete:** For tasks like predicting the next 5-30 minutes of coding work across multiple files, custom models provide the necessary speed (within 300 milliseconds) and cost efficiency that foundation models cannot <a class="yt-timestamp" data-t="35:32:00">[35:32:00]</a>. These models are specifically trained for "autocompleting a series of diffs" <a class="yt-timestamp" data-t="36:08:00">[36:08:00]</a>.
*   **Assisting Foundation Models:** Smaller, specialized models sit on both the input and output sides of larger models like Sonnet, Gemini, or GPT <a class="yt-timestamp" data-t="36:35:00">[36:36:00]</a>. On the input side, they act like a "mini Google search" to find relevant codebase parts to show big models <a class="yt-timestamp" data-t="36:46:00">[36:46:00]</a>. On the output side, they take high-level "sketches" from large models and fill in the details, turning them into full code diffs <a class="yt-timestamp" data-t="37:03:00">[37:03:00]</a>.

> [!info] Ensemble of Models
> This approach of using a combination of different models, including custom and open-source models (like Llama) alongside commercial ones, is called an "ensemble of models" <a class="yt-timestamp" data-t="37:44:00">[37:44:00]</a>. It optimizes for cost and leverages each model's strengths <a class="yt-timestamp" data-t="37:48:00">[37:48:00]</a>.

### Market Dynamics & Defensibility
Michael believes [[building_brands_in_the_ai_industry | AI markets]] are not friendly to incumbents <a class="yt-timestamp" data-t="45:06:00">[45:06:00]</a>. The "ceiling is so high" that companies must constantly strive to build the best product to avoid being leapfrogged <a class="yt-timestamp" data-t="39:25:00">[39:25:00]</a>. This resembles markets like search engines in the late 90s or the development of personal computers, where continuous innovation and product quality are paramount <a class="yt-timestamp" data-t="39:46:00">[39:46:00]</a>. This is more akin to a "consumer sort of moat," focusing on being the best and consistently providing value <a class="yt-timestamp" data-t="40:56:00">[40:56:00]</a>.

Despite the current market being fragmented, Michael foresees one company building the "general tool that builds almost all the world's software," becoming a "generationally big business" <a class="yt-timestamp" data-t="43:42:00">[43:42:00]</a>.

## Building the Team

### Hiring Philosophy
Cursor initially "hired too slow" <a class="yt-timestamp" data-t="53:23:00">[53:23:00]</a>, prioritizing patience in building a world-class group of engineers and researchers <a class="yt-timestamp" data-t="52:16:00">[52:16:00]</a>. Key traits sought in candidates include:
*   **Intellectual Curiosity & Experimentation:** Necessary for building new things <a class="yt-timestamp" data-t="52:42:00">[52:42:00]</a>.
*   **Intellectual Honesty & Micro Pessimism/Bluntness:** Important for maintaining a level head amidst industry noise and growth <a class="yt-timestamp" data-t="52:46:00">[52:46:00]</a>.
*   **Focus on Building Quality:** Prioritizing internal validation and high-quality work over external validation <a class="yt-timestamp" data-t="00:59:55">[00:59:55]</a>.

They learned to broaden their search beyond traditionally "high credential" young profiles, finding excellent later-career individuals <a class="yt-timestamp" data-t="54:27:00">[54:27:00]</a>.

### The Two-Day Work Test
A unique aspect of Cursor's [[hiring_and_developing_a_growth_team | hiring]] process is a two-day onsite work test <a class="yt-timestamp" data-t="55:56:00">[55:56:00]</a>. Candidates work on a "canal list" of real mini-projects within Cursor's codebase <a class="yt-timestamp" data-t="56:12:00">[56:12:00]</a>. This helps assess a candidate's real work product, their compatibility with the team, and even gets them excited about the opportunity, especially in early company stages <a class="yt-timestamp" data-t="56:03:00">[56:03:00]</a>.

### Staying Focused in a Noisy Space
To stay focused amidst the constant launches and chatter in AI, Cursor relies on:
*   **Hiring the Right Disposition:** Recruiting level-headed people less focused on external validation and more on building something great <a class="yt-timestamp" data-t="00:59:55">[00:59:55]</a>.
*   **Open Communication:** Talking frequently about focus areas as a company <a class="yt-timestamp" data-t="00:59:51">[00:59:51]</a>.
*   **Leading by Example:** Founders personally demonstrate focus <a class="yt-timestamp" data-t="01:00:57">[01:00:57]</a>.
*   **Developed "Immune System":** Having witnessed many technological shifts since 2021/2022 (e.g., DALL-E, Stable Diffusion, GPT-4), the team has learned to discern which events truly matter for the business <a class="yt-timestamp" data-t="01:01:06">[01:01:06]</a>. This is mirrored in the evolution of deep learning, where a few simple, elegant ideas have staying power while many do not <a class="yt-timestamp" data-t="01:02:17">[01:02:17]</a>.

## Advice for AI Product Users & Builders

### Developing "Taste" for AI Models
For users, success with Cursor currently requires developing a "taste" for what models can do: their complexity handling, required specificity, gaps, and capabilities <a class="yt-timestamp" data-t="00:46:39">[00:46:39]</a>.

### Chopping Up Tasks
Michael advises users to bias towards chopping up large tasks into smaller bits <a class="yt-timestamp" data-t="00:47:28">[00:47:28]</a>. Instead of trying to specify everything in one large prompt and hoping for a perfect output, break it down: specify a little, get a little work, specify a little more, get more work <a class="yt-timestamp" data-t="00:47:35">[00:47:35]</a>. This iterative approach is more successful than attempting large, single-shot generations <a class="yt-timestamp" data-t="00:47:40">[00:47:40]</a>.

### Discovering Limits
Users, especially developers used to existing workflows, are encouraged to explicitly try to "fall on their face" and discover the limits of AI models <a class="yt-timestamp" data-t="00:48:05">[00:48:05]</a>. Doing this in a safe environment, like a side project, allows for ambitious experimentation without professional risk <a class="yt-timestamp" data-t="00:48:14">[00:48:14]</a>. Many users underestimate AI's capabilities, so pushing boundaries helps build a "gut feeling" for what the model can achieve <a class="yt-timestamp" data-t="00:48:25">[00:48:25]</a>.

## Future Outlook for Engineers

Michael believes that [[career_development_for_ai_individual_contributors | engineers]] will continue to be highly needed <a class="yt-timestamp" data-t="01:07:20">[01:07:20]</a>. While AI will enable engineers to do "much more" and automate busy work, the demand for software is very lasting <a class="yt-timestamp" data-t="01:07:24">[01:07:24]</a>. The current cost and labor intensiveness of building software are disproportionate to its perceived simplicity <a class="yt-timestamp" data-t="01:07:35">[01:07:35]</a>. By significantly reducing these barriers, AI will unlock a vast, unmet demand for new software and tools <a class="yt-timestamp" data-t="01:07:53">[01:07:53]</a>. The "physics of working on computers are so great" that there's still much friction to remove, leading to more, not less, demand for engineers in the long term <a class="yt-timestamp" data-t="01:08:27">[01:08:27]</a>.

> [!tip] AI will make engineers more productive, increasing demand for software.
> Michael states, "I think long into the future, yes, there will actually be more demand for engineers" <a class="yt-timestamp" data-t="01:08:49">[01:08:49]</a>.

The rise of companies that both develop underlying technology (integrating best parts from providers and sometimes in-house) and build the product experience for specific areas of knowledge work will be highly consequential, not just for users but also for pushing technology forward <a class="yt-timestamp" data-t="01:04:08">[01:04:08]</a>. The overall [[impact_of_ai_on_startups_and_business_practices | impact of AI]] is expected to be more consequential than the internet, representing a multi-decade technology shift <a class="yt-timestamp" data-t="01:03:06">[01:03:06]</a>.