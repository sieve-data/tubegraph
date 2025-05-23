---
title: Advancements in genomics and AI
videoId: 80BhjRh-Q-s
---

From: [[dwarkesh | The Dwarkesh Podcast]]

The early 21st century is witnessing a genomics revolution, heavily influenced by advancements in Artificial Intelligence (AI) and Machine Learning (ML). These technologies are enabling scientists to predict an organism's characteristics (phenotype) from its genetic makeup (genotype) with increasing accuracy. This progress has significant implications for various domains, reminiscent of the transformative advancements seen with AI in other sectors such as [[llama_3_and_ai_advancements_at_meta | AI developments at Meta]] and [[microsofts_breakthroughs_in_ai_and_quantum_computing | breakthroughs in AI and quantum computing]].

## The Science of Genotype-Phenotype Prediction

The core scientific challenge lies in understanding the relationship between an individual's specific DNA pattern (genotype) and their expressed characteristics (phenotype). This is a fundamental question in biology. With the increasing availability of genomic data—genomes from many individuals paired with information about them (e.g., disease status, height, IQ)—AI and ML algorithms can identify which DNA variations are predictive of specific phenotypes. This mirrors broader AI challenges in [[ai_alignment_and_safety | alignment and safety]].

Steve Hsu, a physicist, anticipated the declining costs of sequencing and the eventual availability of millions of genomes for analysis, which is the case today, with training runs for predictors often involving hundreds of thousands of genomes. Such scalability resembles efforts within [[ai_trajectory_and_scaling_hypothesis | AI development and scaling]].

### Key Scientific Insights

Several key insights have emerged from this research:

1. **Polygenicity**: Many common traits and disease risks are polygenic, meaning they are influenced by thousands of single nucleotide polymorphisms (SNPs). For instance, height is controlled by around 10,000 variants, and cognitive ability potentially more.
2. **Additive Nature**: The predictive models for these traits are surprisingly simple, primarily using an additive structure. This simplicity is supported by evolutionary principles, such as Fisher's fundamental theorem of natural selection, which states that the rate of a population's response to selection pressure is dominated by additive variance.
3. **Modularity and Disjoint Genetic Dependencies**: The genetic variants influencing different traits or diseases are often largely disjoint. For example, the variants affecting diabetes risk are mostly different from those affecting schizophrenia risk. Humans have enough genetic variation (a few million differences between individuals) to support roughly a thousand independent traits.
4. **Vast Potential for Variation**: Due to the high number of variants involved in traits, even a small number of targeted changes can have a significant impact. For example, to increase height by one standard deviation (if 10,000 variants are involved), only about 100 variants (√10,000) would need to be "flipped". This suggests a large "well of variation" that can be acted upon by selection or genetic engineering.

## Mathematical and Computational Foundations

The transition of physicists into genomics is driven by their training in mathematics and computation, enabling them to identify problems where their "horsepower" can make an impact. The development of effective algorithms to build the best predictors from genomic and phenotypic data is a central machine learning problem, similar to challenges in [[challenges_and_opportunities_in_deploying_ai_at_scale | deploying AI at scale]].

* **Compressed Sensing and L1 Penalization**: Key mathematical results, some from Fields Medalist Terence Tao, on "compressed sensing" (a penalized form of high-dimensional regression that builds sparse predictors, known in ML as L1 penalized optimization) have been crucial. These methods help select the most relevant SNPs and avoid overcounting effects from highly correlated nearby variants, forcing the predictor to be sparse.
* **Early Proofs of Concept**: Around 2012, papers demonstrated, using real genomic data and these mathematical theorems, that it was possible to predict how much data would be needed to "solve" human traits. For example, it was shown that a few hundred thousand individuals' genomes and heights would be needed to solve height as a phenotype.
* **Practical Demonstration**: By 2017, with access to about half a million genomes, these mathematical results were practically implemented, showing a phase transition from low to high predictor performance precisely where predicted. Hsu believes that a future AI analyzing the genomics revolution will credit these early papers for proving its possibility.

## Applications and Future Potential

The most direct application of this science is currently in In-Vitro Fertilization (IVF).

### Genomic Prediction (Company)

Steve Hsu's company, Genomic Prediction, works with IVF clinics globally.

