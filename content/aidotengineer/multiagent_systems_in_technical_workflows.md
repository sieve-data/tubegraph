---
title: Multiagent systems in technical workflows
videoId: RR5le0K4Wtw
---

From: [[aidotengineer]] <br/> 

[[Multiagent Systems and Their Applications | Multiagent systems]] are gaining prominence in technical workflows, offering enhanced capabilities beyond traditional single-agent or Retrieval Augmented Generation (RAG) approaches. They are particularly useful for tackling complex, multi-step tasks and integrating diverse data sources.

## Definition and Purpose
A [[Multiagent Systems and Their Applications | multi-agent system]] can be understood as a collection of agents that interact and collaborate to achieve a common goal <a class="yt-timestamp" data-t="03:01:01">[03:01:01]</a>. For Yhar.ai, [[Multiagent Systems and Their Applications | multi-agent systems]] are used to break down complex white-collar workflows, such as those in the legal industry, into specific, testable steps. Each step can have different requirements, frequencies, and states, often controlled by a graph <a class="yt-timestamp" data-t="03:10:01">[03:10:01]</a>.

## Applications and Use Cases

### AI Copilot Development
[[Multiagent orchestration for AI copilot development | Multiagent orchestration]] can be used for developing AI copilots by handling complex taxonomies and decision-making processes <a class="yt-timestamp" data-t="03:00:01">[03:00:01]</a>.

### Network Analysis
Cisco's outshift group uses [[Multiagent Systems and Their Applications | multi-agent systems]] to address challenges in network change management, aiming to reduce failures in production environments <a class="yt-timestamp" data-t="02:47:17">[02:47:17]</a>. This includes tasks like impact assessment, testing, and reasoning about potential network failures <a class="yt-timestamp" data-t="02:48:39">[02:48:39]</a>. The system integrates a natural language interface, a [[MultiAgent Communication Systems | multi-agent system]], and a network knowledge graph (digital twin) <a class="yt-timestamp" data-t="02:48:49">[02:48:49]</a>.

Key aspects of Cisco's approach include:
*   **Data Ingestion:** Processing data from various sources (controllers, SIM systems, telemetry) and transforming it into a standardized schema like OpenConfig <a class="yt-timestamp" data-t="02:53:08">[02:53:08]</a>.
*   **Layered Graph Structure:** The knowledge graph is built in layers, allowing agents to access specific information efficiently without traversing the entire graph for every task (e.g., accessing raw configuration files for drift checks or multiple layers for reachability tests) <a class="yt-timestamp" data-t="02:54:18">[02:54:18]</a>.
*   **Agent Interaction:** An "assistant agent" orchestrates tasks among other agents, such as a "query agent" that directly interacts with the knowledge graph <a class="yt-timestamp" data-t="02:57:04">[02:57:04]</a>.
*   **Performance Optimization:** Fine-tuning the query agent with schema information and example queries significantly reduced token consumption and retrieval time, improving efficiency compared to initial RAG attempts <a class="yt-timestamp" data-t="02:57:48">[02:57:48]</a>.
*   **Standardization:** Cisco is working on an open-source collective, Agency.org, to enable agents from different systems and vendors to communicate and integrate without heavy re-engineering <a class="yt-timestamp" data-t="02:55:02">[02:55:02]</a>.

### Legal Industry Workflows
Yhar.ai uses [[Multiagent Systems and Their Applications | multi-agent systems]] to automate complex workflows in the legal industry, particularly for finding class action and mass tort cases <a class="yt-timestamp" data-t="03:07:03">[03:07:03]</a>. Their process involves:
*   **Web Scraping:** Mass scraping of the web to gather information <a class="yt-timestamp" data-t="03:18:43">[03:18:43]</a>.
*   **Lead Qualification:** Filtering and structuring scraped data based on specific schemas provided by law firms <a class="yt-timestamp" data-t="03:19:05">[03:19:05]</a>.
*   **Report Generation:** Creating personalized reports for lawyers, backed by consistent, pruned graph schemas <a class="yt-timestamp" data-t="03:20:01">[03:20:01]</a>.
*   **Legal Discovery:** Extracting and structuring information from large datasets like emails, which can then be augmented with visual graphs for expert review <a class="yt-timestamp" data-t="03:16:19">[03:16:19]</a>.
*   **Case Research:** Identifying complaint patterns for products (e.g., cars catching fire) by tracking language across various online sources, building a density of complaints for specific issues, and detecting leads significantly earlier than traditional methods <a class="yt-timestamp" data-t="03:21:00">[03:21:00]</a>.

### Agentic Firewalls in Cybersecurity
A proposed use case for [[Multiagent Systems and Their Applications | multi-agent systems]] is an "agentic firewall" that provides a human language shell for interacting with machines in cybersecurity <a class="yt-timestamp" data-t="02:02:21">[02:02:21]</a>. By plugging in [[agentic_workflows_and_their_levels_of_autonomy | agentic memory]] (temporal/episodic memory of shell history and machine context), agents can understand user behavior and control code execution <a class="yt-timestamp" data-t="02:02:48">[02:02:48]</a>. This system would ensure that agents executing code in enterprise environments go through a controlled, secure pathway <a class="yt-timestamp" data-t="02:05:39">[02:05:39]</a>.

