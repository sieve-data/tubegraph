---
title: Embryo selection and genetic prediction
videoId: 80BhjRh-Q-s
---

From: [[dwarkesh | The Dwarkesh Podcast]]

The field of genomics, particularly as it applies to embryo selection and genetic prediction, has seen significant advancements in the early 21st century. This article details the scientific basis, applications, future potential, and ethical considerations surrounding these technologies, primarily based on the work and insights of Steve Hsu, co-founder of Genomic Prediction.

## Genomic Prediction: Overview and Application

Genomic Prediction is a company co-founded by Steve Hsu that works with In Vitro Fertilization (IVF) clinics globally <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a> <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>. The company's primary service involves analyzing the genomes of embryos created during the IVF process to provide predictive information about potential health risks and other traits.

### The IVF Context
IVF procedures often result in the creation of multiple embryos, especially when hormone stimulation is used, which can yield anywhere from 5 to 20 eggs, or even 60 to 100 eggs in young, hormonally stimulated egg donors <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a> <a class="yt-timestamp" data-t="01:35:05">[01:35:05]</a>. Once fertilized, these embryos present families with the "embryo choice problem": deciding which embryo(s) to implant <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>.

Genomic Prediction assists in this decision by genotyping embryos from a small biopsy. This allows them to identify embryos that may be outliers for risks of certain conditions, such as breast cancer or cardiovascular disease, enabling parents and clinicians to make more informed choices <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>. The company reportedly works with 200-300 IVF clinics across six continents <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>.

### Operational Model
Typically, IVF clinics perform the embryo biopsy, a standard procedure <a class="yt-timestamp" data-t="00:47:04">[00:47:04]</a>. The sample is then shipped to Genomic Prediction's lab (e.g., in New Jersey) for genotyping, as DNA is a robust molecule <a class="yt-timestamp" data-t="00:47:17">[00:47:17]</a>. Some larger clinics are trained to perform genotyping on-site, uploading data to the cloud for analysis and receiving reports back <a class="yt-timestamp" data-t="00:48:18">[00:48:18]</a>. Hsu envisions a future where this becomes predominantly a bits-and-cloud business, with local clinics handling sequencing and uploading data for rapid remote analysis <a class="yt-timestamp" data-t="00:49:04">[00:49:04]</a>.

## The Scientific Basis

The core scientific challenge is relating an organism's genotype (its specific DNA pattern) to its phenotype (its expressed characteristics) <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>. This is approached as an AI and machine learning problem, using large datasets of genomes and corresponding phenotype information (e.g., disease status, height, IQ) to identify predictive DNA variations (Single Nucleotide Polymorphisms, or SNPs) <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a> <a class="yt-timestamp" data-t="00:16:23">[00:16:23]</a>.

### Algorithms and Predictive Models
Steve Hsu, leveraging his background in physics and mathematics, anticipated the decreasing cost of sequencing and the eventual availability of large genomic datasets (e.g., half a million to a million genomes for training runs) <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>.

His group focused on developing effective algorithms, drawing on concepts like **compressed sensing** (a penalized form of high-dimensional regression aiming for sparse predictors, known in machine learning as L1 penalized optimization) <a class="yt-timestamp" data-t="00:19:30">[00:19:30]</a>. Early work (around 2012) involved proving theoretically that these methods could predict how much data would be needed to "solve" traits like human height, suggesting a few hundred thousand individuals would be required <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>. This was later practically demonstrated around 2017 with a dataset of half a million genomes, showing a phase transition in predictor performance as predicted <a class="yt-timestamp" data-t="00:20:24">[00:20:24]</a>. Hsu notes that these foundational mathematical insights are not always well-appreciated in the broader computational genomics field <a class="yt-timestamp" data-t="00:20:50">[00:20:50]</a>.

While the training process is complex, the resulting predictive models are often surprisingly simple, employing an **additive structure**. This means the model largely sums the effects of individual genetic variants (SNPs) that are given a non-zero weight, rather than relying on complex non-linear interactions between genomic regions <a class="yt-timestamp" data-t="00:21:40">[00:21:40]</a> <a class="yt-timestamp" data-t="00:22:21">[00:22:21]</a>. The L1 penalization helps ensure sparsity, selecting the most informative SNPs and avoiding overcounting effects from highly correlated nearby variants <a class="yt-timestamp" data-t="00:23:09">[00:23:09]</a>.

