---
title: Implementing AI in enterprises
videoId: VhPfM_aGBVc
---

From: [[aidotengineer]] <br/> 

Anthropic, an AI safety and research company, works closely with customers to implement artificial intelligence solutions in their businesses <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. The insights shared are based on hundreds of customer interactions <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Anthropic's Mission and Models
Anthropic aims to build the world's best and safest large language models (LLMs) <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. They have released multiple iterations of their frontier models, focusing on safety techniques, research, and policy <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

Their marquee model is Sonnet 3.5, launched in late October of the previous year <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. Sonnet is a leading model in the code space, performing strongly in evaluations like sbench, an [[Agentic enterprise and AI agents | agentic coding eval]] <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

Anthropic's research directions include model capabilities, product research, and AI safety <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. A differentiating focus is interpretability, which involves reverse engineering models to understand how they "think" and why, and then steering them for specific use cases <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.

Interpretability research progresses through stages:
*   **Understanding** Grasping AI decision-making <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
*   **Detection** Understanding specific behaviors and labeling them <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
*   **Steering** Influencing AI input <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
*   **Explainability** Unlocking business value from interpretability methods <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

Interpretability is expected to provide significant improvements in AI safety, reliability, and usability <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

## Solving Real Business Problems with AI
When considering [[Integrating AI into business operations | AI in enterprise applications]], Anthropic encourages customers to focus on using AI to solve core product problems, rather than limiting applications to basic chatbots and summarization <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>. The goal is to make bigger bets on more transformative uses <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.

For an onboarding and upskilling platform, instead of just summarizing course content or offering a Q&A chatbot, AI could:
*   Hyper-personalize course content based on individual employee context <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.
*   Dynamically adapt content to be more challenging if an employee is breezing through <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.
*   Dynamically update course material based on individual learning styles (e.g., visual learners receive visual content) <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.

AI is impacting various industries, including taxes, legal, and project management, by significantly enhancing customer experience, making products easier to use, and improving trustworthiness <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. These applications are achieving high-quality outputs, especially in business-critical workflows where accuracy is paramount (e.g., taxes where hallucination is unacceptable) <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.

## Getting Started with Anthropic's Products
Anthropic offers two main products:
*   **API**: For businesses looking to embed AI in their products and services <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
*   **Claude for Work**: Empowers entire organizations to leverage AI in day-to-day work <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.

Anthropic also partners with AWS and GCP, allowing customers to access their frontier models on Bedrock or Vertex. This enables deployment of applications in existing environments without managing new infrastructure, breaking down [[Building and scaling AI use cases for enterprises | barriers to entry]] <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.

## Setting Customers Up for Success
Anthropic's Applied AI team supports the technical aspects of use cases, helping to design architectures, evaluate performance, and tweak prompts to optimize model output <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>. They also feed customer insights back into Anthropic's product and research teams <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.

The team works closely with customers facing niche challenges in specific use case domains, applying the latest research and maximizing model performance through prompting <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>. This often involves:
1.  Kicking off a Sprint when challenges arise (LLM Ops, architectures, evals) <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
2.  Helping define metrics crucial for evaluating the model against the use case <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.
3.  Deploying the iterative results into an A/B test environment and eventually production <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.

### Case Study: Intercom's AI Agent Finn
Intercom, an AI customer service platform, developed an [[Agentic enterprise and AI agents | AI agent]] called Finn <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. Anthropic's Applied AI team collaborated with Intercom's data science team on a two-week sprint, testing Intercom's hardest prompts against prompts optimized with Claude <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. This led to a two-month sprint of fine-tuning and optimizing all of Intercom's prompts for Claude <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.

Results for Intercom's Finn 2, powered by Anthropic's models:
*   Outperformed the previous LLM <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.
*   Can solve up to 86% of customer support volume (51% out of the box) <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.
*   Increased human-like interactions, allowing for tone adjustment and answer length customization <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.
*   Improved policy awareness (e.g., refund policies) <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.

## Best Practices and Common Mistakes in AI Implementation
### Testing and Evaluation
A common mistake is [[Building and scaling AI use cases for enterprises | building a robust workflow]] first and then trying to implement evaluations <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>. Evaluations should guide the workflow, as they direct towards the desired outcome <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>. Other mistakes include struggling with data for eval design, or "trusting the vibes" by only running a few queries without sufficient representative samples for statistical significance <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>.

> "Evals are your intellectual property. If you want to be competitive in a space, you need to be able to out-compete people by navigating that latent space and finding the attractor state faster than anyone else." <a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a>

**Best Practices:**
*   Set up telemetry for back-testing architecture in advance <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>.
*   Design representative test cases, including "silly" or unexpected examples, to ensure the model responds appropriately or reroutes the question <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>.

### Identifying Metrics
Organizations often face a trade-off triangle of intelligence, cost, and latency <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>. It's difficult to optimize for all three simultaneously <a class="yt-timestamp" data-t="00:16:27">[00:16:27]</a>.

The stakes and time sensitivity of the decision being made should drive optimization choices <a class="yt-timestamp" data-t="00:17:12">[00:17:12]</a>:
*   **Customer Support**: Latency is critical; a customer expects a response within 10 seconds <a class="yt-timestamp" data-t="00:16:42">[00:16:42]</a>. User experience (UX) solutions, like a "thinking box" or redirecting to another page, can help manage perceived latency <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.
*   **Financial Research Analyst Agent**: Latency is less critical if the decision made after the response is highly important, such as capital allocation <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a>.

### Fine-tuning
Fine-tuning is not a "silver bullet" and comes at a cost <a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a>. It can limit the model's reasoning in other fields outside the specific domain it was fine-tuned for <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>.

**Best Practices:**
*   Try other approaches first, especially if an evaluation set is not yet in place <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a>.
*   Have clear success criteria established in advance <a class="yt-timestamp" data-t="00:18:26">[00:18:26]</a>. Fine-tuning should only be pursued if the desired intelligence cannot be achieved otherwise <a class="yt-timestamp" data-t="00:18:30">[00:18:30]</a>.
*   Don't let the potential need for fine-tuning slow down the initial development of an [[AI in Workplaces | AI use case]] <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>. Explore other methods first, then swap in a fine-tuned model if necessary <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>.

### Other Methods for Improving Use Case Success
Beyond basic prompt engineering, various features and architectures can significantly impact the success of an [[Integration of AI in Business Operations | AI use case]] <a class="yt-timestamp" data-t="00:19:35">[00:19:35]</a>:
*   **Prompt Caching**: Can lead to significant cost reduction and speed increases without sacrificing intelligence <a class="yt-timestamp" data-t="00:19:52">[00:19:52]</a>.
*   **Contextual Retrieval**: Drastically improves the performance of retrieval mechanisms, feeding information to the model more effectively and reducing processing time <a class="yt-timestamp" data-t="00:20:04">[00:20:04]</a>.
*   **Citations**: An out-of-the-box feature <a class="yt-timestamp" data-t="00:20:09">[00:20:09]</a>.
*   [[Agentic enterprise and AI agents | Agentic Architectures]]: Important architectural decisions for more complex AI systems <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>.