---
title: Introduction and overview of DeepSeek R1 reasoning models
videoId: i9kTrcf-gDQ
---

From: [[gregisenberg]] <br/> 

DeepSeek R1 is a new reasoning model that has gained significant attention in the AI community. Developed in China, this model is noted for its advanced capabilities, rivaling models like ChatGPT's 01 reasoning model <a class="yt-timestamp" data-t="00:56:00">[00:56:00]</a>. Its popularity is partly due to it being free to use on its official website, deepseek.com <a class="yt-timestamp" data-t="01:04:00">[01:04:00]</a>.

## Key Capabilities and Features

DeepSeek R1 models are designed to think and reason, leading to what some describe as "superhuman capabilities" <a class="yt-timestamp" data-t="00:32:00">[00:32:00]</a>.
These models excel at:
*   **Deep Analysis**: They can process extensive text, such as interview transcripts, and perform detailed analysis <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a>.
*   **Content Generation**: DeepSeek R1 can generate high-quality outputs like blog posts from raw transcripts <a class="yt-timestamp" data-t="04:42:00">[04:42:00]</a>. The generated content is described as "pretty human level incredible," comparable to the work of a senior writer or research engineer <a class="yt-timestamp" data-t="14:24:00">[14:24:00]</a>.
*   **Following Instructions**: Reasoning models like DeepSeek R1 spend extra time and pay close attention to detailed instructions, ensuring that every specified detail is addressed in the output <a class="yt-timestamp" data-t="15:14:00">[15:14:00]</a>.
*   **Data Interpretation**: It can pick up specific details discussed in a live stream and even create graphs based on that information <a class="yt-timestamp" data-t="12:35:00">[12:35:00]</a>.
*   **Web Search Integration**: The DeepSeek.com interface allows for enabling web search to verify claims or gather information from the internet <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>, <a class="yt-timestamp" data-t="20:25:00">[20:25:00]</a>.

### Comparison to Other Models
While comparable to ChatGPT in reasoning, DeepSeek R1's full model can produce more detailed and in-depth results than smaller, distilled models, although it may take longer to process <a class="yt-timestamp" data-t="12:09:00">[12:09:00]</a>. Compared to other models, DeepSeek R1 can create highly refined and complete content that requires less human intervention, making it a significant advantage for businesses and startups <a class="yt-timestamp" data-t="13:05:00">[13:05:00]</a>.

## Availability and Usage

DeepSeek R1 can be accessed in several ways, each with its own considerations:

### DeepSeek.com Website
The simplest way to use DeepSeek R1 is directly through deepseek.com <a class="yt-timestamp" data-t="02:25:00">[02:25:00]</a>. Users can paste transcripts or prompts and enable features like "Deep Think" for reasoning <a class="yt-timestamp" data-t="04:09:00">[04:09:00]</a>.

> [!CAUTION] Data Privacy Concerns
> DeepSeek.com is currently hosted in China <a class="yt-timestamp" data-t="02:28:00">[02:28:00]</a>. When data is sent to another country, it falls under that country's laws and regulations. Therefore, users should be extremely cautious about inputting sensitive data, such as tax returns or medical records, as it may not be subject to the user's local privacy controls <a class="yt-timestamp" data-t="01:39:00">[01:39:00]</a>, <a class="yt-timestamp" data-t="05:19:00">[05:19:00]</a>, <a class="yt-timestamp" data-t="21:55:00">[21:55:00]</a>. Server busyness can also be an issue due to its popularity <a class="yt-timestamp" data-t="07:36:00">[07:36:00]</a>.

### API Providers
To mitigate data privacy concerns and improve reliability, DeepSeek R1 can be accessed through API providers.
*   **Fireworks AI**: This provider hosts the DeepSeek model and allows access via an API key, ensuring data remains in regions like North America (e.g., Cursor coding app uses Fireworks API) <a class="yt-timestamp" data-t="03:11:00">[03:11:00]</a>, <a class="yt-timestamp" data-t="05:57:00">[05:57:00]</a>, <a class="yt-timestamp" data-t="08:47:00">[08:47:00]</a>, <a class="yt-timestamp" data-t="10:12:00">[10:12:00]</a>.
*   **Groq**: Also offers access to distilled versions of the DeepSeek model, known for incredible speed <a class="yt-timestamp" data-t="03:13:00">[03:13:00]</a>, <a class="yt-timestamp" data-t="11:13:00">[11:13:00]</a>.
*   **OpenRouter**: Another API provider that offers access to virtually every model, including DeepSeek R1 <a class="yt-timestamp" data-t="38:31:00">[38:31:00]</a>.