### Additive Genetic Architecture and Modularity
The observation that many complex traits are governed by an additive genetic architecture is a significant finding <a class="yt-timestamp" data-t="00:24:22">[00:24:22]</a>.
*   **Evolutionary Basis:** This simplicity is supported by Fisher's fundamental theorem of natural selection, which states that the rate of a population's response to selection pressure is dominated by additive variance. Additive traits are more easily passed on and selected for during sexual reproduction, as complex non-linear mechanisms might be broken apart <a class="yt-timestamp" data-t="00:26:06">[00:26:06]</a>.
*   **Human Genetic Variation:** While complex, non-linear systems are fundamental to being human (as opposed to, say, a frog), the small differences *between* humans appear to be largely due to these additive "switches" <a class="yt-timestamp" data-t="00:27:21">[00:27:21]</a>.
*   **Modularity:** Research indicates that the genetic underpinnings for different traits (e.g., diabetes vs. schizophrenia) are largely disjoint. There's modest overlap in the genomic regions influencing different major diseases <a class="yt-timestamp" data-t="00:31:53">[00:31:53]</a>. Hsu estimates that the human genome has enough informational capacity for roughly a thousand independent traits to be governed by distinct sets of variants, analogous to independent character stats in a role-playing game <a class="yt-timestamp" data-t="00:32:59">[00:32:59]</a>.

This contrasts with older theories like Dawkins' "antagonistic pleiotropy" (where a gene has a positive effect when young but a negative one when old) as a primary explanation for aging. While such specific cases exist, the general picture for common traits is one of control by thousands of largely disjoint variants <a class="yt-timestamp" data-t="00:35:41">[00:35:41]</a>.

## Potential for Trait Enhancement and Longevity

The additive and polygenic nature of traits opens up significant possibilities for selection and, eventually, editing.
*   **Vast Genetic Variation:** For a trait controlled by, say, 10,000 variants (like height), one would only need to flip the state of roughly the square root of N (i.e., 100) variants to achieve a one standard deviation change <a class="yt-timestamp" data-t="00:37:20">[00:37:20]</a>. This implies a large "well of variation" that can be acted upon, a concept known to animal and plant breeders who have dramatically altered traits in livestock (e.g., milk production in cows, egg-laying frequency in chickens) <a class="yt-timestamp" data-t="00:39:01">[00:39:01]</a> <a class="yt-timestamp" data-t="00:43:00">[00:43:00]</a>.
*   **Longevity:** Current polygenic risk scores can predict significant increases in disability-adjusted life years (DALYs) even with selection from a modest number of embryos (e.g., four DALYs from selecting one of ten) <a class="yt-timestamp" data-t="00:36:25">[00:36:25]</a>. Calculations suggest that a "one in a billion" genetic profile for health could correspond to a lifespan of around 120 years <a class="yt-timestamp" data-t="00:41:30">[00:41:30]</a>. Hsu believes it's plausible that individuals could be engineered to live much longer by reducing risks for multiple diseases, though the ultimate limits are unknown <a class="yt-timestamp" data-t="00:39:50">[00:39:50]</a>.
*   **CRISPR and Gene Editing:** The ongoing development of CRISPR gene editing technologies, particularly for massively multiplexed edits, is expected to allow direct navigation of this high-dimensional genetic space within roughly a decade <a class="yt-timestamp" data-t="00:41:03">[00:41:03]</a> <a class="yt-timestamp" data-t="01:08:03">[01:08:03]</a>. This would move beyond selection to direct modification of embryos.

