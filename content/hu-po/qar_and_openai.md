---
title: QAR and OpenAI
videoId: vOA9JSDPJs0
---

From: [[hu-po]] <br/> 

QAR, or Q*, is a rumored algorithm or technique that has been extensively discussed within the AI community, particularly in relation to [[OpenAI and Consistency Models | OpenAI]]. It is believed to represent a "step function improvement" in the current state of artificial intelligence <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>. While shrouded in mystery, leading AI researchers like [[Meta AI research | Yann LeCun]] suggest that QAR is likely [[AI and Reinforcement Learning | reinforcement learning]] combined with planning, concepts that have been explored for decades in [[Open source contributions in AI research | AI research]] <a class="yt-timestamp" data-t="04:04:00">[04:04:00]</a>.

## The Mystery of QAR

The topic of QAR generated significant hype and speculation, with numerous headlines questioning its nature and implications <a class="yt-timestamp" data-t="03:09:00">[03:09:00]</a>. Sam Altman, CEO of [[OpenAI and Consistency Models | OpenAI]], has reportedly shut down questions about QAR, fueling the mystery <a class="yt-timestamp" data-t="03:18:00">[03:18:00]</a>. However, [[Meta AI research | Yann LeCun]] dismisses much of the discussion as "complete nonsense," asserting that top labs, including [[Meta AI research | Facebook AI Research]] (Meta), [[Open source deep seek and deep reinforcement learning | DeepMind]] (Google), and [[OpenAI and Consistency Models | OpenAI]] (Microsoft), are actively working on similar ideas, some of which have already been published <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>.

The "Q" in QAR almost certainly refers to the [[AI and Reinforcement Learning | Q-function]] in [[AI and Reinforcement Learning | reinforcement learning]], which estimates the optimal future reward for taking a specific action in a given state <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>, <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>. The "star" (Q*) denotes the *optimal* Q-function <a class="yt-timestamp" data-t="01:10:46">[01:10:46]</a>. There is also a speculative theory that the star might refer to A* (A-star), a popular search algorithm, suggesting a combination of Q-learning with A* search <a class="yt-timestamp" data-t="01:11:16">[01:11:16]</a>.

## Core Concepts Behind QAR

The underlying idea of QAR, as hinted by research, is the application of [[AI and Reinforcement Learning | reinforcement learning]] (RL) and planning techniques to large language models (LLMs).

### Reinforcement Learning and LLMs
[[AI and Reinforcement Learning | Reinforcement learning]] aims to maximize expected cumulative reward within a Markov Decision Process (MDP) <a class="yt-timestamp" data-t="02:40:54">[02:40:54]</a>. An LLM can be conceptualized as a function approximator and a policy operating in an autoregressive manner within an MDP <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>. Each token output by an LLM can be considered an action, and the sequence of tokens forms a trajectory <a class="yt-timestamp" data-t="02:39:00">[02:39:00]</a>.

Traditionally, LLMs are trained using self-supervised learning (e.g., next-token prediction on large text datasets) and then fine-tuned with supervised learning on high-quality human-annotated data (e.g., instruction tuning) <a class="yt-timestamp" data-t="05:52:00">[05:52:00]</a>, <a class="yt-timestamp" data-t="09:11:00">[09:11:00]</a>. [[AI and Reinforcement Learning | Reinforcement learning]] is seen as the "cherry on top" of this process, adding a crucial layer for advanced capabilities <a class="yt-timestamp" data-t="05:24:00">[05:24:00]</a>.

### Challenges in Applying RL to LLMs
Applying [[AI and Reinforcement Learning | reinforcement learning]] to LLMs faces several challenges:
*   **Vast Search Space:** Unlike games like Go (which has a large but manageable search space), natural language has an exceedingly large action space (e.g., 30,000 possible tokens at each step), leading to an exponential expansion of the search tree <a class="yt-timestamp" data-t="01:45:00">[01:45:00]</a>, <a class="yt-timestamp" data-t="01:50:00">[01:50:00]</a>.
*   **Data Scarcity:** It's difficult to find expert-level data for language tasks compared to games like Go <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>.
*   **Subjective Feedback:** Unlike a clear win/loss in a game, evaluating the quality of a natural language response is often fuzzy and subjective, making it hard to obtain a precise reward signal <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a>.

### Monte Carlo Tree Search (MCTS)
Monte Carlo Tree Search (MCTS) is a sampling-based search algorithm commonly used in game-playing AI (e.g., AlphaGo). It involves four phases: selection, expansion, evaluation, and backpropagation <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a>. MCTS explores potential moves through statistical sampling of the search space <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>. Applying this to LLMs requires adapting the granularity of actions (e.g., option-level instead of token-level actions) to manage the vastness <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>.

### Critics and Reward Models
In [[AI and Reinforcement Learning | reinforcement learning]], "critics" (also known as value functions or reward models) estimate the "goodness" or value of a particular state or sequence of actions <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>. Two types are commonly discussed:
*   **Process Reward Model (PRM):** Provides feedback for each step in a Chain of Thought or trajectory <a class="yt-timestamp" data-t="04:54:00">[04:54:00]</a>.
*   **Outcome Reward Model (OMM):** Provides feedback only on the final result of a trajectory <a class="yt-timestamp" data-t="04:53:00">[04:53:00]</a>.
These critics, or value functions, can themselves be initialized from pre-trained language models <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>.

