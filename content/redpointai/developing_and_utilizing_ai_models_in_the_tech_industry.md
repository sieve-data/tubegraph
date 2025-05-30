---
title: Developing and utilizing AI models in the tech industry
videoId: n6PazYmo_Qo
---

From: [[redpointai]] <br/> 

The "Unsupervised Learning AI Podcast," hosted by Jacob Efron and Pat Chase, featured Omj, founder of Replit, to discuss the dynamic landscape of AI model development and utilization within the tech industry <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Replit, valued at over a billion dollars, is at the forefront of integrating AI into coding solutions <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

## AI in Coding Education and the Evolving Skillset

Omj emphasizes that the best way to learn coding is by "making things," a principle that aligns with Codecademy's approach where he was a founding engineer <a class="yt-timestamp" data-t="01:09:00">[01:09:00]</a> <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>. Large Language Models (LLMs) significantly accelerate this "learn by doing" methodology, allowing users to get something running in minutes using an AI-powered editor <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>. Replit enables users to start by prompting or forking templates, quickly getting a "dopamine hit" from seeing immediate results <a class="yt-timestamp" data-t="03:30:00">[03:30:00]</a>.

The role of a software engineer is expected to [[Challenges and advancements in AI model development | bifurcate]] <a class="yt-timestamp" data-t="04:41:00">[04:41:00]</a>:
*   **Product Creator/Entrepreneur:** Focused on making things, acquiring customers and users, often through prompting and iterating on prompts <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>. This path might involve less traditional software engineering knowledge <a class="yt-timestamp" data-t="06:17:00">[06:17:00]</a>.
*   **Traditional Software Engineer:** Focused on building cloud infrastructure, data pipelines, or backend systems <a class="yt-timestamp" data-t="05:48:00">[05:48:00]</a>. A computer science degree remains relevant for this path <a class="yt-timestamp" data-t="06:10:00">[06:10:00]</a>.

AI disproportionately benefits beginners, offering an unprecedented return on investment (ROI) for learning to code <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a> <a class="yt-timestamp" data-t="01:51:00">[01:51:00]</a>. Studies suggest AI boosts the productivity of less experienced individuals more <a class="yt-timestamp" data-t="01:51:00">[01:51:00]</a> <a class="yt-timestamp" data-t="19:30:00">[19:30:00]</a>. However, advanced users who learn how to leverage AI with sophisticated prompting techniques (like Chain of Thought) will also see significant benefits <a class="yt-timestamp" data-t="02:03:00">[02:03:00]</a>.

Younger generations are proving much better at adapting to new AI tools, naturally building mental models and prompting effectively <a class="yt-timestamp" data-t="02:10:00">[02:10:00]</a> <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>. This adaptation is likened to the introduction of calculators in education, which some teachers initially resisted but later found beneficial <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>.

## Replit's Strategy: Embedding AI in the Core Product

Replit's AI product, originally called "Ghostwriter," has been renamed to "Replit AI" to signify its complete integration into the platform <a class="yt-timestamp" data-t="06:40:00">[06:40:00]</a> <a class="yt-timestamp" data-t="06:48:00">[06:48:00]</a>. This move reflects Omj's view that AI add-ons (like "co-pilots") are a "transitionary period," and companies relying on that revenue should be concerned <a class="yt-timestamp" data-t="07:37:00">[07:37:00]</a>.

Replit's approach is to embed AI into every interaction, making it part of the free plan <a class="yt-timestamp" data-t="08:07:00">[08:07:00]</a>. This ensures designers think from an AI-first perspective <a class="yt-timestamp" data-t="08:42:00">[08:42:00]</a>.
Key AI features at Replit include:
*   **Code Suggestions:** Passive "push model" where AI suggests code as the user types, similar to Gmail's ghost text <a class="yt-timestamp" data-t="08:51:00">[08:51:00]</a>.
*   **Generate File:** An active "pull model" where users can right-click and prompt to generate an entire file based on context <a class="yt-timestamp" data-t="09:29:00">[09:29:00]</a>.
*   **AI Debug Button:** Appears on console errors, opening an AI chat pre-prompted with the error and relevant context <a class="yt-timestamp" data-t="09:53:00">[09:53:00]</a>.

