---
title: Role of compute and infrastructure in the future of AI development
videoId: 64lXQP6cs5M
---

From: [[dwarkesh | The Dwarkesh Podcast]]

The development and future trajectory of artificial intelligence (AI) are inextricably linked to the availability, cost, and efficiency of computational resources and the underlying infrastructure. Discussions from a recent podcast episode featuring Sholto Douglas and Trenton Bricken from Anthropic shed light on the critical interplay between compute power, algorithmic progress, and strategic decision-making in the AI landscape.

## Current State and Trends in AI Compute

### Compute Allocation and Spending
A significant theme is the strategic allocation of compute resources. While base model pre-training consumes hundreds of millions of dollars, Reinforcement Learning (RL) has historically received a smaller fraction, on the order of millions [00:11:10]. This is partly due to a cautious approach: ensuring algorithms are robust before committing to large-scale compute spends, likening it to choosing the right time to launch a technologically advanced space mission [00:11:13]. However, this is changing, with all major labs now scaling up their RL compute efforts [00:12:17]. OpenAI, for instance, reportedly used a 10x compute multiplier for RL between its o1 and o3 models [00:11:59].

The amount of compute invested in training is seen as a "decent proxy for the amount of actual raw new knowledge or capabilities" added to a model [00:10:14]. Currently, the industry trend shows companies spending more on compute than on human data labeling, evidenced by the disparity in revenues between compute providers like NVIDIA and data labeling services like Scale AI [00:20:58].

### Efficiency Gains and Cost Curves
Remarkable efficiency gains in training AI models have been observed. DeepSeek, for example, was able to train a model competitive with Anthropic's Claude 3 Sonnet (which was released nine months prior) for a significantly lower cost (around $5 million) by leveraging these accrued efficiencies [01:24:38], [01:24:50]. This indicates that newer models can benefit from the optimized cost curves established by earlier efforts [01:25:14].

### Algorithmic Design and Hardware Co-evolution
There's a deep connection between algorithmic design and the hardware systems they run on. DeepSeek's research, for instance, demonstrates an understanding of this "dance between the hardware systems...and the algorithmic side" [01:25:50]. Their architectural choices, such as moving from Multi-Head Latent Attention (MLA) to Neighborhood Self-Attention (NSA), illustrate a direct response to hardware constraints like memory bandwidth and the impact of export controls on high-performance chips [01:26:24], [01:26:48]. This co-evolution is crucial for pushing the boundaries of model capabilities.

### Model Scale vs. Human Brain
Current AI models, despite their advancements, are still considered smaller in parameter count than the human brain. For example, a 2 trillion parameter model like Llama is compared against estimates of 30 to 300 trillion synapses in the human brain [00:23:19]. This suggests that models are often "under-parametrized" and forced to cram information, a concept explored in interpretability work on superposition [[superposition_and_feature_representation_in_neural_networks]] [00:23:51].

## Future Compute Bottlenecks and Limitations

### The "Inference Bottleneck"
A major anticipated challenge is the "inference bottleneck" [01:20:05]. As AI models become more capable and widely deployed (e.g., for automating white-collar work [[ais_economic_impact_and_the_future_of_whitecollar_work_automation]] [01:19:04]), the demand for compute to run these models (inference) will skyrocket.
Current estimates suggest around 10 million H100-equivalent GPUs exist, potentially rising to 100 million by 2028 [01:19:22]. If an H100 has roughly the same flops as a human brain [01:19:28], and can process tokens much faster (e.g., an H100 running a 100B model at 1,000 tokens/sec versus human thinking at ~10 tokens/sec [01:21:10], [01:21:31]), this implies a significant increase in available "thinking power." However, this rapid increase in demand is expected to lead to a dramatic inference bottleneck around 2027-2028 [[the_timeline_and_technological_progress_towards_agi_by_2027]] [01:22:31].

### Wafer Production and Fab Capacity
The ability to scale compute is fundamentally limited by semiconductor manufacturing capabilities [[semiconductor_industry_and_trade_secrets]]. It's projected that by 2028, AI development might hit wafer production limits [01:19:57]. While GPUs currently represent a relatively small fraction (around 5%) of the total semiconductor supply chain [01:20:26], significantly ramping up production from facilities like TSMC takes time and massive investment [01:20:14].

### Energy Demands
Underpinning all compute is energy. If intelligence becomes a raw input into economies, then energy is the resource directly beneath it [02:02:37]. Forecasts suggest a significant disparity in energy production growth between nations like the US and China, with the US needing substantial increases in power generation capacity to support AI's future demands [02:02:12], [02:02:26]. Large-scale renewable energy projects, like "tiling the desert with solar panels," are mentioned as necessary steps [[energy_transitions_and_renewable_energy_challenges]] [02:02:40].

