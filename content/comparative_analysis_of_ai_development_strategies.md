---
title: Comparative analysis of AI development strategies
videoId: WLBsUarvWTw
---

From: [[dwarkesh | The Dwarkesh Podcast]]

This article analyzes different perspectives and strategies for artificial intelligence (AI) development, drawing insights from a discussion with Tamay Besiroglu and Ege Erdil, formerly of Epoch AI and now launching Mechanize, a company aiming to automate all work <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. The central theme revolves around contrasting approaches to achieving advanced AI, the timelines involved, and the primary drivers and bottlenecks in AI progress.

## Differing Perspectives on AI Progress

A fundamental divergence in AI development strategy stems from how progress itself is conceptualized and measured.

### The "Intelligence Explosion" Misconception
Tamay Besiroglu argues that the concept of an "intelligence explosion" is misleading, akin to calling the Industrial Revolution a "horsepower explosion" <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. While raw physical power increased during the Industrial Revolution, many other complementary changes in sectors like agriculture, transportation, law, finance, and urbanization were equally crucial for the acceleration of growth and technological change <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. Similarly, AI development will involve many interconnected moving parts beyond just increasingly "smart" AI systems <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. This perspective suggests a strategy focused on broader systemic advancements rather than a singular focus on raw intelligence. This is related to the idea of [[complementary_innovations_and_technological_progress]].

### Timelines to AGI and Automation
Besiroglu and Erdil project longer timelines for achieving Artificial General Intelligence (AGI) or full automation compared to many in San Francisco <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.
*   Tamay Besiroglu estimates a "drop-in remote worker replacement" around 2045 <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
*   Ege Erdil is slightly more bullish but concurs with longer timelines than common short-term predictions <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

They caution against simple extrapolation of recent rapid advances, noting that the fraction of the economy actually automated by AI is currently very small <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. If one were to extrapolate this small automated fraction, it would suggest centuries for full automation <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.

## Drivers of AI Development

Different strategies emerge from identifying different primary drivers of AI capabilities.

### Compute-Centric View and Its Limitations
A "compute-centric view" highlights that the last decade saw AI progress through approximately 9-10 orders of magnitude (OoM) of compute scaling <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>. This unlocked capabilities such as:
*   Advanced gameplay in complex games (e.g., Go, Chess, Dota) between 2015-2020 <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.
*   Sophisticated language capabilities, abstract reasoning, coding, and math <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.

Major capability "unlocks" historically occurred roughly every three years or every three OoM of compute scaling <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. Future desired capabilities include long-horizon coherence, agency, autonomy, and full multimodal understanding <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>. This approach corresponds with the [[ai_trajectory_and_scaling_hypothesis]]. However, this strategy faces limitations:
*   Only an estimated 3-4 OoM of compute scaling might be left before hitting significant constraints related to energy or GPU production <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. This is similar to the challenges discussed in [[data_center_energy_requirements_and_scaling]].
*   Current AI chip production is a small fraction of overall semiconductor manufacturing, even at the leading edge <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>, <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

### Algorithmic Progress and "Unhobblings"
Another perspective emphasizes algorithmic improvements and "unhobbling" existing models.
*   **"Unhobblings"**: This idea, attributed to Leopold, suggests current models are like "baby AGIs" constrained by artificial limitations (e.g., text-only training, lack of environmental context like Slack/Gmail, limited inference time) <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>. Removing these hobbles might be easier than developing entirely new capabilities.
    *   **Counter-argument**: AlphaZero couldn't simply be "unhobbled" by text training to achieve broader intelligence <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>. This relates to the discussions on [[alphazero_and_efficient_search_techniques]].
    *   **Supporting examples**: ChatGPT achieved chatbot competence with only 1% additional compute for post-training <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>. Reasoning capabilities in current models also emerged from a small fraction of total compute spent on RL <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>.
*   **The "Easy Looks Hard" Fallacy**: Erdil notes that while capabilities like reasoning seem "easy" now, achieving them required a massive prior build-up of technology over 5-10 years (e.g., training on tens of thousands of GPUs, internet-scale data, innovations in inference efficiency) <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>. Future capabilities like agency might appear simple in hindsight due to similar cumulative groundwork <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.

