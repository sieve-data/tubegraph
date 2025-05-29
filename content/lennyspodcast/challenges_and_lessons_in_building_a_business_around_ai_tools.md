---
title: Challenges and lessons in building a business around AI tools
videoId: En5cSXgGvZM
---

From: [[lennyspodcast]] <br/> 

Building a business around AI tools presents unique challenges and opportunities, as exemplified by Cursor, an AI code editor. The company achieved historic growth, reaching $100 million ARR in 20 months and $300 million ARR in 2 years <a class="yt-timestamp" data-t="01:13:15">[01:13:15]</a>. This success stems from a deeply opinionated approach to the future of software development and a relentless focus on product quality <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

> [!abstract] Key Takeaways
> *   **Vision Beyond Code**: The future of software development involves humans specifying intent rather than writing detailed code <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.
> *   **Custom Model Development**: Contrary to initial expectations, developing proprietary AI models for specific use cases (like autocomplete) is crucial for product quality, speed, and cost efficiency <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a>, <a class="yt-timestamp" data-t="00:32:10">[00:32:10]</a>.
> *   **Human in the Driver's Seat**: AI tools should augment, not fully replace, human control and decision-making in complex tasks <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>, <a class="yt-timestamp" data-t="00:20:24">[00:20:24]</a>.
> *   **Product-Led Growth**: Prioritizing continuous product improvement and "dogfooding" (using your own product) is vital for sustained growth, especially in a rapidly evolving market <a class="yt-timestamp" data-t="00:20:03">[00:20:03]</a>, <a class="yt-timestamp" data-t="00:27:07">[00:27:07]</a>.
> *   **Market Defensibility**: Defensibility in AI often resembles a consumer-like "best product wins" moat rather than traditional enterprise lock-in <a class="yt-timestamp" data-t="00:56:56">[00:56:56]</a>.
> *   **Strategic Hiring**: Patience and focus on recruiting world-class talent with the right blend of curiosity and intellectual honesty are paramount <a class="yt-timestamp" data-t="00:52:13">[00:52:13]</a>.

## The Vision: "After Code"

The ultimate goal for Cursor is to invent a new type of programming, moving towards a world "after code" <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. This involves distilling software development into describing intent to the computer in the most concise way possible, defining how software should work and look <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. This future envisions a more productive and accessible method of [[future_of_startups_and_product_development_with_ai | building software]] that is legions higher-level than current practices <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

Michael Tru, co-founder and CEO of Any Sphere (the company behind Cursor), argues against two prevailing visions for the future of software:
1.  **Status Quo**: Software building remains largely the same, relying on text editing formal programming languages like TypeScript, Go, C, and Rust <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
2.  **Chatbot-style Automation**: Developers simply type requests into a bot and ask it to build or change something, akin to a chatbot or Slackbot interaction <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.

Tru believes both visions have flaws <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>. The chatbot style lacks precision, as humans need complete control and more precise ways to gesture at desired changes <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. The status quo view underestimates how much technology will improve <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>. Instead, the future will involve a representation of software logic that looks more like English or an evolution of programming language towards pseudocode, being much terser and easier to navigate than millions of lines of impenetrable code <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

In this "after code" world, the human remains in the driver's seat, maintaining significant control over all software aspects and making changes quickly <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. Key skills will shift:
*   **Taste**: Increasingly valuable, not just for visuals (UI/UX) but for the logic and how the software works <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.
*   **Logic Designer**: Being an engineer will feel more like being a logic designer, specifying intent ("the what") rather than the exact implementation details ("the how") <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.
*   **Less Carefulness**: As AI improves, engineers will need to be less painstakingly careful, shifting focus from meticulous detail to overall taste and vision <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.

## Origin Story of Cursor

Cursor began as a solution in search of a problem, born from reflections on how AI would improve over the next decade <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>. Two defining moments spurred its creation:
1.  **GitHub Copilot Beta**: Using the first beta of GitHub Copilot was a revelation, marking the first truly useful AI product and one of the most impactful dev tools adopted <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a>.
2.  **OpenAI Scaling Papers**: Research from OpenAI and others demonstrated that AI capabilities would continuously improve simply by scaling models and data, even without new fundamental ideas <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>.

