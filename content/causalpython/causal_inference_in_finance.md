---
title: Causal inference in finance
videoId: GkqXWC03VYM
---

From: [[causalpython]] <br/> 

Alexander Den, an author, entrepreneur, and investor, discusses the application of [[causal_inference_and_its_applications | causal inference]] in the financial sector, drawing from his unique background in theoretical physics and finance <a class="yt-timestamp" data-t="00:26:00">[00:26:00]</a>. He highlights the shift needed from traditional statistical methods to more robust [[causal_inference_methods_and_applications | causal models]] for better risk management and investment strategies <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.

## Transition from Physics to Finance

Alexander Den initially pursued a PhD in Superstring Theory but found it too detached from experimentation, which he believed betrayed the spirit of physics <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>. He sought a return to observable and relatable phenomena <a class="yt-timestamp" data-t="02:16:00">[02:16:00]</a>. With a strong background in mathematics and statistics, he transitioned to finance at the beginning of the 21st century, seeing the potential for applying scientific rigor to calculate risk based on behavioral patterns and newly available data <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>.

The mathematical tools he found most useful included:
*   Basic statistics and probability <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a>
*   Stochastic processes and stochastic differential equations <a class="yt-timestamp" data-t="05:17:00">[05:17:00]</a>
*   Pattern recognition, early machine learning concepts, statistical classification, and regression models, particularly for credit applications <a class="yt-timestamp" data-t="05:37:00">[05:37:00]</a>

## Limitations of Traditional Finance Models

During the 2008 financial crisis, it became evident that existing financial measurement theories, which relied on statistical repeatability and assumptions of stationary or stable data-generating processes, were flawed <a class="yt-timestamp" data-t="08:50:00">[08:50:00]</a>.

Key issues identified:
*   **Lack of Controlled Environment**: Unlike experimental sciences like physics, economics and finance do not allow for controlled laboratory experiments or statistical repetitions due to dynamic, ever-changing contexts and exogenous factors <a class="yt-timestamp" data-t="07:18:00">[07:18:18]</a>.
*   **Non-Falsifiability**: Economic and financial theories are often not falsifiable, meaning robust statistical conclusions cannot be inferred <a class="yt-timestamp" data-t="08:12:00">[08:12:00]</a>.
*   **Flawed Risk Measurement (Value at Risk - VaR)**: Measures like VaR assume stable statistical distributions derived from historical data. The financial crisis showed that these distributions can change shape drastically, leading to what were considered "Sigma events" (rare events) happening frequently, causing financial institutions to fail <a class="yt-timestamp" data-t="09:10:00">[09:10:00]</a>.
*   **Misaligned Incentives**: Practitioners knew of these limitations but were incentivized to misreport risk using historical data to show lower risk, take more risk, and earn bigger bonuses <a class="yt-timestamp" data-t="10:25:00">[10:25:00]</a>.

## The Need for Forward-Looking and Causal Approaches

Following the financial crisis, there was an "awakening" among regulators and practitioners that a different approach was needed <a class="yt-timestamp" data-t="10:52:00">[10:52:00]</a>. The idea emerged to create "forward-looking distributions" rather than relying on stable historical data <a class="yt-timestamp" data-t="11:25:00">[11:25:00]</a>.

This approach acknowledges:
*   **Approximate Rightness**: It's better to be approximately right about future distributions (with some subjectivity and approximation) than precisely wrong by relying on historical data, as the future is unlikely to be a mere repetition of the past <a class="yt-timestamp" data-t="12:10:00">[12:10:00]</a>.
*   **Uncertainty and Exogenous Events**: Financial systems are constantly affected by unpredictable exogenous factors like meteorological or geopolitical events, which are "Gray Swans" – events that are going to happen but whose precise impact is uncertain <a class="yt-timestamp" data-t="12:51:00">[12:51:00]</a>.
*   **Asymmetric Relationships**: In finance, relationships are not always symmetric (e.g., an S&P 500 crash causes implied volatilities to spike, but the reverse is not necessarily true) <a class="yt-timestamp" data-t="15:08:00">[15:08:00]</a>. This points to the need for understanding directional mechanisms.

## [[Causal inference and its applications | Causality]] in Finance

