---
title: Role of domain experts in AI system development
videoId: Bf71xMwd-Y0
---

From: [[aidotengineer]] <br/> 

Domain experts play a crucial role in the development and refinement of AI systems, particularly at companies like Orbital, which focuses on automating real estate due diligence <a class="yt-timestamp" data-t="02:01:43">[02:01:43]</a>. Their specialized knowledge is vital for teaching AI models, evaluating performance, and ensuring the practical applicability of the AI solutions <a class="yt-timestamp" data-t="07:51:00">[07:51:00]</a>.

## Integration into Engineering Teams
At Orbital, the product engineering team, which is about half of their 80-person staff, includes embedded domain experts alongside product managers, designers, software engineers, and AI engineers <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>.

> [!info] **Composition of an AI Product Team**
> An effective AI product team at Orbital is structured with a product manager and designer, embedded domain experts, software engineers, AI engineers, and a tech lead <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>. This cross-functional setup ensures the delivery of functional agentic products <a class="yt-timestamp" data-t="03:06:00">[03:06:00]</a>.

## Key Responsibilities and Contributions

### Prompt Engineering and Expertise Transfer
A core responsibility of domain experts at Orbital is to write the [[strategies_for_effective_ai_implementation | prompts]] that infuse the AI system with their specialized knowledge <a class="yt-timestamp" data-t="07:45:00">[07:45:00]</a>.

> [!example] **Real Estate Lawyers as Domain Experts**
> Orbital heavily relies on private practice real estate lawyers who have decades of experience <a class="yt-timestamp" data-t="07:34:00">[07:34:00]</a>. These experts effectively "teach" the AI system their legal expertise by writing domain-specific prompts <a class="yt-timestamp" data-t="07:47:00">[07:47:00]</a>. The number of these domain-specific prompts has grown from nearly zero to over 1,000 <a class="yt-timestamp" data-t="09:18:00">[09:18:00]</a>.

### Evaluation and Feedback Loops
Domain experts are instrumental in the [[evaluations_and_finetuning_in_ai_development | evaluation]] and feedback process, particularly given the dynamic nature of AI model development <a class="yt-timestamp" data-t="08:06:00">[08:06:00]</a>.

*   **Testing and Validation:** They are involved in rigorously experimenting with new AI models as they are released <a class="yt-timestamp" data-t="09:39:00">[09:39:00]</a>.
*   **Subjective "Vibes" over Formal Evals:** In the absence of a comprehensive, objective [[evaluations_and_finetuning_in_ai_development | evaluation]] system, Orbital has relied on "vibes," meaning human evaluation by domain experts who test the system before release <a class="yt-timestamp" data-t="08:01:00">[08:01:00]</a>. This involves subjective assessment and sometimes logging issues in spreadsheets to identify regressions from prior model changes <a class="yt-timestamp" data-t="08:36:00">[08:36:00]</a>.
*   **Rapid Feedback Integration:** Domain experts receive user feedback directly through the product, evaluate it, identify which prompt needs modification, and then implement that change into production, often within minutes or hours <a class="yt-timestamp" data-t="17:27:00">[17:27:00]</a>. This rapid cycle allows for quick fixes and continuous product improvement <a class="yt-timestamp" data-t="17:48:00">[17:48:00]</a>.

## Challenges and Future Outlook
The increasing number of prompts introduces a "prompt tax," making it more challenging to manage as the system grows <a class="yt-timestamp" data-t="09:30:00">[09:30:00]</a>. Despite the success achieved through a combination of domain expert input and user feedback, there's an acknowledgment that relying solely on "vibes" may not scale indefinitely as the product's surface area expands <a class="yt-timestamp" data-t="21:06:00">[21:06:00]</a>. The complexity of evaluating aspects like correctness, style, conciseness, and citation accuracy in legal AI makes creating a comprehensive [[evaluations_and_finetuning_in_ai_development | evaluation]] system a challenging task <a class="yt-timestamp" data-t="21:49:00">[21:49:00]</a>.