In late 2021/early 2022, while many focused on building models, Tru and his co-founders noticed a gap: few were deeply considering how specific areas of knowledge work, especially programming, would change as AI matured <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.

Initially, they made a "misstep" by trying to work on a seemingly "uncompetitive, sleepy, and boring" area: automating mechanical engineering <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>. This pivot away from coding was based on the belief that coding was "interchangeable" due to AI and already well-covered <a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a>. However, challenges quickly arose:
*   **Lack of Domain Expertise**: The founders weren't mechanical engineers <a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>.
*   **Model Suitability**: Existing AI models weren't easily adaptable for mechanical engineering, requiring custom model development and data acquisition challenges (e.g., 3D models) <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>.

Ultimately, they realized they weren't passionate about mechanical engineering <a class="yt-timestamp" data=t="00:16:34">[00:16:34]</a>. Returning to programming, they found that despite the time that had passed, little had truly changed in how others were approaching the space. They perceived a lack of sufficient ambition among existing players in [[developing_ai_products_and_utilizing_technology | developing AI products and utilizing technology]], failing to grasp how "all of software creation was going to blow through these models" <a class="yt-timestamp" data-t="00:16:53">[00:16:53]</a>. This insight led them to build Cursor.

## Building the Product: Key Learnings

### Importance of Custom Models
A major counterintuitive lesson was the necessity of **in-house model development** <a class="yt-timestamp" data-t="00:32:10">[00:32:10]</a>. Initially, Cursor didn't expect to build its own models, assuming existing foundation models (like GPT-4) would suffice <a class="yt-timestamp" data-t="00:32:32">[00:32:32]</a>. However, every "magic moment" in Cursor now involves a custom model <a class="yt-timestamp" data-t="00:33:22">[00:33:22]</a>.

This is because:
*   **Cost and Speed**: Foundation models are often too expensive or slow for certain high-frequency, low-latency tasks. For example, Cursor's autocomplete feature needs to provide suggestions within 300 milliseconds and runs "tons and tons and tons of molecules" (models) with every keystroke <a class="yt-timestamp" data-t="00:35:45">[00:35:45]</a>.
*   **Specialty Use Cases**: General foundation models aren't optimized for highly specific tasks. Cursor's autocomplete is designed not just to complete the next text token but to predict "series of diffs" – changes, additions, and deletions across multiple files in a codebase <a class="yt-timestamp" data-t="00:36:00">[00:36:00]</a>.
*   **Complementing Foundation Models**: Custom models are used on both the input and output sides of large foundation models.
    *   **Input**: Models search codebases to find relevant parts to feed to big models (like a "mini Google search for code") <a class="yt-timestamp" data-t="00:36:47">[00:36:47]</a>.
    *   **Output**: Smaller, faster specialty models "fill in the details" by taking high-level change sketches from smart foundation models and converting them into full code diffs <a class="yt-timestamp" data-t="00:37:03">[00:37:03]</a>.

This [[interplay_of_ai_and_traditional_business_and_technology_approaches | ensemble of models]] approach, using the best features of each model and leveraging cheaper, specialized ones, is a key to quality and speed <a class="yt-timestamp" data-t="00:37:50">[00:37:50]</a>.

### Human in the Driver's Seat
Cursor's product philosophy emphasizes keeping humans in control <a class="yt-timestamp" data-t="00:20:24">[00:20:24]</a>. The AI cannot (yet) do everything, and user dogfooding instilled a realism about current AI capabilities <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>. For users, [[tips_for_using_ai_in_product_development | tips for using AI in product development]] effectively with Cursor include:
*   **Chunking Tasks**: Instead of giving the AI a large task at once and expecting a perfect output, break tasks into smaller pieces. Specify a little, get some work, review, then specify a little more. This approach, similar to "autocompletes," is currently more successful than expecting a giant, single output <a class="yt-timestamp" data-t="00:24:08">[00:24:08]</a>, <a class="yt-timestamp" data-t="00:47:28">[00:47:28]</a>.
*   **Experimentation in Safe Environments**: Encourage users to push the limits of what the models can do, ideally on side projects rather than professional work, to develop an intuitive "taste" for their capabilities and limitations <a class="yt-timestamp" data-t="00:47:53">[00:47:53]</a>.

