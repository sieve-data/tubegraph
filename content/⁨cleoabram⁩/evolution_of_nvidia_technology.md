---
title: Evolution of NVIDIA technology
videoId: 7ARBJQn6QkM
---

From: [[⁨cleoabram⁩]] <br/> 

NVIDIA, under the leadership of CEO Jensen Huang, has spearheaded a fundamental shift in how computers operate, leading to the current explosion of technological possibilities in fields like AI, robotics, gaming, self-driving cars, and medical research <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. The company's decisions have profoundly influenced daily life over the past 30 years, and many believe this is just the beginning of even greater transformations <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

## The Genesis: Parallel Processing and GPUs

NVIDIA's journey began in the early 1990s with a crucial observation about software programs: a small fraction of code (around 10%) performs the vast majority of processing (99%), and this processing could be done in parallel <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. The remaining 90% of the code requires sequential processing. This led to the insight that the ideal computer should be capable of both sequential and parallel processing, not just one or the other <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

NVIDIA set out to build a company to solve problems that traditional computers couldn't, marking the beginning of the company <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. This concept is often illustrated by comparing a CPU (Central Processing Unit) to a GPU (Graphics Processing Unit): a CPU solves problems one at a time (sequential processing), while a GPU handles many smaller problems simultaneously (parallel processing) <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

### Gaming as the Catalyst
NVIDIA first applied this parallel processing power to video games, as 3D graphics inherently require parallel processing <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. This choice was driven by a love for the application—simulating virtual worlds—and the belief that video games had the potential to become the largest entertainment market ever, which proved true <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. The large market size allowed for significant R&D budgets, creating a "flywheel" between technology, market, and greater technology that propelled NVIDIA to become one of the most important technology companies globally <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.

GPUs were described as "time machines" because they accelerate computing, enabling users to "see the future sooner" <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>. For instance, a quantum chemistry scientist could complete their life's work within their lifetime due to the speed-up provided by NVIDIA's GPUs, allowing for previously impossible simulations and predictions, such as weather forecasting or self-driving car simulations <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.

## CUDA Platform: Democratizing Parallel Computing

While GPUs initially unlocked power for gaming, their potential extended to other industries <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. Researchers, like the quantum chemistry researcher, began "tricking" GPUs into thinking their non-graphics problems were graphics problems to leverage their parallel processing capabilities <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

Recognizing this, NVIDIA developed [[accelerated_computing_and_cuda_platform | CUDA]], a platform that made it significantly easier for programmers to utilize GPUs for general-purpose acceleration using familiar languages like C <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. The vision behind CUDA stemmed from a "soup" of aspiration, inspiration, and desperation <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. External ideas, such as researchers at Mass General using GPUs for CT reconstruction, inspired its development <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>. Internally, the need to create dynamic and realistic virtual worlds for video games, requiring complex physics and fluid dynamics, also pushed for a more general-purpose parallel computing solution <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.

The success of CUDA was largely predicted because GPUs, driven by the massive video game market, were poised to become the highest-volume parallel processors in the world, ensuring widespread adoption of this architecture <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.

## The AI Revolution: AlexNet and Deep Learning

The true watershed moment for NVIDIA's technology came in 2012 with AlexNet, a neural network developed by Ilya Sutskever, Alex Krizhevsky, and Geoff Hinton at the University of Toronto <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>. Their system significantly outperformed competitors in an image recognition challenge by training on a massive dataset using NVIDIA GPUs <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>. This marked a profound shift: computers were no longer just being instructed with step-by-step directions but were being *trained* to learn from vast numbers of examples <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.

This breakthrough prompted NVIDIA to re-engineer its entire computing stack, leading to the creation of systems like DGX, an AI supercomputer <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>. NVIDIA reasoned that if deep learning architectures could scale, they could represent and solve a vast majority of machine learning problems, potentially reshaping the entire computer industry <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>. Problems once deemed impossible, such as computer vision, speech recognition, and language understanding, began to be solved rapidly <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>.

## Core Beliefs and Long-Term Commitment