### The Role of Data and Real-World Interaction
A crucial, often underestimated, driver is the vast amount of data and interaction with the real world.
*   AI labs deploy LLMs widely (e.g., ChatGPT) to gather user data and feedback, which is vital for improvement <a class="yt-timestamp" data-t="01:10:32">[01:10:32]</a>.
*   The development of technologies like the lightbulb by Edison involved not just the core idea but extensive experimentation with materials and the simultaneous build-out of electrical infrastructure <a class="yt-timestamp" data-t="01:18:30">[01:18:30]</a>.
*   Progress often comes from a "learning by doing" approach, where deployment and iteration drive efficiency and new discoveries, as seen with solar panel technology <a class="yt-timestamp" data-t="01:16:32">[01:16:32]</a>. This is essential for addressing challenges in [[challenges_and_methodologies_in_ai_training_and_data_usage]].

## Bottlenecks in AI Development

Understanding potential bottlenecks is key to formulating effective development strategies.

### Complexity of Human-Level Tasks (Moravec's Paradox)
AI often excels at tasks humans find hard (e.g., abstract reasoning, complex games, math) <a class="yt-timestamp" data-t="00:17:18">[00:17:18]</a>, <a class="yt-timestamp" data-t="00:31:53">[00:31:53]</a>. These are often evolutionarily recent skills for humans <a class="yt-timestamp" data-t="00:32:59">[00:32:59]</a>. Conversely, AI struggles with tasks humans find easy.
*   Current models reportedly cannot reliably perform tasks like booking a flight <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. This is part of the broader [[limitations_of_large_language_models_llms_in_solving_novel_tasks]].
*   Many jobs are far more complex than a single, easily automatable task; for example, travel agents do more than just book flights and hotels <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.
*   AI systems, like Claude playing Pokémon, might possess explicit knowledge from training data but fail to apply it effectively in dynamic situations, getting stuck for extended periods <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>, <a class="yt-timestamp" data-t="00:19:28">[00:19:28]</a>.
*   AI is still far from being able to play a generic, newly released game from Steam without prior specific training <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>, <a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>.

### Automating R&D
While current models are impressive coders and reasoners by human standards <a class="yt-timestamp" data-t="00:24:49">[00:24:49]</a>, automating AI R&D presents further challenges:
*   Real-world R&D involves vague instructions, large codebases, and creative problem-solving, unlike the well-defined tasks in evaluations like METR <a class="yt-timestamp" data-t="00:25:49">[00:25:49]</a>.
*   AI systems lack many general human competencies crucial for research <a class="yt-timestamp" data-t="00:26:35">[00:26:35]</a>.
*   A significant portion of software progress historically has been driven by compute scaling, not just cognitive effort <a class="yt-timestamp" data-t="00:27:01">[00:27:01]</a>. This reflects the importance of the [[role_of_compute_in_ai_development]].
*   Current advanced reasoning models, despite vast knowledge, are not typically creative and have not independently produced novel mathematical concepts interesting to human mathematicians <a class="yt-timestamp" data-t="00:29:55">[00:29:55]</a>, <a class="yt-timestamp" data-t="00:30:43">[00:30:43]</a>, <a class="yt-timestamp" data-t="00:31:19">[00:31:19]</a>.

### Economic and Infrastructural Constraints
Rapid AI development, especially involving physical hardware and broad deployment, faces real-world limitations:
*   The "Shenzhen in the desert" scenario (a dedicated zone for hyper-scaling AI production) would still rely on complex global supply chains (e.g., for semiconductors) and vast existing data troves (e.g., the internet accumulated over 30 years) <a class="yt-timestamp" data-t="01:09:03">[01:09:03]</a>, <a class="yt-timestamp" data-t="01:09:37">[01:09:37]</a>. This has connections to [[geopolitical_implications_on_technology_and_data_centers]].
*   Broad deployment across the existing economy is likely more efficient for data gathering and leveraging existing infrastructure <a class="yt-timestamp" data-t="01:10:18">[01:10:18]</a>. This correlates with [[challenges_and_opportunities_in_deploying_ai_at_scale]].
*   Regulation is a significant potential bottleneck. While international competition and the value of AI might push for adoption <a class="yt-timestamp" data-t="01:13:19">[01:13:19]</a>, global coordination to slow down or restrict certain AI developments (similar to human cloning) cannot be entirely ruled out <a class="yt-timestamp" data-t="02:45:24">[02:45:24]</a>, <a class="yt-timestamp" data-t="02:45:51">[02:45:51]</a>.
*   **Baumol's Cost Disease**: Sectors with slower productivity growth (potentially those harder to automate) can become bottlenecks, as their share of economic output increases <a class="yt-timestamp" data-t="02:38:17">[02:38:17]</a>. However, this needs quantitative specifics regarding which sectors and the elasticity of substitution <a class="yt-timestamp" data-t="02:39:42">[02:39:42]</a>. Human labor can also reallocate to non-automated sectors <a class="yt-timestamp" data-t="02:40:27">[02:40:27]</a>.
*   **O-Ring Effects**: If processes require many components to function (like an O-ring in a rocket), and one fails or doesn't scale, it can limit the whole system <a class="yt-timestamp" data-t="02:43:06">[02:43:06]</a>. However, if AI can replace human "zeros" in such chains, this might not be as limiting, or AI firms could form entirely new, more robust "O-ring" chains <a class="yt-timestamp" data-t="02:44:27">[02:44:27]</a>, <a class="yt-timestamp" data-t="02:44:53">[02:44:53]</a>.