## [[Challenges and advancements in AI model development | Capabilities and Limitations]] of AI Models in Coding

Omj notes that the understanding of LLMs has evolved from a "mystical component" to a more reductive view: they are primarily a function of data, essentially a compression of vast datasets <a class="yt-timestamp" data-t="11:01:00">[11:01:00]</a> <a class="yt-timestamp" data-t="11:36:00">[11:36:00]</a>. The power of LLMs lies in interpolating different distributions of data, such as writing a rap song in the style of Shakespeare <a class="yt-timestamp" data-t="11:53:00">[11:53:00]</a>. This new paradigm is "software 2.0," where you program with data <a class="yt-timestamp" data-t="12:42:00">[12:42:00]</a>.

### Data Quality and Training
To understand a model's capabilities, one must understand the data it was fed and the post-training mechanisms used (e.g., instruction fine-tuning, RLHF, DPO) <a class="yt-timestamp" data-t="12:51:00">[12:51:00]</a>.
*   **Size and Compute:** More tokens, more compute, and greater diversity/freshness of tokens lead to better models <a class="yt-timestamp" data-t="16:11:00">[16:11:00]</a>.
*   **Quality:** Training on minified JavaScript, for example, can "mess up" the model <a class="yt-timestamp" data-t="16:48:00">[16:48:00]</a>. Models should ideally be trained on data generated by the "best programmers" because GPTs are "emulation machines" that clone human behavior <a class="yt-timestamp" data-t="16:58:00">[16:58:00]</a>.
*   **Data Scarcity:** Omj argues that the industry is "running out of open-source tokens" <a class="yt-timestamp" data-t="14:02:00">[14:02:00]</a>. GPT-4, for instance, is trained on all internet code data plus hundreds of millions of dollars spent on annotated coding data <a class="yt-timestamp" data-t="14:24:00">[14:24:00]</a>. Replit has an advantage with its large user base generating unique application code, which is scarcer than high-quality infrastructure code found on GitHub <a class="yt-timestamp" data-t="14:44:00">[14:44:00]</a> <a class="yt-timestamp" data-t="18:14:00">[18:14:00]</a>.
*   **Diverse Data Sources:** Scientific and even legal texts have been shown to improve code generation capabilities, indicating the models learn "coding adjacent reasoning" <a class="yt-timestamp" data-t="15:17:00">[15:17:00]</a>. Omj predicts another 2-3 years of increased coding capabilities <a class="yt-timestamp" data-t="15:34:00">[15:34:00]</a>.

## Organizational Structure and AI Adoption
Replit favors a horizontal organizational structure for AI integration, building platforms that touch every aspect of the software <a class="yt-timestamp" data-t="02:41:00">[02:41:00]</a>. Omj expresses surprise at the slow pace of AI adoption in some areas, particularly within larger corporations, despite rapid advancements like Copilot's spread <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>. He believes AI should move faster to kickstart economic growth, but cultural, legal, and internal forces (e.g., within big AI labs) are slowing it down <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>.

## Build vs. Buy: Replit's Decision to Train Its Own Model

Replit made a strategic decision to train its own AI model (a 3-billion parameter model) for its core code suggestion feature, Ghostwriter <a class="yt-timestamp" data-t="07:12:00">[07:12:00]</a> <a class="yt-timestamp" data-t="03:05:00">[03:05:00]</a>. The primary reasons were:
*   **Latency:** Commercial models couldn't meet the low latency requirements for real-time code suggestions <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>. Omj notes that even Copilot, which had a deep partnership with OpenAI for custom models, has gotten slower <a class="yt-timestamp" data-t="02:17:00">[02:17:00]</a>.
*   **Cost:** To offer AI as part of Replit's free experience, commercial model pricing was prohibitive <a class="yt-timestamp" data-t="02:28:00">[02:28:00]</a>. Training their 3B model cost around $100,000, which is not a "huge capital expenditure" <a class="yt-timestamp" data-t="02:35:00">[02:35:00]</a>.
*   **Small Model Capabilities:** Replit was early to realize that small models are capable, affordable to train, and deploy effectively for specific tasks <a class="yt-timestamp" data-t="02:41:00">[02:41:00]</a>.