This recognition led to reasoning in terms of [[causal_inference_and_its_applications | causality]] <a class="yt-timestamp" data-t="14:49:00">[14:49:00]</a>. Alexander Den emphasizes moving from David Hume's concept of necessary conjunction to a probabilistic setting <a class="yt-timestamp" data-t="17:01:00">[17:01:00]</a>.
*   **Probabilistic Influence**: Causal influence in finance is probabilistic, not deterministic <a class="yt-timestamp" data-t="17:17:00">[17:17:00]</a>. Probability captures the uncertainty about unmodeled background causes and details of the system <a class="yt-timestamp" data-t="17:42:00">[17:42:00]</a>.
*   **Structural Information**: By using existing structural information, probabilities can be assigned to different events and their ramifying consequences <a class="yt-timestamp" data-t="17:09:00">[17:09:00]</a>. For example, knowing potential outcomes of elections and assigning probabilities to them based on polls and market information allows for scenario analysis <a class="yt-timestamp" data-t="15:56:00">[15:56:00]</a>.
*   **Joint Probability Distributions**: Causal models, such as Bayesian Networks, allow for the derivation of a forward-looking joint probability distribution, which can then be used to calculate a forward-looking Value at Risk <a class="yt-timestamp" data-t="19:28:00">[19:28:00]</a>.

## Benefits of [[Causal inference methods and applications | Causal Models]]

[[Causal inference methods and applications | Causal models]] offer several advantages over traditional associative models:
*   **Transparency and Auditability**: Graphical causal models make the structure more transparent, allowing for better understanding of cause-and-effect relationships <a class="yt-timestamp" data-t="22:27:00">[22:27:00]</a>.
*   **Improved Communication**: They provide a clear language for communication, fostering discussion and brainstorming, even among senior management <a class="yt-timestamp" data-t="22:32:00">[22:32:00]</a>.
*   **Enhanced Preparation**: Explicitly defining hypotheses in a causal model, even if they turn out to be approximately right, allows for better preparation for various scenarios. As General Eisenhower stated, "all plans in battle turn to be useless but preparation will prove to be indispensable" <a class="yt-timestamp" data-t="23:31:00">[23:31:00]</a>.
*   **Deriving Future Joint Probability**: Causal models enable the construction of a future joint probability distribution, which is crucial for forward-looking risk assessment and investment strategies <a class="yt-timestamp" data-t="20:48:00">[20:48:00]</a>.
*   **Stable Relationships**: Understanding the underlying causal mechanisms leads to more stable, robust, and reliable results, unlike purely associational relationships that can break down (e.g., Google flu trends) <a class="yt-timestamp" data-t="51:57:00">[51:57:00]</a>.

## Challenges to Adoption in Finance

Despite the benefits, [[industrial_applications_of_causal_inference | causal models]] have struggled to gain widespread adoption in finance and economics <a class="yt-timestamp" data-t="24:36:00">[24:36:00]</a>.
*   **Dominance of Econometrics**: The field is heavily influenced by econometrics, which primarily relies on historical data, leading to resistance to new methodologies <a class="yt-timestamp" data-t="25:46:00">[25:46:00]</a>.
*   **Institutional Inertia**: Financial institutions have invested heavily in existing methodologies, training, and software systems, making them reluctant to change without significant regulatory pressure <a class="yt-timestamp" data-t="26:32:00">[26:32:00]</a>.
*   **Regulatory Imperfections**: Regulators often mandate stress tests that require replay of past scenarios or provide inconsistent macroeconomic data, which further disincentivizes innovation <a class="yt-timestamp" data-t="26:51:00">[26:51:00]</a>.
*   **Macroeconomic Complexity**: In macroeconomics, determining clear causal directions between aggregate variables is challenging due to feedback loops and low-frequency data <a class="yt-timestamp" data-t="30:38:00">[30:38:00]</a>.

## [[Causal inference in fintech | Causal Inference in Fintech]] and Investment Strategies

[[Causal inference and decision making | Causal models]] can significantly impact investment strategies, particularly in developing forward-looking efficient frontiers for portfolio optimization <a class="yt-timestamp" data-t="37:52:00">[37:52:00]</a>.

Two main approaches are considered:
1.  **Scenario-Based Investment**: This involves building forward-looking data-generating processes based on specific events (e.g., political elections) and their probabilistic consequences <a class="yt-timestamp" data-t="39:45:00">[39:45:00]</a>.
2.  **Structural Causal Models of the Economy**: This approach aims to build a comprehensive causal model of the economy to predict various macro-financial variables for investment decisions <a class="yt-timestamp" data-t="40:02:00">[40:02:00]</a>. This is seen as a "holy grail" research problem due to the dynamic, adaptive, and often non-directional nature of macroeconomic systems <a class="yt-timestamp" data-t="40:43:00">[40:43:00]</a>.

