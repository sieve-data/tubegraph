---
title: Developing AI Agents using Python
videoId: q7_5eCmu0MY
---

From: [[colemedin]] <br/> 

OpenAI has introduced Swarm, an open-source AI agent orchestration tool designed for [[building_ai_agents_with_python | building AI agents with Python]] using clean and simple code. Swarm facilitates the seamless connection of these agents to perform complex tasks <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This framework addresses a growing need for tools that can connect [[building_ai_agents | AI agents]] as they become ubiquitous in managing various systems <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## What is OpenAI Swarm?

Swarm is an open-source library provided by OpenAI, with all its code available for public access <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. It allows users to fork the repository, modify the code, and even run their own fine-tuned Large Language Models (LLMs) within their swarms <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. The project includes extensive documentation and examples to guide users <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. Swarm is a very new tool, having been initially committed just days before its reveal <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.

## Why use Swarm for AI Agent Orchestration?

While setting up a single [[building_ai_agents | AI agent]] with tools like [[setting_up_ai_agents_with_python_and_langchain | LangChain]] or n8n is straightforward <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>, managing a "swarm" of agents connected in specific ways for a particular use case becomes challenging <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. Swarm provides a solution for this orchestration, serving both as a usable tool and a learning resource <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

The framework's primary purpose is educational <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>. It teaches a "bulletproof architecture" for [[understanding_ai_agents | AI agent orchestration]] <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. Specifically, Swarm showcases the "handoff and routine patterns" explored in OpenAI's cookbook, which are crucial concepts for [[building_ai_agents | building robust and reliable AI agent architectures]] <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. By examining its source code, users can gain significant insights into advanced AI agent design <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.

## Practical Example: Managing a SQL Database with Swarm Agents

A key demonstration of Swarm's capabilities involves [[building_ai_agents | building a swarm of AI agents]] to manage a SQL database <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. These agents can extract insights using SQL queries, create and manage tables, and clean data <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. This is particularly useful for large SQL databases with many tables, where specialized agents can handle different areas of the database <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

### The Problem: Overwhelming a Single LLM

Relying on a single [[building_ai_agents | AI agent]] with many functions or instructions can limit its effectiveness <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. Even if an LLM can handle a large context, feeding it too much information can lead to the "needle in the haystack" problem, where specific instructions or functions might be missed or result in errors <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

### The Solution: Multi-Agent Architecture

The solution is to employ multiple agents working collaboratively, each tackling different parts of a problem or managing distinct system components <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. For the SQL database example, this involves a "router agent" and several specialized "sub-agents" <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

When a user query (e.g., "how many likes does this category of posts have?") comes in, the router agent, with its contextual understanding, determines which specialized sub-agent is best suited to handle the request <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>. Each sub-agent specializes in different data parts within the RSS feed database, and they can be instructed to respond differently <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>. This approach enhances robustness and flexibility <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

### Setting up the Swarm

Setting up this multi-agent system with Swarm can be achieved in less than 100 lines of [[building_ai_agents_with_python | Python]] code <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.

The general [[step_by_step_process_for_building_ai_agents | process for building AI agents]] with Swarm includes:
1.  **Database Setup:** Connect to a SQLite database and load SQL scripts to provide table schemas to the agents <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>.
2.  **Tool Creation:** Define functions that agents can invoke, such as `run_sql_select_statement`, which queries the database and formats results for the agent <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>. Docstrings for these functions automatically serve as prompts for the agents, helping them understand when and how to use the tools <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.
3.  **Instruction Functions:** Create Python functions to generate dynamic or hard-coded instructions for the agents, providing them with their roles (e.g., "orchestrator," "SQL expert") and database schema information <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>.
4.  **Agent Instantiation:** Create agents using the `swarm.Agent` object, providing them with a name, instructions, and a list of functions they can call <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>. Each agent can have specialized instructions, such as an "RSS feed agent" being "super enthusiastic" in its responses <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>.
5.  **Transfer Functions:** Define functions that allow agents to transfer requests between each other (e.g., from a router to a specialized agent, or a specialized agent back to the router) <a class="yt-timestamp" data-t="00:16:39">[00:16:39]</a>. These transfer functions are added to the respective agents' list of available functions <a class="yt-timestamp" data-t="00:17:12">[00:17:12]</a>.

A `run.py` script, typically just five lines of code, can utilize Swarm's `run_demo_loop` to create an interactive chat interface in the terminal for testing the agents <a class="yt-timestamp" data-t="00:17:44">[00:17:44]</a>.

## Swarm as an Educational Tool

Swarm is intended to be an experimental and educational framework <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. Its goal is not to be a production-grade library for enterprise applications but rather to teach concepts related to [[advancing_ai_agents_with_python_and_custom_coding | building robust and reliable AI agent architectures]] <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

> "The goal here again, it's not to be a production piece of software, a library that you could actually use in production to run Enterprise grade applications, it's more to teach you something." <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>

## Alternative for Database Management: Chat2DB

For those who prefer not to [[building_ai_agents_from_scratch_with_python | build AI agents from scratch]], platforms like Chat2DB offer out-of-the-box functionality for managing SQL databases using natural language <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. Chat2DB is an open-source platform with a cloud offering that allows users to connect almost any SQL database, leverage LLMs to improve and write SQL queries with natural language, gain insights, and manage tables <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

## Swarm vs. Other Frameworks

While Swarm offers an incredible way to [[building_ai_agents_with_python | develop AI agents using Python]], it might entail less customization compared to other frameworks like [[setting_up_ai_agents_with_python_and_langchain | LangChain]] plus LangGraph, or tools like n8n, as Swarm can be more of a "black box" in certain aspects <a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a>.