However, Replit also uses commercial models for other use cases, such as general-purpose chat features <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>. The decision to build internally or use commercial APIs should start from the customer pain point, explore solutions, and run the numbers, considering strategic goals (e.g., wanting to be an AI company) <a class="yt-timestamp" data-t="03:24:00">[03:24:00]</a>.

## The Illusion of Open Source AI Models

Omj stirred discussion with a tweet arguing that "true open source models" don't exist in AI today because they cannot be easily reproduced <a class="yt-timestamp" data-t="03:18:00">[03:18:00]</a>. He draws an analogy to Linux: if you could only use the binary or had the source code but no compiler, it wouldn't be considered open source <a class="yt-timestamp" data-t="03:20:00">[03:20:00]</a>.

Critically, if companies use open-source models like Meta's Llama, they remain dependent on the goodwill of the creators (e.g., Mark Zuckerberg) to continue pushing out new versions <a class="yt-timestamp" data-t="03:27:00">[03:27:00]</a>.

From a security perspective, not having clarity on the training process and data of a model poses a huge risk <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>. Since "you're programming with data," the data acts as the "source code" in this analogy <a class="yt-timestamp" data-t="03:12:00">[03:12:00]</a>. Omj references Ken Thompson's "Reflections on Trusting Trust" paper from the 1970s, which describes how a backdoor can be embedded in a compiler and evade inspection, a concept with parallels in LLM training <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>.

Given these dependencies and risks, Omj believes that in the long term, companies shouldn't depend on current open-source models as primary solutions. Instead, they should treat them like commercial models for prototyping and experimentation, while having a sustainable path that avoids external dependencies <a class="yt-timestamp" data-t="03:30:00">[03:30:00]</a>. He hopes for a truly open-source project that allows contributions and fosters an open-source flywheel <a class="yt-timestamp" data-t="03:39:00">[03:39:00]</a>.

## Future Trends and Challenges

### Agents
Omj believes that agents are the "next big thing" after multimodal AI <a class="yt-timestamp" data-t="04:56:00">[04:56:00]</a>. While multimodal is a profound incremental improvement, agents represent a more significant shift <a class="yt-timestamp" data-t="04:03:00">[04:03:00]</a>.
*   **Cost:** Recursive calls by agents (like AutoGPT) and larger models (GPT-4) can become very expensive quickly, making them cost-prohibitive for many users <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>.
*   **Current State:** LLMs often have "accidental" agent capabilities, but true agents might require "action transformers" that predict actions instead of tokens <a class="yt-timestamp" data-t="04:11:00">[04:11:00]</a>.
*   **Milestone:** A key milestone for agents will be their ability to reliably follow a bulleted list of actions without "going off the rails" or requiring "insane amounts of Chain of Thought and recursive debugging" <a class="yt-timestamp" data-t="04:49:00">[04:49:00]</a>. This dependability is crucial for financial or legal workflows <a class="yt-timestamp" data-t="05:27:00">[05:27:00]</a>.
*   **Timeline:** Omj expects some version of agentic workflows and background agents to start emerging this year <a class="yt-timestamp" data-t="04:06:00">[04:06:00]</a>. He encourages entrepreneurs to "walk through walls" and try to make agents work even with current limitations, as it's a bet worth making <a class="yt-timestamp" data-t="04:30:00">[04:30:00]</a>.

### Hyperreality
Omj notes that the world is rapidly moving towards "hyperreality," where it becomes incredibly difficult to distinguish what's fiction from what's real due to generative AI <a class="yt-timestamp" data-t="03:03:00">[03:03:00]</a>. He expresses concern that there isn't enough focus on building technology to counteract this, like a Chrome extension to identify fake media <a class="yt-timestamp" data-t="03:58:00">[03:58:00]</a>.