### Product-Led Growth & Dogfooding
Cursor's success is attributed to "dogfooding" – building and using the product intensely themselves every day <a class="yt-timestamp" data-t="00:20:03">[00:20:03]</a>. They didn't ship anything that wasn't useful to themselves <a class="yt-timestamp" data-t="00:20:09">[00:20:09]</a>. The first version, a hand-rolled editor built from scratch (now based on VS Code) <a class="yt-timestamp" data-t="00:24:54">[00:24:54]</a>, was usable enough for them to switch to it full-time after just five weeks <a class="yt-timestamp" data-t="00:25:52">[00:25:52]</a>.

The company launched to the public within three months of the first line of code, embracing a "build in public quickly" philosophy <a class="yt-timestamp" data-t="00:26:07">[00:26:07]</a>. Initial user feedback was crucial, even leading to fundamental changes like switching to a VS Code base <a class="yt-timestamp" data-t="00:26:38">[00:26:38]</a>. The growth has been a consistent exponential rather than a single inflection point <a class="yt-timestamp" data-t="00:28:12">[00:28:12]</a>. The "secret to success" is a sustained paranoia about how the product can always be better, constantly iterating and evolving the tool <a class="yt-timestamp" data-t="00:27:16">[00:27:16]</a>.

### Iterative Development & User Feedback
The rapid development from scratch, even for basic editor features like language support, navigation, and error tracking, demonstrated a commitment to putting a functional product out quickly <a class="yt-timestamp" data-t="00:25:12">[00:25:12]</a>. The initial "crush of interest" and user feedback were invaluable, driving early product decisions <a class="yt-timestamp" data-t="00:26:25">[00:26:25]</a>. This iterative approach in public has continued <a class="yt-timestamp" data-t="00:26:41">[00:26:41]</a>.

## Market Dynamics and Defensibility

### Consumer-like Moat
Michael Tru believes that defensibility in the AI space is primarily about building the "best thing possible" <a class="yt-timestamp" data-t="00:41:46">[00:41:46]</a>. It's more akin to a consumer-like moat, where consistent product superiority retains users, rather than traditional enterprise software lock-in through contracts or switching costs <a class="yt-timestamp" data-t="00:40:56">[00:40:56]</a>. The "ceiling is so high" for what can be built that companies are constantly susceptible to being "leapfrogged" if they don't innovate continuously <a class="yt-timestamp" data-t="00:39:32">[00:39:32]</a>.

### Market Size and Competition
The market for AI-powered developer tools is considered "so very big," much larger than past editor markets <a class="yt-timestamp" data-t="00:41:54">[00:41:54]</a>. This is because AI enables automation of "busy work" and fundamentally changes "knowledge work" across many areas, not just coding <a class="yt-timestamp" data-t="00:43:08">[00:43:08]</a>. While there might be one dominant "general tool" for programming, there will also be numerous niche solutions for specific market segments or parts of the software development lifecycle <a class="yt-timestamp" data-t="00:43:48">[00:43:48]</a>.

### Incumbents vs. Innovators
The AI market is "not super friendly to incumbents" <a class="yt-timestamp" data-t="00:45:06">[00:45:06]</a>. Unlike commoditized markets where bundling or high switching costs favor established players, AI's high ceiling means new innovations can quickly outpace existing solutions <a class="yt-timestamp" data-t="00:45:11">[00:45:11]</a>. This makes it more favorable for whoever has the most innovative product <a class="yt-timestamp" data-t="00:45:54">[00:45:54]</a>.

## Hiring and Team Building

### Hiring Too Slow vs. Too Fast
A key lesson was realizing they "hired too slow to begin with" <a class="yt-timestamp" data-t="00:53:23">[00:53:23]</a>, contrasting with the common advice that many startups hire too fast <a class="yt-timestamp" data-t="00:53:18">[00:53:18]</a>. While patience in hiring is crucial, they could have been more efficient in their early recruitment efforts <a class="yt-timestamp" data-t="00:53:25">[00:53:25]</a>.