### Hybrid Models and Interventions
For complex systems like financial networks, hybrid models combining directed (causal) and undirected (associational) graphical models (like chain graphs) can be beneficial <a class="yt-timestamp" data-t="33:03:00">[33:03:00]</a>. These allow modeling interventions and how they propagate across interconnected systems <a class="yt-timestamp" data-t="35:05:00">[35:05:00]</a>.

## Data, Computation, and Market Efficiency

*   **Data Availability**: The Information Age provides vast amounts of data (e.g., satellite images, news, social media, consumer surveys) that can be used to populate [[causal_inference_concepts_and_applications | causal models]] <a class="yt-timestamp" data-t="24:16:00">[24:16:00]</a>. This enables the measurement of previously latent variables at higher frequencies, supporting the disentanglement of micro-causal structures <a class="yt-timestamp" data-t="43:05:00">[43:05:00]</a>.
*   **Computational Challenges**: Learning [[causal_inference_concepts_and_applications | causal models]], especially discrete ones, can be computationally intensive (NP-hard), requiring significant resources <a class="yt-timestamp" data-t="45:26:00">[45:26:00]</a>. However, advancements in computational power and AI are making this more feasible <a class="yt-timestamp" data-t="45:49:00">[45:49:00]</a>.
*   **Market Efficiency**: Markets are not fully efficient, as evidenced by successful investors exploiting inefficiencies <a class="yt-timestamp" data-t="48:49:00">[48:49:00]</a>. However, they tend to be better predictors than the average opinion of economists <a class="yt-timestamp" data-t="50:33:00">[50:33:00]</a>. Building a relevant [[causal_inference_concepts_and_applications | causal model]] can help exploit these inefficiencies more stably by understanding the underlying mechanisms <a class="yt-timestamp" data-t="51:19:00">[51:19:00]</a>.

## Advice for Aspiring Professionals in the Field

For those entering complex fields like [[causal_inference_and_its_applications | causality]], machine learning, or finance:
*   **Understand the Domain**: Deep understanding of the subject matter is crucial, not just crunching numbers <a class="yt-timestamp" data-t="53:41:00">[53:41:00]</a>.
*   **Master Core Skills**: Proficiency in data engineering, programming (Python), and machine learning is essential <a class="yt-timestamp" data-t="55:23:00">[55:23:00]</a>.
*   **Build on Foundations**: Do not disregard traditional methods (e.g., econometrics, classical financial models); build upon the knowledge of those who came before <a class="yt-timestamp" data-t="56:53:00">[56:53:00]</a>.
*   **Continuous Learning**: The field is constantly evolving, requiring an open mind and dedication to continuous learning <a class="yt-timestamp" data-t="57:32:00">[57:32:00]</a>.
*   **Patience**: Given the complexity, patience is key <a class="yt-timestamp" data-t="57:52:00">[57:52:00]</a>.

## Influential Books and Mentors

Alexander Den highlights several books that influenced his thinking:
*   **"Causality" by Judea Pearl**: This book "opened his eyes" and changed his perspective from associational thinking to asking "why" <a class="yt-timestamp" data-t="58:37:00">[58:37:00]</a>.
*   **"Coherent Stress Testing" by Ricardo Rebonato**: The first book to introduce [[causal_inference_in_fintech | causality]] into finance <a class="yt-timestamp" data-t="59:05:00">[59:05:00]</a>.
*   **"Elements of Statistical Learning" by Hastie, Tibshirani, and Friedman**: A foundational machine learning textbook <a class="yt-timestamp" data-t="59:26:00">[59:26:00]</a>.
*   **"Machine Learning: A Probabilistic Perspective" by Kevin P. Murphy**: Another key machine learning text discussing graphical models <a class="yt-timestamp" data-t="59:34:00">[59:34:00]</a>.

His mentors include Ricardo Rebonato (Global Head of Market Risk at Royal Bank of Scotland and Oxford professor) and Daniel Amit (his supervisor, author of a book on modeling brain functions) <a class="yt-timestamp" data-t="01:01:00">[01:01:00]</a>. He also credits Marcos Lopez de Prado for inspiring his latest book on alternative data <a class="yt-timestamp" data-t="01:01:00">[01:01:00]</a>.