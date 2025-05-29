---
title: Intersection of causality and AI technologies
videoId: bTTSg91pFUk
---

From: [[causalpython]] <br/> 

[[Causality in AI | Causality]] is described as fundamental for humanity, serving as a framework for improved decision-making processes, with curiosity highlighted as a key component <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. The Causal Bandits podcast focuses on [[causal_ai_and_machine_learning_intersection | causality and machine learning]] <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## Dr. Juan Orus: A Pioneer in Applied Causality

Dr. Juan Orus, originally from Bogotá, Colombia, initially pursued a PhD in geometric analysis before transitioning to data science <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. He became a leading advocate for using [[Causal AI in business applications | causality in marketing]] <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. His shift from pure mathematics to an applied context was driven by a desire for broader impact and personal happiness, as academic work felt too limited <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. He found that his pure mathematics background, especially in linear algebra, provided a strong foundation for problem-solving in data science, teaching him to break down complex problems and not be intimidated by ill-defined tasks <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

## The Role of Causality in Industry

Dr. Orus realized the need for [[Causality in AI | causality]] early in his career, particularly when dealing with marketing analytics problems like estimating media efficiency and optimizing budgets <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>. Traditional methods, such as linear regression, often led to biased estimations when marketers "threw everything into the model," making it possible to "torture the data to get a story" <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.

### Bayesian Modeling as an Entry Point
His journey into [[Causality in AI | causal thinking]] was influenced by Bayesian modeling, particularly through the book "Statistical Rethinking" by Richard McElreath, which highlights the focus on [[Causality in AI | causality]] within Bayesian statistics <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>. This approach requires explicitly stating assumptions about the data generation process, which is crucial for building robust models and simulations <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.

### Challenges in Applied Settings
A significant challenge in applying [[Causal AI in business applications | causal AI]] is communicating its conceptual framework to non-technical stakeholders <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>. For example, in media mix models, marketers instinctively want to include all channels in a regression, but this can lead to biased estimations due to mediator effects (e.g., TV ads creating awareness, leading to search, then conversion) <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>. It's counter-intuitive for them that leaving certain channels out can improve estimation accuracy <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.

### Communicating Causal Concepts
To bridge the communication gap, Dr. Orus uses simulations as a powerful tool <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>. By controlling the "truth" in a simulated environment, he can demonstrate how naive models yield misleading results, which could lead to significant financial losses <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>. This empirical evidence helps convince stakeholders without delving into complex [[Causality in AI | causal inference]] details <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.

### Causal Tools and Methods

*   **Directed Acyclic Graphs (DAGs)**: Considered a fundamental tool, DAGs allow for a transparent and systematic way to state assumptions about a model as a graph, which then helps determine the necessary model structure for unbiased estimation <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a>. This approach makes everything "much transparent" <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>.
*   **Bayesian Framework**: Forces explicit statement of data generation process assumptions, which is helpful for simulations and incorporating domain knowledge <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.
*   **Do-calculus and Structural Models**: While not explicitly detailed, the ability to automate calculations based on the DAG and "do calculus" is mentioned as very handy <a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>.
*   **Python Libraries**: Popular libraries like `econ-ml` and `do-why` are used when models become more complex <a class="yt-timestamp" data-t="00:21:15">[00:21:15]</a>.
*   **Quasi-Experimental Methods (e.g., Geo-Lift, Synthetic Control)**: These methods are used to estimate counterfactuals when true A/B tests are not feasible <a class="yt-timestamp" data-t="00:31:38">[00:31:38]</a>. For example, in a city-wide campaign (like in Berlin), one can use similar cities (e.g., Hamburg, Munich) as a control group to estimate what conversions would have been without the campaign <a class="yt-timestamp" data-t="00:32:42">[00:32:42]</a>. DAGs complement these methods by forcing researchers to state assumptions and identify potential limitations, ensuring transparency and awareness of unfeasible estimations <a class="yt-timestamp" data-t="00:22:50">[00:22:50]</a>. These methods can work "surprisingly well" under mild assumptions <a class="yt-timestamp" data-t="00:34:12">[00:34:12]</a>.
*   **Model Evaluation**: Evaluating [[Causality in AI | causal models]] involves assessing statistical estimation and, crucially, the causal structure <a class="yt-timestamp" data-t="00:35:34">[00:35:34]</a>. Techniques like shuffling data, removing data, or adding edges to the DAG to test stability are used <a class="yt-timestamp" data-t="00:35:58">[00:35:58]</a>. Cross-validation is also performed to ensure the model isn't just seeing noise <a class="yt-timestamp" data-t="00:35:09">[00:35:09]</a>.

