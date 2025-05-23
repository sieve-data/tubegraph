---
title: Evolutionary biology and AI parallels
videoId: _kRg-ZP1vQc
---

From: [[dwarkesh | The Dwarkesh Podcast]]

Here is the modified article:

Carl Shulman, in a podcast discussion, explored numerous parallels between evolutionary biology and the development of Artificial Intelligence (AI), particularly concerning the trajectory towards and potential characteristics of Artificial General Intelligence (AGI). These analogies offer frameworks for understanding AI scaling, constraints, and potential reward system behaviors.

## The Brain as an Existence Proof and Evolutionary Search

Shulman notes that the human brain serves as a physical, information-processing device created by evolution, demonstrating that intelligence is possible <a class="yt-timestamp" data-t="00:39:21">[00:39:21]</a>. Evolution itself can be seen as a form of "intensive massive brute force search" that successfully produced intelligence <a class="yt-timestamp" data-t="00:39:35">[00:39:35]</a>. The existence of sophisticated intelligence in other species, like octopi, points to convergent evolution, suggesting intelligence is not a complete freak accident <a class="yt-timestamp" data-t="00:39:59">[00:39:59]</a>. While neuroscience could theoretically serve as a "backstop" for AI development by reverse-engineering the brain, current AI progress is not primarily driven by neuroscience; rather, AI develops new capabilities, and then parallels to neuroscience may be observed, much like airplanes were inspired by birds but don't flap their wings <a class="yt-timestamp" data-t="01:01:37">[01:01:37]</a>, <a class="yt-timestamp" data-t="01:02:03">[01:02:03]</a>, <a class="yt-timestamp" data-t="01:02:18">[01:02:18]</a>.

## Scaling Intelligence: Biological and Artificial Parallels

A core theme is the idea of scaling, both in biology and AI.

### Brain Size, Training Time, and Algorithmic Progress
Drawing on the work of neuroscientist Suzana Herculano-Houzel, Shulman explains that the human brain can be understood as a scaled-up primate brain, with predictable changes in neuron numbers and brain region sizes <a class="yt-timestamp" data-t="00:40:52">[00:40:52]</a>, <a class="yt-timestamp" data-t="00:41:18">[00:41:18]</a>. Much of human uniqueness can be attributed to a "brute force story":
*   **Larger "model size":** Humans have brains more than three times larger than chimpanzees <a class="yt-timestamp" data-t="00:42:00">[00:42:00]</a>.
*   **More "training time":** Humans have an unusually long childhood for learning <a class="yt-timestamp" data-t="00:41:54">[00:41:54]</a>, <a class="yt-timestamp" data-t="00:42:08">[00:42:08]</a>.
This is analogous to AI models, where consistent benefits and qualitatively new capabilities emerge from increasing compute spent on larger models and more training data <a class="yt-timestamp" data-t="00:42:26">[00:42:26]</a>. Many "fundamental limitations" previously claimed for AI have been overcome through scaling [[ai_scalability_and_breakthroughs]] <a class="yt-timestamp" data-t="00:42:40">[00:42:40]</a>.

### Chinchilla Scaling and Biological "Undertraining"
The "Chinchilla scaling laws" from AI research (which suggest optimal data amounts for a given model size) <a class="yt-timestamp" data-t="00:52:27">[00:52:27]</a> offer an interesting lens for biology. Shulman suggests that, according to these principles, a brain of human size would optimally require "many millions of years of education" <a class="yt-timestamp" data-t="00:53:34">[00:53:34]</a>. This is impractical for humans due to exogenous mortality. Consequently, animals are likely "systematically way undertrained" compared to how AI might be trained <a class="yt-timestamp" data-t="00:53:54">[00:53:54]</a>. The cost of extending childhood (training time) for animals increases exponentially due to predation and disease risk <a class="yt-timestamp" data-t="00:53:11">[00:53:11]</a>, whereas increasing GPU time for AI training has a more linear cost [[data_center_energy_requirements_and_scaling]] <a class="yt-timestamp" data-t="00:53:23">[00:53:23]</a>.

## Constraints on Biological Intelligence Not Applicable to AI

AI development is largely free from many harsh constraints that shape biological intelligence.

### Metabolic and Survival Costs
Biological organisms face trade-offs where the energy cost of a larger brain may not be worth the fitness benefit <a class="yt-timestamp" data-t="00:43:18">[00:43:18]</a>. AI models, however, are not subject to predation if they "spend too much time becoming more intelligent" <a class="yt-timestamp" data-t="00:51:36">[00:51:36]</a>. They are explicitly trained for intelligence within a "technological culture" where cognitive output is valued, unlike natural environments where resources must also be allocated to immune systems, digestion, or physical prowess <a class="yt-timestamp" data-t="00:52:08">[00:52:08]</a>.

### Exogenous Mortality
The high probability of death from predation or disease for young animals makes long developmental periods (and thus, extensive learning) extremely costly. A 50% chance of dying every few months means extending childhood from three to 30 months incurs not a 10x cost but a 2<sup>-10</sup> (1/1024) reduction in the benefit realized, as most individuals would die before completing development <a class="yt-timestamp" data-t="00:45:09">[00:45:09]</a>, <a class="yt-timestamp" data-t="00:45:29">[00:45:29]</a>. AI does not face this constraint.

