---
title: Building and scaling an AI code editor
videoId: 5Z0RCxDZdrE
---

From: [[lennyspodcast]] <br/> 

Windsurf, a leading [[Innovations in code editors and IDEs | AI coding tool]], has quickly become a favorite among developers, accumulating over 1 million users within four months of its launch <a class="yt-timestamp" data-t="00:56:56">[00:56:56]</a>. Co-founded and led by Varun Mohan, Windsurf emerged from a series of strategic pivots by its parent company, Kodium <a class="yt-timestamp" data-t="00:48:00">[00:48:00]</a>.

## Kodium's Evolution: From Infrastructure to Application
Kodium was founded approximately four years ago, initially focusing on GPU virtualization and compiler software for deep learning applications <a class="yt-timestamp" data-t="00:41:40">[00:41:40]</a>. This venture enabled complex applications to run on computers without GPUs, optimizing workloads significantly <a class="yt-timestamp" data-t="00:50:50">[00:50:50]</a>. By mid-2022, Kodium had achieved a couple of million in revenue and managed over 10,000 GPUs with an eight-person team, operating as a free cash flow positive company <a class="yt-timestamp" data-t="00:51:50">[00:51:50]</a>.

However, with the rise of generative AI models, the company realized that their infrastructure-focused offerings would become less valuable as all companies would eventually run similar infrastructure <a class="yt-timestamp" data-t="00:54:50">[00:54:50]</a>. Recognizing [[the evolution of software development with AI | generative AI]] as the "next internet," Kodium decided to pivot and [[The role of AI in software development | build applications]] higher up the stack <a class="yt-timestamp" data-t="01:06:50">[01:06:50]</a>.

This led to the creation of Kodium, an [[AI and software development | AI coding tool]], initially a simple autocomplete model offered for free across various IDEs like VS Code, JetBrains, Eclipse, Visual Studio, Vim, and Emacs <a class="yt-timestamp" data-t="01:07:50">[01:07:50]</a>. Their infrastructure background allowed them to optimize these workloads, providing the product for free <a class="yt-timestamp" data-t="01:08:50">[01:08:50]</a>.

### The Bold Pivot to its Own IDE
Around six months prior to the discussion, Kodium faced limitations with existing IDEs, particularly VS Code, in showcasing advanced [[user experiences with AI and evolving AI capabilities | AI capabilities]] <a class="yt-timestamp" data-t="01:10:50">[01:10:50]</a>. This prompted the decision to fork VS Code and build their own IDE, Windsurf, to incorporate new agentic functionalities <a class="yt-timestamp" data-t="01:11:50">[01:11:50]</a>.

The pivot to building their own IDE was driven by the belief that [[The role of AI in software development | AI would write over 90% of software]], fundamentally changing the developer's role to reviewing code rather than primarily writing it <a class="yt-timestamp" data-t="01:14:50">[01:14:50]</a>. Custom review flows and enhanced UI features were necessary to support this new paradigm <a class="yt-timestamp" data-t="01:15:50">[01:15:50]</a>. For instance, when Windsurf launched its `windsurf tab` feature, providing inline refactors with a custom UI, the acceptance rate of suggestions tripled compared to the same feature in VS Code <a class="yt-timestamp" data-t="01:18:50">[01:18:50]</a>.

Varun Mohan emphasizes the importance of not being "in love with your ideas" and ruthlessly re-evaluating hypotheses, even if previous ventures were successful <a class="yt-timestamp" data-t="01:11:50">[01:11:50]</a>. This constant re-evaluation and willingness to make "bet the company" decisions overnight are crucial for survival in a rapidly evolving space <a class="yt-timestamp" data-t="01:12:50">[01:12:50]</a>.

## Windsurf: An AI-Native IDE
Windsurf is an integrated development environment (IDE) designed to build and modify software applications <a class="yt-timestamp" data-t="01:13:50">[01:13:50]</a>. Its core distinction lies in its deep integration of [[AI and software development | AI capabilities]] to streamline software development <a class="yt-timestamp" data-t="01:14:50">[01:14:50]</a>.