### The "This Decade or Bust" Scenario
The combination of escalating compute requirements for further progress (historically, reasoning breakthroughs required orders of magnitude more compute [01:23:19]) and the aforementioned physical limitations (chips, power, even raw GDP [01:23:27]) leads to a "this decade or bust" hypothesis [[ai_trajectory_and_scaling_hypothesis]] [01:23:49]. This suggests a critical window in the coming years where significant training compute increases are still feasible, after which progress might slow if breakthroughs aren't achieved.

## Role of Compute in Reinforcement Learning (RL)

### Scaling RL Compute
RL is considered particularly exciting because of the current ability to "dramatically increase the amount of compute" applied to it [01:23:56]. Dario Amodei was quoted as saying, "We aren't in the compute limited regime for RL yet, but we will be soon" [00:11:04]. The progress in RL is tied to having sufficient compute and the right algorithms [00:10:48].

### Compute vs. Scaffolding in RL
There's an ongoing optimization between investing in compute versus human effort for scaffolding and curriculum design for RL tasks [00:19:43]. While dense rewards and detailed curricula are beneficial, they are expensive to create. The alternative is to "keep letting the monkey hit the typewriter" if an end reward is good enough, relying on more compute to find solutions [[reinforcement_learning_rl_in_language_models_and_its_impact_on_software_engineering]] [00:19:55].

### Optimizing RL Compute
The cost of inference during RL training is a critical factor. The choice of model size for RL involves a trade-off: smaller models are faster to run but less capable, while extremely large models are slow, making their learning efficiency gains potentially not worth the inference cost [02:14:06], [02:14:28]. The calculus for allocating flops has evolved from merely training data vs. model size, to now heavily including the inference compute budget for RL and strategies like sampling multiple solutions [02:15:05], [02:15:16].

## Adaptive Compute and Model Architectures

### End-to-End vs. Bi-level Systems
There's a preference for "end-to-end maxi" systems, meaning a single, large model that handles all aspects of a task, rather than bi-level systems (e.g., a high-level planner and a separate motor policy in robotics [01:12:12]). The argument is that, eventually, a single large model, if trainable, offers better integration and scaling of understanding [[ai_systems_and_planning_mechanisms]] [01:12:54].

### Variable Compute
The concept of variable compute, where a model uses only the necessary amount of computation for a given task or token, is important for efficiency. Models already exhibit "variable compute per answer" [01:13:42]. The residual stream and multiple layers in Transformers are described as a "poor man's adaptive compute," where simpler parts of a problem might be resolved in earlier layers [[understanding_and_leveraging_long_context_lengths_in_llms]] [01:13:50]. This dynamic allocation is key as inference costs for large models producing many tokens can be substantial [01:17:48].

## Geopolitical and Economic Implications

### Compute as a Strategic Resource
In a future where AI capabilities are significantly advanced, "compute becomes the most valuable resource in the world" [01:58:53]. A nation's GDP could be dramatically affected by the amount of compute it can deploy [[impact_and_future_of_ai_in_economic_systems]] [01:58:56].

### National Strategies for Compute and Energy
Countries are advised to secure "guaranteed amount of compute" through investments in data centers and ensuring access for domestic companies, even if just for inference, which is where much economic value is expected to derive [01:59:05], [01:59:22]. A "dramatic allocation of resource towards compute" is considered sensible for nation-states to increase future optionality [02:02:01]. This is closely tied to energy policy, emphasizing the need for massive scaling of power generation [[data_center_energy_requirements_and_scaling]] [02:02:37].

## Open Problems and Career Advice

### Performance Engineering
A critical skill area highlighted is "performance engineering" [02:22:24]. Creating extremely efficient Transformer implementations on various hardware (TPUs, Trainium, CUDA) is highly valued [02:22:35]. Deep expertise in this area provides valuable intuitions for model architecture design, as intimate knowledge of hardware trade-offs informs algorithmic choices [[innovations_and_challenges_in_ai_hardware]] [02:23:07], [02:23:20]. There's a relatively small pool of people who can own the end-to-end performance of a model [02:22:47].

In conclusion, compute and infrastructure are not merely enabling factors but are central to the pace, direction, and ultimate impact of AI development, influencing everything from algorithmic breakthroughs to global economic shifts [[impact_of_ai_on_future_technology_and_society]].