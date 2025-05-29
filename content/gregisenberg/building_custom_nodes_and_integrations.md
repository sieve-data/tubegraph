---
title: Building custom nodes and integrations
videoId: QFc7jXZ2pdE
---

From: [[gregisenberg]] <br/> 

Gumloop offers the ability to create custom nodes and integrations, allowing users to connect workflows with internal data or third-party services not natively supported <a class="yt-timestamp" data-t="0:57:00">[0:57:00]</a>. This feature is particularly beneficial for large customers like Instacart or Samsara who need to interact with their own endpoints or specific third-party tools <a class="yt-timestamp" data-t="0:53:00">[0:53:00]</a>.

## Creating a Custom Node

To build a custom node, users access the custom node category within Gumloop <a class="yt-timestamp" data-t="0:11:14">[0:11:14]</a>. The process involves:
*   **Naming the node** <a class="yt-timestamp" data-t="0:41:42">[0:41:42]</a>.
*   **Defining inputs and outputs**: Users can add as many inputs as needed, choosing the type of data <a class="yt-timestamp" data-t="0:48:48">[0:48:48]</a>.
*   **Adding a logo** (optional) <a class="yt-timestamp" data-t="0:54:00">[0:54:00]</a>.
*   **Prompting AI with documentation**: Users can copy and paste API documentation directly into the custom node builder <a class="yt-timestamp" data-t="0:32:00">[0:32:00]</a>. The AI understands the context of a Gumloop integration, including available packages, and suggests where to input API keys <a class="yt-timestamp" data-t="0:03:00">[0:03:00]</a>.

### AI Assistance in Custom Node Development
The platform's AI assists in code generation, providing comments throughout the code for clarity <a class="yt-timestamp" data-t="0:34:00">[0:34:00]</a>. This feature enables semi-technical users to build complex integrations, such as Twitter scrapers or Blue Sky analysis tools, without needing to be a developer <a class="yt-timestamp" data-t="0:51:00">[0:51:00]</a>.

The long-term vision for custom nodes includes allowing users to simply describe the desired integration, and the AI will automatically name it, select an icon, determine inputs, write the code, and test it, making the process even more seamless <a class="yt-timestamp" data-t="0:16:00">[0:16:00]</a>.

## Sharing and Collaboration

Once a custom node is built, everyone within the user's workspace can access and utilize it, similar to how official Gumloop integrations are used <a class="yt-timestamp" data-t="0:12:00">[0:12:00]</a>. The original creators can also go back and modify the code if needed <a class="yt-timestamp" data-t="0:32:00">[0:32:00]</a>.

## Integrating Workflows as APIs (Webhooks)

Any [[Building Simple and Powerful Workflows | Gumloop workflow]] can be treated as an API and triggered via a webhook <a class="yt-timestamp" data-t="0:44:00">[0:44:00]</a>. This allows users to integrate Gumloop workflows directly into their own products or websites based on specific events <a class="yt-timestamp" data-t="0:49:00">[0:49:00]</a>. For example, a workflow can be triggered when a user creates an account on a platform, passing their email dynamically to Gumloop for further processing <a class="yt-timestamp" data-t="0:51:00">[0:51:00]</a>.

This capability enables users to build and charge for [[Building and deploying apps with AI integration | SaaS products]] where Gumloop handles the backend automation <a class="yt-timestamp" data-t="0:57:00">[0:57:00]</a>. While many users implement webhooks in internal dashboards, they might not expose them directly on a landing page to prevent high credit usage from mass workflow runs <a class="yt-timestamp" data-t="0:50:00">[0:50:00]</a>. Alerts can be set up to notify users if workflows encounter issues <a class="yt-timestamp" data-t="0:33:00">[0:33:00]</a>.

### Cost Implications
Users have the option to provide their own API keys for services like Apollo or Gemini <a class="yt-timestamp" data-t="0:22:00">[0:22:00]</a>. This significantly reduces the cost of running workflows on Gumloop, potentially dropping it to near zero, even for large-scale operations with thousands of runs <a class="yt-timestamp" data-t="0:29:00">[0:29:00]</a>.