### Ideal Candidate Profile
Building a "world-class group of engineers and researchers" was paramount for Cursor's strategy <a class="yt-timestamp" data-t="00:52:26">[00:52:26]</a>. They sought a mix of:
*   **Intellectual Curiosity & Experimentation**: For building new things in a rapidly evolving field <a class="yt-timestamp" data-t="00:52:42">[00:52:42]</a>.
*   **Intellectual Honesty & "Micro Pessimism"**: To maintain a level head amidst industry noise and ensure realistic assessments <a class="yt-timestamp" data-t="00:52:47">[00:52:47]</a>.

They initially biased too much towards highly credentialed, young individuals straight out of "well-known schools" but found success with "later careered" fantastic people who didn't fit that archetype <a class="yt-timestamp" data-t="00:54:21">[00:54:21]</a>.

### Two-Day Work Test
A successful and scalable hiring technique is a two-day onsite work test <a class="yt-timestamp" data-t="00:55:56">[00:55:56]</a>. Candidates work on a real, mock project within Cursor's codebase, largely unsupervised but with collaboration <a class="yt-timestamp" data-t="00:57:40">[00:57:40]</a>. This allows the team to:
*   **Evaluate Real Work Product**: See candidates' output on a tangible project over two days <a class="yt-timestamp" data-t="00:56:16">[00:56:16]</a>.
*   **Assess Cultural Fit**: Determine if they "want to be around this person" given extended interaction <a class="yt-timestamp" data-t="00:56:40">[00:56:40]</a>.
*   **Generate Excitement**: Especially in early stages, it provides an opportunity for candidates to meet the team and get convinced to join <a class="yt-timestamp" data-t="00:56:57">[00:56:57]</a>.

This method has scaled even with a relatively small team (currently around 60 people, mostly engineers and researchers) <a class="yt-timestamp" data-t="00:58:08">[00:58:08]</a>.

## Maintaining Focus in a Fast-Paced AI Landscape

Staying focused amidst constant AI news and new technologies is challenging <a class="yt-timestamp" data-t="00:59:12">[00:59:12]</a>. Strategies include:
*   **Hiring Disposition**: Bringing in people less focused on external validation and more on building something truly great and high-quality work <a class="yt-timestamp" data-t="00:59:54">[00:59:54]</a>. Level-headed individuals who avoid extreme highs and lows are crucial <a class="yt-timestamp" data-t="01:00:07">[01:00:07]</a>.
*   **Immune System to Noise**: Having worked in AI since 2021-2022, the team has developed an "immune system" to the constant "chatter" and can discern which events truly matter for the business <a class="yt-timestamp" data-t="01:01:06">[01:01:06]</a>. Most new ideas in AI (like many academic papers) haven't had staying power <a class="yt-timestamp" data-t="01:02:22">[01:02:22]</a>.

## Misunderstandings about AI's Future

A common misunderstanding is the expectation of either extremely rapid, overnight changes or that AI is mere "bluster and hype" <a class="yt-timestamp" data-t="01:02:53">[01:02:53]</a>. Tru believes AI represents a "multi-decade" technological shift, more consequential than the internet or the advent of computers <a class="yt-timestamp" data-t="01:03:07">[01:03:07]</a>. Progress requires knocking down many independent problems across both the science (making models smarter, faster, cheaper) and the user experience (how humans interact with and control AI) <a class="yt-timestamp" data-t="01:03:30">[01:03:30]</a>.

Another key point is the role of companies focused on "automating and augmenting a particular area of knowledge work" <a class="yt-timestamp" data-t="01:04:15">[01:04:15]</a>. These companies, by [[leveraging_ai_tools_in_product_management | leveraging AI tools in product management]] and building both the underlying technology and the product experience, will be highly consequential, not just for user value but for pushing the broader AI technology forward <a class="yt-timestamp" data-t="01:04:30">[01:04:30]</a>.

Finally, despite AI writing more code, the demand for engineers is expected to increase long into the future <a class="yt-timestamp" data-t="01:08:49">[01:08:49]</a>. This is because the underlying demand for software remains vast, and current software creation is still incredibly expensive and labor-intensive <a class="yt-timestamp" data-t="01:07:26">[01:07:26]</a>. Reducing friction and cost will unlock much more software development <a class="yt-timestamp" data-t="01:07:49">[01:07:49]</a>.