## Benefits and Advantages
*   **Handling Complex Tasks:** [[Multiagent Systems and Their Applications | Multi-agent systems]] excel at breaking down complex workflows into manageable, testable steps, each with specific requirements <a class="yt-timestamp" data-t="03:10:01">[03:10:01]</a>.
*   **Orchestration and Decision Making:** They provide a framework for orchestrating various tasks and enabling agents to make informed decisions <a class="yt-timestamp" data-t="03:00:01">[03:00:01]</a>.
*   **Accuracy and Control:** In fields requiring high accuracy, like legal applications, [[Multiagent Systems and Their Applications | multi-agent systems]] allow for precise control, structure, and schema, enabling pinpoint testing of what goes right or wrong at any point in time <a class="yt-timestamp" data-t="03:10:40">[03:10:40]</a>.
*   **Contextual Understanding:** By integrating with knowledge graphs, agents can leverage rich contextual information and relationships, which is crucial for tasks like competitive analysis <a class="yt-timestamp" data-t="03:01:01">[03:01:01]</a>.
*   **Scalability:** An open framework for building agents is considered critical for scalable systems <a class="yt-timestamp" data-t="03:59:57">[03:59:57]</a>.
*   **Overcoming LLM Limitations:** [[Multiagent Systems and Their Applications | Multi-agent systems]] help mitigate the probabilistic nature of LLMs by imposing structure and allowing for specific control <a class="yt-timestamp" data-t="03:10:34">[03:10:34]</a>.

## Challenges and Considerations
*   **Workflow Imbalances:** Some parts of a [[agentic_workflows_and_their_levels_of_autonomy | multi-agent workflow]] might be more critical or complex than others <a class="yt-timestamp" data-t="03:11:02">[03:11:02]</a>.
*   **Agent Quality:** The effectiveness of a [[Multiagent Systems and Their Applications | multi-agent system]] depends on the quality of individual agents. A poorly designed prompt can lead to a "bad agent" <a class="yt-timestamp" data-t="03:11:12">[03:11:12]</a>.
*   **Accuracy Chaining:** The cumulative accuracy of sequentially chained agents can drop significantly, as a 95% accurate agent chained five times yields only 77% expected accuracy <a class="yt-timestamp" data-t="03:12:16">[03:12:16]</a>. This highlights the challenge of decision-making under uncertainty <a class="yt-timestamp" data-t="03:12:39">[03:12:39]</a>.
*   **Evaluation:** Establishing quantifiable metrics for evaluating the performance of [[Multiagent Systems and Their Applications | multi-agent systems]], especially in combination with knowledge graphs and digital twins, is an ongoing learning process <a class="yt-timestamp" data-t="03:03:19">[03:03:19]</a>.
*   **Integration with Existing Systems:** Ensuring seamless [[Integration of AI agents into existing infrastructure | integration of AI agents into existing infrastructure]] and support for multiple vendors is crucial for adoption <a class="yt-timestamp" data-t="02:51:48">[02:51:48]</a>.

## Integration with Other AI Components
*   **Knowledge Graphs:** [[Multiagent Systems and Their Applications | Multi-agent systems]] frequently leverage knowledge graphs to manage state, provide structure, and control information across workflow steps <a class="yt-timestamp" data-t="03:10:12">[03:10:12]</a>.
*   **LLMs:** LLMs can be used to "glue" together predefined tasks within [[Multiagent Systems and Their Applications | multi-agent systems]] <a class="yt-timestamp" data-t="03:09:56">[03:09:56]</a> or to translate commands into human language <a class="yt-timestamp" data-t="02:02:16">[02:02:16]</a>. However, LLMs alone might not be sufficient for workflows demanding high accuracy <a class="yt-timestamp" data-t="03:10:34">[03:10:34]</a>.
*   **RAG (Retrieval Augmented Generation):** While some initial attempts might use RAG for knowledge graph querying, fine-tuning specific agents can offer significant performance improvements in terms of tokens consumed and response time <a class="yt-timestamp" data-t="02:57:48">[02:57:48]</a>.
*   **Episodic Memory:** The concept of [[agent_continuations_for_ai_workflows | agent continuations]] with episodic or temporal memory, like in "agentic firewalls," allows agents to track historical events and user behaviors within a shell, providing crucial context for decision-making and security <a class="yt-timestamp" data-t="02:03:26">[02:03:26]</a>.
*   **Simulation Arenas:** Since the evolution of [[agentic_workflows and their levels of autonomy | agentic graph memory]] is unpredictable, simulation arenas (like a "web arena but for memory") are necessary for evaluating and optimizing [[evaluating_and_optimizing_ai_agents_and_workflows | AI agents and workflows]] <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>.