## The Human Niche and Limits to Biological Intelligence

Humans occupy a unique self-reinforcing niche where language, technology, and complex social structures (including extensive parental instruction and play) greatly increase the returns on larger brains and longer learning periods <a class="yt-timestamp" data-t="00:43:42">[00:43:42]</a>, <a class="yt-timestamp" data-t="00:44:38">[00:44:38]</a>. This allows for sustained cultural transmission and accumulation of knowledge [[cultural_transmission_knowledge_accumulation_and_social_learning]], unlike other primates who may innovate but often lose these innovations within a generation <a class="yt-timestamp" data-t="00:48:55">[00:48:55]</a>, <a class="yt-timestamp" data-t="00:49:04">[00:49:04]</a>. Larger, more connected human populations also saw faster technological progress, as posited by Michael Kramer <a class="yt-timestamp" data-t="00:49:42">[00:49:42]</a>, with small, isolated populations like historical Tasmanians even losing technologies <a class="yt-timestamp" data-t="00:50:25">[00:50:25]</a>.

Despite the advantages, humans are not "maximally" intelligent due to several biological trade-offs <a class="yt-timestamp" data-t="00:54:31">[00:54:31]</a>:
*   **Metabolic Costs:** The brain consumes ~20% of human metabolic energy, higher in children <a class="yt-timestamp" data-t="00:55:22">[00:55:22]</a>. This energy could otherwise go to surviving famine or powering the immune system against diseases <a class="yt-timestamp" data-t="00:55:43">[00:55:43]</a>, <a class="yt-timestamp" data-t="00:56:01">[00:56:01]</a>.
*   **Mutational Load:** Evolution must constantly purge deleterious mutations. If mutations impacting, say, malaria resistance have a greater effect on fitness than those slightly degrading cognitive ability, the former will be prioritized for purging <a class="yt-timestamp" data-t="00:56:20">[00:56:20]</a>, <a class="yt-timestamp" data-t="00:57:08">[00:57:08]</a>.
*   **Modest Returns to Further Increases:** In modern humans, the correlation between brain size and cognitive ability is modest (r ≈ 0.25-0.3) <a class="yt-timestamp" data-t="00:58:58">[00:58:58]</a>. A hypothetical doubling of brain size (costing an additional ~20% metabolic energy) might yield only about two standard deviations in cognitive ability <a class="yt-timestamp" data-t="00:59:24">[00:59:24]</a>. The average observed income return to cognitive ability is also relatively modest <a class="yt-timestamp" data-t="01:00:06">[01:00:06]</a>.
*   **Physical Constraints:** Obstetric limitations like hip size constrain head size at birth <a class="yt-timestamp" data-t="01:01:05">[01:01:05]</a>.

## Evolutionary Parallels in AI Reward Systems and Alignment

Shulman discusses how evolutionary reward mechanisms might inform thinking about AI alignment [[ai_alignment_and_safety]]. Evolution "rewards" organisms for behaviors conducive to survival and reproduction through mechanisms like the sex drive, hunger, and social imitation <a class="yt-timestamp" data-t="02:20:15">[02:20:15]</a>. However, humans develop complex motivations and values that are not simple optimizations of these base rewards, sometimes even acting counter to direct evolutionary "goals" (e.g., using condoms, resulting in sub-replacement fertility in educated populations) <a class="yt-timestamp" data-t="02:20:32">[02:20:32]</a>. This "misgeneralization" is key: robust values can emerge that don't perfectly optimize the original reward signal <a class="yt-timestamp" data-t="02:25:35">[02:25:35]</a>. The "ideal" behavior for an organism purely optimizing its innate reward predictors might be "wireheading" (directly stimulating reward centers). Yet, many humans reject this (e.g., Nozick's experience machine thought experiment), caring about real-world outcomes instead <a class="yt-timestamp" data-t="02:22:17">[02:22:17]</a>, <a class="yt-timestamp" data-t="02:23:23">[02:23:23]</a>. This suggests it's possible for systems (biological or artificial) to develop motivations that are not simply about maximizing their immediate reward/loss signals, which has implications for training aligned AI.

## Biological Reproduction as an Analogy for System Replication

The reproductive rates of biological organisms offer an analogy for the potential speed of AI system self-replication or expansion, should advanced AI gain control over physical production. 
*   Some heterotrophic bacteria can double every 20-60 minutes under ideal conditions <a class="yt-timestamp" data-t="02:02:30">[02:02:30]</a>.
*   Solar-powered cyanobacteria can double in a day <a class="yt-timestamp" data-t="02:03:07">[02:03:07]</a>.
*   Insects like fruit flies can produce hundreds of offspring in weeks <a class="yt-timestamp" data-t="02:03:55">[02:03:55]</a>. 

A significant difference, however, is that biologically grown brains are unique due to developmental randomness and cannot have software simply "copied" onto them like a GPU <a class="yt-timestamp" data-t="02:04:43">[02:04:43]</a>, <a class="yt-timestamp" data-t="02:05:14">[02:05:14]</a>. Each biological brain must learn from scratch, lacking the direct data transfer capabilities of artificial systems [[role_of_compute_in_ai_development]] <a class="yt-timestamp" data-t="02:06:00">[02:06:00]</a>.