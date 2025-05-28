---
title: AI algorithms and computational constraints
videoId: Ii_7-wsTjLo
---

From: [[hu-po]] <br/> 

AI algorithms and their associated [[computational_challenges_in_training_large_models | computational challenges]] are central to the development of advanced models like DeepSeek-Math. The choices made in algorithm design, data utilization, and [[hardware_infrastructure_and_computational_challenges | hardware infrastructure]] significantly impact model performance, training efficiency, and overall cost.

## DeepSeek-Math and GRPO

DeepSeek-Math utilizes a specific variant of reinforcement learning called Group-wise Reward Policy Optimization (GRPO) <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. This algorithm, along with data and engineering effort, is considered key to the model's performance <a class="yt-timestamp" data-t="00:18:42">[00:18:42]</a>.

### PPO vs. GRPO: Algorithmic Differences

*   **PPO (Proximal Policy Optimization)**: PPO is a foundational reinforcement learning algorithm <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
    *   It typically samples a single observation (`o`) <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.
    *   PPO often relies on a learned value function (`V(s)`) model, which is typically a neural network of comparable size to the policy model <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>. This introduces substantial memory and [[computational_challenges_in_training_large_models | computational burden]] <a class="yt-timestamp" data-t="00:19:53">[00:19:53]</a> <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a>.
    *   The ratio of the current policy to the old policy (`Pi Theta / Pi Theta old`) is "clipped" between `1 - Epsilon` and `1 + Epsilon` to prevent erratic behavior during updates <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.
    *   A Beta Kullback–Leibler (KL) Divergence term helps prevent the policy from drifting too far from a reference policy (e.g., an SFT model) <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a> <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>.

*   **GRPO (Group-wise Reward Policy Optimization)**: GRPO introduces several [[challenges_and_innovations_in_ai_model_architecture_and_scaling | innovations]] to PPO:
    *   **Group Sampling**: Instead of a single observation, GRPO samples a group of `G` observations from the old policy <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a> <a class="yt-timestamp" data-t="00:19:17">[00:19:17]</a>.
    *   **Elimination of Value Function**: A key [[challenges_and_innovations_in_ai_model_architecture_and_scaling | innovation]] in GRPO is the removal of the separate value model <a class="yt-timestamp" data-t="00:20:36">[00:20:36]</a>. It uses group reward scores to compute advantage, effectively acting as a Monte Carlo estimate of the learned value function <a class="yt-timestamp" data-t="00:20:55">[00:20:55]</a>. This reduces memory and [[computational_challenges_in_training_large_models | computational burden]] <a class="yt-timestamp" data-t="01:08:14">[01:08:14]</a>.

### Reinforcement Learning Paradigms: On-Policy vs. Off-Policy

Reinforcement learning involves an agent (policy/neural net) interacting with an environment, receiving rewards that provide gradient updates to refine the policy <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>.

*   **On-Policy RL**: The gradient update is applied to the *same* policy that generated the observations <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.
*   **Off-Policy RL**: Observations are stored in a replay buffer, and policy updates can use examples from *older* policies <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. This can lead to complications if the experience-collecting policy is too "distant" from the policy receiving the updates <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.

## Computational Challenges and Optimizations

Training large AI models faces significant [[computational_challenges_in_training_large_models | computational challenges]], particularly concerning hardware availability and cost.

### Hardware Constraints

*   **GPU Poverty**: Running large-scale experiments, such as a single GRPO run on the full 70,000-example Num-Math-TI dataset using 8 H100 GPUs, would cost approximately $1,300 and take 56 hours <a class="yt-timestamp" data-t="00:33:45">[00:33:45]</a> <a class="yt-timestamp" data-t="00:33:57">[00:33:57]</a>. Smaller-scale experiments are necessary for those without significant GPU resources <a class="yt-timestamp" data-t="00:33:26">[00:33:26]</a>. Reducing the dataset size to 2,000 examples allows a run to complete in 42 minutes at a cost of $16 <a class="yt-timestamp" data-t="00:34:10">[00:34:10]</a> <a class="yt-timestamp" data-t="00:34:17">[00:34:17]</a>.
*   **GPU Interconnect**: While H800 and H100 GPUs have similar computational performance (Teraflops), the H100 has higher interconnect bandwidth, which affects how quickly GPUs can communicate <a class="yt-timestamp" data-t="00:59:30">[00:59:30]</a>.
*   **CUDA Compatibility Issues**: Issues with NVIDIA drivers and CUDA versions can lead to significant debugging time, which is perceived as unproductive work <a class="yt-timestamp" data-t="00:46:36">[00:46:36]</a> <a class="yt-timestamp" data-t="00:47:06">[00:47:06]</a>. Changing GPUs can exacerbate these [[hardware_infrastructure_and_computational_challenges | dependency and config hell]] issues <a class="yt-timestamp" data-t="01:37:25">[01:37:25]</a>.

### Efficiency Optimizations

