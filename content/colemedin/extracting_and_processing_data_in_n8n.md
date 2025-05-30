---
title: Extracting and processing data in n8n
videoId: Nsu9BzQv5C4
---

From: [[colemedin]] <br/> 

[[overview_of_n8n_as_a_workflow_automation_tool | n8n]] is a powerful no-code AI automation tool that allows users to build AI agents and integrate with over 500 applications <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This article focuses on underutilized and trickier parts of the platform to enhance data extraction and processing workflows.

## Data Extraction from Various File Types

When building AI agents, especially those using Retrieval Augmented Generation (RAG), it's crucial to extract text from different file types <a class="yt-timestamp" data-t="02:45:00">[02:45:00]</a>. [[using_different_nodes_in_n8n_for_file_type_extraction | Different nodes in n8n are required for different file types]] <a class="yt-timestamp" data-t="02:48:00">[02:48:00]</a>:

*   Extracting text from a PDF document requires a different node than extracting text from a plain text document or an Excel spreadsheet <a class="yt-timestamp" data-t="02:52:00">[02:52:00]</a>.
*   When adding an "extract from file" node, you'll find various options <a class="yt-timestamp" data-t="03:02:00">[03:02:00]</a>.
*   It's essential to include all relevant nodes in your workflow based on the file types you plan to ingest into your vector database <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>.

## Working with Previous Node Outputs

Understanding how to reference outputs from previous nodes is fundamental for [[ai_automation_with_n8n | n8n workflows]] <a class="yt-timestamp" data-t="03:20:00">[03:20:00]</a>.

### Referencing Data

*   To reference an output, such as a `file ID` or `MIM type` from a preceding node (e.g., a Google Drive trigger), you first need to run a test execution of that node by clicking "test step" <a class="yt-timestamp" data-t="03:27:00">[03:27:00]</a>.
*   This action populates the output on the left-hand side, allowing you to drag and drop values to create expressions that dynamically reference them <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>.

### Important Distinction: `json.` vs. Node Name

A common point of confusion is how to correctly reference values:

*   Using `json.file ID` (or `json.variableName`) only works for referencing values from the *immediately preceding* node <a class="yt-timestamp" data-t="03:57:00">[03:57:00]</a>.
*   If you need to reference a value from a node that is *two or more steps back* in the workflow, you must explicitly reference the name of that node <a class="yt-timestamp" data-t="04:09:00">[04:09:00]</a>. For example, if a node named "set file ID" produced the desired output, you would reference it by that name to access its values <a class="yt-timestamp" data-t="04:18:00">[04:18:00]</a>.

## Handling Looping and Multiple Items

Properly handling looping is crucial for robust [[workflow_automation_with_n8n | n8n workflows]] <a class="yt-timestamp" data-t="05:53:00">[05:53:00]</a>.

*   Nodes, such as Google Drive triggers, can output multiple items in a single execution <a class="yt-timestamp" data-t="05:57:00">[05:57:00]</a>.
*   [[workflow_automation_with_n8n | n8n]] automatically handles looping by processing multiple items one at a time for the subsequent node <a class="yt-timestamp" data-t="06:09:00">[06:09:00]</a>.
*   However, you must design your workflow to handle scenarios where multiple items are generated simultaneously <a class="yt-timestamp" data-t="06:22:00">[06:22:00]</a>. For instance, if two files are created at the same time, the workflow must process both <a class="yt-timestamp" data-t="06:31:00">[06:31:00]</a>.
*   **Example:** After extracting text from multiple files, a "summarized" node can concatenate the output of all files into a single parameter for further processing by a large language model <a class="yt-timestamp" data-t="06:51:00">[06:51:00]</a>.
*   Always consider how your workflow will manage multiple items from a single output to ensure proper data processing <a class="yt-timestamp" data-t="07:13:00">[07:13:00]</a>.

## Data Pinning for Development Efficiency

Data pinning is an underutilized feature that significantly speeds up development within [[creating_powerful_ai_workflows_with_n8n | n8n]] <a class="yt-timestamp" data-t="07:25:00">[07:25:00]</a>.

*   Typically, to get output on the right-hand side for referencing in subsequent nodes, you need to execute a test event <a class="yt-timestamp" data-t="07:30:00">[07:30:00]</a>.
*   However, this output is lost when you refresh [[ai_automation_with_n8n | n8n]] or close and reopen the platform, requiring you to re-execute the test event <a class="yt-timestamp" data-t="07:43:00">[07:43:00]</a>.
*   By clicking the "pin data" button in the top right of a trigger node, that specific output will persist even after a hard reload <a class="yt-timestamp" data-t="07:51:00">[07:51:00]</a>. This eliminates the need to repeatedly run test events, making workflow development much faster <a class="yt-timestamp" data-t="08:06:00">[08:06:00]</a>.