---
title: Strategies for improving reasoning abilities in models through RL
videoId: Xk8FtcSlFxs
---

From: [[hu-po]] <br/> 

The field of artificial intelligence is increasingly focused on **test-time scaling**, which involves increasing the computational resources used during inference to enhance a model's accuracy [00:02:26], [01:26:47]. This approach is emerging as a new [[challenges_and_potentials_of_ai_in_language_and_reasoning_tasks | scaling law]], complementing traditional methods of increasing performance by scaling up training compute [01:27:05].

## Simple Test-Time Scaling

One straightforward demonstration of test-time scaling comes from the "Simple Test Time Scaling" (S1) paper. A relatively small S1 32B model was shown to exceed OpenAI's O1 Preview performance on competition math questions by up to 27% [00:03:35]. This significant improvement was achieved by simply modifying how the model uses its "thinking" tokens. By replacing the default "end of thinking" token with an "extra token weight," the model was forced to continue its reasoning process for a longer duration [00:04:07]. The research clearly showed a direct correlation: as the "average thinking time in tokens" increased, so did the accuracy [00:04:48]. This phenomenon is akin to the "let's think step by step" prompting technique, where instructing a model to articulate its reasoning process leads to better outcomes [00:05:02].

## Advanced Test-Time Strategies and Their Evolution

OpenAI's "Competitive Programming with Large Reasoning Models" paper further illustrates test-time scaling. It highlights that increasing compute at test time yields a more significant return on investment compared to increasing pre-training compute [00:09:27]. Scaling pre-training compute is capital-intensive, requiring massive data centers and GPU clusters [00:09:37]. In contrast, scaling test-time compute is easier, as it can be done at the edge, leveraging existing computational power on devices like cell phones or robots [00:10:18].

Early test-time strategies involved techniques like:
*   **Best-of-N**: The model generates 'N' responses, and a scoring or voting method selects the best one [00:15:58]. This often employs a "process reward model" (PRM) to evaluate potential paths [00:16:06].
*   **Beam Search**: A more sophisticated method where the model explores multiple paths simultaneously, looking ahead to find optimal sequences of tokens [00:16:27].
*   **Diverse Verifier Tree Search (DVTS)**: An even more advanced variant of beam search [00:17:18].

However, these human-engineered test-time strategies require "human intervention to define and implement these strategies" [00:22:08]. The research suggests that as models become larger and are fine-tuned with [[ai_and_reinforcement_learning | Reinforcement Learning]] (RL), the need for these explicit search strategies diminishes [00:22:55]. Larger models, especially those trained with [[ai_and_reinforcement_learning | RL]], appear to internalize these search abilities, effectively "baking in" the capacity to select the correct reasoning paths without external prompting or complex test-time compute strategies [00:20:54], [00:23:00]. This trend points towards a future where the inference pipeline is simplified due to more capable models [00:23:58].

## The Role of Reinforcement Learning (RL) in Reasoning

[[ai_and_reinforcement_learning | Reinforcement Learning]] plays a crucial role in enhancing reasoning abilities. Methods like Generalizable Reinforcement Learning from Human Feedback (GRPO) involve sampling numerous reasoning paths, identifying good and bad ones, and then using RL to reinforce the good paths while discouraging the bad ones [00:27:41]. This process makes the model inherently better at choosing the right path during inference, reducing the need for explicit beam search or other computationally intensive test-time methods [00:28:06].

### Distillation for Efficient Deployment

A key strategy for deploying intelligent models to edge devices (like cell phones) is distillation. Larger, powerful models that have undergone extensive [[ai_and_reinforcement_learning | RL]] training can distill their knowledge into smaller, more efficient models [00:30:27]. This allows for the deployment of highly intelligent models that can run on consumer hardware without requiring server racks [00:13:09], [00:14:59].

Distillation is "architecture agnostic" [00:31:48], meaning a large model with one architecture can distill its intelligence into a small model with a completely different, optimized architecture [00:32:05]. This allows companies to design models specifically for efficient serving on target hardware (e.g., TPUs, mobile phones) [00:32:47]. The vision is to have incredibly intelligent models running directly on a user's cell phone [00:15:03], with the intelligence derived from the "big models" trained with [[ai_and_reinforcement_learning | RL]] in giant data centers [00:33:05].

Furthermore, distillation is not limited to single models. An entire pipeline of multiple, specialized models (e.g., a reasoning model, a cat detection model, a segmentation model) can be distilled into a single, compact model optimized for inference [00:36:21], [00:39:14]. This suggests that complex, multi-modal capabilities could eventually be consolidated into efficient, on-device models.

## [[SelfImprovement in AI Models | Self-Improvement in AI Models]]