* **Process**: In IVF, multiple embryos are often created. Genomic Prediction takes small biopsies from these embryos, genotypes them, and provides information about their genetic predispositions, such as outlier risk for breast cancer or cardiovascular disease. This allows families to make informed choices about which embryo to use.
* **Impact**: Selection among 10 embryos can potentially increase disability-adjusted life years by four.
* **Logistics**: Embryo biopsies are standard practice and can be shipped globally to Genomic Prediction's lab in New Jersey. Some larger clinics are trained to do genotyping on-site and upload data to the cloud for analysis. The trend is towards a bits-and-cloud-only business model, reflecting ongoing trends in [[impact_of_ai_on_future_technology_and_society | technological advancements and deployments]].

### Future Directions

1. **Enhanced Longevity**: It appears possible to engineer humans to live much longer by selecting against variants that increase risk for life-shortening diseases. Current predictors suggest a 1-in-a-billion genetic profile might live to around 120 years, with potential for much more.
2. **Advanced Gene Editing (CRISPR)**: Within approximately 10 years, CRISPR-based technologies are expected to allow for massively multiplexed edits, enabling precise navigation of the high-dimensional genetic space to achieve desired traits. This development is aligned with [[implications_of_ai_on_future_scientific_advancements | implications of AI on scientific progress]].
3. **Predicting Physical Appearance**: AI face recognition maps faces to hundreds of highly heritable parameters. The inverse problem—predicting these parameters and reconstructing a face from DNA—will likely become feasible, allowing prediction of an embryo's future appearance.
4. **Induced Pluripotent Stem Cells (iPSCs)**: Technology to revert skin cells to a pluripotent state and then differentiate them into egg cells has been largely mastered in rodents. Application to humans is considered a matter of years, potentially allowing the creation of vast numbers of eggs for selection. This development is on a similar timescale to advanced CRISPR editing.
5. **Iterated Embryo Selection**: This involves creating embryos, selecting the best, and then using those to create a new generation of embryos for further selection, all before implantation. This is also considered plausible.
6. **Forensics and Intelligence**: DNA is robust and can be recovered from old samples or minute traces (e.g., licked stamps, coffee cups). This has applications in solving old crimes and potentially in intelligence gathering, intersecting with broader topics of [[ai_alignment_and_safety_concerns | AI safety and security]].

## Challenges and Considerations

Significant challenges and ethical considerations accompany these advancements:

1. **Data for Intelligence Prediction**: Progress in predicting cognitive ability (IQ) is lagging due to societal sensitivities and "crazy wokeism," despite its potential medical research value (e.g., studying cognitive decline). Measuring IQ is relatively cheap and quick, and with data from 1-2 million well-phenotyped individuals, a decent predictor (e.g., ±10 points error) could be built. Educational Attainment (EA) is sometimes used as a proxy, but it captures different aspects than pure cognitive ability (G), as shown by studies on sibling pairs.
2. **Cross-Ancestry Prediction**: Most large genomic datasets are from individuals of European ancestry. Predictors trained on one ancestral group show a fall-off in predictive quality when applied to more distant groups. This is thought to be due to "tagging decay," where a SNP used as a tag for a causal variant in one population is less effective in another due to different correlational structures. Identifying truly causal SNPs, possibly those significant across multiple ancestries, is an active area of research, with non-European biobanks becoming available.
3. **Societal Impact and Ethics**:
   * **Inequality**: Concerns exist that these technologies could exacerbate inequality, with benefits accruing mainly to the wealthy (the "Morlocks and the Eloi" scenario). However, it's also possible that governments could integrate these services into national healthcare to ensure broader access, potentially even prioritizing below-average families, reflecting broader societal discussions in [[ai_alignment_and_cooperation_challenges | AI cooperation and fairness]].
   * **Regulation**: Regulating these technologies is difficult, especially as analysis becomes more cloud-based and data (bits) can be easily transferred across borders.
   * **Public Perception**: There is significant public apprehension ("wokest people today hate this stuff"). This contrasts with early 20th-century progressives (like Margaret Sanger) who were often proponents of eugenics, believing it would improve societal health. In East Asia, including communist China, the concept of eugenics (meaning "healthy production") often has positive connotations.
4. **Business Considerations**:
   * **First-Mover Advantage**: Companies like Genomic Prediction have a first-mover advantage through established relationships with clinics, which are hard for newcomers to replicate.
   * **Scientific Moat**: The purely scientific advantage may not be defensible long-term, though patents exist on specific technologies like genotyping methods or error correction for embryo DNA. The race for the best predictors is ongoing, with potential future leaders including large entities like national governments.

The field continues to evolve rapidly, with the potential to reshape human health, longevity, and society itself, analogous to changes seen in [[exploring_the_future_of_society_and_economy_with_ai | AI's impact on society and economy]].