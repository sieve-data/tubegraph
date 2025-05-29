---
title: causality in agentbased systems
videoId: 8yWKQqNFrmY
---

From: [[causalpython]] <br/> 

[[Causality in AI | Causality]] is predicted to become increasingly important for agents as they begin to interact in the real world or web environments [00:00:06]. These interactions introduce fundamental [[causality_in_ai | causal abstractions]] like notions of action, reward, and the optimization or penalization of behavior [00:00:25].

## Causal Questions and Abstractions for Agents

As agents interact, new [[causal reasoning in AI | causal questions]] will emerge. These include determining which agent is most useful, which agent should receive more rewards, and counterfactual notions of blame [00:05:27]. If agents within a system are underperforming, the ability to identify and address this through [[causal reasoning in AI | causal principles]] will be crucial for their improvement or removal [00:00:34].

Research from Google DeepMind, by Richardson and Everett, has proposed a theory for how agents can learn robust world models [00:00:43]. These ideas primarily revolve around interventional distributions, where an intervention is made in an environment, and the agent learns the response [00:00:57].

## Pathways to Causal Agents

There are multiple ways to develop agents that can act causally:

### Learning from Diverse Data
One approach suggests that if an agent is exposed to a sufficiently diverse set of environments and aims to perform well in all of them, it can learn actions that mimic a true [[causality_in_ai | causal agent]], even without explicit knowledge of a world model [00:07:27]. Theoretical abstractions even suggest that the underlying world model can be recovered by observing these actions [00:07:55]. This highlights the power of diverse data in imparting [[causality_in_ai | causality]] and discovering causal relationships [00:08:12].

### Leveraging Domain Knowledge and Axioms
Another way involves building an agent's foundation on existing domain knowledge, theorems, and axioms [00:10:56]. This allows the agent to apply known rules, similar to how large language models (LLMs) answer causal questions by having "read books" containing physics theorems [00:10:26]. This method avoids the difficult learning process of discovering principles from scratch, instead enabling the agent to adapt easily by knowing the context [00:14:19].

## Missing Pieces in Agentic Frameworks: Verification

A significant challenge in contemporary agentic frameworks is the lack of robust verification mechanisms [00:14:42]. While current frameworks work well in controlled environments like coding (where compilers act as verifiers) or API calls (where failures provide clear signals), they struggle in vague, real-world problems where human feedback is insufficient or not scalable [00:15:27].

For agents to function effectively, there's a need to:
*   Create verifiers for new domains, initially for outcomes, and later for individual actions an agent takes [00:15:42].
*   Design systems from the ground up that behave as intended [00:05:56].

The open-source library DoWhy and its newer modules, like `econml`, have been developed to address the [[causal inference in practical applications | assessment, evaluation, and verification]] of causal models [00:17:46]. DoWhy's approach draws from how economists and social scientists evaluate studies, focusing on robustness checks and identifying "placebos" or "negative controls" to validate causal claims [00:19:09]. These involve:
*   **Sensitivity analysis:** Testing what happens if an unobserved confounder was missed [00:20:05].
*   **Negative controls:** Removing elements not thought to matter and re-running experiments to ensure the cause-effect relationship holds [00:20:44].
*   **Dummy outcomes:** Creating outcomes known not to be caused by treatment, expecting a causal effect of zero [00:21:31].
*   **Graph verification:** Comparing the informativeness of a causal graph against a random graph and checking conditional independencies [00:22:52].

This emphasis on verification is crucial because if initial assumptions in the causal graph are incorrect, subsequent analysis can be flawed [00:23:09].

## How Causality Can Enhance LLMs and Agents

The integration of [[integration of language models and causality | language models and causality]] is a promising area. While LLMs can streamline the process of building initial causal graphs by providing domain knowledge [00:32:53], they are prone to "hallucinations," making full automation risky where accuracy is critical [00:35:18].

However, [[causality_in_ai | causality]] can also make LLMs more robust. Instead of directly imparting complex causal knowledge, the focus is on teaching LLMs *how to learn causal knowledge* [00:38:55]. This involves training them on basic causal axioms (like transitivity or d-separation) [00:39:12]. Early results show that models trained on these axioms can generalize to larger graphs and improve performance on other causal tasks, suggesting a different way of imparting [[causal reasoning in AI | reasoning]] to these models without relying on memorization [00:40:13]. This research is inspired by the idea of learning active causal strategies from passive data [00:43:11].

## Challenges and Future Directions

A significant technical challenge in [[causality_in_ai | causality]] today is to develop "model-free" approaches, similar to model-free reinforcement learning [00:48:23]. This requires building new causal theory to extract maximum information from data while still providing the guarantees typically associated with model-based approaches [00:48:52].

A key concept in this area is "exchangeable distributions," which assumes data comes from many diverse environments [00:49:37]. If we can leverage such data, where the causal mechanism remains static across environments, it could unlock richer identification results and help address why [[causal inference in practical applications | causality]] isn't more broadly used [00:50:27]. This "still point in the turning world" analogy from T.S. Eliot emphasizes finding invariant causal structures despite varying observations [00:53:11].

Sociologically, the "bitter lesson for [[causality_in_ai | causality]]" suggests that while [[causality_in_ai | causality]] is the desired end result, it may not always be the means to achieve it [01:51:56]. Alternative methods, like data augmentation (which is not inherently causal), could lead to causal outcomes [01:52:49].

The future of [[causality in agentbased systems | causality in agent-based systems]] will involve:
*   **Scalable tools**: Building tools to help scientists use LLMs to generate graphs from literature, plan experiments, and accelerate the scientific cycle [01:08:11].
*   **Democratizing access**: Making causal inference accessible to non-experts through user-friendly systems like PY LLM, where text inputs lead to causal answers using advanced libraries [00:29:56].
*   **Community Contributions**: Encouraging contributions to open-source projects like PY from researchers and practitioners alike, especially real-world use cases [01:09:19].

Ultimately, in an LLM-driven agent world, [[causality_in_ai | causality]] will be paramount, requiring new ways of thinking about rewards, blame, and constraints for agent behavior [01:07:39].