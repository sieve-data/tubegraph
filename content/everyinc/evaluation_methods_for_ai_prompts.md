---
title: Evaluation methods for AI prompts
videoId: exzPO4hAD9s
---

From: [[everyinc]] <br/> 

Effective evaluation is a critical component of [[practical_approaches_to_ai | practical approaches to AI]] and prompt engineering. According to Jared, co-founder and CEO of PromptLayer, prompt engineering involves three core primitives: the prompt itself, the evaluation (eval), and the dataset [02:09:09]. While prompts can be automated, the evaluation dataset still needs to be built [02:13:58]. The core theory is that prompt engineering is about inputting domain knowledge into an LLM system [02:30:46].

## Challenges in AI Prompt Evaluation

A significant challenge in [[challenges_and_strategies_in_ai_evaluation | AI evaluation]] is that there isn't "one prompt that rules them all" for any given problem [03:19:09, 04:00:02]. For instance, an AI math tutor could have infinite solutions, making a single, universally effective prompt impossible [03:15:00]. This complexity is due to the inherent "computational irreducibility" of problems, where certain outcomes cannot be predicted without running the system [08:05:06, 09:16:17].

The best prompt engineers tend to treat Large Language Models (LLMs) as black boxes, focusing on mapping inputs to desired outputs rather than understanding the internal workings [02:42:00, 02:44:00]. If the desired outputs aren't achieved, it's often considered a skill issue, not a fundamental problem with the model [02:55:00].

Another challenge arises from the need for a perspective when collecting data and closing feedback loops [03:29:00]. Different approaches to data collection embody different worldviews, leading to varied results and behaviors [03:43:00]. Human domain experts develop a perspective over many "data gathering loops" that an AI might take a while to replicate [03:10:00].

Generic evaluation benchmarks are often unreliable because it's difficult to evaluate problems without a clear "ground truth" in a generic way [03:59:00, 33:00:00].

## Practical Evaluation Strategies

Jared suggests approaching prompt evaluation with the scientific method: try something, then fix it [02:47:00]. The focus should be on making the iteration loop as quick as possible [02:35:00, 02:46:00].

Key strategies include:
*   **Backtesting** The easiest approach for evaluations (the "80% case") is to backtest on old data [02:41:00]. Users can create a backtest using their last thousand or ten thousand prompt responses to see how much a new prompt changes the output [03:00:00]. This helps in identifying unexpected changes, even if it's just by eyeballing the differences [03:14:00].
*   **Ground Truth Data** If a "ground truth" exists, such as explicit user feedback (thumbs up/down) or real-world metrics (e.g., whether a sale was made or a ticket closed), AB testing can be employed [03:24:00, 03:37:00]. For example, in building an AI email summarizer, one could manually write desired summaries from their inbox to establish a baseline [03:52:00]. If ground truth is available, prompt engineering becomes straightforward, as it's a matter of achieving 100% accuracy [03:38:00].
*   **Heuristics and Human Graders** When ground truth is unavailable, such as with AI summarization, the prompt engineer needs to define heuristics by analyzing their own decision-making process when evaluating outputs [03:09:00, 03:24:00]. Human graders can also be used to read and assess outputs based on these heuristics [03:59:00]. For example, checking if an email summary avoids a specific "excerpt" at the bottom or if it uses the correct markdown formatting [03:05:00, 03:11:00].
*   **Synthetically Generating Data Sets** For datasets, especially when backtest data is not available, synthetically generating ground truth data sets can be a powerful way to bootstrap the process [03:48:00, 03:50:00].

## The Role of Domain Expertise in Evaluation

A significant insight is that organizations will "win" in the age of generative AI not by hiring the best ML engineers, but by collaborating with domain experts who can clearly define the problem and its specifications [02:52:00, 03:12:00]. For AI applications in fields like teaching, therapy, or law, engineers are not the ideal people to be in the "driver seat" of defining how the AI should respond [03:07:00].

PromptLayer found that a non-technical prompt engineer, such as a teacher with 15 years of experience, could effectively edit prompts based on their domain knowledge and observe immediate changes in the application [03:15:00, 03:26:00]. This highlights that prompt engineering is about closing the feedback loop and iterating quickly [02:42:00, 02:46:00].

Companies that are building revenue-generating products and putting teams behind them are realizing the need for non-technical domain experts [03:40:00, 04:40:00]. These teams often experience friction from handoffs to QA testers or legal experts, necessitating domain experts to directly fix prompt issues [04:48:00].

### Structuring Prompts for Better Evaluation

Instead of stacking messages in one monolithic prompt, a better approach is to build a workflow or a directed acyclic graph (DAG) of prompts, routing the user to the appropriate prompt [02:54:00, 03:04:00]. This "prompt router approach" ensures that each prompt does one thing well, making it easier to test, collaborate on, and build unit tests for [03:14:00, 03:29:00]. This structured approach also helps prevent "jailbreaking" by isolating functionalities [03:57:00].

While models may improve and require less routing over time, there's always a trade-off between flexibility and reliability [03:40:00, 03:45:00]. A single, comprehensive prompt offers high flexibility but risks more failures, whereas specialized prompts offer high reliability but less flexibility [03:05:00].

## Critique of General-Purpose AI Evaluations

General-purpose AI models like ChatGPT or Anthropic's Claude often have "bad" system prompts [04:57:00, 41:57:00]. These prompts are long and "run on," accumulating "prompt debt" by continuously adding conditions (e.g., "do this if they say this, don't say this") [04:27:00, 42:30:00]. This approach leads to prompts that are not clear and concise, essentially overfitting to numerous edge cases [04:51:00, 43:00:00]. The lack of a specific use case or defined evaluation metrics for these general models contributes to their suboptimal prompt design [04:22:00].

For general-purpose AI tools, a better approach might involve having different prompts for different types of interactions and routing requests accordingly, similar to how Snapchat's AI uses multiple models based on user queries [04:39:00, 04:48:00]. However, there are trade-offs between explicit routing (like selecting tools/plugins in earlier ChatGPT versions) and implicit routing (where the model internally manages the routing) [04:53:00, 04:42:00].