---
title: Efficiency and smart execution in AI systems
videoId: Th5e4h-oVmc
---

From: [[aidotengineer]] <br/> 

Traditional large language models (LLMs) often struggle with complex instruction following, especially when prompts become convoluted with extensive context, constraints, and requirements [00:00:19][00:01:02][00:01:14]. Even for seemingly simple tasks, LLMs alone are often insufficient [00:01:14][00:07:21]. This challenge highlights the need for more sophisticated approaches, leading to the development of AI agents.

## The Role of AI Agents

AI agents extend beyond simple prompting, incorporating "planning" as a core capability [00:01:21][00:01:24][00:01:26]. From an engineering perspective, an agent is simply "whatever works" to achieve a goal, regardless of its philosophical definition [00:01:45][00:01:48][00:02:30].

Various concepts are sometimes referred to as "agents" due to their expanded capabilities:
*   **LLM as a Router** A routing model directs queries to specialized LLMs [00:01:53][00:01:57].
*   **Function Calling** LLMs are provided with external tools or APIs they can use to interact with the world, such as Google search [00:02:08][00:02:10][00:02:13][00:02:15].
*   **ReAct (Reason and Act)** This popular framework allows any language model to engage in a thought-action-observation loop [00:02:39][00:02:41][00:02:45][00:02:49]. However, ReAct processes one step at a time, lacking a "look ahead" to an entire plan [00:03:00][00:03:02].

## The Importance of Planning

Planning is crucial for AI agents, especially when dealing with complex, non-straightforward problems [00:03:20][00:03:26][00:03:28]. It involves figuring out the necessary steps to reach a goal [00:03:20][00:03:22].

Key benefits of planning include:
*   **Parallelization** Enables tasks to be executed concurrently [00:03:31].
*   **Explainability** Unlike ReAct, planning allows for a clearer understanding of why certain steps were taken [00:03:33][00:03:36].
*   **Dynamic Planning** The ability to replan mid-execution if the initial plan proves suboptimal or if circumstances change [00:03:56][00:03:57][00:04:00][00:04:09].

Planners can be [[effective_design_of_ai_in_products | form-based]] (like text-based or semantic planners) or code-based [00:03:43][00:03:47][00:03:50][00:03:52].

## Smart Execution for Efficiency

For a planner to be effective, it requires a robust execution engine [00:04:19][00:04:22]. This engine is vital for [[cost_and_efficiency_in_deploying_ai_systems | efficiency improvements with AI in financial analysis]] and overall system performance.

A smart execution engine can:
*   **Analyze Dependencies** Determine relationships between steps to enable parallel execution [00:04:24][00:04:26].
*   **Manage Trade-offs** Optimize between speed and cost [00:04:29][00:04:31]. For instance, branch prediction can be used for faster systems [00:04:34][00:04:37].

## AI21 Mastro: A Case Study

AI21 Mastro is an example system that combines a planner with a smart execution engine to enhance performance [00:04:40][00:04:43][00:04:47].

In a simplified instruction-following scenario, Mastro separates the prompt (context and task) from explicit requirements (e.g., paragraph limits, tone, brand mentions) [00:04:49][00:04:53][00:04:55][00:04:58][00:05:01][00:05:03][00:05:05][00:05:07]. This separation makes validation easier [00:05:12][00:05:13].

The system uses an execution graph or tree where the planner and execution engine:
*   Choose several candidate solutions at each step [00:05:15][00:05:18][00:05:20][00:05:23][00:05:26].
*   Continue to refine and improve only the most promising candidates [00:05:26][00:05:29].
*   Employ techniques like "best of N," sampling multiple generations from an LLM (or different LLMs) and pursuing only the best candidates based on a predefined budget [00:05:32][00:05:34][00:05:36][00:05:38][00:05:41][00:05:44][00:05:49][00:05:51][00:05:53][00:05:56].
*   Incorporate validation and iteration to continuously refine results [00:05:59][00:06:01][00:06:03].

For more complex scenarios, the execution engine tracks expected cost, latency, and success probability, allowing the planner to choose the most [[costeffective_ai_strategies | cost-effective AI strategies]] and optimal path [00:06:07][00:06:09][00:06:12][00:06:15][00:06:18][00:06:20][00:06:22][00:06:26]. Ultimately, multiple results are "reduced" (combined or selected) to form a complete answer [00:06:30][00:06:33][00:06:34][00:06:37].

## Results and Takeaways

Implementing planning and smart execution engines significantly improves results compared to single LLM calls, as demonstrated by higher accuracy scores on evaluation datasets like "ifval" and "requirement satisfaction" [00:06:42][00:06:45][00:06:48][00:06:51][00:06:54][00:06:56][00:07:00][00:07:02][00:07:04][00:07:06][00:07:08][00:07:10]. While this often incurs slightly more runtime and cost, the increase in quality justifies it [00:07:12][00:07:13][00:07:16][00:07:19].

### [[best_practices_for_building_ai_systems | Best Practices for Building AI Systems]] and [[best_practices_for_ai_deployment_and_optimization | Best Practices for AI Deployment and Optimization]]

*   **Start Simple** For simple tasks, LLMs alone or LLMs with basic tools might suffice [00:07:27][00:07:30][00:07:32][00:07:35][00:07:38].
*   **Progressive Complexity** Use ReAct for moderately complex tasks [00:07:41].
*   **Advanced Solutions for Complex Tasks** For highly complex tasks, adopting a planning and execution engine framework is necessary to achieve desired outcomes and support [[continuous_improvement_in_ai_systems | continuous improvement in AI systems]] [00:07:43][00:07:46][00:07:48][00:07:51]. This approach is crucial for [[building_scalable_ai_systems | building scalable AI systems]] and adheres to [[best_practices_for_ai_evaluation | best practices for AI evaluation]].