## Strategies for Accelerating AI

Given these drivers and bottlenecks, distinct strategic approaches to accelerating AI emerge.

### The "Software-Only Singularity" Argument
This strategy posits that by automating AI R&D, AI systems can recursively improve their own software efficiency <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>, <a class="yt-timestamp" data-t="00:45:46">[00:45:46]</a>. This is akin to the concept of a [[recursive_selfimprovement_and_ai_capabilities]].
*   This creates a feedback loop: more efficient AIs lead to more AI researchers, which allows for cheaper and more parallel experiments, further accelerating capabilities. The ~100x cost reduction from GPT-4 to GPT-4o is cited as an example <a class="yt-timestamp" data-t="00:47:28">[00:47:28]</a>.
*   **Critique**: This view may underestimate:
    *   Diminishing returns to pure R&D effort <a class="yt-timestamp" data-t="00:48:50">[00:48:50]</a>.
    *   The strong complementarity between software/algorithmic progress and hardware/compute scaling. Historically, software progress rates often mirrored hardware progress (e.g., Moore's Law, then the deep learning compute acceleration) <a class="yt-timestamp" data-t="00:50:26">[00:50:26]</a>.
    *   Many key AI innovations (Transformer, Flash Attention, Chinchilla scaling laws) were driven by the need to better utilize available compute and were developed in GPU-rich environments <a class="yt-timestamp" data-t="00:51:06">[00:51:06]</a>.

### The Importance of Broad Economic Upgrading
Advocated by Besiroglu and Erdil, this strategy emphasizes that transformative AI will arise from a broad upgrading of the entire economy and its technological base, not just isolated breakthroughs in "intelligence."
*   It parallels the Industrial Revolution, where progress was a result of complementary innovations across many sectors <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
*   The goal of Mechanize is to accelerate this broad automation of all labor to unlock enormous wealth, new products (e.g., in healthcare), and a significantly higher quality of life <a class="yt-timestamp" data-t="02:13:08">[02:13:08]</a>, <a class="yt-timestamp" data-t="02:13:24">[02:13:24]</a>. This echoes the potential [[the_impact_of_ai_on_future_technology_and_society]].
*   This view considers the economic, infrastructural, and societal changes necessary to deploy and benefit from advanced AI.

### The Role of AI Firms and Collective Advantages
A significant shift in AI's impact could come from new organizational structures, termed "AI firms" <a class="yt-timestamp" data-t="00:42:34">[00:42:34]</a>, <a class="yt-timestamp" data-t="02:49:39">[02:49:39]</a>. This strategy focuses on leveraging AI's unique collective capabilities:
*   **Perfect Replication**: AI systems, including their tacit knowledge, can be copied flawlessly. This allows scaling expertise (e.g., the AI equivalent of a top engineer) instantly and maintaining organizational culture perfectly, unlike human firms which suffer from dilution, turnover, and mortality <a class="yt-timestamp" data-t="02:49:48">[02:49:48]</a>, <a class="yt-timestamp" data-t="02:50:09">[02:50:09]</a>.
*   **Incentive Alignment**: AI preferences can potentially be controlled and aligned with organizational goals, mitigating principal-agent problems common in human firms <a class="yt-timestamp" data-t="02:52:23">[02:52:23]</a>. This reflects the ongoing research into [[ai_alignment_and_safety_concerns]].
*   **Superior Information Processing**: Higher communication bandwidth and the ability to maintain a coherent vision across a vast organization (e.g., a "hyper-Jensen" model overseeing all operations) become possible <a class="yt-timestamp" data-t="02:53:07">[02:53:07]</a>, <a class="yt-timestamp" data-t="02:53:32">[02:53:32]</a>.
*   **Efficient Learning**: AI can learn once through a massive training run and then be deployed universally, avoiding the duplicated learning effort required by every human <a class="yt-timestamp" data-t="02:55:04">[02:55:04]</a>.
*   This could enable a faster evolutionary process for firms, as they would possess selection, variation, and high-fidelity replication <a class="yt-timestamp" data-t="02:50:52">[02:50:52]</a>.
*   The potential for more effective **central planning** within these AI firms (or even larger economic units) is debated. Arguments for include better communication, scalable "planner" intelligence, and improved incentive alignment <a class="yt-timestamp" data-t="02:55:23">[02:55:23]</a>. Counterarguments highlight the massively increased complexity of a larger, more advanced economy <a class="yt-timestamp" data-t="02:58:18">[02:58:18]</a>.

## Predicting and Navigating the Future

Given the transformative potential and the differing strategic outlooks, navigating the future of AI development requires careful consideration.

### Uncertainty and the Limits of Foresight
A strong theme is the profound epistemic uncertainty surrounding AI's trajectory and ultimate impact <a class="yt-timestamp" data-t="02:04:52">[02:04:52]</a>.
*   Detailed long-term plans made today are likely to become obsolete due to new information and unforeseen developments <a class="yt-timestamp" data-t="02:07:33">[02:07:33]</a>.
*   Historical analogies, like pre-WWII predictions about aerial bombardment casualties, show how inaccurate detailed forecasts about new technologies can be <a class="yt-timestamp" data-t="02:08:01">[02:08:01]</a>. The actual casualties were orders of magnitude lower than initial high-level predictions <a class="yt-timestamp" data-t="02:09:06">[02:09:06]</a>, <a class="yt-timestamp" data-t="02:11:12">[02:11:12]</a>.
*   This suggests a strategy of humility, emphasizing flexibility, adaptation, and robust institutions rather than rigid, detailed plans <a class="yt-timestamp" data-t="02:06:51">[02:06:51]</a>. Classical liberalism and decentralized decision-making are proposed as societal responses to such high uncertainty <a class="yt-timestamp" data-t="02:06:05">[02:06:05]</a>. This approach follows the principles outlined in [[decentralization_vs_central_planning_in_economics]].

### The Value of Acceleration vs. Caution
The debate over whether to accelerate AI development involves weighing immense potential benefits against risks.
*   **Arguments for acceleration**:
    *   Enormous economic growth, leading to unprecedented wealth and solutions to major problems like disease <a class="yt-timestamp" data-t="02:13:24">[02:13:24]</a>.
    *   Each year of delay incurs massive opportunity costs, estimated in tens of trillions of dollars in consumption and potentially hundreds of millions of lives lost that could have been saved <a class="yt-timestamp" data-t="02:15:01">[02:15:01]</a>, <a class="yt-timestamp" data-t="02:17:53">[02:17:53]</a>. These concerns are akin to the [[economic_growth_and_technological_acceleration]].
    *   It's unclear if slowing down development improves safety outcomes; continued scaling and research (including on alignment) are seen as necessary for progress <a class="yt-timestamp" data-t="02:16:03">[02:16:03]</a>, <a class="yt-timestamp" data-t="02:16:51">[02:16:51]</a>. Attempting alignment research with outdated compute (e.g., 2016 levels) would yield little progress <a class="yt-timestamp" data-t="02:16:32">[02:16:32]</a>.
*   **Considerations for caution**: While not extensively detailed as a counter-strategy in this discussion, the implicit concern is that rapid, unchecked development might increase risks if safety and alignment cannot keep pace. However, the speakers argue that the leverage to predictably affect the long-run future is low, even if higher now than in the past <a class="yt-timestamp" data-t="02:19:11">[02:19:11]</a>, and that the transition is likely to be diffuse rather than concentrated in a few labs, reducing idiosyncratic risks <a class="yt-timestamp" data-t="02:19:56">[02:19:56]</a>.

## Conclusion

The discussion with Besiroglu and Erdil highlights a strategic divergence in AI development. One path emphasizes targeted breakthroughs in "intelligence" and software, potentially leading to a "software-only singularity." The alternative, favored by the speakers, posits that truly transformative AI will emerge from a broader, systemic automation of labor, driven by the interplay of compute, algorithms, vast data, real-world deployment, and economic integration. This latter strategy acknowledges significant bottlenecks but sees them as addressable through comprehensive, economy-wide upgrading, rather than solely through advances in AI's cognitive capabilities. Both perspectives grapple with profound uncertainties, suggesting that flexibility, adaptation, and a focus on near-term, robustly beneficial actions are critical components of any AI development strategy.