The concept of [[SelfImprovement in AI Models | self-improvement in AI models]] suggests that models can continually get smarter over time [01:28:26]. The "Self-Improving Transformers" paper demonstrates that a model can generate its own training data, filter it, and then train on the improved data [00:45:22]. This process leverages a phenomenon called "Transcendence," where a student model generalizes slightly beyond the difficulty of the data provided by its teacher [00:45:52].

Crucially, **filtering** is essential for this [[SelfImprovement in AI Models | self-improvement]] loop to succeed [00:53:30]. Without filtering, self-generated data degrades, leading to a "collapse in the self-improvement process" [00:53:31]. Filtering methods include:
*   **Length Filtering**: Removing outputs shorter than a threshold [00:51:01].
*   **Majority Voting**: Filtering data based on consensus among predictions from multiple models [00:51:07].

This mirrors the scientific method, where peer review (a form of majority voting) filters out less robust research, allowing future generations to train on higher-quality information [00:51:25]. This suggests that even without an external "reward signal" from the environment, collective intelligence derived from a group of models can provide a signal for improvement, allowing for [[Selfimproving AI through reinforcement learning and reasoning | self-improving AI through reinforcement learning and reasoning]] even in subjective domains like philosophy or poetry [00:55:09], [00:56:17].

## Beyond Token Space Reasoning

Current [[chain_of_thought_in_ai_reasoning | Chain of Thought]] (CoT) reasoning models primarily operate in "token space," where reasoning traces are sequences of words or sub-word units [00:58:10]. However, this limits the model's "thinking" to a discrete vocabulary [01:03:59].

New approaches propose **multimodal visualization of thought** and **latent space reasoning**:
*   **Multimodal CoT**: Models can use verbal thought to condition an image generation model, then integrate vision tokens derived from the generated images back into the reasoning chain [00:59:23]. This has shown improved performance in tasks like maze solving [01:00:01].
*   **Latent Space Reasoning**: In this advanced approach, models perform their internal reasoning entirely within a continuous, high-dimensional "latent space" rather than discrete tokens [01:03:16]. This allows for richer, less constrained reasoning processes [01:12:20].

Models employing latent space reasoning can achieve a greater "effective depth" during computation, potentially allowing for deeper reasoning than even the largest fixed-depth Transformers [01:17:16]. While harder to interpret (as the reasoning is not in human-readable tokens), latent space reasoning offers significant capacity for complex internal computations [01:12:02]. Examples of observed behaviors in latent space include trajectories converging to a fixed point, repeating loops, or "sliders" that drift in a specific direction, potentially for counting [01:13:38].

## Architectural Implications: RNNs/LSTMs vs. Transformers

The shift towards increased test-time compute has significant implications for model architectures. While Transformers excel in many tasks, their quadratic scaling of memory and compute with sequence length (due to the attention mechanism and KV cache) can be a bottleneck for very long reasoning traces [01:17:14], [01:20:09].

Recurrent Neural Networks (RNNs), Long Short-Term Memory networks (LSTMs), and Mamba architectures, in contrast, maintain a fixed-size memory ("hidden state"), leading to linear scaling with sequence length [01:17:42], [01:18:29]. This allows for "100 times more thinking" at inference time compared to attention-based models [01:19:34].

For edge devices like cell phones and robots, which have limited memory, the ability to perform extensive reasoning in a fixed-size latent space without exploding memory requirements makes recurrent architectures particularly attractive [01:21:09], [01:21:41]. This could mean future robots won't "word cell" their reasoning, but rather "latent weave" it [01:21:56].

Furthermore, recurrent depth networks (using recurrent blocks for latent reasoning) perform more floating-point operations per parameter, reducing communication costs between accelerators during training [01:22:36]. This can enable more efficient distributed training, potentially fostering decentralized systems rather than relying solely on giant data centers with very fast interconnects [01:24:30].

In summary, improving model reasoning through RL involves a multifaceted approach:
1.  **Extended Reasoning Traces**: Simply encouraging more "thinking" tokens.
2.  **RL-Baked Strategies**: Using [[ai_and_reinforcement_learning | RL]] to train models to inherently pick better reasoning paths, reducing reliance on complex external search algorithms.
3.  **Distillation**: Transferring intelligence from large, powerful models into small, efficient ones for widespread deployment.
4.  **[[SelfImprovement in AI Models | Self-Improvement Loops]]**: Allowing models to generate, filter, and train on their own outputs for continuous enhancement.
5.  **Latent Space Reasoning**: Moving beyond token-based thought to continuous, abstract reasoning spaces for greater capacity and efficiency.
6.  **Architectural Shifts**: Potentially favoring recurrent architectures like LSTMs for their linear scaling, enabling deeper reasoning on resource-constrained devices and in distributed training environments.

These strategies collectively pave the way for increasingly intelligent and widely deployable AI models.