These services typically charge per million tokens. Fireworks AI charges around $8 per million tokens <a class="yt-timestamp" data-t="16:49:00">[16:49:00]</a>.

### Local Hosting
For maximum data privacy and control, DeepSeek R1 can be run locally on a personal machine. This is particularly useful for sensitive business data (e.g., lawyers, doctors) <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>.
The recommended setup involves:
1.  **Docker**: Download and install Docker Desktop, which provides a containerized environment <a class="yt-timestamp" data-t="23:00:00">[23:00:00]</a>.
2.  **Open Web UI**: This user-friendly interface can be run within Docker <a class="yt-timestamp" data-t="08:14:00">[08:14:00]</a>, <a class="yt-timestamp" data-t="22:54:00">[22:54:00]</a>. It supports connecting to API providers and local models.
3.  **Ollama**: Download Ollama to manage and run local models <a class="yt-timestamp" data-t="25:12:00">[25:12:00]</a>. Ollama allows downloading various models, including DeepSeek R1 (e.g., `deepseek-coder:latest`), directly to the machine <a class="yt-timestamp" data-t="25:47:00">[25:47:00]</a>, <a class="yt-timestamp" data-t="26:37:00">[26:37:00]</a>.
4.  **Mobile Access**: The Apollo app allows users to download and run local models directly on their mobile devices (e.g., Apple Silicon optimized models) <a class="yt-timestamp" data-t="37:04:00">[37:04:00]</a>, <a class="yt-timestamp" data-t="41:50:00">[41:50:00]</a>. This provides "reasoning on your phone, no internet, completely running locally" <a class="yt-timestamp" data-t="43:40:00">[43:40:00]</a>.

## Prompting and Model Efficiency

[[prompting_techniques_for_effective_use_of_AI_models | Prompting techniques]] are crucial for effectively utilizing DeepSeek R1 and other reasoning models. Users can configure instructions to get specific outputs, such as generating graphs or detailed analysis <a class="yt-timestamp" data-t="14:40:00">[14:40:00]</a>. OpenAI's playground, `platform.openai.com`, can assist in reconfiguring and improving prompts for better efficiency <a class="yt-timestamp" data-t="18:31:00">[18:31:00]</a>.

Model efficiency can also be adjusted:
*   **Parameter Count**: Larger models (e.g., 600+ billion parameters) offer more intelligence but take longer to process <a class="yt-timestamp" data-t="07:01:00">[07:01:00]</a>.
*   **Distilled Models**: Smaller, distilled versions (e.g., 7 billion parameter models) run much faster and can be just as efficient for certain tasks, though they may not provide the same depth of reasoning as full models <a class="yt-timestamp" data-t="07:17:00">[07:17:00]</a>, <a class="yt-timestamp" data-t="29:00:00">[29:00:00]</a>.
*   **Temperature Setting**: Adjusting the "temperature" parameter (e.g., from default 0.8 to lower values) can reduce "hallucinations" and make the model follow instructions more closely, while higher values promote creativity <a class="yt-timestamp" data-t="29:40:00">[29:40:00]</a>.

## Future Implications

The emergence of powerful and accessible models like DeepSeek R1 signifies a significant shift in the AI landscape, often referred to as a "llama world" or "deep seek world" <a class="yt-timestamp" data-t="17:17:00">[17:17:00]</a>, <a class="yt-timestamp" data-t="17:55:00">[17:55:00]</a>. The ability to run sophisticated AI models locally on personal devices, including phones, without internet connectivity, opens up vast possibilities for new applications and innovative startup ideas <a class="yt-timestamp" data-t="42:08:00">[42:08:00]</a>, <a class="yt-timestamp" data-t="43:40:00">[43:40:00]</a>, <a class="yt-timestamp" data-t="45:14:00">[45:14:00]</a>. This includes applications in areas like real-time medical assistance and advanced negotiation support by analyzing tone and cadence <a class="yt-timestamp" data-t="43:57:00">[43:57:00]</a>, <a class="yt-timestamp" data-t="45:49:00">[45:49:00]</a>.

The ongoing "AI arms race" is driving demand for chips and hosting providers capable of managing these large, complex models <a class="yt-timestamp" data-t="15:52:00">[15:52:00]</a>. Despite the rapid advancements, the field is still in its early stages, and users are encouraged to experiment and share their discoveries within the community <a class="yt-timestamp" data-t="50:40:00">[50:40:00]</a>, <a class="yt-timestamp" data-t="50:57:00">[50:57:00]</a>.