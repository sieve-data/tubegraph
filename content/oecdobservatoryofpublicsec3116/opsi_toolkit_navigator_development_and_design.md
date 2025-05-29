---
title: OPSI Toolkit Navigator development and design
videoId: 9_5wh_aTnu0
---

From: [[oecdobservatoryofpublicsec3116]] <br/> 

The [[opsi_toolkit_navigator | OPSI Toolkit Navigator]] is a public service project supported by the European Commission through the Horizon 2020 program, developed by the full OPSI (Observatory of Public Sector Innovation) team <a class="yt-timestamp" data-t="00:36:00">[00:36:00]</a>. Its purpose is to help users find appropriate innovation toolkits for their specific needs <a class="yt-timestamp" data-t="02:15:00">[02:15:00]</a>.

## Development Context and Rationale

In 2017, OPSI was tasked with building a toolkit for public sector innovation globally <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>. However, the developers believed the world did not need "another toolkit," noting that "hundreds" already existed, leading to a state of "peak toolkit" <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>. The goal shifted from creating more noise to providing "signal through that noise" <a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a>.

Instead of building a new toolkit, the focus became helping people find the right existing toolkits based on their needs <a class="yt-timestamp" data-t="02:17:00">[02:17:00]</a>. This approach was influenced by a quote from Andrea Snook of UK Policy Lab: "Toolkits are like toothbrushes: everybody has one but nobody wants to use someone else's" <a class="yt-timestamp" data-t="02:25:00">[02:25:00]</a>.

## User-Centric Design Process

The development of the [[opsi_toolkit_navigator | OPSI Toolkit Navigator]] was highly user-centered:
*   **User Research** In 2017, a workshop was conducted at the OPSI conference with public sector leaders and civil servants. The aim was to understand their innovation journey, including how they found information, who they contacted, and what [[methods_and_tools_in_innovation_toolkits | tools and methods]] they used <a class="yt-timestamp" data-t="01:34:00">[01:34:00]</a>. This research informed the structure of the navigator <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>.
*   **Toolkit Analysis** Hundreds of existing toolkits were analyzed in depth to understand their contents, disciplines, and "jobs to be done" <a class="yt-timestamp" data-t="06:01:00">[06:01:00]</a> <a class="yt-timestamp" data-t="13:23:00">[13:23:00]</a>.
*   **Prototyping and Iteration** Initial designs and several different prototypes were tested with public sector innovators and national government innovation leaders from various governments <a class="yt-timestamp" data-t="14:17:00">[14:17:00]</a>. This feedback led to significant changes in the navigator's design <a class="yt-timestamp" data-t="14:37:00">[14:37:00]</a>.

## Underlying Innovation Model

A key backdrop for the navigator's design is OPSI's Multifaceted Innovation Model, derived from system-level studies of the Canadian and Brazilian governments <a class="yt-timestamp" data-t="03:13:00">[03:13:00]</a>. This model identifies different purposes for innovation in the public sector:
*   **Directed/Shaping/Top-down/Mission-oriented innovation** Examples include "putting a person on the moon" <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>.
*   **Undirected/Responding/Bottom-up innovation** This focuses on creating space and an entrepreneurial spirit to find new solutions without a predetermined outcome <a class="yt-timestamp" data-t="03:50:00">[03:50:00]</a>.
*   **Enhancement-oriented innovation (High certainty)** Improving existing processes and services, such as using behavioral insights to increase timely tax payments <a class="yt-timestamp" data-t="04:09:00">[04:09:00]</a>.
*   **Exploring/Radical shifts (Uncertain spaces)** Examining how internal and external factors will fundamentally change the nature of work <a class="yt-timestamp" data-t="04:26:00">[04:26:00]</a>.

Different facets of innovation are supported by distinct [[methods_and_tools_in_innovation_toolkits | methods and tools]], processes, disciplines, and domains of practice <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>. The choice of methods significantly biases innovation outcomes, making it crucial to select methods aligned with purpose <a class="yt-timestamp" data-t="05:38:00">[05:38:00]</a>.

## Key Findings from Toolkit Research

Research into existing toolkits and user experiences revealed several issues:
*   **Over-reliance on past tools** <a class="yt-timestamp" data-t="06:21:00">[06:21:00]</a>
*   **Misalignment with problems** Toolkits are often chosen for superficial reasons (e.g., "bright and shiny") rather than suitability <a class="yt-timestamp" data-t="06:27:00">[06:27:00]</a>.
*   **Lack of consideration for existing skills** Some toolkits require advanced skills <a class="yt-timestamp" data-t="06:40:00">[06:40:00]</a>.
*   **Granularity issues** Toolkits can be either too specific or too broad <a class="yt-timestamp" data-t="06:52:00">[06:52:00]</a>.
*   **Learned helplessness** Polished toolkits can be intimidating, leading innovators to hesitate in adapting them to their specific context <a class="yt-timestamp" data-t="07:03:00">[07:03:00]</a>.

## Ideal Toolkit Characteristics

Based on these findings, the ideal toolkit should be:
*   **Adaptable and transferable** <a class="yt-timestamp" data-t="07:46:00">[07:46:00]</a>
*   **Approachable and user-centered** <a class="yt-timestamp" data-t="07:53:00">[07:53:00]</a>
*   **Obvious what to do with it** <a class="yt-timestamp" data-t="07:55:00">[07:55:00]</a>
*   **Action-oriented** Focused on getting to action rather than just guidance or knowledge <a class="yt-timestamp" data-t="07:57:00">[07:57:00]</a>.
*   **Modular** Allowing users to combine parts from different toolkits to suit their needs <a class="yt-timestamp" data-t="08:08:00">[08:08:00]</a>.

