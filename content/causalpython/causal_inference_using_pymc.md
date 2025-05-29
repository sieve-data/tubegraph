---
title: Causal inference using PyMC
videoId: QAzAFess1AA
---

From: [[causalpython]] <br/> 

PyMC is one of the most recognizable Python probabilistic programming frameworks [00:00:26]. Dr. Thomas Wiecki, one of its key developers, began learning programming as a child and later studied bioinformatics before becoming fascinated with Bayesian modeling, which inspired PyMC's growth [00:00:11].

## Dr. Thomas Wiecki's Journey and PyMC's Mission

Dr. Wiecki's fascination with programming stemmed from the idea of creating something from nothing and controlling a system [00:01:04]. His interest later extended to neuroscience and bioinformatics, eventually leading him to Bayesian modeling [00:01:11]. He realized Bayesian modeling tools were not only useful for his PhD research but also for industry problems, such as portfolio construction and evaluating algorithms at a FinTech startup in Boston [00:01:40]. This experience confirmed to him that these tools were valuable for both academic and many data science problems where a deep understanding and incorporation of that understanding into the model are needed [00:02:21].

The most enjoyable aspect for Dr. Wiecki today is the community behind PyMC [00:03:22]. He appreciates the open-source arena where talented individuals from around the world contribute, fostering friendships and a strong sense of community [00:03:39]. The work with PyMC and PyMC Labs involves solving advanced problems and pushing the boundaries of what's possible, making previously unimaginable things achievable [00:04:12]. This element of discovery and enabling humanity to solve potentially massive problems, like climate change, is endlessly motivating [00:04:37]. PyMC, for example, has over 2,000 citations in its original publication, with people using it to solve applied problems in diverse fields like astrophysics [00:05:52].

## Integrating Causal Inference into PyMC

Dr. Wiecki emphasizes that his understanding of [[causal_inference_concepts_and_applications | causal inference concepts and applications]] is through a Bayesian lens, finding it helpful as the two fields have largely developed independently [00:06:36]. He believes there are interesting cross-connections, similar to those between Bayesian statistics and machine learning [00:06:51].

### The `do`-operator

A significant new addition to PyMC is the [[causal_inference_methods_and_applications | causal do-operator]] [00:06:20]. This operator was primarily driven by Ben Vincent, who mapped causal theory into a language understandable for Bayesian practitioners [00:07:05]. The `do`-operator fit well into the PyMC framework from a software perspective, despite requiring some graph manipulation functionality, which Ricardo V. implemented [00:07:43]. Its inclusion is a critical missing piece to make PyMC a framework for answering structural causal problems and building models that integrate direct [[causal_inference_and_its_applications | causal inference and its applications]] machinery [00:08:11].

### CausalPy

Another key development in the PyMC ecosystem is the CausalPy package [00:41:07]. CausalPy, also developed by Ben Vincent, focuses on quasi-experimentation, a well-constrained problem domain [00:41:20]. It helps understand how causal analysis approaches problems by fitting data in an in-sample period and predicting out-of-sample, comparing it to actual outcomes [00:41:55]. CausalPy allows users to choose between a scikit-learn model or a Bayesian model, with the latter providing uncertainty estimates [00:42:18]. This package highlighted that while there might be historical misunderstandings or "baggage" suggesting causal analysis cannot be done in a Bayesian framework (e.g., traditional Bayesian networks not covering interventions), there's nothing to stop the addition of tools like the `do`-operator [00:42:35]. Ultimately, these are all probabilistic tools, and the goal is to build the best ones, freely exploring methods and improving upon existing approaches [00:43:27].

## Bayesian Modeling and Causal Inference: A Symbiotic Relationship

Dr. Wiecki observed a strong parallel between Bayesian modeling and [[causal_inference_concepts_and_applications | causal inference concepts and applications]], particularly in their structural aspects [00:08:41]. He recalls attending a talk on [[causal_inference_methods_and_applications | causal inference methods and applications]] where structural causal models were used to answer data science questions, such as price elasticity, and realized it was similar to what Bayesian modeling does by defining a "data generative process" [00:09:08]. Initially, no one seemed to know the difference, but the conclusion is that "those two things are the same just to a different lens through a different framework" [00:10:07].

### Structural Aspects

Both probabilistic programming languages like PyMC and [[causal_inference_methods_and_applications | causal inference methods and applications]] emphasize structural aspects in their modeling [00:08:33]. Dr. Wiecki believes [[causal_inference_methods_and_applications | causal inference methods and applications]] offers powerful ideas by putting causality front and center for estimating treatment effects and understanding the world [00:10:29]. While much of [[causal_inference_methods_and_applications | causal inference methods and applications]] is expressed in a frequentist framework, there's value in expressing these ideas in a Bayesian framework [00:10:40]. Conversely, Bayesian methods can learn from adopting the causal language and framework [00:11:03].

Bayesian modeling excels at incorporating expert understanding into the model [00:02:30]. When building a structural model, there is a perceived fear of being wrong by explicitly defining the structure [00:19:20]. Dr. Wiecki advises embracing mistakes: "it's great to be wrong... that's how we learn" [00:19:54]. Bayesian tools like posterior predictive checks and simulations help identify where the model is wrong, leading to learning about the data and fixing issues [00:20:16]. This process also fosters communication with domain experts, whose insights improve the model [00:20:50]. The alternative, simply training black-box classifiers, doesn't offer learning or explainability [00:21:42].

> "most of the things we care about because even with that usually I would say that we're always a bit under um underutilized in terms of what the data can provide" <a class="yt-timestamp" data-t="00:32:06">[32:06]</a>

