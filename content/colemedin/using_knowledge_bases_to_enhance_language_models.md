---
title: Using knowledge bases to enhance language models
videoId: mDikQrVRmtU
---

From: [[colemedin]] <br/> 

One of the significant [[limitations_of_large_language_models | limitations of large language models]] (LLMs) is their general knowledge and limited understanding of new information due to their training data cut-off [00:00:00]. For instance, a model like Claude may not recognize a new framework such as Pydantic AI [00:00:10]. Even LLMs capable of searching the web provide only basic, "bare bones" information on novel topics [00:00:20].

## The Role of Knowledge Bases

To address this, if extensive documentation for a specific framework, like Pydantic AI, is integrated into a [[setting_up_and_running_a_local_knowledge_base | knowledge base]] accessible to the LLM, the model can provide highly accurate and detailed answers to specific queries [00:00:27]. This highlights the importance of [[integrating_knowledge_bases_with_ai | integrating knowledge bases with AI]] for enhanced performance.

## Retrieval Augmented Generation (RAG)

The process of augmenting LLMs with external, curated knowledge is a prominent area in AI known as Retrieval Augmented Generation, or RAG [00:00:38].

> [!INFO] **Retrieval Augmented Generation (RAG)**
> RAG is a method for providing an LLM with external, curated knowledge that you manage yourself [00:00:45]. Its primary goal is to transform an LLM into an expert on a specific subject, such as an [[ai_agents_and_large_language_models | AI agent]] framework or an e-commerce store [00:00:51].

## Overcoming Curation Challenges with Crawl4AI

While RAG is powerful, the step of curating external data can be challenging and time-consuming [00:00:58]. This is where Crawl4AI offers a solution [00:01:03].

Crawl4AI is an open-source web crawling framework specifically developed to scrape websites [00:01:06]. It formats the extracted information in a way that is optimally understood by LLMs [00:01:10].

## Practical Application

An example of RAG in action is an [[ai_agents_and_large_language_models | AI agent]] designed to be an expert on the Pydantic AI framework [00:01:17]. This agent leveraged Crawl4AI to gather and curate all the necessary framework knowledge into its [[setting_up_and_running_a_local_knowledge_base | knowledge base]] [00:01:22]. The approach demonstrated with this AI agent can be adapted and applied to any website to create specialized knowledge bases for LLMs [00:01:28].