DeepSeek's 40x cost reduction is attributed to an accumulation of many small tricks rather than a single innovation <a class="yt-timestamp" data-t="01:08:41">[01:08:41]</a> <a class="yt-timestamp" data-t="01:27:40">[01:27:40]</a>.
*   **Quantization**: Using lower precision data types like FP8 (f8 E4 M3) enables faster computation (e.g., 4,000 Teraflops vs. 67 Teraflops for FP32) <a class="yt-timestamp" data-t="01:22:56">[01:22:56]</a> <a class="yt-timestamp" data-t="01:23:06">[01:23:06]</a>. This is a "hardcore hack" from DeepSeek <a class="yt-timestamp" data-t="00:32:07">[00:32:07]</a>.
*   **Low-Level GPU Code**: DeepSeek engineers reportedly wrote better GPU code than NVIDIA's engineers by dropping down to PTX (NVIDIA's Assembly Language) <a class="yt-timestamp" data-t="00:52:06">[00:52:06]</a> <a class="yt-timestamp" data-t="01:00:44">[01:00:44]</a>. This allowed them to effectively turn H800s into H100s by increasing interconnect speed <a class="yt-timestamp" data-t="01:01:07">[01:01:07]</a>.
*   **Dedicated Inference GPUs**: Hugging Face's Open R1 implementation of GRPO uses one GPU for dedicated inference (faster generation) and the remaining GPUs for training <a class="yt-timestamp" data-t="00:44:13">[00:44:13]</a> <a class="yt-timestamp" data-t="00:44:21">[00:44:21]</a>.
*   **Increasing Prompt/Completion Lengths**: An increase in prompt and completion lengths in an active project often indicates progress, as longer reasoning chains can lead to more accurate answers <a class="yt-timestamp" data-t="00:45:00">[00:45:00]</a> <a class="yt-timestamp" data-t="00:45:12">[00:45:12]</a>.
*   **Hyperparameter Tuning on Smaller Models**: To save costs, hyperparameters are often tuned on smaller models, and the findings are then "zero-shot transferred" to full-size models <a class="yt-timestamp" data-t="00:37:54">[00:37:54]</a>.

## Implications for AI Development

### Data vs. Algorithms
The speaker suggests that the specific algorithm is not as crucial as the quality of the data and the engineering effort involved in training <a class="yt-timestamp" data-t="00:18:40">[00:18:40]</a> <a class="yt-timestamp" data-t="02:29:40">[02:29:40]</a>. Conflicting results between papers on optimal approaches (e.g., process vs. outcome supervision, or the need for a value model) suggest that no single algorithm is universally superior <a class="yt-timestamp" data-t="00:24:52">[00:24:52]</a> <a class="yt-timestamp" data-t="00:25:29">[00:25:29]</a>.

### Open Source and Decentralization
*   **Open Source Acceleration**: The open-sourcing of models and techniques (like DeepSeek's innovations) allows all AI players to move faster, accelerating overall progress in the field <a class="yt-timestamp" data-t="01:28:44">[01:28:44]</a> <a class="yt-timestamp" data-t="01:29:09">[01:29:09]</a>.
*   **Decentralized Training**: The future of AI training might involve decentralized systems, leveraging the combined [[hardware_for_ai_training_and_deployment | computational power]] of millions of personal devices worldwide, similar to Bitcoin's distributed network <a class="yt-timestamp" data-t="01:41:43">[01:41:43]</a> <a class="yt-timestamp" data-t="01:41:59">[01:41:59]</a>. This could eventually surpass corporate or national superclusters <a class="yt-timestamp" data-t="01:41:36">[01:41:36]</a>.
*   **Local AI Control**: Running AI models locally allows users to bypass censorship or restrictions imposed by API providers, ensuring individual control over their intelligence <a class="yt-timestamp" data-t="01:05:15">[01:05:15]</a>.

### Reasoning Models and Generalization
*   **Longer Reasoning Chains**: Reasoning models are encouraged to generate longer "thought processes" (sequences of tokens) before arriving at a final answer. This iterative thinking process often leads to more accurate results <a class="yt-timestamp" data-t="01:26:50">[01:26:50]</a> <a class="yt-timestamp" data-t="01:26:59">[01:26:59]</a>.
*   **Transfer Learning**: Superhuman performance in domains like math and coding (where reward signals are easily verifiable, often without human input) is expected to transfer to other disciplines, including philosophy, due to the underlying general reasoning capabilities developed <a class="yt-timestamp" data-t="01:31:42">[01:31:42]</a> <a class="yt-timestamp" data-t="01:32:02">[01:32:02]</a>.
*   **Simulation for Robotics**: Reinforcement learning with long-horizon generated data (e.g., through simulation) is posited to outperform imitation learning from teleoperation data in robotics. The idea is to train models extensively in simulation and then deploy them to the real world <a class="yt-timestamp" data-t="01:55:31">[01:55:31]</a> <a class="yt-timestamp" data-t="01:56:28">[01:56:28]</a>. This mirrors how superhuman Go performance was achieved entirely in simulation <a class="yt-timestamp" data-t="00:56:55">[00:56:55]</a>.

### Model Distillation
*   **Knowledge Transfer**: Model distillation involves using a larger, more capable "teacher" model to generate a dataset (input-output pairs). A smaller "student" model is then trained on this dataset to mimic the teacher's behavior <a class="yt-timestamp" data-t="01:14:03">[01:14:03]</a>.
*   **Efficiency**: While most efficient when using the teacher model's exact logits (probability distributions over tokens), distillation can still occur with only the final output word <a class="yt-timestamp" data-t="01:16:09">[01:16:09]</a> <a class="yt-timestamp" data-t="01:16:19">[01:16:19]</a>.
*   **Inherent Capacity**: The ability of smaller models to perform well after distillation suggests that they inherently possess the capacity for high intelligence; distillation helps them find the "magical combination of values for weights" more effectively than traditional training methods <a class="yt-timestamp" data-t="01:21:53">[01:21:53]</a>. Distillation is framed as a continuous, pervasive process within humanity itself <a class="yt-timestamp" data-t="01:19:18">[01:19:18]</a>.