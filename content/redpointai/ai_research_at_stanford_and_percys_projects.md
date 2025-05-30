---
title: AI research at Stanford and Percys projects
videoId: ZEi4OTuFa3I
---

From: [[redpointai]] <br/> 

Percy Liang, a leading [[AI research and development|AI researcher]] and co-founder of Together AI, shares his insights on the current state and future direction of [[AI research and development|AI research]] from his vantage point at Stanford University <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## Academic AI Research Philosophy

Liang emphasizes that academic [[AI research and development|AI research]] should be orthogonal to the work of large corporate labs like OpenAI to remain relevant and impactful <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>. If a research project is enhanced or remains largely irrelevant when new, powerful models like GPT-5 are released, it indicates a good choice for academic focus <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. He advises choosing projects that will benefit from models getting better <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>.

Three key directions for academia include:
1.  **Orthogonal Research**: Focusing on novel use cases of language models rather than raw model development, as exemplified by his work on Generative Agents <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>. Similarly, benchmarks like ML Agent Bench are enhanced when new models come out <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>.
2.  **Open Source Contributions**: Academia, aligned with open science, should contribute to the open-source community by discovering and publishing knowledge, even if it means reinventing concepts, to allow broader community adoption and product development <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>. Examples include understanding data quality and weighting in pre-training <a class="yt-timestamp" data-t="00:12:55">[00:12:55]</a>.
3.  **Transparency, Benchmarking, and Auditing**: Academia is uniquely positioned to develop tools and conduct research that assesses transparency and benchmarks AI systems, as it lacks the commercial interests that might hinder such efforts in private companies <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>. This work includes collaborating with areas like law to address unique problems <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.

## Key Projects and Research Areas

### Generative Agents
Liang's work on Generative Agents created a virtual world, similar to The Sims, where AI agents interact with each other <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. This project was driven by the idea of generating not just text, but agents or a society of agents <a class="yt-timestamp" data-t="00:23:08">[00:23:08]</a>. Each agent is powered by a language model with specific prompts and operates within a virtual environment, allowing researchers to study complex social dynamics <a class="yt-timestamp" data-t="00:23:25">[00:23:25]</a>.

Key outcomes and future potential include:
*   **Emergent Behavior**: The simulation revealed phenomena like information diffusion, similar to human social dynamics <a class="yt-timestamp" data-t="00:23:49">[00:23:49]</a>.
*   **Valid Simulations**: The goal is to move from believable simulations to those that are actually valid and reflect reality <a class="yt-timestamp" data-t="00:24:26">[00:24:26]</a>.
*   **Digital Twin of Society**: This could enable running experiments, such as testing the impact of policies (e.g., mask mandates, new laws) in a simulated environment <a class="yt-timestamp" data-t="00:24:50">[00:24:50]</a>.
*   **Social Science Studies**: It offers a way to conduct social science research more efficiently and cost-effectively, even allowing for counterfactuals (giving an agent both treatment and control) <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>.
*   **Distinction from Prior Simulations**: Unlike physical or agent-based models governed by simple equations, large language models allow for simulations with much greater detail and complexity <a class="yt-timestamp" data-t="00:28:17">[00:28:17]</a>.

### Evaluations and Benchmarking
Liang notes that [[Experimenting and testing AI use cases|AI evaluation]] is currently "a huge mess" due to the difficulty in trusting benchmarks, primarily because the training data for large models is unknown and proprietary, leading to "train-test overlap" concerns <a class="yt-timestamp" data-t="00:30:09">[00:30:09]</a>.

Key aspects of his work in evaluations include:
*   **Helm (Holistic Evaluation of Language Models)**: Initially a manual effort to cover all aspects of language models, Helm has evolved into a framework with vertical-specific leaderboards for areas like safety, healthcare, and finance <a class="yt-timestamp" data-t="00:34:42">[00:34:42]</a>.
*   **Auto Bencher**: This paper explores using language models themselves to generate automatic, intelligent inputs for benchmarking, particularly leveraging asymmetry where the question-generating model has information the test-taker does not <a class="yt-timestamp" data-t="00:32:13">[00:32:13]</a>.
*   **Rubrics**: He advocates for evaluation anchored in concrete terms, similar to grading exams with a rubric, rather than superficial judgments <a class="yt-timestamp" data-t="00:33:35">[00:33:35]</a>.
*   **SideBench**: A challenging Capture the Flag cyber security benchmark where the hardest problems take human teams over 24 hours to solve <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. Current models can only solve challenges humans solved in around 11 minutes <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
*   **ML Agent Bench**: A benchmark for evaluating language models' ability to solve machine learning research tasks <a class="yt-timestamp" data-t="00:47:44">[00:47:44]</a>.