## [[The future of AI integrating generative AI and causal AI | Causality and AI Technologies]]

### [[Causal AI and machine learning intersection | Causality and Large Language Models (LLMs)]]
Dr. Orus acknowledges the significant potential of [[causal_ai_and_machine_learning_intersection | LLMs]] in areas like creativity and optimizing communication, particularly for automated experimentation <a class="yt-timestamp" data-t="00:19:15">[00:19:15]</a>. However, he emphasizes the early stage of development and the need for caution, especially in marketing campaigns where an unexpected response from an LLM could harm a brand <a class="yt-timestamp" data-t="00:19:28">[00:19:28]</a>. Currently, he finds LLMs most useful for boosting productivity through tools like GitHub Copilot, code generation, text summarization, and automating calls <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>.

## Learning and Future Outlook for [[Causality in AI | Causality]]

Dr. Orus hopes that [[Causality in AI | causality]] is not just a trend, but something "fundamental for Humanity" as it is central to decision-making <a class="yt-timestamp" data-t="00:43:52">[00:43:52]</a>. He believes it is a guaranteed investment that will pay off <a class="yt-timestamp" data-t="00:15:50">[00:15:50]</a>. He stresses the need for more [[Causality in AI | causal education]] and thinking in the industry, ensuring it's seen as a fundamental concept rather than a hype or a tool <a class="yt-timestamp" data-t="00:44:24">[00:44:24]</a>.

### Advice for Aspiring Practitioners
*   **Focus on Fundamentals**: Prioritize understanding core concepts like linear algebra and probability theory, as they form the backbone of many techniques <a class="yt-timestamp" data-t="00:41:39">[00:41:39]</a>.
*   **Prioritize Concepts over Tools**: When starting with [[Causality in AI | causality]], focus on the conceptual understanding and model structure (e.g., DAGs) rather than getting distracted by the latest software or estimation methods <a class="yt-timestamp" data-t="00:25:28">[00:25:28]</a>.
*   **Iterative Approach**: Start simple and iterate, delivering basic solutions quickly and then adding complexity <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>. In industry, speed is crucial <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>.
*   **Practical Experience**: Solve concrete problems that genuinely interest you, even if they are simple, as this hands-on experience provides invaluable learning and builds confidence <a class="yt-timestamp" data-t="00:48:05">[00:48:05]</a>.
*   **Embrace Curiosity**: Maintain a "childlike curiosity" and be open to learning new things <a class="yt-timestamp" data-t="00:47:10">[00:47:10]</a>. Don't trust everything blindly; challenge assumptions and experiment to see when methods break <a class="yt-timestamp" data-t="00:46:26">[00:46:26]</a>.

### Recommended Resources
*   "Statistical Rethinking" by Richard McElreath <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>
*   Books by Judea Pearl (for theory lovers) <a class="yt-timestamp" data-t="00:45:26">[00:45:26]</a>
*   "Causal Inference: The Brave and The True" by Mateus <a class="yt-timestamp" data-t="00:25:03">[00:25:03]</a> <a class="yt-timestamp" data-t="00:46:00">[00:46:00]</a>

## Beyond Modeling: Causal Thinking for Decision-Makers
Causal thinking is not only useful for modelers but also for anyone making decisions <a class="yt-timestamp" data-t="00:36:55">[00:36:55]</a>. Business analysts or marketing managers can be fooled by their intuition if they don't understand basic [[Causality in AI | causal principles]], such as the effect of filtering by colliders in a dashboard, which can lead to contradictory results <a class="yt-timestamp" data-t="00:37:35">[00:37:35]</a>. Humans, while capable of [[Causality in AI | causal thinking]], learn it through experience and iteration rather than initial intuition <a class="yt-timestamp" data-t="00:39:15">[00:39:15]</a>.