### Pricing and Business Models
For AI-native products, Omj advocates for a [[Impact of AI advancements on business models | value-based pricing]] model rather than "cost-plus" <a class="yt-timestamp" data-t="04:41:00">[04:41:00]</a>. He anticipates a future where AI inference costs continue to decrease and the inference stack becomes more efficient <a class="yt-timestamp" data-t="04:11:00">[04:11:00]</a>.
*   **Usage-based pricing** is becoming more prevalent, especially with AI, because power users can incur significant costs on models, making a pure subscription SaaS model less viable <a class="yt-timestamp" data-t="04:29:00">[04:29:00]</a>. Replit, for example, offers bundles but also allows for overages <a class="yt-timestamp" data-t="04:51:00">[04:51:00]</a>.
*   The industry is in a period of "VC subsidized models training and tokens," which won't last forever <a class="yt-timestamp" data-t="04:49:00">[04:49:00]</a>.

### Industry Consolidation vs. Specialization
The "default pessimistic assumption" is that Microsoft, with its vast install base, Enterprise relationships, and sales team, will win the entire AI coding space <a class="yt-timestamp" data-t="05:26:00">[05:26:00]</a>. However, Omj is optimistic about a new crop of specialized companies <a class="yt-timestamp" data-t="05:03:00">[05:03:00]</a>:
*   Companies that take a holistic approach, like Replit, providing a cloud development environment with AI sitting on top of the entire stack, can build more ambitious AI products, including [[Trends in AI model training and deployment | agentic workflows]] <a class="yt-timestamp" data-t="05:38:00">[05:38:00]</a>.
*   Specialized companies, like Codium (generating tests), will also do well <a class="yt-timestamp" data-t="05:59:00">[05:59:00]</a>.
*   The challenge for pure code generation startups is that future models (e.g., GPT-5) might leapfrog their capabilities, making their heavy training investments less competitive <a class="yt-timestamp" data-t="05:46:00">[05:46:00]</a>. While Code Llama has shown strong benchmarks, the "Vibes" (actual user experience) may still fall short of proprietary models like GPT-4 <a class="yt-timestamp" data-t="05:57:00">[05:57:00]</a>.

## Surprises and Underhyped Areas

*   **Biggest Surprise:** How much latency matters in AI features <a class="yt-timestamp" data-t="05:27:00">[05:27:00]</a>. A 2-3 second response time changes the user experience entirely compared to 300 milliseconds <a class="yt-timestamp" data-t="05:37:00">[05:37:00]</a>.
*   **Failed Features:** Replit initially struggled to expose "inline actions" effectively <a class="yt-timestamp" data-t="05:14:00">[05:14:00]</a>. These actions, which derive information from cursor context, are superior to chat windows but required UI prompting for user adoption <a class="yt-timestamp" data-t="05:31:00">[05:31:00]</a>.
*   **Most Exciting AI Startup (outside Replit's space):** OpenAI for its ambition and diverse ventures (education, robotics, self-driving) <a class="yt-timestamp" data-t="05:58:00">[05:58:00]</a>. Perplexity AI is also highly regarded for its engineering competency, which allowed it to zoom ahead of competitors <a class="yt-timestamp" data-t="06:04:00">[06:04:00]</a>.
*   **Underhyped Area:** Using LLMs as part of everyday systems and backend call chains <a class="yt-timestamp" data-t="05:05:00">[05:05:00]</a>.
*   **Overhyped Area:** Chatbots <a class="yt-timestamp" data-t="05:51:00">[05:51:00]</a>.

## Impact on Engineering Teams
Omj predicts that in 5 years, what's done now could be achieved with 1/10th of the engineers <a class="yt-timestamp" data-t="06:46:00">[06:46:00]</a>. In 10 years, there could be a "1000x component" leading to significantly smaller company sizes <a class="yt-timestamp" data-t="06:55:00">[06:55:00]</a>. While the number of people doing "software creation" will grow, they might be called "software creators" rather than traditional "software engineers" <a class="yt-timestamp" data-t="07:14:00">[07:14:00]</a>.