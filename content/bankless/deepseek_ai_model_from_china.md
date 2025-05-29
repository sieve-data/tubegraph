---
title: DeepSeek AI model from China
videoId: OC61Vo4tAaE
---

From: [[bankless]] <br/> 

The [[chinas_deepseek_ai_model_and_its_impacts | DeepSeek AI model from China]] has made significant waves in the artificial intelligence (AI) industry due to its remarkable efficiency and low operational costs, leading to a notable market recalibration, particularly for companies like Nvidia. Its emergence has highlighted shifts in the competitive landscape of [[developments_in_ai_model_competition | AI model development]] and the underlying hardware supply chain.

## DeepSeek's Breakthrough Efficiency
The [[chinas_deepseek_ai_model_and_its_impacts | DeepSeek V3 technical paper]], detailing its efficiency gains, was released on December 27th [00:00:20], with an even newer R1 model paper focusing on Chain of Thought capabilities coming out a week prior to a major market reaction [00:00:31]. Despite these earlier releases, the market's significant response occurred suddenly, attributed by some to an article explaining its implications to hedge fund managers [00:00:43].

DeepSeek is reportedly:
*   45 times more cost-efficient than US-based AI models [00:01:34], a figure believed to be "in the right ballpark" [00:44:43].
*   Charges 95% less money to use than [[frontier_ai_models_and_advancements_by_openai | OpenAI's ChatGPT]] [00:01:39].
*   Cost only $6 million to train [00:01:58], compared to the much more expensive models developed by leading US labs [00:01:53].

### Market Reaction and Impact
The news surrounding DeepSeek's capabilities resulted in a significant market downturn, with $2 trillion being wiped off global equity markets [00:00:08]. Nvidia, a key supplier of AI hardware, saw its stock drop by 20%, equating to a $600 billion loss in market value [00:01:42]. This event prompted [[frontier_ai_models_and_advancements_by_openai | OpenAI]] and Meta's AI labs to scramble to understand how a "relatively unheard of Chinese AI lab" [00:01:51] achieved such performance with a low training cost [00:01:58].

The efficiency of DeepSeek suggests that the entire industry might have been "massively over-provisioning compute resources" [00:06:36], potentially leading to a "significantly lower" aggregate demand for compute than previously projected [00:06:44]. The ability of DeepSeek to match GPT-4 level performance while charging 95% less for API calls implies that either Nvidia's customers are spending unnecessarily, or margins for AI services must decrease dramatically [00:06:50]. This situation is seen by some as a win for the software side in the "tug-of-war between hardware and software" [00:07:12].

For consumers of AI products, this development is highly positive, as it suggests that future AI applications will be more accessible and affordable [01:09:18].

### Technical Innovations Behind DeepSeek's Efficiency
[[chinas_advances_in_ai | Chinese advancements in AI]], particularly with DeepSeek, are influenced by a "necessity's mother of invention" approach, given fewer resources compared to Western companies [00:46:09]. Instead of a bifurcated approach where researchers prototype and then engineers optimize, the DeepSeek team demonstrated expertise in both areas [00:49:42]. They focused on saturating GPU performance and optimizing communication overhead [00:50:01], leading to a collection of "optimization tricks" [00:50:59], some of which were based on ideas published by American researchers but cleverly implemented [00:51:01].

Key innovations include:
*   **Efficient KV Cache Storage**: DeepSeek developed an "incredibly smart" method for storing key-value (KV) caches and indices, which are crucial for Transformer models and consume significant memory on the GPU's VRAM [00:52:51]. By storing only the "meaningful" subset of data in a compressed form, they achieved substantial memory savings, allowing more to be done with fewer GPUs and reducing data transfer [00:55:02].
*   **Multi-Token Predictions (Speculative Decoding)**: Unlike traditional models that predict one token (word) at a time, DeepSeek attempts to predict multiple tokens (e.g., two or three) simultaneously [00:55:13]. While the second token usually depends on the first, DeepSeek uses "speculative decoding" with a 95% accuracy rate, effectively doubling throughput for inference at no additional cost [00:55:47].
*   **Compressed Parameter Storage**: The model's parameters (a gigantic list of numbers) are stored in a more compressed form [00:56:39]. Instead of training at higher precision and then quantizing (truncating/rounding numbers) for cheaper GPUs, DeepSeek largely handles the entire process end-to-end using a "smaller representation" [00:57:28]. These efficiency gains compound due to their multiplicative nature [00:58:17].

### Broader Implications and Market Outlook
The sudden and significant [[developments_in_ai_model_competition | step function change]] in efficiency, rather than a predictable [[developments_in_ai_model_competition | Moore's Law]] progression, caught the market off guard [01:06:09]. The market had priced Nvidia "to perfection" [01:06:27], expecting sustained triple-digit revenue growth and high margins [01:06:42]. However, the emergence of more efficient models like DeepSeek, along with competitive hardware (e.g., Cerebras, Groq) and hyperscalers developing their own custom silicon (e.g., Amazon's Graviton and Trinimum chips, Microsoft, [[frontier_ai_models_and_advancements_by_openai | OpenAI]], Meta) [01:12:47], poses threats to Nvidia's market share and profitability [01:27:01]. Even if competitors' chips are not "as good as Nvidia's" [01:24:18], their significantly lower cost (due to not needing to pay Nvidia's high margins) makes them economically compelling [01:13:13].

The concept of "Jevons Paradox" suggests that increased efficiency could lead to increased demand, but the immediate impact on hardware demand might still be negative due to delayed capital expenditure decisions by major players like Mark Zuckerberg [00:08:01].

The market also faces a challenge with the limited supply of high-quality training data [01:13:59]. This is being addressed by [[ai_agents_and_model_developments | synthetic data]], where AI models generate text that is then used to train new models [01:14:32]. While seemingly circular, this works effectively for logic, math, and computer programs because the generated data can be verified for correctness [01:15:13]. This allows for a continuous generation of high-quality training data, accelerating the improvement of models in these areas [01:16:31]. This suggests that quantitative jobs might be particularly susceptible to AI advancements [01:16:54].

Jeffrey Emanuel, an investor and technologist, is the author of a 12,000-word article titled "The Short Case for Nvidia Stock" [01:00:43] that significantly contributed to the market's reaction. He explains that his article was written in a way that resonated with hedge fund managers [00:00:43]. It gained massive traction after being shared by prominent figures like Chamath Palihapitiya and Naval Ravikant, accumulating over 2 million views [01:23:02]. This broad dissemination of a detailed analysis is believed to have "precipitated the decline" [01:23:36] by informing institutional investors and potentially even Nvidia employees about the underlying competitive threats and unsustainable valuation.