NVIDIA's decade-long commitment to this vision, from AlexNet in 2012 to the widespread AI adoption a decade later, stemmed from deep-seated core beliefs <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>. These beliefs are:
*   **[[accelerated_computing_and_cuda_platform | Accelerated computing]]**: The conviction that parallel processing, combined with general-purpose computing, is the optimal approach <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>.
*   **Scalability of Deep Learning Networks (DNNs)**: The recognition that DNNs can learn increasingly nuanced features and relationships from various data types by growing larger and larger <a class="yt-timestamp" data-t="00:20:06">[00:20:06]</a>. Empirical evidence has shown that larger models and data sizes lead to more learned knowledge, with no apparent physical, architectural, or mathematical limits <a class="yt-timestamp" data-t="00:20:40">[00:20:40]</a>.
*   **Learning from Data**: The understanding that AI can learn from "digital versions of human experience" (data) across almost any modality—from object recognition in images to speech from sound, and even language, vocabulary, syntax, and grammar from text <a class="yt-timestamp" data-t="00:21:05">[00:21:05]</a>. This enables transformations between modalities, such as text to text (summarization, translation), text to images (image generation, like [[how_dalle_2_functions_and_its_technology | DALLE 2 functions and its technology]]), images to text (captioning), and even amino acid sequences to protein structures <a class="yt-timestamp" data-t="00:21:42">[00:21:42]</a>. This opens a "universe of opportunities and problems" for AI to solve <a class="yt-timestamp" data-t="00:22:33">[00:22:33]</a>.

NVIDIA invested "tens of billions of dollars" in this future before it fully materialized, maintaining conviction even when faced with impatience or pressure from investors <a class="yt-timestamp" data-t="00:19:17">[00:19:17]</a>.

## Future Vision: Applied AI and Robotics

The next decade will shift from the "science of AI" to the "application science of AI" <a class="yt-timestamp" data-t="00:23:07">[00:23:07]</a>. This means applying AI to various fields like digital biology, climate technology, agriculture, robotics, transportation, logistics optimization, and even teaching and podcasting <a class="yt-timestamp" data-t="00:23:24">[00:23:24]</a>.

### Physical AI: Robots and Omniverse
A significant focus for NVIDIA is [[the_future_advancements_in_ai_beyond_art_generation | physical AI]], encompassing humanoid robots, self-driving cars, smart buildings, autonomous warehouses, and more <a class="yt-timestamp" data-t="00:24:07">[00:24:07]</a>. The training of robots is undergoing a "big bang moment" <a class="yt-timestamp" data-t="00:25:07">[00:25:07]</a>. Historically, robots were trained in the real world (risking damage) or with limited data from motion capture suits <a class="yt-timestamp" data-t="00:24:37">[00:24:37]</a>. Now, NVIDIA is enabling robot training in digital worlds using **Omniverse** and **Cosmos** <a class="yt-timestamp" data-t="00:25:11">[00:25:11]</a>.

*   **Cosmos** provides a "world language model" or "world common sense" for AI, encoding fundamental physical principles like gravity, friction, inertia, geometric and spatial awareness, object permanence, and cause and effect <a class="yt-timestamp" data-t="00:28:08">[00:28:08]</a>. This provides a "foundation model" for robots, similar to how ChatGPT has a core language model <a class="yt-timestamp" data-t="00:27:35">[00:27:35]</a>.
*   **Omniverse** acts as a physical simulator that uses principled solvers based on Newtonian physics to provide "ground truth" for Cosmos <a class="yt-timestamp" data-t="00:28:42">[00:28:42]</a>. The combination allows for generating infinite, physically plausible future scenarios for robots to learn from, vastly accelerating their training compared to real-world methods <a class="yt-timestamp" data-t="00:29:09">[00:29:09]</a>.

The vision is that "everything that moves will be robotic someday and it will be soon," including lawnmowers, cars, and humanoid robots <a class="yt-timestamp" data-t="00:30:22">[00:30:22]</a>. This future envisions personal AI companions, like an "R2-D2" that lives with you, present in smart glasses, phones, PCs, and cars, growing up with you over a lifetime <a class="yt-timestamp" data-t="00:31:32">[00:31:32]</a>.

### Other Key Bets
NVIDIA's current bets include:
*   The fusion of Omniverse and Cosmos for generative world creation, crucial for robotics and physical systems <a class="yt-timestamp" data-t="00:44:43">[00:44:43]</a>.
*   Further development of tooling, training, and human demonstration systems for human robotics <a class="yt-timestamp" data-t="00:45:06">[00:45:06]</a>.
*   Work in [[digital_biology | digital biology]] to understand the language of molecules and cells, aiming for a digital twin of the human body and capabilities like predicting drug targets <a class="yt-timestamp" data-t="00:45:28">[00:45:28]</a>.
*   Advancements in climate science, enabling high-resolution regional weather predictions <a class="yt-timestamp" data-t="00:45:56">[00:45:56]</a>.

## Challenges and Limitations

