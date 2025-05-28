---
title: Algorithmic fairness and bias
videoId: AzdxbzHtjgs
---

From: [[lexfridman]] <br/> 

Algorithmic fairness and bias are critical aspects of machine learning and artificial intelligence (AI) systems. These topics involve the equitable treatment of individuals and groups by algorithms, ensuring that automated systems do not perpetuate existing social inequalities or introduce new forms of discrimination.

## Ethical Algorithms

Michael Kerns, a Professor at the University of Pennsylvania and co-author of the book "Ethical Algorithm," discusses how ethical considerations in algorithms have become increasingly important in the design and implementation of AI systems. The book emphasizes the need to address algorithmic fairness, bias, privacy, and ethics [00:00:06]. Kerns notes that while most of the book focuses on technical aspects, understanding algorithmic fairness requires engaging with broader societal debates on fairness and equality [00:33:01].

## Algorithmic Fairness

Algorithmic fairness refers to the objective of designing algorithms that do not unjustly favor any individual or group over others. This involves ensuring that the output of machine learning models does not disproportionately affect certain demographic groups, a phenomenon often referred to as algorithmic bias. Achieving fairness necessitates defining which groups are protected and what harms are being mitigated [00:17:42].

### Group vs. Individual Fairness

Kerns highlights the tension between group fairness and individual fairness in algorithmic systems. Group fairness involves ensuring equitable outcomes across defined groups (e.g., racial or gender groups), while individual fairness seeks to treat similar individuals similarly [00:26:41]. This distinction is crucial when considering how to develop fair algorithms, as it dictates the dimensions along which fairness is measured.

## Measuring Fairness

There are challenges in quantifying fairness. Unlike computational measures like running time (Big O notation) or accuracy, fairness is subjective and contextual [00:13:16]. However, Kerns suggests that by defining specific notions of fairness, such as the disparity in false rejection rates between groups, it is possible to measure an algorithm's ethical performance [00:15:18].

## Trade-offs in Fairness

Implementing fairness constraints often requires balancing trade-offs between algorithmic fairness and other metrics, such as accuracy. These trade-offs can be illustrated using Pareto curves, which depict the relationship between error rates and unfairness, guiding stakeholders in selecting preferred balances [00:34:52].

## Algorithmic Bias

Bias in algorithms can emerge from the data they are trained on. For example, if a facial recognition system is predominantly trained on images of white males, it may perform poorly on marginalized groups [00:42:00]. Correcting such biases might involve collecting more diverse data or explicitly incorporating fairness into the learning objective [00:42:24].

## Privacy Considerations

Algorithmic privacy, particularly through concepts like [[differential privacy]], ensures that individual data contributions do not adversely affect privacy outcomes. This is achieved by introducing probabilistic elements (noise) into the data processing pipeline, protecting personal information while allowing data analysis [01:06:00].

## Philosophical Underpinnings

The philosophical roots of algorithmic fairness relate to broader questions of what constitutes a fair and just society. This includes debates from Plato's definitions of justice to modern-day discussions on [[value_alignment_and_ethical_considerations_in_ai | ethical alignment]] in AI [00:12:10].

Michael Kerns acknowledges that while algorithmic approaches can address some overt biases and privacy concerns, deeper philosophical issues often remain unresolved, requiring ongoing discourse and exploration [01:01:01].

> [!info] Key Takeaway
> Algorithmic fairness and bias require an intersection of technical advancements and philosophical inquiry to ensure that AI systems promote equitable and just outcomes. Balancing accuracy and fairness, incorporating diverse datasets, and embedding ethical standards are paramount in mitigating bias and promoting fairness.