---
title: Enterprise adoption and use cases for AI
videoId: MvxtIIqJRUQ
---

From: [[redpointai]] <br/> 

The "Unsupervised Learning" AI podcast featured Jacob Efron and guest host Rob Taves from Radical Ventures, joined by Peter Welinder, VP of Product and Partnerships at OpenAI <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. The conversation explored various aspects of AI, including where value will accrue in the AI ecosystem, OpenAI's product strategy, [[challenges_in_ai_adoption_and_deployment | enterprise AI adoption challenges]], and the future of AI.

## Value Accrual in the AI Ecosystem

Peter Welinder believes that most value will accrue at the application layer across many different applications <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. OpenAI's strategy is to enable as many builders as possible to create products on top of their technology <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>. They deliberately keep prices low at the model infrastructure layer to foster development <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>, noting dramatic price cuts over the years, such as a 70% reduction and a 10x cheaper GPT-3.5 Turbo model <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. This approach broadens access and applicability of their models to more applications <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

OpenAI acknowledges that the right tools for this technology have yet to be invented and prefers the developer ecosystem to figure out and build these tools <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. With millions of people building on top of their technology, there is significantly more innovation in the application and tooling space than OpenAI's internal team of around 400 people could achieve <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. Value capture is expected to occur at the application layer through competitive modes like network effects and branding <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.

## OpenAI's Product Strategy

OpenAI aims to remain at the platform level, providing general models and tools rather than specialized end-user applications <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>. While ChatGPT serves consumers as a general application for answering generic questions, it is not designed to be the best AI teacher, doctor, or lawyer <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>. Companies are expected to build these specialized applications by integrating with other products, proprietary content, and domain expertise <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.

OpenAI prioritizes developing core language models due to their flexibility <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>. Their strategy involved a significant bet on language models and their generality, focusing most of their compute and personnel on training these models <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>. This singular focus allows them to move quickly with features like browsing and plugins <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>. The product evolution, including plugins, code interpreter, and external API connections, aims to unify different functionalities and make it easier for research teams to deploy innovations to users <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>.

OpenAI sees plugins as mini-agents that perform tasks by connecting to APIs <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>. The company anticipates models becoming smarter and more robust, leading to more agent-like behaviors where the AI only checks in when uncertain about a task <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.

## [[Challenges in AI Adoption and Deployment | Enterprise AI Adoption Challenges]]

The biggest challenge preventing full-steam enterprise adoption of AI models is the problem of hallucinations, where models fabricate facts <a class="yt-timestamp" data-t="00:26:17">[00:26:17]</a>. This is an open research problem at the cutting edge of the field <a class="yt-timestamp" data-t="00:26:36">[00:26:36]</a>.

Companies are addressing this by grounding models in external data, such as internal company documentation <a class="yt-timestamp" data-t="00:26:55">[00:26:55]</a>. This involves embedding questions and documents, using a vector search database to find relevant information, and then having the language model summarize and answer based on those documents <a class="yt-timestamp" data-t="00:27:11">[00:27:11]</a>. Models can also be instructed to state "I don't know" if they cannot find an answer, which improves reliability <a class="yt-timestamp" data-t="00:27:34">[00:27:34]</a>.

OpenAI prioritizes core model improvements—such as lower prices, higher reliability, and lower latency—because these fundamentals are crucial regardless of the tooling built on top <a class="yt-timestamp" data-t="00:29:19">[00:29:19]</a>. They listen to developers to identify obstacles and build tooling that is universally needed to help them get off the ground quickly <a class="yt-timestamp" data-t="00:28:22">[00:28:22]</a>.

## Open Source vs. Proprietary Models in Enterprise

Peter Welinder holds an "unpopular opinion" that proprietary models will consistently be superior to open-source models for the foreseeable future <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>. He expects there will always be a category of AI systems that are significantly better than their open-source counterparts <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>. This is analogous to how desktop Linux, despite existing for 30 years, has not caught up to proprietary operating systems like macOS or Windows, largely due to insufficient investment in detailed refinement <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>.

The substantial capital and engineering effort required for training and running models at scale make it difficult to replicate at an open-source level <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>. Companies investing heavily in these models have no incentive to open-source their most advanced creations, partly due to investment protection and safety concerns <a class="yt-timestamp" data-t="00:17:24">[00:17:24]</a>.

However, Welinder is "very excited" about open-source development <a class="yt-timestamp" data-t="00:17:59">[00:17:59]</a>. Open-source models are valuable for pushing research forward, trying new training approaches, and exploring different applications <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>. They also make sense for specific product areas, such as smaller models deployed on devices, at the edge, or for on-premise deployments where latency and control are paramount <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>.

For applications requiring the best performance and reliability, proprietary models are the most rational choice, as they will remain a couple of years ahead of open-source options for the foreseeable future <a class="yt-timestamp" data-t="00:19:05">[00:19:05]</a>.

While some tasks (e.g., summarizing) may not require the smartest model, products tend to evolve towards generality over time, necessitating a generally smart model <a class="yt-timestamp" data-t="00:20:14">[00:20:14]</a>. Using a less capable model for a commercial product places a company at a competitive disadvantage <a class="yt-timestamp" data-t="00:22:28">[00:22:28]</a>. OpenAI believes most value will accrue in the smartest models because they can tackle the most economically valuable problems <a class="yt-timestamp" data-t="00:22:37">[00:22:37]</a>.

