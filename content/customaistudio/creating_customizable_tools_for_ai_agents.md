---
title: Creating customizable tools for AI agents
videoId: dq9CtjloFAs
---

From: [[customaistudio]] <br/> 

This article provides a step-by-step guide on how to [[building_and_deploying_ai_agents | build]] a personal [[five_types_of_ai_agents_you_can_build | AI agent]] with customizable [[tools_and_resources_for_building_ai_agents | tools]] and the underlying philosophy behind their construction <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. The approach emphasizes understanding the functions, integrations, [[tools_and_resources_for_building_ai_agents | tools]], and components involved, along with the strategic mindset for [[building_and_deploying_ai_agents | building]] them <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## Agent Capabilities and Resources

A personal [[five_types_of_ai_agents_you_can_build | AI agent]] can be equipped with various [[tools_and_resources_for_building_ai_agents | tools]] to manage daily operations <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. The demonstrated agent can perform actions related to:
*   Email <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>
*   Calendar <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>
*   Google Drive <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>
*   Updating and accessing a database (specifically a vector database like Pinecone) <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>

Key [[tools_and_resources_for_building_ai_agents | resources]] for [[building_and_deploying_ai_agents | building]] these [[tools_and_resources_for_building_ai_agents | tools]] include:
*   n8n <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>
*   Pinecone (for the vector database) <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>
*   OpenAI API model (or any preferred language model) <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>

The agent can be connected to various communication channels, including Telegram (chosen for its ease of setup), Slack, Discord, email, SMS, WhatsApp, and Facebook <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

## Step-by-Step Tool Construction

### 1. Collect Your Data

The initial step involves collecting relevant data, which can be time-consuming, sometimes taking days <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. For a personal agent, this might involve extracting contacts from email and calendar, including names, email addresses, and company affiliations <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. This collected data populates a database that the agent can access to pull information when needed, such as an email address <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

### 2. Create Your Database and Upsert Data

This involves setting up a vector database, such as Pinecone <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.
*   Log in or create an account <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   Create an index, naming it appropriately (e.g., "data") <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
*   Set up the model, typically using a small embedding model <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
*   Retrieve your API key <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.

> [!NOTE] Data Capture Automations
> While it's possible to create a "hive mind" for agents by vectorizing all your data in a database, it's often more accurate for the agent to pull data directly from its original source (e.g., Google Drive, email, calendar) <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. This approach minimizes accuracy issues that can arise from chunking and batching methods used in vector databases <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. Therefore, data capture automations are not always necessary for building an [[five_types_of_ai_agents_you_can_build | agent]] <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.

### 3. Build Your Tools

This is the core of [[building_and_deploying_ai_agents | building]] custom [[tools_and_resources_for_building_ai_agents | tools]]. The philosophy is to give the agent access to the *platform* (e.g., all Gmail actions) rather than just a single action (e.g., send email), allowing the agent to decide what needs to be done <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.

#### **Common Elements for Tool Construction**
*   **Trigger Node**: Use a "When called by another workflow" node to allow the agent to invoke the tool <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.
*   **AI Node (GPT-4)**: Use an AI node to parse queries and output parameters separately <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
    *   **Prompt**: The system prompt should instruct the AI to "parse the query and output the parameters separately" <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.
    *   **Stringify Output**: Crucially, always wrap the AI node's output in `JSON.stringify()` to ensure the output is a string and not an object, preventing issues when passed to tools <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.
*   **Service-Specific Nodes**: Use nodes like Gmail, Google Calendar, Google Drive, or Pinecone to interact with the respective services.
*   **Parameter Mapping**: Drag the parsed parameters from the AI node to the corresponding fields in the service node <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>.
*   **Response Node**: Add a "Set" node at the end of the tool's workflow to provide a response back to the agent, confirming task completion (e.g., "sent," "event created," "done") <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a>.

#### **Examples of Built Tools**

1.  **Send Email Tool** <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>
    *   **Parameters**: `to`, `subject`, `message`, `bcc`, `cc`, `senderName` <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.
    *   **Process**: Agent sends a query with email details -> AI node parses -> Gmail node sends email -> Response node confirms "sent" <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>.
2.  **Create Calendar Event Tool** <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>
    *   **Parameters**: `summary` (title), `start`, `end`, `attendees` (as a comma-separated stringified list), `description` <a class="yt-timestamp" data-t="00:19:21">[00:19:21]</a>.
    *   **Process**: Similar to email, but maps to Google Calendar's "Create an Event" node <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>.
    *   **Output**: Agent receives "event created" <a class="yt-timestamp" data-t="00:24:21">[00:24:21]</a>.
3.  **Create Document in Google Drive Tool** <a class="yt-timestamp" data-t="00:24:42">[00:24:42]</a>
    *   **Parameters**: `fileContent`, `fileName` <a class="yt-timestamp" data-t="00:28:28">[00:28:28]</a>.
    *   **Process**: Maps to Google Drive's "Create a File" node <a class="yt-timestamp" data-t="00:26:17">[00:26:17]</a>.