### Key Differentiators:
*   **Deep Codebase Understanding**: Windsurf excels at understanding very large and complex codebases, such as those with over 100 million lines of code found at companies like Dell <a class="yt-timestamp" data-t="01:38:50">[01:38:50]</a>. This is achieved by building [[impact of custom model development in AI tools | custom models]] that consume and rank large chunks of code in parallel across thousands of GPUs, identifying the most relevant snippets for any query <a class="yt-timestamp" data-t="01:38:50">[01:38:50]</a>.
*   **Agentic Capabilities**: The IDE allows users to interact with [[AI and software development | AI agents]] to perform complex tasks, from generating an entire application based on an image to refactoring code across multiple files <a class="yt-timestamp" data-t="01:41:50">[01:41:50]</a>. It can even understand and bridge user-initiated manual changes with its own AI-generated modifications <a class="yt-timestamp" data-t="01:47:50">[01:47:50]</a>.
*   **Hybrid Model Architecture**: Windsurf uses a combination of models:
    *   **Planning**: Sonnet or OpenAI's GPT-4o for high-level planning <a class="yt-timestamp" data-t="01:54:50">[01:54:50]</a>.
    *   **Retrieval**: Internally run models for high-quality retrieval to understand the codebase efficiently, avoiding sending massive codebases to external APIs due to cost and latency <a class="yt-timestamp" data-t="01:54:50">[01:54:50]</a>.
    *   **Edits/Autocomplete**: [[AI development and model improvement | Custom models]] post-trained on open-source models for rapid code edits and autocomplete, often outperforming frontier models in speed and contextual understanding of incomplete code <a class="yt-timestamp" data-t="01:55:50">[01:55:50]</a>.
*   **User Feedback for Model Training**: Windsurf receives tens of millions of pieces of user feedback every hour, including preference data on what users like and don't like, and data from incomplete code as users type <a class="yt-timestamp" data-t="01:56:50">[01:56:50]</a>. This unique and proprietary dataset allows them to train models specifically tailored for code completion and contextual understanding in real-time development environments <a class="yt-timestamp" data-t="01:57:50">[01:57:50]</a>.
*   **Enterprise-Grade Security**: Windsurf supports secure environments, including FedRAMP compliance for government entities, and offers a hybrid mode where indexed code resides on the user's tenant, protecting sensitive IP <a class="yt-timestamp" data-t="01:40:50">[01:40:50]</a>.

## The Future of Software Development with AI
Varun Mohan asserts that [[The role of AI in software development | AI will likely write over 90% of software]] <a class="yt-timestamp" data-t="01:19:50">[01:19:50]</a>. This means the engineer's role will shift from "solving it" (the pure act of coding) to focusing on "what should I solve" —identifying critical business problems and product capabilities <a class="yt-timestamp" data-t="01:21:50">[01:21:50]</a>.

### Skills for the Future
*   **Problem-Solving**: A strong understanding of how computers and systems work, including parallel processing, memory, and networking, remains valuable for making informed technical decisions and debugging <a class="yt-timestamp" data-t="01:19:50">[01:19:50]</a>. Computer science degrees, while not solely about writing code, teach fundamental problem-solving principles <a class="yt-timestamp" data-t="01:20:50">[01:20:50]</a>.
*   **Agency**: The ability to independently identify problems and take initiative to build solutions, rather than simply following defined paths <a class="yt-timestamp" data-t="01:21:50">[01:21:50]</a>. This is critical for startups that need to constantly innovate <a class="yt-timestamp" data-t="01:22:50">[01:22:50]</a>.
*   **Taste**: Developing good taste in design and product, as AI will handle the execution, leaving the "what" and "how it should look" to humans <a class="yt-timestamp" data-t="01:45:50">[01:45:50]</a>.

## Organizational Philosophy and Hiring
Kodium's approach to [[building a highgrowth AI company | building a high-growth AI company]] is rooted in ambitious goals and a unique hiring philosophy.

### Hiring Strategy
Varun emphasizes being "the smallest company we can be to satisfy our ambitions" <a class="yt-timestamp" data-t="01:23:50">[01:23:50]</a>. The goal is to reduce the time to build apps and technology by 99% <a class="yt-timestamp" data-t="01:24:50">[01:24:50]</a>.

Kodium only hires for a role when they are "underwater" in that function, likening the company to a "dehydrated entity" that only takes a "little bit of water" (a new hire) when truly needed <a class="yt-timestamp" data-t="01:24:50">[01:24:50]</a>. This strategy forces ruthless prioritization and prevents "weird politics" where employees manufacture work <a class="yt-timestamp" data-t="01:27:50">[01:27:50]</a>. It ensures that everyone is pushing for the most important tasks, aligning with the startup principle of winning by doing "one thing really well" <a class="yt-timestamp" data-t="01:28:50">[01:28:50]</a>.

Kodium's interview process has an extremely low acceptance rate (around 6% post-take-home assignment, with the take-home itself filtering 10-15x more candidates) <a class="yt-timestamp" data-t="01:33:50">[01:33:50]</a>. They look for high technical bar, passion for the mission, and a willingness to work very hard <a class="yt-timestamp" data-t="01:31:50">[01:31:50]</a>.