OpenAI does invest in open-sourcing auxiliary models that enable broader use cases for smarter models, such as their Whisper model for accurate audio transcription. This allows for more applications that feed into large language models, even if OpenAI doesn't expect to monetize speech recognition directly <a class="yt-timestamp" data-t="00:24:31">[00:24:31]</a>.

## [[Strategic uses of AI in enterprises | Future Applications of AI in Workplace Automation]]

AI is expected to enable "co-pilots" for various professions, including lawyers and medical providers <a class="yt-timestamp" data-t="00:22:58">[00:22:58]</a>. Over time, AI could extend to areas like science, assisting in drug discovery or climate change solutions, leading to significant economic output and a higher standard of living <a class="yt-timestamp" data-t="00:23:10">[00:23:10]</a>.

## AI Risks and Safety

Peter Welinder believes that risks such as misinformation, deepfakes, and bias are largely surmountable <a class="yt-timestamp" data-t="00:30:50">[00:30:50]</a>. Misinformation becomes a problem at scale, but existing platforms have infrastructure to protect against it <a class="yt-timestamp" data-t="00:31:08">[00:31:08]</a>. Regarding bias, OpenAI's goal is to provide tools for product developers and users to instruct the model on desired biases within acceptable bounds <a class="yt-timestamp" data-t="00:31:36">[00:31:36]</a>.

The risk receiving too little attention, according to Welinder, is the progression from AGI to superintelligence—models that are "really, really smart" and capable beyond human intellect <a class="yt-timestamp" data-t="00:32:10">[00:32:10]</a>. He notes a surprising lack of research on how to ensure a beneficial outcome when this occurs <a class="yt-timestamp" data-t="00:33:33">[00:33:33]</a>. OpenAI has teams dedicated to this, but there isn't a widespread "superintelligence safety department" at universities <a class="yt-timestamp" data-t="00:32:41">[00:32:41]</a>. This concern is existential for humanity <a class="yt-timestamp" data-t="00:32:54">[00:32:54]</a>.

Welinder speculates that AGI, defined as autonomous systems capable of economically valuable work at human levels, could be achieved before 2030 <a class="yt-timestamp" data-t="00:34:41">[00:34:41]</a>. He notes a significant shift in the field over the past 15-20 years, making AGI feel like it's "on the path of kind of just happening" <a class="yt-timestamp" data-t="00:35:53">[00:35:53]</a>. Early signs of superintelligence might appear around 2030 <a class="yt-timestamp" data-t="00:36:40">[00:36:40]</a>.

OpenAI's strategy involves releasing models with low stakes to learn about risks like misinformation and bias, which prepares them for higher stakes scenarios with superintelligence <a class="yt-timestamp" data-t="00:38:42">[00:38:42]</a>. They prioritize establishing the right organizational processes, frameworks, and safety safeguards, rather than trying to figure it out after a superintelligent model is trained <a class="yt-timestamp" data-t="00:39:02">[00:39:02]</a>. OpenAI notably held back on releasing GPT-4 for almost half a year to gain clarity on potential downsides <a class="yt-timestamp" data-t="00:39:40">[00:39:40]</a>.

Areas for research in superintelligence safety include:
*   **Interpretability**: Understanding what is happening inside black-box models <a class="yt-timestamp" data-t="00:41:18">[00:41:18]</a>.
*   **Alignment Definition**: Clearly specifying goals and guardrails for AI behavior <a class="yt-timestamp" data-t="00:42:16">[00:42:16]</a>. This requires collaboration between technical experts, social scientists, and philosophers <a class="yt-timestamp" data-t="00:42:45">[00:42:45]</a>.
*   **Technical Approaches**: Such as shaping reward functions for reinforcement learning or having one model oversee the actions of another <a class="yt-timestamp" data-t="00:42:55">[00:42:55]</a>.

## Internal Use of AI at OpenAI

Internally at OpenAI, employees use ChatGPT for a broad range of tasks, including:
*   **Coding**: Debugging issues and analyzing stack traces <a class="yt-timestamp" data-t="00:44:30">[00:44:30]</a>.
*   **Writing Assistance**: Overcoming writer's block, improving writing quality, and drafting emails based on desired points <a class="yt-timestamp" data-t="00:44:44">[00:44:44]</a>.

## Future Outlook

Peter Welinder continues to believe that it's crucial to seriously consider the implications of superintelligence <a class="yt-timestamp" data-t="00:45:36">[00:45:36]</a>. He feels many people still underestimate how quickly AI capabilities are advancing beyond previous expectations <a class="yt-timestamp" data-t="00:45:50">[00:45:50]</a>.

OpenAI's primary focus remains on making models better in terms of capability and safety <a class="yt-timestamp" data-t="00:47:14">[00:47:14]</a>. The main concern for OpenAI's continued leadership is losing touch with its users and developers <a class="yt-timestamp" data-t="00:47:24">[00:47:24]</a>. There is a tension where model improvements can sometimes replace developer-built solutions <a class="yt-timestamp" data-t="00:47:40">[00:47:40]</a>. Scaling the "great customer experience" from when OpenAI had few customers to millions is a key challenge to ensure people continue to embrace and build on their technology <a class="yt-timestamp" data-t="00:48:34">[00:48:34]</a>.

For those interested in learning more about OpenAI's technology and philosophy, Welinder encourages checking out their blog <a class="yt-timestamp" data-t="00:49:32">[00:49:32]</a>.