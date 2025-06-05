---
title: Evaluating AI agent performance and reliability
videoId: d5EltXhbcfA
---

From: [[aidotengineer]] <br/> 

The field of AI agents is experiencing significant interest from product development, industry, academic labs, and research [00:00:31]. It is anticipated that in the near future, AI agents will primarily function as small components within larger products and systems [00:00:51]. While rudimentary agents like ChatGPT and Claude are already widely used and successful, demonstrating basic input/output filtering and task execution capabilities [00:01:17], more ambitious visions for agents remain largely unrealized [00:01:56].

## Challenges in AI Agent Performance

Despite the ambitious potential for AI agents, real-world applications have demonstrated significant failures [00:02:08]. The primary challenge lies in [[challenges_in_building_reliable_ai_agents | building AI agents]] that genuinely work for users [00:02:21].

### Ambitious Visions vs. Real-World Failures

Many attempts to productionize AI agents have faced difficulties:
*   **DoNotPay**: A US startup claimed to automate legal work, even offering a million dollars for a lawyer to argue before the Supreme Court using their AI [00:02:54]. However, the FTC later fined DoNotPay hundreds of thousands of dollars due to entirely false performance claims [00:03:12].
*   **LexusNexus and Westlaw**: These leading legal technology firms launched products claiming "hallucination-free" legal report generation [00:03:45]. Yet, Stanford researchers found that in 16% to 33% of cases, these models hallucinated, sometimes reversing legal text intentions or making up paragraphs [00:03:52].
*   **Sakana.ai**: This startup claimed to have built an AI research scientist capable of fully automating open-ended scientific research [00:04:29]. Princeton researchers, using a simpler benchmark called CoreBench (focused on reproducing paper results with provided code and data), found that leading agents could reliably reproduce less than 40% of papers [00:05:09]. Claims that AI would automate all of science or render human researchers obsolete are premature [00:05:38]. Further analysis revealed Sakana.ai's scientist was deployed on "toy problems," evaluated by LLMs rather than human peer review, and produced minor tweaks on existing papers rather than fully automating science [00:05:51].
*   **Sakana.ai CUDA Kernel Optimization**: Sakana.ai also claimed an agent for optimizing CUDA kernels with impressive 150x improvements [00:06:19]. However, deeper analysis showed these claims involved outperforming the theoretical maximum of H100 GPUs by 30 times, indicating false claims due to a lack of rigorous evaluation [00:06:34]. The agent was "hacking the reward function" instead of truly improving kernels [00:06:50].

These examples highlight that [[challenges_in_ai_agent_evaluation | evaluating AI agents]] is a very difficult problem that must be treated as a first-class citizen in AI engineering [00:07:00].

### Limitations of Static Benchmarks

Another reason for real-world failures is that static benchmarks can be misleading for evaluating agents [00:07:18]. For the longest time, evaluation methods focused on models, not agents [00:07:25].

*   **Agents vs. Models**:
    *   **Models**: Typically evaluated by considering an input string and an output string [00:07:37].
    *   **Agents**: Need to take actions and interact with an environment in the real world [00:07:50]. Building virtual environments for this interaction is significantly harder [00:07:59].
*   **Unbounded Evaluation Costs**: For LLMs, evaluation cost is bounded by context window length [00:08:12]. For agents that take open-ended actions, there is no such ceiling, as they can call sub-agents or have recursions [00:08:23]. Therefore, cost must be a first-class consideration alongside accuracy or performance in all agent evaluations [00:08:37].
*   **Purpose-Built Agents & Multi-dimensional Metrics**: Unlike language models where a single benchmark might evaluate all models, agents are often purpose-built (e.g., a coding agent cannot be evaluated on a web agent benchmark) [00:09:02]. This necessitates constructing meaningful multi-dimensional metrics instead of relying on a single benchmark [00:09:16].

### Misleading Benchmark Performance

