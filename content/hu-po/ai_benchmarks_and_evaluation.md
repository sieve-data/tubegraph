---
title: AI benchmarks and evaluation
videoId: oQqOiwUhJkA
---

From: [[hu-po]] <br/> 

The latest OpenAI release, referred to informally as "Strawberry" or "01," has sparked considerable discussion due to its performance on various [[evaluation_of_ai_coding_through_benchmarks | benchmarks]] <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. While some perceive it as a significant advancement, others express skepticism, labeling it as "glorified Chain of Thought" <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

## The "Strawberry" Release and Benchmark Performance

The new OpenAI model, known as 01 (and its variants like 01 Preview and 01 Mini), reportedly outperforms GPT-4o on various [[evaluation_of_ai_coding_through_benchmarks | benchmarks]] <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. This success has led to claims of it being a "new scaling paradigm" <a class="yt-timestamp" data-t="01:05:01">[01:05:01]</a>. However, the exact nature of the model and its internal workings remain largely undisclosed by OpenAI <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

## Controversy: Glorified Chain of Thought?

A significant point of contention revolves around whether 01's improved performance is genuinely due to novel [[model_training_and_evaluation_methods | model training and evaluation methods]] or simply an advanced application of "Chain of Thought" prompting <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. Critics argue that OpenAI is presenting a known technique as a revolutionary breakthrough <a class="yt-timestamp" data-t="01:06:46">[01:06:46]</a>.

This contention is fueled by past incidents, such as an "AI grifter" achieving high benchmark scores by combining an existing Anthropic model (Sonnet 3.5) with extensive prompt engineering and Chain of Thought <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. The discrepancy in public reaction—praise for OpenAI versus criticism for others using similar techniques—highlights a perceived double standard <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

## Test Time Computation and Chain of Thought

A core concept underlying 01's performance is "test time computation" <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>. This refers to the additional compute allocated during evaluation or inference to improve a model's output <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>.

Older research from January 2023 demonstrated that "Chain of Thought prompting," which elicits complex multi-step reasoning through step-by-step answers, significantly improves large language model performance <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>. This technique allows models to "think" internally, using more computational resources to arrive at a better answer <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>.

OpenAI acknowledges that 01 generates "internal reasoning tokens" that exceed the number of tokens visible to the user, consuming more total compute <a class="yt-timestamp" data-t="00:24:31">[00:24:31]</a>. These internal tokens may involve abstract "action tokens" (e.g., "use a calculator," "think step-by-step") that compress reasoning steps, potentially reducing context length and allowing for more efficient internal processing <a class="yt-timestamp" data-t="00:24:52">[00:24:52]</a>.

### Tree Search and Monte Carlo Tree Search (MCTS)

Advanced methods like Beam Search and Look-Ahead Search (which build on "best of n" sampling) employ a "process-based reward model" (PRM) or verifier to evaluate intermediate steps in the Chain of Thought <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>. This allows the model to explore multiple reasoning paths and select the most promising one <a class="yt-timestamp" data-t="00:19:19">[00:19:19]</a>.

A more sophisticated approach, Monte Carlo Tree Search (MCTS), is used in games like Tic-Tac-Toe to simulate actions and explore potential future states, accumulating "search" to find optimal moves <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a>. This process involves discretizing states and actions, which is also applicable to language models due to their finite vocabulary of tokens <a class="yt-timestamp" data-t="00:22:01">[00:22:01]</a>.

## The Role of Reinforcement Learning (RL) in Model Improvement

Beyond just inference-time computation, a key differentiator for 01 might be its deep integration of Reinforcement Learning (RL) during [[model_training_and_evaluation_methods | model training and evaluation methods]] <a class="yt-timestamp" data-t="01:05:17">[01:05:17]</a>.

Traditional fine-tuning, such as Reinforcement Learning from Human Feedback (RLHF), relies on human preference data to align models, which can sometimes lead to models becoming "stupider" at core reasoning tasks <a class="yt-timestamp" data-t="00:47:35">[00:47:35]</a>. RLHF is likened to a "contextual bandit" approach, where the model learns preferences without necessarily understanding the objective <a class="yt-timestamp" data-t="00:59:53">[00:59:53]</a>.

However, "real RL," akin to the self-play mechanisms used in AlphaGo Zero, trains models by having them play against themselves, generating millions of simulated games or reasoning traces <a class="yt-timestamp" data-t="00:36:00">[00:36:00]</a>. This allows the model to identify winning strategies and backpropagate rewards through entire sequences of actions, leading to [[selfimprovement_in_ai_models | self-improvement in AI models]] and superhuman performance <a class="yt-timestamp" data-t="00:48:00">[00:48:00]</a>.

