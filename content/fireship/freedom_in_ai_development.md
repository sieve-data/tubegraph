---
title: freedom in AI development
videoId: GyllRd2E6fg
---

From: [[fireship]] <br/> 

Many prominent large language models, such as GPT-4, Groq, and Gemini, are not "free" in terms of freedom. This means they are often censored, aligned with specific political ideologies, and are closed-source, preventing developers from modifying or fixing inherent issues <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## The Push for Open Source AI

Despite statements from figures like OpenAI CEO Sam Altman, who suggested it's "impossible" for startups to compete with OpenAI in training foundation models <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>, there is significant hope in the [[open_source_advancements_in_ai_model_technology | open source advancements in AI model technology]] community.

### Mistral and Mixol 8x7B
A French company named Mistral, founded less than a year ago and already valued at $2 billion, simultaneously released a torrent link for their new Apache 2.0 license model, Mixol 8x7B, when Google announced Gemini <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

Key features of Mixol:
*   **Architecture** Based on a mixture of experts architecture, rumored to be the "secret sauce" behind GPT-4 <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
*   **Performance** While not yet at GPT-4's level, Mixol 8x7B outperforms GPT-3.5 and Llama 2 on most benchmarks <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
*   **License** It offers a true [[open_source_advancements_in_ai_model_technology | open source]] Apache 2.0 license, allowing users to modify and monetize it with minimal restrictions <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. This differs from Meta's Llama 2, which has been called [[open_source_ai_models | open source]] but includes caveats protecting Meta <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. However, Meta has contributed significantly to making AI more open than other major tech companies <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

## Uncensored AI Models

A common issue with both Llama and Mixol is that they are highly censored and "aligned" out of the box <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. While this can be beneficial for customer-facing products, it is impractical for certain use cases <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. Fortunately, it is possible to "un-align" these AIs <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

Eric Hartford, creator of the MixDolphin model, has written a blog post explaining how uncensored models work and their valid applications <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. The MixDolphin model not only improved coding ability but was also uncensored by filtering its dataset to remove alignment and bias <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. Examples of its capabilities include teaching users how to cook, ride a horse, and even how to infect a Windows machine with a keylogger in Python <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

## Running Large Language Models Locally

One way to achieve freedom in [[ai_in_software_engineering | AI in software engineering]] is by running uncensored large language models (LLMs) on a local machine <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

### Olama
Among various options like the Oobabooga web UI <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>, Olama is a popular open-source tool written in Go that simplifies the download and execution of [[open_source_ai_models | open source AI models]] locally <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

*   **Installation** Olama can be installed with a single command on Linux or Mac and can be run on Windows using WSL <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.
*   **Usage** After installation, users can run `olama serve` in one terminal and then use the `run` command for specific models in another <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>. Olama supports popular [[open_source_ai_models | open source AI models]] like Mixol and Llama 2, including the Dolphin Mixol uncensored model <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   **Requirements** Running these models locally requires downloading the model (e.g., MixDolphin is about 26 GB) and a machine with substantial RAM (e.g., 40 GB out of 64 GB for MixDolphin) <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. Once set up, users can prompt the LLM directly from the command line, accessing powerful capabilities without standard safety guards <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. This impacts the [[role_and_value_of_ai_tools_in_programming | role and value of AI tools in programming]] by giving developers direct control.

## Fine-Tuning Models with Custom Data

Users can further customize models by fine-tuning them with their own data <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.

### Hugging Face AutoTrain
Hugging Face AutoTrain simplifies this process <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
*   **Process** Users create a new space on Hugging Face, choose the Docker image for AutoTrain, and select a base model (e.g., from "the bloke") <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. AutoTrain supports not only LLMs but also image models like Stable Diffusion <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **Hardware** While possible to run AutoTrain locally, it typically requires significant GPU power. Hardware can be rented from cloud providers like Hugging Face, AWS Bedrock, or Google Vertex AI <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. For instance, the MixDolphin model took approximately three days to train on four A100 GPUs, costing around $1,200 (at $4.3 per hour per A100) <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
*   **Training Data** Training data usually consists of prompt and response pairs <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. To create an uncensored model, the training data should encourage the model to comply with any request, even if unethical or immoral. Incorporating esoteric content from banned books or the dark web can also contribute to this <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

By running and fine-tuning these models, users gain unprecedented control, fostering a new era of freedom in [[ai_in_software_engineering | AI in software engineering]] <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. This represents a significant [[impact_of_ai_tools_on_coding_and_developers | impact of AI tools on coding and developers]].