In the context of causal graphs, a key advantage of the Bayesian framework is that it can directly estimate the complete structural model [00:34:45]. Unlike frequentist approaches, which often require careful variable selection to avoid biases (e.g., including a collider), Bayesian models can include all relevant structure, and the inference process correctly incorporates these relationships [00:34:50]. This is particularly beneficial when estimating the strength of connections in a causal graph, as frequentist point estimates can be biased or noisy, whereas Bayesian methods provide more representative and useful estimates by considering the full posterior distribution (e.g., the mean, often found via Markov Chain Monte Carlo) [00:35:27].

Bayesian modeling, in the way PyMC offers it, is generative [00:37:19]. This allows users to first build a hypothesized causal structure, then generate data from it to immediately see if the model behaves as expected [00:37:51]. This generative aspect aids in "structural discovery" by allowing users to test different hypotheses and observe their implications on the generated data patterns [00:38:49]. This iterative process of learning a structure, incorporating expert knowledge, and comparing it to real-world data or experiments is very similar to how [[practical_implementation_of_causal_discovery_using_python | practical implementation of causal discovery using Python]] is done [00:39:06].

### Addressing Uncertainty

The Bayesian framework naturally provides uncertainty quantification [00:44:26]. While other methods like conformal prediction also estimate uncertainty, Bayesian models allow for a more nuanced understanding, including the potential to split between aleatoric (data-inherent) and epistemic (model-inherent) uncertainty [00:47:54].

However, the interpretation and trust in these uncertainty splits depend on factors like priors and model assumptions [00:48:06]. Dr. Wiecki cautions that uncertainty estimates need to be validated against reality, citing examples from Bayesian deep learning where the type of uncertainty derived might not align with intuitive expectations [00:48:30]. Instead of absolute measures, he finds it more useful to compare relative uncertainty (e.g., across different datasets or marketing channels) [00:51:19].

Crucially, Bayesian uncertainty estimates become actionable when integrated into an optimizer [00:52:15]. For instance, in a marketing mix model, instead of just providing effectiveness estimates with uncertainty bounds, the uncertainty can be used to optimize budget allocation to maximize sales [00:52:48]. This allows the optimizer to make decisions that factor in risk aversion, preferring marketing channels with more data and lower uncertainty over those with high point estimates but limited data [00:53:14]. This approach aligns with how humans make decisions, incorporating risk and leading to more robust and actionable solutions [00:54:18].

### Practical Benefits: Decision Making and Communication

Dr. Wiecki emphasizes that the ultimate purpose of data science is to make better actions and decisions [00:14:11]. To achieve this, understanding "what causes what" is essential [00:12:01].

> "if you want to act on the the world you have to understand what causes what to take the most effective action" <a class="yt-timestamp" data-t="00:11:56">[11:56]</a>

He argues that while prediction is useful, it is not the same as decision-making [00:14:04]. Predictive models might forecast what will happen, but without a causal understanding, one cannot effectively *affect* what will happen [00:14:40]. This distinction is critical, as illustrated by an example where a marketing team using predictive machine learning models for three years experienced pure losses [00:16:18]. This highlights that a black-box machine learning algorithm might make good predictions but fail to solve the underlying business problem if it lacks a causal understanding [00:17:51]. While black-box ML algorithms suffice for legitimate forecasting problems, Dr. Wiecki's experience suggests these are fewer than currently applied [00:18:09]. A more careful, causal approach, even if harder and requiring new tools, is crucial for solving actual business problems and maintaining the relevance of data science [00:18:32].

Communicating the value of Bayesian frameworks to business stakeholders can be challenging, but framing it around [[causal_inference_and_decision_making | causal inference and decision making]] resonates effectively [00:12:57]. The idea that data science aims to enable better actions by understanding how actions affect outcomes is a powerful narrative [00:14:13]. This approach fosters trust by combining domain expertise with data-driven insights, leading to solutions that are not only effective but also understandable and acceptable to those making decisions [00:22:28].

## Challenges and Approach to Modeling

Building complex models involves decisions at every step, from data processing to algorithm choice [00:23:51]. These choices introduce uncertainty and impact the final result [00:24:02]. Dr. Wiecki believes it's better to be conscious and transparent about these choices rather than ignoring them [00:24:20].

When modeling complex environments like marketing, there are two main approaches: building a single, huge global model or a series of smaller, localized models [00:26:40]. In practice, PyMC users often start with more localized, specialized models, as overly ambitious global models tend to crumble [00:27:16]. However, there is a significant appeal to global models because many different factors influence each other in complex systems (e.g., various types of marketing, competitors' actions, pricing) [00:27:41]. The ideal approach involves starting with individual pieces and then connecting them in sensible ways, linking different datasets (e.g., marketing spend, purchasing behavior, lift tests) to improve model fit [00:29:20].

Regarding the boundary between explicitly modeling a process and treating it as an "exogenous variable" or "noise," Dr. Wiecki advises testing whether simplifying the model by summarizing noise terms works [00:31:15]. If it does, great; if not, more structure can be added [00:31:39]. In practice, there's a tendency to err on the side of including more variables of interest, as models are often underutilized in terms of the data they could process [00:31:54].

## Resources for Learning

To learn more about PyMC, its open ecosystem, Bayesian modeling, and [[causal_inference_concepts_and_applications | causality]]:
- Visit the PyMC website: [PyMC.io](https://www.pymc.io/) [01:04:25]. It features a comprehensive examples gallery with notebooks on various problems [01:04:29].
- Explore the PyMC Labs blog: [PyMC Labs Blogs](https://www.pymc-labs.io/blog/) [01:04:45]. This is where much of the current thinking, ideas, and exciting developments, including the post on the `do`-operator, are shared [01:04:52].
- Connect on social media, primarily LinkedIn [01:05:09].
- Dr. Thomas Wiecki can also be found on Twitter (TWei) or contacted via email [01:07:38].