This "real RL" approach, particularly for domains with clear correct answers like math and coding, enables the generation of high-quality synthetic data for training <a class="yt-timestamp" data-t="00:50:09">[00:50:09]</a>. The belief is that even if this form of RL is only directly applicable to tasks with objective correctness (like [[evaluation_of_ai_coding_through_benchmarks | evaluating AI coding through benchmarks]]), the reasoning capabilities can transfer to other, more subjective tasks like writing <a class="yt-timestamp" data-t="00:51:47">[00:51:47]</a>.

## OpenAI's Secrecy and its Implications

OpenAI's decision not to disclose the model's size or show the raw Chain of Thought to users has raised concerns <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. They cite security and safety arguments for hiding the internal reasoning, claiming they monitor the Chain of Thought for signs of user manipulation <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>. However, critics suggest this secrecy serves anti-competitive purposes <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.

By withholding the Chain of Thought, OpenAI prevents others from easily "distilling" their model's intelligence <a class="yt-timestamp" data-t="01:15:15">[01:15:15]</a>. This practice, similar to how Vuna fine-tuned LLaMA on GPT-generated data, could allow open-source models to approach proprietary model performance without incurring the same massive computational costs <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. Hiding the internal reasoning also allows OpenAI to use an "un-lobotomized" base model for internal reasoning, and then apply a safety filter *after* the reasoning process, presenting a clean output to the user <a class="yt-timestamp" data-t="01:21:08">[01:21:08]</a>.

Another aspect of OpenAI's strategy involves subsidizing API usage, limiting responses to 30 per day <a class="yt-timestamp" data-t="01:12:23">[01:12:23]</a>. This loss-leading strategy is common among Silicon Valley startups to gain market dominance by making it difficult for competitors to match prices <a class="yt-timestamp" data-t="01:12:03">[01:12:03]</a>.

## Future Outlook: Superhuman Reasoning and Hardware Implications

The integration of RL suggests a shift in the distribution of computational resources in [[ai_algorithms_and_computational_constraints | AI algorithms and computational constraints]]. Previously, pre-training consumed the vast majority of compute, with RLHF (post-training) being a small fraction <a class="yt-timestamp" data-t="00:35:06">[00:35:06]</a>. With "real RL," the "green bar" of RL compute is expected to grow significantly, potentially rivaling the pre-training costs <a class="yt-timestamp" data-t="00:38:35">[00:38:35]</a>.

This shift will likely lead to specialized [[hardware_for_ai_training_and_deployment | hardware for AI training and deployment]] and data centers tailored for different parts of the pipeline: one for pre-training (GPU-intensive) and another for RL simulations (potentially more CPU-intensive for rollouts) <a class="yt-timestamp" data-t="00:30:58">[00:30:58]</a>. It could even enable inference to be performed on user devices, with the foundation model hosted centrally, while the inference-time compute (tree search, etc.) is handled locally <a class="yt-timestamp" data-t="00:32:04">[00:32:04]</a>.

The ability to train models with "real RL" on discrete, verifiable tasks like math and coding offers a path to "superhuman reasoning" <a class="yt-timestamp" data-t="00:48:48">[00:48:48]</a>. While the exact form of superhuman reasoning in language is unknown, like how AlphaGo's moves felt alien to human Go players, it is expected to transfer across domains <a class="yt-timestamp" data-t="00:49:11">[00:49:11]</a>. This represents a potential path not just to Artificial General Intelligence (AGI) but to Artificial Superintelligence (ASI) <a class="yt-timestamp" data-t="01:09:01">[01:09:01]</a>.

## Challenges and Limitations of Evaluation

A key challenge in [[benchmarking_ai_agents_with_osworld_and_web_arena | benchmarking AI agents with OSWorld and Web Arena]] and other complex tasks is the difficulty in reliably assigning rewards, especially for subjective domains like literature or philosophy <a class="yt-timestamp" data-t="00:51:06">[00:51:06]</a>. True RL requires a clear, automated feedback signal (like a win/loss in a game or correct/incorrect for code/math) that can be backpropagated through reasoning traces <a class="yt-timestamp" data-t="01:03:01">[01:03:01]</a>.

The "bitter lesson" in AI research suggests that complex, engineered solutions often yield to simpler, more scalable approaches with sufficient compute and data <a class="yt-timestamp" data-t="01:17:22">[01:17:22]</a>. While current progress involves increasingly complex systems like 01's combination of pre-training and RL, the ultimate trajectory might be models so powerful from massive pre-training alone that these additional complexities become unnecessary <a class="yt-timestamp" data-t="01:18:52">[01:18:52]</a>.

The secretive nature of OpenAI's models also poses a fundamental challenge to scientific reproducibility and verification <a class="yt-timestamp" data-t="01:34:52">[01:34:52]</a>. Without knowing the exact methods or having access to internal processes, independently validating benchmark claims becomes difficult <a class="yt-timestamp" data-t="01:35:05">[01:35:05]</a>.