> [!QUOTE] Varun Mohan on Work Ethic
> "If we have many smart people at our company that also work hard, what's the differentiator going to be? Are you just going to pull them down?" <a class="yt-timestamp" data-t="01:31:50">[01:31:50]</a>

### Go-to-Market Approach
Uniquely, Kodium invested heavily in enterprise sales early in its history, with the go-to-market team now comprising over 80 people out of approximately 160 total employees <a class="yt-timestamp" data-t="01:34:50">[01:34:50]</a>. This decision was influenced by early investors who were go-to-market operators <a class="yt-timestamp" data-t="01:35:50">[01:35:50]</a>. While many technical founders prefer a product-led growth model, Kodium recognized the value of enterprise sales, especially when large companies like Dell and JP Morgan Chase proactively sought their product <a class="yt-timestamp" data-t="01:35:50">[01:35:50]</a>. Selling to Fortune 500 companies is challenging purely through self-service <a class="yt-timestamp" data-t="01:36:50">[01:36:50]</a>.

### Team Structure
Kodium's core engineering team operates without dedicated product managers because the product is built by and for developers, whose intuition serves as a strong guide <a class="yt-timestamp" data-t="02:01:50">[02:01:50]</a>. For the enterprise side, where requirements (like FedRAMP compliance) are not naturally understood by engineers, they have product strategy roles that bridge customer needs with technical capabilities <a class="yt-timestamp" data-t="02:01:50">[02:01:50]</a>. The engineering team is fairly flat, organized into "two-pizza teams" to ensure leaders remain deeply involved in the technology <a class="yt-timestamp" data-t="02:02:50">[02:02:50]</a>. Teams are highly flexible and centrally planned, quickly re-prioritizing and moving resources when needed <a class="yt-timestamp" data-t="02:03:50">[02:03:50]</a>.

## Insights and Advice
### Counterintuitive Learnings
Varun notes a tension between satisfying short-term user requests and making long-term, disruptive bets <a class="yt-timestamp" data-t="02:06:50">[02:06:50]</a>. He aims for Windsurf to cannibalize its existing product every 6 to 12 months, making the previous version seem "silly" or "dumb" <a class="yt-timestamp" data-t="02:07:50">[02:07:50]</a>. This requires making proactive, non-user-requested innovations rather than just incremental improvements <a class="yt-timestamp" data-t="02:07:50">[02:07:50]</a>.

The most crucial lesson learned is the importance of being "okay with being wrong faster" <a class="yt-timestamp" data-t="02:09:50">[02:09:50]</a>. Founders must constantly re-evaluate hypotheses and enter uncomfortable spaces frequently, despite the need for irrational optimism to drive progress <a class="yt-timestamp" data-t="02:09:50">[02:09:50]</a>.

### Advice for the Future of AI and Software Development
*   **Get Your Hands Dirty**: Varun strongly advises everyone to "get your hands dirty" with [[AI and software development | AI products]] as quickly as possible <a class="yt-timestamp" data-t="02:11:50">[02:11:50]</a>. This includes downloading tools like Windsurf, building apps, creating mocks, and modifying existing codebases <a class="yt-timestamp" data-t="02:12:50">[02:12:50]</a>.
*   **Become a Force Multiplier**: By leveraging these tools, individuals can become "force multipliers" within their organizations, gaining respect and achieving more <a class="yt-timestamp" data-t="02:13:50">[02:13:50]</a>. For example, a product manager can use Windsurf to make quick edits to a codebase and even push changes to GitHub, demonstrating direct impact without relying solely on engineers <a class="yt-timestamp" data-t="02:13:50">[02:13:50]</a>. This effectively makes "everything open season" regarding roles and responsibilities <a class="yt-timestamp" data-t="02:13:50">[02:13:50]</a>.

> [!EXAMPLE] Impact on Product Managers
> Imagine a product manager who can quickly make edits to a codebase and push changes themselves. This capability leads to a "tremendous amount of respect" from engineering peers and enables them to get "way more done" <a class="yt-timestamp" data-t="02:14:50">[02:14:50]</a>.

The [[The role of AI in software development | ROI of building technology has increased]], meaning companies with high technology ceilings will likely hire more engineers, not fewer <a class="yt-timestamp" data-t="02:05:50">[02:05:50]</a>. The future of software development involves **[[Scaling and Enhancing Product Design with AI | AI-powered tools]]** that allow for unprecedented agency and efficiency, making it an exciting time for those willing to adapt and experiment.