4.  **Update Database Tool (Pinecone)** <a class="yt-timestamp" data-t="00:31:16">[00:31:16]</a>
    *   **Action**: Inserts data into a specific namespace within the Pinecone vector database <a class="yt-timestamp" data-t="00:32:07">[00:32:07]</a>.
    *   **Embedding**: Uses an embedding model (e.g., OpenAI's text embedding small) to chunk and embed the document <a class="yt-timestamp" data-t="00:33:15">[00:33:15]</a>.
    *   **Accuracy**: Chunk size affects accuracy; well-structured data is key for precise information retrieval <a class="yt-timestamp" data-t="00:33:51">[00:33:51]</a>.
    *   **Schema**: Does not require explicit input schema definition in the agent settings because it directly handles data insertion into Pinecone without prior manipulation <a class="yt-timestamp" data-t="00:40:29">[00:40:29]</a>.

> [!TIP] Optimizing Tool Workflows
> AI nodes can replace various traditional nodes (code, function, aggregator, concatenation) that primarily manipulate and reformat data, simplifying workflows <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.

## Putting It All Together: The Agent and Prompt

The agent orchestrates the use of these [[tools_and_resources_for_building_ai_agents | tools]]. The key is to define the agent's prompt, ensuring it knows how to use its [[tools_and_resources_for_building_ai_agents | tools]], its job, and the context in which it operates <a class="yt-timestamp" data-t="00:35:32">[00:35:32]</a>.

### **Agent Configuration**
*   **Agent Type**: Use a "Tools Agent" <a class="yt-timestamp" data-t="00:36:01">[00:36:01]</a>.
*   **Model**: Provide the agent with its "brain" (e.g., GPT-4) <a class="yt-timestamp" data-t="00:36:33">[00:36:33]</a>.
*   **Attach Tools**: Each custom tool workflow is attached to the agent <a class="yt-timestamp" data-t="00:37:02">[00:37:02]</a>.
    *   **Description**: Crucial for informing the agent about the tool's purpose <a class="yt-timestamp" data-t="00:37:13">[00:37:13]</a>.
    *   **Workflow ID**: Unique identifier for the tool's workflow <a class="yt-timestamp" data-t="00:38:18">[00:38:18]</a>.
    *   **Input Schema**: **Defining the input schema (Schema type: Defined below) for each tool is the ultimate key to reliable tool usage by the agent** <a class="yt-timestamp" data-t="00:37:37">[00:37:37]</a>. This ensures the agent outputs the exact JSON parameters required by the tool consistently <a class="yt-timestamp" data-t="00:55:27">[00:55:27]</a>.

### **Prompt Engineering**
The prompt is critical for the agent's performance; a poorly dialed-in prompt can prevent the agent from working correctly <a class="yt-timestamp" data-t="00:42:01">[00:42:01]</a>.
*   **Template**: A good prompt template includes:
    *   **Objective**: The agent's overall goal.
    *   **Context**: Information about the [[tools_and_resources_for_building_ai_agents | tools]] it has and its operational environment <a class="yt-timestamp" data-t="00:46:52">[00:46:52]</a>.
    *   **Instructions**: Steps like analyzing user requests, retrieving information, preparing parameters, and executing actions <a class="yt-timestamp" data-t="00:46:54">[00:46:54]</a>.
    *   **Parameter Definition**: Explicitly stating the parameters for each tool <a class="yt-timestamp" data-t="00:47:03">[00:47:03]</a>.
    *   **Output Requirements**: How the agent should respond <a class="yt-timestamp" data-t="00:47:13">[00:47:13]</a>.
*   **Iterative Refinement**: If a tool operates almost correctly but makes minor errors, the issue is almost always in the prompt <a class="yt-timestamp" data-t="00:54:46">[00:54:46]</a>.

> [!INFO] Troubleshooting
> If an agent tool doesn't work, check the specific tool's execution logs rather than the agent's workflow logs <a class="yt-timestamp" data-t="00:51:50">[00:51:50]</a>.

## Benefits and Future Potential

By adopting an iterative, bottom-up approach focused on building [[tools_and_resources_for_building_ai_agents | tools]] rather than monolithic workflows, developers can create powerful [[five_types_of_ai_agents_you_can_build | agents]] with access to entire platforms <a class="yt-timestamp" data-t="01:00:05">[01:00:05]</a>.
*   **Reusability**: Once a robust tool (like an "Email Agent" with all possible email actions) is built, it can be copied and integrated into any other [[five_types_of_ai_agents_you_can_build | agent]] that requires email functionality <a class="yt-timestamp" data-t="00:58:37">[00:58:37]</a>.
*   **Reliability**: Defining the input schema for [[tools_and_resources_for_building_ai_agents | tools]] ensures consistent and reliable operation <a class="yt-timestamp" data-t="01:00:50">[01:00:50]</a>.
*   **Scalability**: Multiple [[five_types_of_ai_agents_you_can_build | AI agents]] can be [[building_and_deploying_ai_agents | built]] on top of each other and interact, potentially leading to autonomous business operations <a class="yt-timestamp" data-t="01:01:07">[01:01:07]</a>. This represents a significant aspect of [[developing_ai_agents_and_their_market_potential | developing AI agents and their market potential]].
*   **Organizational Efficiency**: [[implementing_and_utilizing_ai_agent_tools_for_various_business_operations | Implementing and utilizing AI agent tools for various business operations]] means humans can focus on strategizing, planning, and defining tasks, while agents execute them <a class="yt-timestamp" data-t="01:01:18">[01:01:18]</a>. Success with agents heavily relies on being organized with tasks, workflows, and clear instructions <a class="yt-timestamp" data-t="01:02:02">[01:02:02]</a>.

This approach aligns with [[the_role_of_custom_ai_tools_versus_offtheshelf_solutions | the role of custom AI tools versus off-the-shelf solutions]], offering flexibility and tailored functionality. The emphasis on [[data_management_and_prompt_engineering_for_ai_agents | data management and prompt engineering for AI agents]] is crucial for [[building_efficient_ai_agents_with_prompts | building efficient AI agents with prompts]] and [[integrating_ai_agents_with_business_tools | integrating AI agents with business tools]] effectively.