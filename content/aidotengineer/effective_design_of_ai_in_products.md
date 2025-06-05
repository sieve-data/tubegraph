---
title: Effective design of AI in products
videoId: 2cEGQEllBGc
---

From: [[aidotengineer]] <br/> 

Current trends in AI integration often involve simply adding chatbots to products, which may not genuinely assist users <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. Arthur, a product designer at Evil Martians, challenges this approach, advocating for a different perspective on integrating AI into products <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## Challenging the Status Quo

Arthur's work on Tigon, an AI issue tracker, involved taking the complete opposite approach to conventional AI integration, which proved successful <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. The core idea for effective AI has been around for 25 years, reminiscent of Clippy <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. While Clippy had terrible execution and timing, the underlying concept was correct, and current technology allows for its proper implementation <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

Instead of making AI assistants more reactive, the focus should be on proactive AI that anticipates user needs <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

### Proactive AI in Practice (Tigon Examples)

Tigon demonstrates AI that doesn't wait for user input but rather observes real-time user actions, understands context, and intervenes at the opportune moment with relevant, contextual questions <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

#### Suggestion Mode
In "suggestion mode," the AI tracks what the user is writing in real-time, understands the context, and proactively offers specific, non-generic questions to move work forward, all without needing a chat window <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. For example, if a user reports a legality issue, the AI immediately asks specific questions related to the issue <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

#### Action Mode
"Action mode" is demonstrated when a user writes an issue that could be split into sub-issues <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. Unlike typical reactive AI, Tigon's AI recognizes the complexity and suggests a better way to organize the work <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. It identifies sub-issues, leveraging previous data and general understanding of optimal organization <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>. This represents AI that truly understands the domain <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. Beyond organization, this AI can consider timelines and resources, acting like a constantly attentive project manager <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

#### Question + Action Mode
This combined mode facilitates interaction within the natural workflow, eliminating context switching, extra windows, or chat interfaces <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. It asks relevant questions and assists in managing issues more effectively <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>. Users maintain control and can easily revert any changes with a single click <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

### Benefits of Proactive AI
This form of AI seamlessly guides the user, eliminating time wasted on trying to articulate needs <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. It supports users in creating better work without disrupting their flow <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. This pattern, while built for issue tracking, holds significant potential across various professional tools <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

## Principles for Developing Proactive AI Systems

To foster [[guidelines_for_developing_proactive_ai_systems | proactive AI systems]] in products, three simple rules should be followed <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>:

> [!rule] Rules for Proactive AI
> 1.  AI should **supplement user agency**, not replace it <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
> 2.  AI should **offer recommendations**, never force them <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
> 3.  AI should be a part of the **natural workflow**, not interrupt it <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

### Applications in Other Tools
This approach can be applied broadly, leading to [[design_process_improvements_with_ai | design process improvements with AI]]:
*   **Code editors** can proactively watch for common pitfalls and suggest improvements, especially valuable for developers learning new languages or frameworks <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
*   **Design tools** could make suggestions for accessible design as the user works, removing the need for post-design checks <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
*   **Communication tools** could prepare relevant context before meetings or find documents mentioned during calls <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

In all these scenarios, the user remains in control, benefiting from an integrated advisor <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

## How to Integrate Proactive AI into Products

To begin implementing this approach in your own products, consider these steps:
1.  **Identify Friction Points**: Look for areas where users pause their work to ask for help; these are opportunities for proactive assistance <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
2.  **Recognize User Behavior Patterns**: Identify common scenarios where users need help or frequently ask questions, providing clues for automation <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
3.  **Prioritize Context**: Focus on where users get stuck, as this is where AI can provide the most assistance <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

## Conclusion

[[design_challenges_for_ai_agents | AI interface design]] is still in its nascent stages, meaning there isn't a complete playbook of [[best_practices_for_building_ai_systems | best practices]] yet <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. Simply replicating chat interfaces is not the solution <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>. It is crucial to experiment, challenge the status quo, and propose unexpected UI solutions in product development <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.