While the future is exciting, NVIDIA also considers potential challenges:
*   **AI Safety**: Addressing issues like bias, toxicity, hallucination (generating plausible but untruthful answers), and impersonation <a class="yt-timestamp" data-t="00:32:24">[00:32:24]</a>.
*   **Engineering Challenges**: Ensuring AI systems function properly and safely, particularly for real-world applications like self-driving cars, where malfunctions could cause harm <a class="yt-timestamp" data-t="00:33:11">[00:33:11]</a>. This includes building redundancy into systems, similar to flight computers in airplanes <a class="yt-timestamp" data-t="00:34:13">[00:34:13]</a>.
*   **Physical Limits**: The ultimate limitation is the amount of work that can be done within energy constraints, particularly concerning transporting and flipping bits <a class="yt-timestamp" data-t="00:35:47">[00:35:47]</a>. However, current technology is "far from having any fundamental limits that keep us from advancing" <a class="yt-timestamp" data-t="00:36:23">[00:36:23]</a>. NVIDIA's focus is on building "better and more energy-efficient computers," having increased the [[impact_of_gpus_on_computing_and_ai | energy efficiency]] of AI computing by 10,000 times since 2016 <a class="yt-timestamp" data-t="00:36:29">[00:36:29]</a>.

## Design Philosophy: Flexibility vs. Specificity

NVIDIA's design philosophy prioritizes architectural flexibility to enable continuous innovation rather than optimizing hardware for specific, current AI models like transformers <a class="yt-timestamp" data-t="00:39:03">[00:39:03]</a>. The belief is that no single algorithm or architecture will remain dominant indefinitely; innovation and new ideas will continue to emerge, requiring adaptable computing platforms <a class="yt-timestamp" data-t="00:40:01">[00:40:01]</a>. For example, while transformers rely on an "attention mechanism," new variants like "flash attention" and "hierarchical attention" are constantly being invented <a class="yt-timestamp" data-t="00:41:05">[00:41:05]</a>.

To push the limits of what's physically possible, NVIDIA maintains deep internal expertise in semiconductor physics, system engineering, and cooling systems (like liquid and air cooling), even though manufacturing is outsourced <a class="yt-timestamp" data-t="00:42:56">[00:42:56]</a>.

## Preparing for the AI Future

Jensen Huang advises that the next decade, driven by [[technological_advances_enabling_ai_capabilities | technological advances enabling AI capabilities]], will make intelligence superhuman in some areas <a class="yt-timestamp" data-t="00:50:13">[00:50:13]</a>. This will not make humans unnecessary but will empower them to tackle more ambitious challenges <a class="yt-timestamp" data-t="00:50:56">[00:50:56]</a>.

He encourages everyone, especially students, to learn how to interact with AI <a class="yt-timestamp" data-t="00:55:48">[00:55:48]</a>. This involves mastering "prompting" AI tools like ChatGPT, Gemini Pro, or Grok <a class="yt-timestamp" data-t="00:55:54">[00:55:54]</a>. The key question for any profession will be: "How can I use AI to do my job better?" <a class="yt-timestamp" data-t="00:56:40">[00:56:40]</a>. AI lowers the barriers to understanding, knowledge, and intelligence, acting as a personal tutor that can teach, program, write, analyze, think, and reason <a class="yt-timestamp" data-t="00:51:32">[00:51:32]</a>.

## NVIDIA Products and AI in Gaming

NVIDIA's technology continues to evolve:
*   **GeForce RTX 50 Series**: A graphics card that acts as a supercomputer for PCs, used in gaming, design, and creative arts. It leverages AI, predicting 7.5 million of 8 million pixels on a 4K display while only computing 500,000, making images perfect and incredibly energy-efficient <a class="yt-timestamp" data-t="00:52:27">[00:52:27]</a>. This demonstrates how AI makes humans "superhuman" by offloading mundane tasks, allowing focus on valuable aspects <a class="yt-timestamp" data-t="00:54:11">[00:54:11]</a>.
*   **DGX Mini**: A smaller, more accessible version of the DGX AI supercomputer (originally $250,000, delivered the first to OpenAI in 2016 <a class="yt-timestamp" data-t="00:54:52">[00:54:52]</a>). Priced around $3,000, it aims to make AI development accessible to every engineer, student, and AI scientist, enabling them to "build your own AI, build your own R2-D2" <a class="yt-timestamp" data-t="00:55:06">[00:55:06]</a>.

NVIDIA aims to make an extraordinary impact by ensuring its capabilities are pervasively available across all fields of science, whether profitable or not, large or small <a class="yt-timestamp" data-t="01:00:14">[01:00:14]</a>. The hope is that future generations will look back and see how NVIDIA, originating from gaming technology, transformed fields like [[digital_biology | digital biology]], material sciences, and made robots pervasive, turning cars into personal mobile spaces <a class="yt-timestamp" data-t="01:01:59">[01:01:59]</a>.