## Organization and Features

The navigator organizes toolkits, which are referred to as the "compendium of toolkits," around "innovation tasks" or "jobs to be done" <a class="yt-timestamp" data-t="08:23:00">[08:23:00]</a>. These tasks extend beyond typical "problem-solving jobs" (e.g., discovery, prototyping) to include:
*   **Group behavioral jobs** (e.g., building consensus, shared understanding, challenging assumptions, cultivating mindsets) <a class="yt-timestamp" data-t="08:58:00">[08:58:00]</a> <a class="yt-timestamp" data-t="10:09:00">[10:09:00]</a>.
*   **Approach planning jobs** (e.g., preliminary scoping) <a class="yt-timestamp" data-t="09:06:00">[09:06:00]</a>.
*   **Contextualization jobs** (e.g., visualizing systems, imagining futures) <a class="yt-timestamp" data-t="09:15:00">[09:15:00]</a> <a class="yt-timestamp" data-t="10:50:00">[10:50:00]</a>.

The navigator also distinguishes between different levels of granularity for resources (e.g., methodologies, tactics, playbooks, tools) to help users find content at the right level of abstraction for their needs <a class="yt-timestamp" data-t="11:13:00">[11:13:00]</a>.

### Emphasis on Adaptability and Capacity Building

A special emphasis is placed on free and easily adaptable toolkits to build innovative capacity within teams <a class="yt-timestamp" data-t="14:51:00">[14:51:00]</a>.
*   Only **freely accessible toolkits** are included <a class="yt-timestamp" data-t="15:00:00">[15:00:00]</a>.
*   Toolkits that are **easier to adapt, modify, and remix** are given preference in sorting and ranking <a class="yt-timestamp" data-t="15:27:00">[15:27:00]</a>. This act of remixing and adapting helps build capacity <a class="yt-timestamp" data-t="15:40:00">[15:40:00]</a>.

### Toolkit Badges

The navigator uses badges to indicate adaptability:
*   **Open Source Basic**: Allows for reuse (download, print) <a class="yt-timestamp" data-t="16:00:00">[16:00:00]</a>.
*   **Open Source Champion**: Licensed with Creative Commons for remixing and adaptation <a class="yt-timestamp" data-t="16:12:00">[16:12:00]</a>.
*   **Hero**: Provides editable files or code to facilitate remixing and adaptation <a class="yt-timestamp" data-t="16:30:00">[16:30:00]</a>.

### Social Proof and Community Connection

To address the hesitancy in trying new [[methods_and_tools_in_innovation_toolkits | methods and tools]], the navigator provides social proof by connecting toolkits to:
*   **Case studies**: Links to hundreds of innovation cases in government on the OPSI website, showing real-world impact <a class="yt-timestamp" data-t="17:22:00">[17:22:00]</a>.
*   **User base**: Connects to the OPSI platform's global network of over 1,700 public sector innovators, allowing users to discuss, review toolkits, and find collaborators <a class="yt-timestamp" data-t="17:54:00">[17:54:00]</a>. Users can also indicate if they've used a toolkit or save it to their profile <a class="yt-timestamp" data-t="23:37:00">[23:37:00]</a>.

## User Interaction and Navigation

The [[user_interaction_with_the_opsi_toolkit_navigator | OPSI Toolkit Navigator]] allows users to navigate in several ways:
*   **Topics**: Organized by disciplines or practices (e.g., "digital and technology transformation") <a class="yt-timestamp" data-t="19:12:00">[19:12:00]</a>. Each topic includes an index article with principles, OECD guidance, considerations for public sector use, and related methods/tools <a class="yt-timestamp" data-t="19:41:00">[19:41:00]</a>.
*   **Actions**: Organized by common actions users want to take on their innovation journey (e.g., "design a new strategy") <a class="yt-timestamp" data-t="19:16:00">[19:16:00]</a> <a class="yt-timestamp" data-t="24:45:00">[24:45:00]</a>.
*   **Connecting to Others**: Guides users on accessing expertise or advice and finding toolkits related to team building or setting up innovation labs <a class="yt-timestamp" data-t="27:18:00">[27:18:00]</a>.
*   **Filters**: Users can refine searches by criteria such as target audience (e.g., policymakers, practitioners), features (e.g., checklists, steps in a process), type (guidance, tool set), license, country, and specific techniques <a class="yt-timestamp" data-t="25:40:00">[25:40:00]</a>.
*   **Search Bar**: A keyword search function allows users to find toolkits based on specific terms like "policy innovation" <a class="yt-timestamp" data-t="29:03:00">[29:03:00]</a>.
*   **Curated Collections**: Specific collections are available based on demand, such as "game-based toolkits," "highly adaptable toolkits," and "starter toolkits" (those with extensive guidance for beginners) <a class="yt-timestamp" data-t="29:38:00">[29:38:00]</a>.

## Community Contribution

Users are encouraged to submit new toolkits that are freely accessible, relevant to the public sector, and focused on stimulating action rather than just reports or research <a class="yt-timestamp" data-t="30:45:00">[30:45:00]</a>. Submissions are reviewed before publishing <a class="yt-timestamp" data-t="31:39:00">[31:39:00]</a>. The [[opsi_toolkit_navigator | OPSI Toolkit Navigator]] is a continuously developing "work in progress" <a class="yt-timestamp" data-t="32:20:00">[32:20:00]</a>.