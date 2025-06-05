---
title: Agent continuations for AI workflows
videoId: ZB7l4uxW3Yo
---

From: [[aidotengineer]] <br/> 

Agent continuations represent a novel mechanism developed at Snaplogic for managing agent state and facilitating [[integrating_ai_into_natural_workflows | human-in-the-loop]] processing within [[ai_in_workflow_automation_and_augmentation | AI workflows]] <a class="yt-timestamp" data-t="00:34:34">[00:34:34]</a>. This approach allows for the capture of the [[stateful_ai_agents | full state]] of complex agents, enabling arbitrary human and loop processing, and providing a basis for reliable agent continuation through snapshots <a class="yt-timestamp" data-t="00:50:07">[00:50:07]</a>.

## Challenges with Modern AI Agents

As agents move into [[scaling_ai_agents in production | production settings]], several [[benefits_and_challenges_of_using_ai_in_workflow | challenges]] arise <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>:

*   **Human Oversight and Approval**
    Agents often require human approval during their processing steps, especially for high-value or high-risk tasks such as transferring money or deleting accounts <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>. Key aspects of agent execution need some amount of human oversight to ensure comfort with [[automation_of_manual_workflows_with_ai_web_agents | agent automation]] <a class="yt-timestamp" data-t="00:29:00">[00:29:00]</a>.
*   **Long-Running Agents and Failure Tolerance**
    Many agents are designed to be long-running, involving numerous steps <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>. The longer a process runs, the greater the chance of failure <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>. A mechanism is needed to prevent the loss of work and allow agents to checkpoint their [[stateful_ai_agents | state]] for resumption from a specific point rather than restarting from the beginning <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>.
*   **Distributed Environments**
    Increasingly, agents operate in distributed environments beyond a single desktop <a class="yt-timestamp" data-t="00:40:00">[00:40:00]</a>. Considerations for running agents scalably in such environments are essential <a class="yt-timestamp" data-t="00:48:00">[00:48:00]</a>.
*   **Multi-level Agents**
    Sophisticated agent configurations often involve a main "orchestrator" agent with multiple sub-agents, which themselves can have sub-agents <a class="yt-timestamp" data-t="06:00:00">[00:06:00]</a>. Addressing human approval and state saving in the presence of these complex [[multiagent_orchestration_for_ai_copilot_development | multi-level agents]] is a significant challenge <a class="yt-timestamp" data-t="06:30:00">[00:30:00]</a>.
*   **Agent Loop Persistence**
    Most current frameworks require the agent loop to run continuously, even when waiting for human input <a class="yt-timestamp" data-t="07:23:00">[00:23:00]</a>. This requires continuous physical machine resources <a class="yt-timestamp" data-t="07:03:00">[00:07:03]</a>. A solution is needed to allow the agent loop to be fully shut down and restarted later <a class="yt-timestamp" data-t="07:56:00">[00:56:00]</a>.

## Basic Agent Execution

An agent typically operates as a loop involving calls to a Large Language Model (LLM) that specify potential tools <a class="yt-timestamp" data-t="03:01:00">[03:01:00]</a>. If the LLM decides to use a tool, it returns to the agent loop, which then calls the tool, collects results, and sends them back to the LLM in a progressive cycle <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>. A tool can also be an agent itself, forming a sub-agent relationship <a class="yt-timestamp" data-t="03:31:00">[03:31:00]</a>. Even simple agents involve significant interaction with LLMs and tools <a class="yt-timestamp" data-t="03:53:00">[03:53:00]</a>.

## Agent Continuations Explained

Inspired by the programming language concept of continuations, agent continuations enable pausing agent execution, saving its [[stateful_ai_agents | state]], and then resuming or continuing execution from that point at a later time <a class="yt-timestamp" data-t="08:11:00">[08:11:00]</a>. This allows for a snapshot of the agent's execution <a class="yt-timestamp" data-t="08:49:00">[08:49:00]</a>.

### Key Insight: Leveraging the Messages Array