Regarding OpenAI's O1 model, Liang found its product experience to be slow and difficult to use <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. From a research perspective, O1 signals a shift towards "test-time compute" and agents that can reason, plan, and perform ambitious tasks over days or weeks <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. However, when evaluating O1 on SideBench, simply dropping it in as a replacement did not significantly improve overall performance because O1 ignored existing reflection and planning templates, making it incompatible with the framework <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. This highlights the importance of compatibility when integrating new models into larger systems <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

### Interpretability
Liang notes that [[challenges_in_ai_research_and_potential_solutions|interpretability]] has become even harder because, unlike in 2017, model weights and training data are often not accessible <a class="yt-timestamp" data-t="00:36:08">[00:36:08]</a>. He identifies two main audiences for interpretability:
1.  **Scientific Understanding**: Pure curiosity about how a model functions, such as mechanistic interpretability that analyzes individual neurons <a class="yt-timestamp" data-t="00:37:16">[00:37:16]</a>.
2.  **Debugging and Accountability**: For developers to fix problems or for regulated industries (finance, healthcare) to understand why a decision was made <a class="yt-timestamp" data-t="00:37:24">[00:37:24]</a>.

He discusses:
*   **Influence Functions**: A method developed in 2016-2017 to attribute a model's prediction to specific training examples <a class="yt-timestamp" data-t="00:37:38">[00:37:38]</a>. While adaptable to language models, it's difficult to scale and presents privacy concerns if training data is private <a class="yt-timestamp" data-t="00:37:53">[00:37:53]</a>.
*   **Explanations (Chain of Thought)**: Models can generate explanations, but research shows these might not accurately reflect what's actually happening internally <a class="yt-timestamp" data-t="00:39:04">[00:39:04]</a>.

Liang concludes that for meaningful interpretability, researchers need a return to the 2017 level of access to model weights and training data <a class="yt-timestamp" data-t="00:39:45">[00:39:45]</a>.

### Model Architectures
Historically, architectures like LSTMs, CNNs, and Transformers arose from intuition and experimentation <a class="yt-timestamp" data-t="00:40:47">[00:40:47]</a>. However, the Mamba (State Space Model) architecture notably emerged from mathematical research on fitting online polynomial updates to sequences <a class="yt-timestamp" data-t="00:41:03">[00:41:03]</a>.

Liang believes that current architectures like Transformers may not be the enduring ones, and new innovations are likely to come from tackling different types of problems beyond language, such as video processing or agentic search settings, where existing architectures might break <a class="yt-timestamp" data-t="00:42:02">[00:42:02]</a>.

### Open Source Models for Robotics
Liang believes that robotics is currently in a "BERT era" rather than a "ChatGPT moment" <a class="yt-timestamp" data-t="00:50:27">[00:50:27]</a>. While vision-language models for robotics are effective, they still require fine-tuning for narrow tasks, and the resulting policies remain brittle <a class="yt-timestamp" data-t="00:50:39">[00:50:39]</a>. He is optimistic for the future, noting increased interest and funding, along with data collection efforts <a class="yt-timestamp" data-t="00:51:07">[00:51:07]</a>. He hopes that many so-called robotics problems will ultimately be solvable as language and vision problems, leveraging existing infrastructure <a class="yt-timestamp" data-t="00:52:19">[00:52:19]</a>.

### [[AI applications in sports analytics|AI in Music]]
As a classical musician, Liang observes that the same "giant transformer, some data" recipe is effective in [[AI product market fit and emerging applications|AI music]] <a class="yt-timestamp" data-t="00:53:16">[00:53:16]</a>. However, he highlights challenges:
*   **Copyright**: A significant hurdle <a class="yt-timestamp" data-t="00:53:28">[00:53:28]</a>.
*   **Control**: His work on the "Anticipatory Music Transformer" focuses on models that allow users to control generation (e.g., conditioning on melody to generate harmony, or infilling sections) rather than just unconditional or text-to-music generation <a class="yt-timestamp" data-t="00:53:38">[00:53:38]</a>.

He envisions [[AI product market fit and emerging applications|AI music]] as a co-pilot for musicians, similar to GitHub Co-pilot for programmers, helping artists realize their musical visions <a class="yt-timestamp" data-t="00:54:35">[00:54:35]</a>.