### Why Hasn't Evolution Optimized These Traits?
The reasons why evolution hasn't already "maxed out" desirable traits like longevity or intelligence are complex:
1.  **Changing Environments:** The human environment has changed radically (e.g., agriculture, modern medicine, dating apps), so "optimization" is a moving target <a class="yt-timestamp" data-t="00:28:45">[00:28:45]</a>.

    For more on the impact of cultural and technological changes, see this article on [the effects of agriculture on human genetics and societal development](https://the_effects_of_agriculture_on_human_genetics_and_societal_development).

2.  **Late-Onset Diseases:** Many common diseases manifest after typical reproductive ages in our evolutionary past, so there was limited selection pressure against them <a class="yt-timestamp" data-t="00:29:52">[00:29:52]</a>.
3.  **High-Dimensional Space:** Evolution explores a vast, high-dimensional genetic space. The "fitness landscape" may be relatively flat in many directions, meaning significant time or selection pressure is needed for large changes <a class="yt-timestamp" data-t="00:28:15">[00:28:15]</a> <a class="yt-timestamp" data-t="00:40:21">[00:40:21]</a>.

## Challenges and Limitations

### Cross-Ancestry Prediction and Tagging Decay
A significant current challenge is that most large genomic datasets are from individuals of European ancestry <a class="yt-timestamp" data-t="01:00:42">[01:00:42]</a>. Predictors trained on one ancestral group tend to show a fall-off in predictive quality when applied to more distant groups <a class="yt-timestamp" data-t="01:00:50">[01:00:50]</a>. This is often attributed to **"tagging decay"**:
*   Predictors often identify a "tag" SNP that is statistically correlated with a nearby truly causal SNP.
*   The correlational structure (linkage disequilibrium) between SNPs varies across populations due to different ancestral and mating histories.
*   A good tag SNP in Europeans might be a poor tag for the same causal SNP in, for example, a South Asian population <a class="yt-timestamp" data-t="01:01:07">[01:01:07]</a>.

The assumption is often that the underlying causal genetic architecture is largely the same across human populations, but this itself is a hypothesis <a class="yt-timestamp" data-t="01:01:50">[01:01:50]</a> <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>. Identifying truly causal variants (e.g., by finding SNPs consistently significant across diverse populations) is an active area of research, with the expectation that larger, more diverse biobanks (non-European ones are coming online) will help resolve this within 5 years or so <a class="yt-timestamp" data-t="01:02:22">[01:02:22]</a> <a class="yt-timestamp" data-t="01:03:34">[01:03:34]</a>.

### Data for Intelligence Prediction
Prediction of cognitive ability (intelligence) is lagging, according to Hsu, due to "crazy wokeism" and fear among researchers of collecting such data <a class="yt-timestamp" data-t="01:12:11">[01:12:11]</a> <a class="yt-timestamp" data-t="01:12:44">[01:12:44]</a>. While there are valid medical reasons to measure cognitive function (e.g., in aging studies), the controversial social implications have made researchers hesitant to collect this phenotype alongside genomic data <a class="yt-timestamp" data-t="01:13:01">[01:13:01]</a>. Hsu estimates that with a dataset of a quarter-million to two million well-phenotyped individuals (including cognitive measures, which can be obtained cheaply via short tests like the Wonderlic <a class="yt-timestamp" data-t="01:13:43">[01:13:43]</a>), a decent IQ predictor with a standard error of perhaps 10 points could be built <a class="yt-timestamp" data-t="01:14:24">[01:14:24]</a>.

For a broader perspective on the impact of culture and environment on intelligence, you may refer to [impact of culture and environment on intelligence](https://impact_of_culture_and_environment_on_intelligence).

### Height Prediction and Environmental Factors
While height is highly heritable, environmental factors like nutrition play a significant role. Height predictors are most accurate for individuals raised in favorable environments where they can reach their genetic potential <a class="yt-timestamp" data-t="00:59:09">[00:59:09]</a>. In populations where malnutrition was historically prevalent (e.g., older generations in parts of Asia), individuals may be shorter than their genetic prediction due to these environmental limitations <a class="yt-timestamp" data-t="00:59:34">[00:59:34]</a>.

## Business and Regulatory Landscape

### First-Mover Advantage and Competition
Genomic Prediction benefits from a first-mover advantage, particularly in its established channel relationships and trust with IVF clinics globally <a class="yt-timestamp" data-t="00:44:34">[00:44:34]</a>. While the company has patents on specific technologies (e.g., genotyping methods, error correction for embryo DNA <a class="yt-timestamp" data-t="00:45:50">[00:45:50]</a>), the core science of predicting traits from DNA may not be a defensible long-term moat. Large entities with vast datasets (e.g., 23andMe, or even national governments) could potentially develop strong predictors, though Hsu notes his team has deep expertise built over years <a class="yt-timestamp" data-t="00:44:51">[00:44:51]</a> <a class="yt-timestamp" data-t="00:45:36">[00:45:36]</a>.

### Regulation
The ease of transmitting genomic data digitally makes regulation challenging. If a country restricts certain types of genetic selection, data can be uploaded to vendors in less restrictive jurisdictions <a class="yt-timestamp" data-t="00:49:39">[00:49:39]</a>.

## Future Technologies and Applications

### Facial Reconstruction from DNA
The parameters used by facial recognition AI are highly heritable. Hsu foresees the ability to reverse-engineer this: predict facial parameters from an embryo's DNA and then reconstruct what that individual might look like at various ages (e.g., 16 or 32 years old) <a class="yt-timestamp" data-t="00:50:14">[00:50:14]</a> <a class="yt-timestamp" data-t="00:50:51">[00:50:51]</a>. This is considered an AI/ML problem pending sufficient data.

For insights into AI's capabilities in various domains, refer to [impact of AI on future technology and society](https://impact_of_ai_on_future_technology_and_society).

### Induced Pluripotent Stem Cells (iPSCs) for Egg Production
The technology to revert adult cells (like skin cells) to a pluripotent state and then differentiate them into egg cells (oocytes) has been largely mastered in model organisms like mice/rats <a class="yt-timestamp" data-t="01:37:40">[01:37:40]</a>. Hsu believes translating this to humans is a matter of years, with startups already working on it <a class="yt-timestamp" data-t="01:38:26">[01:38:26]</a>. This could overcome the limitation of egg availability, potentially allowing selection from thousands of embryos <a class="yt-timestamp" data-t="01:39:34">[01:39:34]</a>. However, its adoption may be tempered by the concurrent development of advanced gene editing, which might offer a more direct route to desired genetic outcomes <a class="yt-timestamp" data-t="01:39:48">[01:39:48]</a>.

### Iterated Embryo Selection
This involves creating embryos, selecting a preferred subset, and then using those selected embryos to create a subsequent generation of embryos for further selection, all before any are implanted to become a person <a class="yt-timestamp" data-t="01:40:55">[01:40:55]</a>. This is also considered technologically plausible <a class="yt-timestamp" data-t="01:41:15">[01:41:15]</a>.

### Genetic Matching for Reproduction
Dating apps owned by major companies have expressed interest in features where users could upload their genomes to assess genetic compatibility for offspring traits <a class="yt-timestamp" data-t="00:55:59">[00:55:59]</a>. This could extend to predicting if a couple's genetic combination is likely to produce children with exceptionally high levels of a trait (e.g., intelligence) due to complementary genetic profiles <a class="yt-timestamp" data-t="00:57:05">[00:57:05]</a>. Hsu notes that an early 23andMe patent application explored advising parents on mating based on predicted offspring traits <a class="yt-timestamp" data-t="00:57:55">[00:57:55]</a>.

## Ethical and Societal Considerations

### Historical Context and "Wokeism"
Hsu points out the irony that many early 20th-century progressives (e.g., Margaret Sanger) were proponents of what would now be termed eugenics, believing in improving societal health through informed reproduction <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a> <a class="yt-timestamp" data-t="01:09:07">[01:09:07]</a>. He contrasts this with current "wokeist" perspectives that are often hostile to such technologies <a class="yt-timestamp" data-t="01:09:10">[01:09:10]</a>. He argues that the goal of healthier, longer-lived individuals should be universally desirable and that these technologies could potentially address inequalities if made accessible <a class="yt-timestamp" data-t="01:41:41">[01:41:41]</a> <a class="yt-timestamp" data-t="01:42:23">[01:42:23]</a>.

For a reflection on how historical influences can affect leadership and innovation, see [historical influences on leadership and innovation](https://historical_influences_on_leadership_and_innovation).

### Inequality
A major concern is that these technologies could exacerbate societal inequality, leading to a "Morlocks and Eloi" scenario where only the wealthy can afford enhancements, creating a genetically stratified society <a class="yt-timestamp" data-t="00:54:57">[00:54:57]</a> <a class="yt-timestamp" data-t="01:08:03">[01:08:03]</a> <a class="yt-timestamp" data-t="01:43:38">[01:43:38]</a>. Hsu acknowledges this risk but suggests that societal choices, such as integrating these services into national healthcare systems (as some countries like Denmark and Israel do for IVF <a class="yt-timestamp" data-t="01:08:10">[01:08:10]</a>), could mitigate this. Governments could even offer more aggressive interventions or more embryos to below-average families as a form of redistribution <a class="yt-timestamp" data-t="01:44:47">[01:44:47]</a>.

### Consumer Uptake
While some, like the blogger Guenon, express pessimism about widespread adoption due to cost, the IVF process itself, and societal hostility <a class="yt-timestamp" data-t="01:25:01">[01:25:01]</a>, Hsu notes high IVF rates in some developed countries (e.g., 1 in 10 babies in Denmark <a class="yt-timestamp" data-t="01:26:31">[01:26:31]</a>, 3-5% in the US <a class="yt-timestamp" data-t="01:29:46">[01:29:46]</a>). He questions whether families already undergoing IVF and chromosomal screening would refuse additional, low-cost information about polygenic risks <a class="yt-timestamp" data-t="01:28:18">[01:28:18]</a>.

### Pleiotropy
The concern that selecting for one trait (e.g., intelligence) might have unintended negative consequences on other traits (pleiotropy) is often raised. Examples include the higher incidence of certain genetic disorders in Ashkenazi Jews (who also have high average intelligence) or the hypothesized link between schizophrenia risk and creativity <a class="yt-timestamp" data-t="01:15:57">[01:15:57]</a>. Hsu argues that if intelligence is controlled by tens of thousands of variants, genetic engineers could likely "drive around" such obstacles by choosing sets of variants that enhance intelligence without negative side effects, pointing to historical geniuses who were otherwise normal or even athletic <a class="yt-timestamp" data-t="01:17:34">[01:17:34]</a>.

For more on advancements in genomics and AI, you might find [advancements in genomics and AI](https://advancements_in_genomics_and_ai) interesting.

The ongoing advancements in genetic prediction and embryo selection promise significant changes to human reproduction and health, while also presenting profound ethical and societal questions that will require careful consideration.