A core insight behind agent continuations is that interactions with LLMs in agents already maintain a "messages array," which serves as a log of all interactions <a class="yt-timestamp" data-t="10:04:00">[10:04:00]</a>. This history is replayed back to the LLM for its next inference <a class="yt-timestamp" data-t="10:24:00">[10:24:00]</a>. While not entirely sufficient, this array already captures much of the agent's [[stateful_ai_agents | state]] <a class="yt-timestamp" data-t="11:00:00">[11:00:00]</a>.

### Implementation and Usage

To use agent continuations, a `continuation agent class` is utilized instead of a standard agent class <a class="yt-timestamp" data-t="12:50:00">[12:50:00]</a>. Tools can be designated as needing approval <a class="yt-timestamp" data-t="12:37:00">[12:37:00]</a>.

When an agent needs to suspend (e.g., for [[implementation_and_benefits_of_agent_continuations | human approval]] or another condition), it creates a "continuation object" <a class="yt-timestamp" data-t="13:16:00">[13:16:00]</a>.

This object:
*   Embeds the standard messages array.
*   Includes additional metadata, such as a `resume request` (indicating where to resume) and `processed` (to be populated with approval status) <a class="yt-timestamp" data-t="15:21:00">[15:21:00]</a>.
*   Is designed to be recursive, supporting arbitrary layers of nesting for [[multiagent_orchestration_for_ai_copilot_development | sub-agents]] <a class="yt-timestamp" data-t="18:20:00">[18:20:20]</a>.

The application layer inspects this object, provides necessary updates (like human approval), and then sends the continuation object back to the agent <a class="yt-timestamp" data-t="16:26:00">[16:26:00]</a>. The agent then reconstructs its [[stateful_ai_agents | state]] and resumes processing from the suspension point <a class="yt-timestamp" data-t="16:34:00">[16:34:00]</a>.

A significant benefit is that once the continuation object is created, the agent loops do not need to keep running; they can be shut down, as enough information has been captured to restart everything <a class="yt-timestamp" data-t="16:54:00">[16:54:00]</a>.

### Example Scenario: Multi-level HR Agent

Consider a multi-level HR agent where a top-level HR agent uses an email tool and an account agent sub-tool <a class="yt-timestamp" data-t="18:50:00">[18:50:00]</a>. The account agent itself has tools like "create account" and "authorize account," with "authorize account" requiring [[implementation_and_benefits_of_agent_continuations | human approval]] <a class="yt-timestamp" data-t="19:17:00">[19:17:00]</a>.

When the account agent reaches the "authorize account" tool, it suspends execution, creates a continuation object, and propagates it back to the application layer <a class="yt-timestamp" data-t="20:01:00">[20:01:00]</a>. The application layer processes the approval, updates the continuation object, and sends it back to the HR agent. The framework then restores the state of both the main agent and sub-agent, allowing processing to continue <a class="yt-timestamp" data-t="21:20:00">[21:20:00]</a>.

## Prototype and Future Directions

A prototype implementation of agent continuations has been built on top of the OpenAI Python API, with no other dependencies <a class="yt-timestamp" data-t="24:12:00">[24:12:00]</a>.

### Further Development:
*   **General Agent Suspension**: Implementation of more general agent suspension beyond just human approval, allowing for arbitrary suspension points based on time, turns, or asynchronous requests <a class="yt-timestamp" data-t="24:27:00">[24:27:00]</a>.
*   **Integration with Existing Frameworks**: The focus is on extending existing agent frameworks like Strands or Pydantic AI, rather than developing a separate framework <a class="yt-timestamp" data-t="24:50:00">[24:50:00]</a>.

While other frameworks have considered [[stateful_ai_agents | state]] management, this approach is novel in combining both a robust [[implementation_and_benefits_of_agent_continuations | human approval]] mechanism and support for arbitrary nesting of complex agents <a class="yt-timestamp" data-t="25:03:00">[25:03:00]</a>.

This work originated from the Agent Creator research group at Snaplogic, where the concept was prototyped both at the Python layer and within Snaplogic's visual agent building interface and platform, Agent Creator <a class="yt-timestamp" data-t="25:48:00">[25:48:00]</a>.