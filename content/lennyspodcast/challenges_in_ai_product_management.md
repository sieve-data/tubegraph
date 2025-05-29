---
title: Challenges in AI product management
videoId: scsW6_2SPC4
---

From: [[lennyspodcast]] <br/> 

Developing and managing products in the field of artificial intelligence presents unique [[impact_and_challenges_of_ai_in_product_management | challenges]] that differ significantly from traditional software development. The dynamic nature of AI models means that the technology is constantly evolving, requiring a fundamentally different approach to product strategy and execution [00:00:00].

## Rapidly Evolving Technology

Unlike traditional technology, where the underlying components like databases improve incrementally (e.g., 5% better over two years), AI models are experiencing exponential growth in capabilities [00:16:51]. Every couple of months, computers can perform tasks they were previously unable to do, forcing product teams to rethink their approach entirely [00:00:13]. This rapid advancement means that "the AI models you're using today is the worst AI model you will ever use for the rest of your life" [01:16:59].

This presents a paradox:
*   **Constant Change**: Product roadmaps must be agile, as the technology underlying the product is changing so quickly that plans made three months out are unlikely to remain entirely accurate [00:28:01].
*   **"Model Maximalism"**: There is a philosophy to embrace the current limitations of models, building products that are *just* on the edge of current capabilities [00:31:59]. The expectation is that improved models will soon "blow away" current limitations, making barely functional products "sing" in a few months [00:31:46].

## Managing Fuzzy Inputs and Outputs

Traditional software operates on defined inputs to produce defined outputs [00:17:27]. In contrast, Large Language Models (LLMs) excel at handling "fuzzy, subtle inputs" like the nuances of human language and communication [00:17:48]. However, they don't always produce the exact same output, even for the same input, providing "spiritually the same answer" rather than an identical one [00:17:56].

This introduces complexity in product design:
*   **Accuracy Thresholds**: The design of an AI product must account for the model's accuracy rate for a given use case [00:18:11]. A product built on a model that is 60% accurate will differ greatly from one that is 95% or 99.5% accurate [00:18:19].
*   **User Experience**: For tasks requiring "thinking time" from the model (e.g., 10-25 seconds), the user interface needs to be designed to keep users engaged and informed, mimicking human interaction patterns like providing small updates or thinking out loud [00:37:40].

## The Critical Role of Evals

Given the probabilistic nature of AI models, a core skill for product builders, especially product managers, is learning the "craft of writing evals" [00:19:03].
*   **Definition**: Evals (evaluations) are essentially "quizzes for a model" or "unit tests for models" [00:19:24] that gauge their proficiency in specific subject material or their ability to respond to certain questions [00:19:29].
*   **Importance**: Evals are crucial for:
    *   **Measuring Capability**: Understanding how accurate a model is for a specific use case (e.g., creative writing, graduate-level science, competitive coding) [00:19:47].
    *   **Continuous Improvement**: Evals serve as benchmarks for hill-climbing, allowing teams to continuously fine-tune and teach the model to improve performance for specific use cases [00:22:05].
    *   **Data-Driven Development**: They help identify where the model performs well (e.g., 99.95% accuracy) versus where it struggles (e.g., 60% accuracy), informing product design decisions [00:20:21].
    *   **Unlocking Potential**: The quality of AI is "capped" by the quality of evals [00:22:36]. As models are multi-dimensional, effective evals are needed to measure and improve specific intelligences, such as different types of coding [00:22:50].
    *   **Customization**: With a vast amount of the world's data and processes being private, models need to be fine-tuned with company-specific or use-case-specific data to perform well, and this performance is measured with custom evals [00:23:46].

## Organizational and Product Development Philosophies

The rapid pace and unique nature of AI development necessitate specific organizational approaches:
*   **Agile Roadmapping**: While quarterly and yearly strategies are set for alignment, the expectation is that these plans will change due to continuous learning and technological shifts [00:27:12]. The "moment of planning is helpful" [00:28:06], even if the written plan is only partially right.
*   **Bottoms-Up Empowerment**: Strong, opinionated, and product-focused engineers, PMs, and designers are empowered to make decisions and drive development, as they have the closest understanding of model capabilities [00:28:40].
*   **Iterative Deployment**: The philosophy is to "ship and iterate" quickly, even if the full capabilities of the models are not yet known [00:30:51]. This allows for "co-evolution" with society as understanding of AI grows [00:31:01].
*   **Research and Product Integration**: Moving from a pure research company to one that is both world-class in research and product is a challenge [00:46:07]. The best products result from iterative feedback loops where product design and research work together as a single team, influencing model fine-tuning with use-case-specific data and evals [00:47:19].
*   **Lean Product Management**: A "PM light" organization is preferred to prevent over-planning and micromanagement, relying on high-agency, product-focused engineers [00:48:21]. Product Managers are expected to be decisive, comfortable with ambiguity, and lead through influence rather than direct authority [00:50:14].

## Societal and Human Impact

AI's rapid advancement also brings broader societal [[impact_and_challenges_of_ai_in_product_management | challenges]]:
*   **Job Displacement and Reskilling**: While technology drives economic advancement, there are "temporary dislocations" and impacts on individuals as jobs change [01:09:02]. AI tools like Chat GPT can serve as powerful "reskilling apps" [01:09:35], but ensuring a "graceful and well-supported" transition for everyone is crucial [01:09:50].
*   **Unrealized Potential**: Despite AI's capability, some highly impactful applications, like ubiquitous personalized AI tutoring, have not yet reached their full potential [01:06:40].
*   **"Prompt Engineering"**: The current need for users to be skilled in "prompt engineering" to get the best results from models is a "sharp edge" that developers aim to eliminate over time for broader adoption [01:27:00].
*   **Hallucinations**: While models are getting safer, they still "hallucinate less every iteration" [01:16:23], indicating that reliability remains an ongoing challenge.

## Overcoming Disappointments: The Libra Project

Kevin Weil cited the Libra (later Novi) project at Facebook as the "biggest disappointment" of his career [00:00:57], despite its potential to improve global remittances and financial inclusion [01:18:43].
*   **Vision**: The project aimed to enable free, instant, and simple money transfers through platforms like WhatsApp and Messenger, similar to sending a text message [01:19:25].
*   **Challenges and Failure**: The attempt to launch a new blockchain, a basket of currencies, and integrate it deeply into existing platforms all at once was too much change [01:19:51]. This, combined with Facebook's negative reputation at the time, contributed to its failure [01:20:04].
*   **Lesson**: The experience highlights the importance of introducing significant technological and societal changes more gently and incrementally [01:20:24].
*   **Legacy**: Despite the product not shipping, its underlying open-source technology lives on in other blockchain companies like Aptos and Mysten [01:21:26].