### [[AI powered tutoring tools|AI in Education]]
Liang is bullish on the use of AI as teachers and coaches, particularly for explaining complex concepts simply, citing its effectiveness in teaching children <a class="yt-timestamp" data-t="00:56:20">[00:56:20]</a>.

## Broader AI Landscape and Future Outlook

### Holistic View of AI and Safety
Liang believes that many [[AI research and development|AI researchers]] narrowly focus on the model as the central object <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>. He advocates for a more holistic perspective, viewing the model as one piece of a larger ecosystem with various actors and incentives <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>. For AI safety, the goal should be to ensure the entire system is safe, not just the model <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a>.

He argues that bad actors can circumvent model-level safety measures by decomposing problems (e.g., generating personalized email content separately for a phishing attack) <a class="yt-timestamp" data-t="00:16:29">[00:16:29]</a>. More investment is needed in "defense" mechanisms like anti-spam filters and anti-fraud detectors, analogous to dual-use technologies like email or the internet <a class="yt-timestamp" data-t="00:17:22">[00:17:22]</a>. Gating access to models is a losing battle as they become cheaper and widespread, but defense measures can secure the ecosystem <a class="yt-timestamp" data-t="00:17:55">[00:17:55]</a>.

### Regulation
Liang emphasizes that it is still very early in AI's development, and much is not understood, making heavy-handed regulation challenging <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a>. He supports regulation that focuses on transparency and disclosure, as understanding risks and benefits is the first step <a class="yt-timestamp" data-t="00:20:11">[00:20:11]</a>. With everything currently "closed off," it's hard for policymakers, researchers, or third-party auditors to understand what's happening <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a>. He suggests "nutrition labels" or spec sheets for AI models to inform downstream product developers <a class="yt-timestamp" data-t="00:21:49">[00:21:49]</a>.

He questions whether regulation should occur "upstream" (Foundation model developers) or "downstream" (end products) <a class="yt-timestamp" data-t="00:20:59">[00:20:59]</a>. While sectoral regulation (e.g., in finance or healthcare) is effective for visible harms, heavy-handed upstream regulation can be blunt or ineffective <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a>.

### Meaningful Milestones for AI
Liang identifies several meaningful milestones for AI progress:
*   **Current Benchmarks**: Continual improvement on existing benchmarks like SideBench for cybersecurity or ML Agent Bench for ML research tasks <a class="yt-timestamp" data-t="00:47:41">[00:47:41]</a>.
*   **Extending Human Knowledge**: Solving open math problems, creating new research, or discovering something new that hasn't been solved by humans, such as finding a zero-day exploit in cybersecurity <a class="yt-timestamp" data-t="00:48:22">[00:48:22]</a>. This represents a shift from mimicking human experts to extending human knowledge <a class="yt-timestamp" data-t="00:48:46">[00:48:46]</a>.
*   **[[AI coding and software engineering advancements|Coding Productivity]]**: AI's ability to create new code and help people code is a simpler version of how it can aid research <a class="yt-timestamp" data-t="00:58:43">[00:58:43]</a>.

He believes progress is still moving quickly, with qualitative changes like O1's approach to computation and continuous advancements in chip power driving the entire ecosystem <a class="yt-timestamp" data-t="00:49:26">[00:49:26]</a>.

### Underexplored Application Areas
Liang suggests that while many [[AI product market fit and emerging applications|AI applications]] are driven by commercial needs (e.g., RAG solutions, Q&A, summarization), areas like fundamental science, scientific discovery, and improving researcher productivity are currently underexplored <a class="yt-timestamp" data-t="00:59:02">[00:59:02]</a>. These areas are crucial because they can "feed into the whole cycle of improving the whole ecosystem" <a class="yt-timestamp" data-t="00:59:34">[00:59:34]</a>.

### Overhyped and Underhyped
*   **Overhyped**: Agents <a class="yt-timestamp" data-t="00:57:05">[00:57:05]</a>.
*   **Underhyped**: Agents <a class="yt-timestamp" data-t="00:57:05">[00:57:05]</a>.
    *   Liang clarifies that while agents have gone through a hype cycle, the potential for ML agents to contribute novel insights to ML work (e.g., running experiments) is not far off <a class="yt-timestamp" data-t="00:57:11">[00:57:11]</a>. He is optimistic that models can meaningfully contribute to research in the coming years <a class="yt-timestamp" data-t="00:58:33">[00:58:33]</a>.