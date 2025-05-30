---
title: Chinese AI development and restrictions
videoId: 7EH0VjM3dTk
---

From: [[redpointai]] <br/> 

The United States has implemented significant regulations aimed at limiting China's progress in artificial intelligence (AI), viewing AI as a critical factor for global hegemony in the coming century <a class="yt-timestamp" data-t="00:31:00">[00:31:00]</a>. These regulations, particularly the "AI diffusion rule," are the most far-reaching seen by some experts, regulating clouds overseas and limiting what foreign companies can buy <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>.

## Regulatory Landscape

The initial October 2022 regulations primarily targeted the semiconductor industry with the explicit goal of regulating AI due to its anticipated rapid advancement <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>. These regulations were intended to maintain the US lead over China in AI, believing the next few years of progress will shape the next century of global dominance <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>. While well-intentioned from a perspective of immediate AI transformation, these regulations could negatively impact US competitiveness long-term if AI development takes 20 years instead of five <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>. Subsequent rounds of regulations in 2023 and December continued to patch loopholes <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>.

### Key Restrictions and Loopholes

Current [[regulation_and_policy_implications_of_ai | regulations]] impose strict caps on GPU purchases, with each country limited to buying 50,000 GPUs over four years, a negligible amount compared to Nvidia's total production <a class="yt-timestamp" data-t="13:30:00">[13:30:00]</a>. A notable loophole exists where purchases of 1,700 or fewer GPUs do not count towards the 50,000 unit cap <a class="yt-timestamp" data-t="13:43:00">[13:43:00]</a>. This could allow for the use of numerous shell companies to acquire GPUs and route them to China <a class="yt-timestamp" data-t="13:50:00">[13:50:00]</a>.

Furthermore, there are explicit prohibitions on exporting model weights outside of the US or trusted cloud environments, which are primarily US hyperscalers <a class="yt-timestamp" data-t="10:46:00">[10:46:00]</a>. [[regulatory_and_safety_issues_in_ai_model_development | Regulations]] also target synthetic data generation, a technique widely used by Chinese companies to improve their models using data from advanced models like GPT-4 <a class="yt-timestamp" data-t="11:05:00">[11:05:00]</a>. Accessing cloud services is also heavily regulated <a class="yt-timestamp" data-t="11:27:00">[11:27:00]</a>.

### Impact on Chinese Companies and Cloud Providers

The "AI diffusion rule" has significantly hampered Chinese AI players and various cloud companies <a class="yt-timestamp" data-t="13:07:00">[13:07:00]</a>. Before these [[regulation_and_policy_implications_of_ai | regulations]], the AI development landscape was largely unregulated globally <a class="yt-timestamp" data-t="09:40:00">[09:40:00]</a>. Now, Chinese companies are heavily restricted in the size of clusters they can obtain and face notification requirements and demands for observability into their workloads <a class="yt-timestamp" data-t="12:54:00">[12:54:00]</a>.

Many smaller cloud companies, particularly those in foreign countries, are severely impacted as their business model relied on selling GPU access to Chinese firms like ByteDance <a class="yt-timestamp" data-t="08:32:00">[08:32:00]</a>. ByteDance, which previously rented GPUs from various global clouds, is now heavily limited in cluster size and access to compute <a class="yt-timestamp" data-t="12:17:00">[12:17:00]</a>.

Some Chinese companies like Alibaba have their own hyperscale partners, but many new players such as Moonshot and DeepSeek lack such partnerships <a class="yt-timestamp" data-t="11:54:00">[11:54:00]</a>. Foreign firms, including American companies, are also impacted; for example, Oracle faced challenges due to a rule limiting data center capacity in non-US ally countries to 7% <a class="yt-timestamp" data-t="05:51:00">[05:51:00]</a>.

## Chinese Response and Future Outlook

Facing these restrictions, China's numerous skilled engineers will be forced to innovate <a class="yt-timestamp" data-t="14:08:00">[14:08:00]</a>. Companies like DeepSeek are noted for their strong engineering capabilities, allowing them to outperform competitors with similar compute levels <a class="yt-timestamp" data-t="14:11:00">[14:11:13]</a>. However, American labs' compute continues to scale rapidly, while China's cannot keep pace <a class="yt-timestamp" data-t="14:26:00">[14:26:00]</a>. This necessitates a "way, way, way, way better" engineering approach from China to overcome this compute deficiency <a class="yt-timestamp" data-t="14:32:00">[14:32:00]</a>.

### Focus on Test-Time Compute and Inference

The push towards test-time compute (also known as inference) could offer a path for China <a class="yt-timestamp" data-t="14:34:00">[14:34:00]</a>. While test-time compute requires significant training, particularly post-training with synthetic data generation and reward models, it represents a less mature "rung of the ladder" compared to traditional training <a class="yt-timestamp" data-t="15:00:00">[15:00:00]</a>. This means Chinese companies might be able to achieve significant gains through engineering improvements with their limited compute resources <a class="yt-timestamp" data-t="16:08:00">[16:08:00]</a>.

However, scaling inference is crucial for AI to "change the world," and China's GPU limitations will make this very difficult <a class="yt-timestamp" data-t="17:48:00">[17:48:00]</a>. The high costs associated with inference, even with low margins, translate to massive hardware investments that exceed the caps imposed by regulations <a class="yt-timestamp" data-t="18:14:00">[18:14:00]</a>.

### Domestic Supply Chain and Geopolitical Considerations

The stricter [[regulation_and_policy_implications_of_ai | regulations]] force China to either build its own domestic supply chain for semiconductors and AI hardware or access limited Western sphere resources <a class="yt-timestamp" data-t="23:41:00">[23:41:00]</a>. Some believe that if these regulations are highly effective in preventing China from developing its own semiconductor industry, or if China builds a competitive one, it could increase the likelihood of action on Taiwan <a class="yt-timestamp" data-t="23:48:00">[23:48:00]</a>. The "Goldilocks zone" for policy would be to keep China behind but with enough hope of catching up to avoid inducing greater risk <a class="yt-timestamp" data-t="24:26:00">[24:26:00]</a>.

The US government's approach reflects a desire to maintain hegemony, even if it means creating a semi-monopoly for large US tech companies in the global AI infrastructure market, akin to Henry Ford producing tanks during World War II <a class="yt-timestamp" data-t="07:07:00">[07:07:00]</a>. This approach centralizes power and could potentially stifle [[strategic_considerations_for_ai_application_developers | innovation]] in hardware and infrastructure outside of the major players <a class="yt-timestamp" data-t="07:32:00">[07:32:00]</a>.

### Sovereign AI Initiatives

Many countries are pursuing "Sovereign AI" initiatives, seeking to develop their own AI expertise and models internally <a class="yt-timestamp" data-t="08:36:00">[08:36:00]</a>. American startups serving these firms in regions like Malaysia, Singapore, India, and the Middle East are heavily impacted by the [[regulation_and_policy_implications_of_ai | regulations]] <a class="yt-timestamp" data-t="08:40:00">[08:40:00]</a>. The case of G42 in the UAE illustrates this, where initial concerns over Chinese links led to a partnership with Microsoft, demonstrating how the US can enforce its sphere of influence through hyperscalers <a class="yt-timestamp" data-t="20:11:00">[20:11:00]</a>. Future US administrations may tweak these rules, potentially shifting focus from human rights considerations to economic influence <a class="yt-timestamp" data-t="21:50:00">[21:50:00]</a>.