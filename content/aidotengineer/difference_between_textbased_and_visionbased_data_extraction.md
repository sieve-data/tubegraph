---
title: Difference between textbased and visionbased data extraction
videoId: kjSGc7uwDo8
---

From: [[aidotengineer]] <br/> 

When it comes to AI agents extracting data from web pages, two primary approaches are employed: vision-based and text-based methods. These methods differ significantly in their underlying technology, performance, cost-effectiveness, and security implications <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.

## Vision-Based Approach

The vision-based approach is commonly used by many existing AI agents, including [[Natural Language Processing and AI | OpenAI Operator]], [[Natural Language Processing and AI | Anthropic Claude]], and [[Natural Language Processing and AI | Google Mariner]] <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>.

### How it Works
This method involves taking screenshots of web pages and then extracting the desired data from these visual representations <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.

### Disadvantages and Problems
*   **Prone to Hallucination**: Vision-based models are more susceptible to hallucination compared to text-based methods <a class="yt-timestamp" data-t="00:12:33">[00:12:33]</a>.
*   **High Cost**: It is highly expensive, often requiring multiple screenshots for even a single action or page scroll <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>.
*   **Cloud-Based Browsers**: Many companies using this approach operate browsers on the cloud <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>. This introduces several issues:
    *   **Non-Personalized Results**: Content seen on a cloud-based browser might differ from what a user sees in their own browser <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>.
    *   **Expensive Proxies**: Supporting cloud browsers necessitates implementing numerous proxies to funnel network requests, which significantly increases costs <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.
    *   **Security Risks**: Users often have to store or provide their passwords, leading to various security vulnerabilities <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.
    *   **Access Limitations**: Cloud-based browsers may struggle to bypass paywalls or Cloudflare website protections <a class="yt-timestamp" data-t="00:14:06">[00:14:06]</a>.
*   **Limited Parallel Processing**: Vision-based approaches cannot take actions on multiple background tabs simultaneously because these tabs don't get rendered <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>.
*   **Exponential Failure Rates**: Tasks that involve long horizons or many steps on a single tab can lead to higher failure rates <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>.

## Text-Based Approach (Retriever's Method)

Retriever.com utilizes a text-based approach for its AI web agent, delivered as a Chrome extension <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

### How it Works
This method leverages the text-based structure and content of web pages directly <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>.

### Advantages and Benefits
*   **Reduced Hallucination**: There is significantly less hallucination in the output because the text is directly in context for the model <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>.
*   **Cost-Effective**: Retriever's approach is highly cost-effective, with page extraction potentially costing less than a penny <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
*   **Multi-Tab Processing**: It can process not only active tabs but also background tabs or multiple tabs simultaneously <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>. This parallel processing capability speeds up performance and allows for multi-tab contextual actions <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.
*   **Client-Side Extension**: Being a client-side Chrome extension, it avoids the issues associated with cloud-hosted browsers <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>.
*   **Enhanced Security**: Retriever does not store or require users to share passwords, as it operates directly within the user's logged-in browser session <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>. This makes it much more secure <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>.
*   **Access to Restricted Content**: It can access local wall sites and login-protected content, and navigate beyond paywalls or Cloudflare protections <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>.
*   **Distributed Subtasks**: Instead of long-horizon tasks on a single tab, Retriever distributes subtasks as new tabs, significantly reducing failure rates <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>.
*   **Extensible Function Calling**: Users can define and set up their own function calls for [[Data extraction from web pages to Google Sheets | third-party integrations]], making the system more extensible and scalable than fixed custom integrations <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>.

## Conclusion
The text-based approach offers significant advantages in terms of accuracy, cost, security, and parallel processing capabilities when compared to vision-based methods for data extraction by AI agents <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>. Retriever aims to revolutionize [[Data extraction from web pages to Google Sheets | data extraction]] with its transparent and efficient AI agent <a class="yt-timestamp" data-t="00:16:34">[00:16:34]</a>.