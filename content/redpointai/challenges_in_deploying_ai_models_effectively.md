---
title: Challenges in deploying AI models effectively
videoId: a0bEU83P8g8
---

From: [[redpointai]] <br/> 

Deploying Artificial Intelligence (AI) models effectively presents a range of significant challenges, particularly as models become more advanced and integrate into complex environments. These challenges span from reliability and contextual understanding to the underlying infrastructure and adoption strategies within organizations.

## Reliability and Performance Scaling
A primary challenge in deploying advanced AI models, especially those capable of taking actions or engaging in long-term reasoning, is ensuring their reliability [00:08:57]. When an AI agent performs tasks on a user's behalf, even for tasks like thinking or code generation, unreliability can lead to wasted time if it goes off-task or makes mistakes [00:09:08]. The risk increases dramatically when agents take actions in the real world, such as purchasing items or sending communications, where consequences can range from embarrassment to financial loss [00:09:22].

Achieving high reliability is computationally intensive. Improving reliability from 90% to 99% can require an order of magnitude increase in compute, and moving from 99% to 99.9% requires another order of magnitude increase [00:09:51]. This roughly translates to one to two years of development work per "nine" of reliability improvement [00:10:01]. This underscores the difficulty in reaching the levels of reliability needed for widespread, trusted deployment.

## New Form Factors and User Interfaces
While current chatbots like GPT-4 handle basic interactions well, unlocking the full capabilities of more advanced models like O1 requires new user interfaces and "form factors" [00:06:09]. These models excel at tasks requiring a coherent Chain of Thought, such as programming or writing detailed policy briefs, where they can make consistent progress over time [00:07:03].

The most exciting development is using these models to enable long-term actions through "agents" [00:07:50]. This involves the AI interacting with the real world, for instance, booking travel or shopping [00:08:16]. However, the ideal form factor for this type of interaction has yet to be fully defined [00:08:28].

## Enterprise Integration and Contextual Understanding
Deploying AI within an enterprise introduces a distinct set of [[Enterprise AI deployment models | challenges and strategies in enterprise AI deployment]] compared to consumer applications [00:10:25]. A major hurdle is providing the AI with sufficient context specific to the organization [00:11:17]. Unlike consumer interactions, where context is minimal, enterprise tasks require understanding co-workers, projects, codebases, and organizational preferences [00:11:36].

This enterprise-specific information is often "ambiently" available in various systems like Slack, internal documents, or design files [00:11:44]. Integrating Large Language Models (LLMs) into this ecosystem often requires building bespoke connectors or leveraging platforms designed for data integration, similar to the work done by Palantir [00:11:55].

There are two main approaches to providing this context:
1.  **Library of Connectors**: Building a collection of specific integrations for different enterprise tools [00:12:02].
2.  **Computer Use Agents**: Using a general-purpose model that can control a mouse and keyboard to interact with any application [00:12:39]. While compelling due to its broad applicability, this approach often requires significantly more "tokens" (10x to 100x) due to the greater number of steps involved [00:13:32].

The development of computer use agents has been a long-standing area of research for major AI labs, but the reliability for widespread adoption remains a significant barrier [00:13:03]. It is likely that a mix of bespoke integrations and computer use agents will be employed for the foreseeable future [00:14:46]. For specific applications like Salesforce, it is expected that application providers would make their data available to foundational models, rather than specialized models being trained for each application, to enhance usability and competitiveness [00:15:20].

## Pace of Adoption and Productivity Paradox
Despite rapid advancements in AI capabilities, the actual adoption rate and its impact on broader productivity statistics have been slower than anticipated [00:31:17]. Some estimates suggest a mere 0.1% increase in GDP growth from AI, primarily driven by capital expenditures on data centers rather than direct productivity gains [00:31:55]. This mirrors the "productivity paradox" seen with the internet in the 1990s [00:32:15].

The slower adoption stems from the complexity of real-world jobs. While AI can automate individual "tasks," most jobs are composed of many tasks, and often a few non-automataable tasks can hold back full automation [00:33:24]. For instance, in programming, AI excels at boilerplate code, but the complex "giving direction" aspect remains a human domain [00:33:36].

## [[Challenges of building AI infrastructure companies | Challenges in AI product development]]
The path to productizing AI capabilities, especially in new modalities like video, faces unique [[Challenges in productizing AI capabilities | challenges in AI product development]] [00:19:11].
-   **Video Models**: While the instantaneous quality of video models like Sora is impressive, the challenge lies in creating extended, coherent sequences of events, which requires sophisticated user interfaces to manage story progression over time [00:19:46]. Video model training and inference are also very expensive [00:20:21]. However, expect similar cost reductions as seen in LLMs (e.g., GPT-3 quality tokens are 100 times cheaper now) [00:22:24].
-   **Robotics**: Integrating foundation models offers a huge breakthrough for robotics, enabling faster setup and better generalization [00:25:11]. This includes enhanced vision capabilities and easier human-robot interaction via voice commands [00:25:31]. However, a significant open question is whether to train robots primarily in simulation or using real-world data [00:26:29]. While simulators offer benefits, they struggle with "floppy" objects (e.g., cloth, cardboard), making real-world demonstrations currently the only general approach for such materials [00:27:01].
    -   Mass consumer adoption of robotics is still distant due to safety concerns (robot arms can be dangerous) and the unstructured nature of home environments [00:28:10]. However, widespread adoption in constrained work environments like warehouses is anticipated within five years [00:28:36].

## Organizational and Cultural [[Challenges and strategies in deploying AI models for developers | Challenges and strategies in deploying AI models for developers]]
The rapid evolution of AI technology, particularly within organizations like OpenAI, necessitates frequent and significant strategic pivots. OpenAI itself underwent several "refounding" moments:
-   Transition from a non-profit to a for-profit entity, which was controversial but necessary for funding [00:41:03].
-   Partnership with Microsoft, initially met with internal resistance [00:41:41].
-   Decision to build their own products with an API [00:42:04].
-   The accidental, yet deliberate, move to launch ChatGPT for consumers, which forced the company to adapt rapidly to unexpected demand [00:43:34].

These dramatic shifts, occurring every 18 months to two years, required fundamentally changing the company's purpose and the identity of its workforce, moving from paper-writing research to building a single model for global use [00:42:20]. The ability to make these shifts was driven by necessity and a startup-like culture that fostered collaboration and a clear product vision, contrasting with the more individualistic, credit-focused incentives often found in academia [00:55:01].