### Direct Preference Optimization (DPO)
DPO is an [[AI and Reinforcement Learning | RLHF]] method that treats the entire model response as a single "arm" in a multi-armed bandit problem <a class="yt-timestamp" data-t="01:17:30">[01:17:30]</a>. Research suggests that DPO, when interpreted at the token level, is effectively the [[AI and Reinforcement Learning | Q-learning algorithm]] and satisfies the Bellman equation, enabling credit assignment <a class="yt-timestamp" data-t="01:20:12">[01:20:12]</a>.

## Key Research Papers on Self-Improvement and Q-Functions

Two recent papers, both released on April 18, 2024, shed light on the potential nature of QAR:

### 1. Toward Self-Improvement of LLMs via Imagination Searching and Criticizing
*   **Authorship:** Tencent AI Lab <a class="yt-timestamp" data-t="06:43:00">[06:43:00]</a>.
*   **Concept:** Introduces "AlphaLLM," a framework inspired by AlphaGo's self-learning loop, applied to LLMs <a class="yt-timestamp" data-t="10:24:00">[10:24:00]</a>. AlphaLLM allows LLMs to refine outputs and learn from self-assessed rewards <a class="yt-timestamp" data-t="10:01:00">[10:01:00]</a>.
*   **Methodology:**
    *   Uses MCTS decoding, where the model looks ahead and evaluates potential token sequences (options) rather than just greedily picking the next token <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>.
    *   Employs an "option-level MCTS" where actions can be variable-length sequences of tokens, determined by a "termination function" <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>.
    *   Integrates multiple critics (PRM, OMM, value function) to guide the search for high-quality trajectories <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>.
    *   Uses a "fast rollout policy" (a smaller, specialized LLM) for rapid simulation within the search tree, coupled with importance-based filtering to avoid redundant branches <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>.
    *   The self-improvement loop involves data generation (via MCTS) and policy fine-tuning, iteratively collecting higher-quality synthetic data to train the LLM <a class="yt-timestamp" data-t="05:45:00">[05:45:00]</a>.
*   **Results:** AlphaLLM, starting from [[Open source AI models and accessibility | Llama 2 70B]], showed drastic improvements on mathematical reasoning problems like GSM8K (57% to 92%) and Math (20% to 51%) <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>, achieving performance comparable to [[OpenAI and Consistency Models | GPT-4]] *when MCTS is used during inference* <a class="yt-timestamp" data-t="01:03:30">[01:03:30]</a>.
*   **Limitations:** The self-improvement loop was only demonstrated for two iterations, raising questions about its long-term stability and whether performance degrades in subsequent iterations <a class="yt-timestamp" data-t="01:04:47">[01:04:47]</a>. The critics remained static during training, and the model's performance without MCTS decoding was substantially inferior <a class="yt-timestamp" data-t="01:06:39">[01:06:39]</a>.

### 2. From R to Q*: Your Language Model is Secretly a Q Function
*   **Authorship:** Stanford University, advised by Chelsea Finn <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a>.
*   **Concept:** This theoretical paper argues that the practices of [[AI and Reinforcement Learning | reinforcement learning]] and LLM training, particularly DPO, are fundamentally equivalent <a class="yt-timestamp" data-t="01:25:00">[01:25:00]</a>. It claims that an LLM is always the optimal soft Q function for some reward function in the token MDP <a class="yt-timestamp" data-t="01:28:26">[01:28:26]</a>.
*   **Justification:** The paper provides theoretical justifications for empirically observed DPO training phenomena, such as the unexpected decrease in the likelihood of chosen responses over time, by reframing LLMs and DPO within the context of maximum entropy [[AI and Reinforcement Learning | reinforcement learning]] <a class="yt-timestamp" data-t="01:37:00">[01:37:00]</a>.
*   **Implications:** The paper shows that simple beam search yields meaningful improvements over base DPO policies, mirroring the results of the Tencent paper <a class="yt-timestamp" data-t="01:20:00">[01:20:00]</a>. This suggests that LLMs can learn "credit assignment" directly from feedback data <a class="yt-timestamp" data-t="01:32:59">[01:32:59]</a>, which is crucial for generalizing from offline data and has significant implications for [[AI and Reinforcement Learning | robotics]] <a class="yt-timestamp" data-t="01:34:00">[01:34:00]</a>.

## The Broader Implications: QAR and Embodied AI

The ability to apply these self-play and planning strategies effectively relies on having a clear and unambiguous reward signal. This is why the demonstrated successes are primarily in domains like math and coding, where answers are objectively correct or incorrect <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>.

However, the true breakthrough of QAR, if the hype is real, would be the ability to extend this self-play loop and value function learning to more generic natural language reasoning, beyond math and programming <a class="yt-timestamp" data-t="00:45:00">[00:45:00]</a>. This would mean generating synthetic language datasets that are "better" than human expert datasets, a concept that is difficult to define but potentially transformative <a class="yt-timestamp" data-t="00:56:00">[00:56:00]</a>.

Furthermore, these concepts are highly applicable to [[AI and Reinforcement Learning | robotics]] and embodied AI. If a robot's actions can be represented as discrete "action tokens," and the success of its tasks can be objectively evaluated (e.g., "did it grab the object or not?"), then the same self-play loops could enable superhuman robot performance <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>. The recent trend of top AI talent leaving major companies like Google to found humanoid robot companies suggests a strong belief in the imminent realization of such capabilities <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>.

In essence, QAR likely represents the convergence of advanced [[AI and Reinforcement Learning | reinforcement learning]] techniques, specifically planning and value function learning, with the powerful capabilities of large language models. The key challenge remains how to generate reliable reward signals for complex, open-ended natural language tasks, a problem that, if solved by [[OpenAI and Consistency Models | OpenAI]], could indeed lead to a monumental leap in AI capabilities.