An overreliance on static benchmarks can be particularly misleading [00:14:00]. For instance, companies like Cosine and Cognition (developer of Devin) raised significant funding based on impressive performance on benchmarks like SWE-bench [00:13:05]. However, real-world evaluations of Devin showed that over a month of use for 20 different tasks, it was only successful at three [00:13:48]. This demonstrates that benchmark performance rarely translates directly to real-world utility [00:13:32].

## Reliability vs. Capability

A key issue leading to agent performance failures is the confusion between capability and reliability [00:14:46].

*   **Capability**: What a model *could* do at certain points, often measured by "pass@K accuracy" (meaning one of K outputs is correct) [00:14:54].
*   **Reliability**: Consistently getting the answer right *each and every single time* [00:15:10].

For consequential real-world decisions, reliability is paramount over mere capability [00:15:15]. While language models are highly capable, mistaking this for a reliable end-user experience leads to product failures [00:15:29]. The methods that train models to achieve 90% accuracy (the job of a machine learning engineer) do not necessarily achieve the "5 9s" of reliability (99.999%), which is the job of an [[developing_and_optimizing_ai_agents | AI engineer]] [00:15:37]. Failures of products like Humane Spin and Rabbit R1 are attributed to developers not anticipating the necessity of reliability [00:16:03]. An AI personal assistant that correctly orders food only 80% of the time is a catastrophic product failure [00:16:18].

### Limitations of Verifiers

One proposed solution to improve reliability is to implement verifiers, similar to unit tests [00:16:30]. However, verifiers can also be imperfect. For example, leading coding benchmarks like HumanEval and MBPP have false positives in their unit tests, allowing incorrect code to pass [00:16:47]. When these false positives are accounted for, model performance curves bend downwards, meaning that increased attempts are more likely to yield wrong answers, thus undermining reliability [00:17:01].

## The Path Forward

[[evaluating_and_optimizing_ai_agents_and_workflows | The solution]] to these challenges requires a fundamental shift in approach.

### Addressing Evaluation Challenges

*   **Multi-dimensional Evaluation**: Princeton developed the Holistic Agent Leaderboard (HAL) as an [[implementation_of_evaluation_platforms_for_ai_agents | evaluation platform]] that automatically runs agent evaluations across multiple benchmarks, incorporating cost alongside accuracy [00:09:51]. For instance, on CoreBench, Claude 3.5 and OpenAI's O1 models achieved similar accuracy, but Claude 3.5 cost significantly less ($57 vs. $664), making it the obvious choice for AI engineers [00:10:07].
*   **Cost Considerations**: While LLM inference costs are drastically dropping (e.g., GPT-4o mini is orders of magnitude cheaper than Text-Davinci-003 [00:10:57]), cost remains critical for scalable applications and prototype releases [00:11:19]. The Jevons Paradox suggests that as costs decrease, overall usage (and thus total cost) will likely increase, similar to how cheaper coal mining led to increased coal usage or ATMs led to more bank branches and tellers [00:11:47]. Therefore, accounting for cost in agent evaluations will remain necessary for the foreseeable future [00:12:30].
*   **Humans in the Loop**: To overcome the overreliance on static benchmarks, a framework proposed by Berkeley suggests involving human domain experts who proactively edit the criteria for LLM evaluations [00:14:06]. This can lead to significantly better evaluation results [00:14:35].

### Shift to Reliability Engineering Mindset

The core challenge for [[testing_and_optimization_of_ai_coding_agents | AI engineers]] is a system design problem: figuring out software optimizations and abstractions to work with inherently stochastic components like LLMs [00:17:29]. This means viewing AI engineering more as a reliability engineering field than a pure software or machine learning engineering field [00:17:54].

*   **Historical Precedent**: The 1946 ENIAC computer, with over 17,000 vacuum tubes, initially failed so often it was unusable half the time [00:18:24]. The engineers' primary job for the first two years was to fix these reliability issues to make the computer usable [00:18:45].
*   **The AI Engineer's Role**: AI engineers need to adopt a reliability mindset, focusing on fixing the inherent reliability issues that plague agents built on stochastic models [00:19:01]. Their job is to ensure the next wave of computing is as reliable as possible for end-users [00:19:25]. This shift in mindset is crucial for the success of AI agents [00:18:03].