---
title: User feedback and AI development
videoId: Ghc-qalQFLw
---

From: [[aidotengineer]] <br/> 

Alma's core belief is that eating well should not be difficult, and good health stems from simple, personalized nutrition <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. Traditional nutrition apps often demand extensive information from users while providing minimal value in return <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. Alma aims to solve this with AI, envisioning a true nutrition companion <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

The vision for Alma's AI nutrition companion rests on three pillars:
1.  **Simple Nutrition Tracking**: Making tracking easy, natural, and conversational, like texting a friend, rather than tedious searches or unreliable photo analysis <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
2.  **Contextualized Insights**: Building strong, powerful context around the user's preferences, habits, and interests to guide them towards their goals <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
3.  **Product Connection**: Connecting users with appropriate products, restaurants, and meals to help them achieve their health objectives <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

Alma also developed the "Alma Score," a score out of 100, in collaboration with Dr. Eric Prim at Harvard University <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. This score helps users understand the holistic quality of their diet, nudging them towards beneficial foods and away from less healthy options <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. This concept emerged from early user feedback indicating a desire to understand food quality beyond just calories and macros <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

## The Pivotal Role of User Feedback in AI Development

A significant lesson learned during Alma's beta phase (a closed beta for about 4 months, shipped in February) was the critical importance of relying on user feedback <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>, <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>, <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. While [[Evaluation and feedback in AI systems | AI evaluation]] methods are explored, nothing surpasses real-time, in-the-moment feedback from users <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

### Directly Soliciting Feedback

One of Alma's key [[Best practices and lessons learned in AI agent development | best practices]] for gathering feedback is a pop-up toast notification that asks, "How did Alma do?" after every interaction <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. This feature has been invaluable in guiding development and measuring accuracy and improvements <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.

### Lessons Learned from User Interactions

Through consistent user engagement, Alma has gained several insights influencing its [[developing_and_optimizing_ai_agents | development process]]:

*   **Constraining LLMs**: Large Language Models (LLMs) tend to have high error rates when given open-ended, very large tasks <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. It's crucial to constrain the LLM to specific tasks <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. Alma addresses this by breaking down the information relay process into steps, sending down certain aspects at each stage (e.g., recognizing a food item, extracting it, sending it to the client, then processing it with a USDA database) <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. This approach makes the experience feel much faster and more interactive for users <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   **User Value of "Streaks"**: A bug that broke user "streaks" (consistent tracking) caused significant outcry in Alma's WhatsApp community <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>. This revealed that a feature initially considered minor was highly valued by users, prompting Alma to double down on it <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
*   **[[Continuous improvement in AI systems | Building User Context]]**: Users become frustrated when they have to reiterate information <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. Alma addresses this by constantly learning about the user; any novel piece of information from an interaction is added to a knowledge dataset about the user <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>. Users can view, delete, or add to this information, ensuring Alma gets smarter with every interaction <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
*   **Proactive Insights**: Users don't always open the app to ask questions <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>. Alma therefore proactively detects insights about users' eating habits and surfaces information they might not know <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>. This creates a constant, bite-sized learning process for the user <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.
*   **Multimodality**: While some developers might prefer a specific interaction modality (e.g., voice), user feedback showed that users appreciate the flexibility of multimodality <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>, <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. Alma makes it easy to track food via voice, photo, or text, allowing users to choose based on context <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.

## Looking Forward: User-Centric Strategic Pillars

Alma's future strategy is heavily influenced by these [[best_practices_for_ai_evaluation | user-centric learnings]]:

*   **Brand and Design**: As code becomes a commodity, strong brand identity and visually appealing, user-centric design are crucial for standing out <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>. This is ingrained in Alma's DNA <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
*   **Trust and Partnerships**: Earning user trust, especially as a new product, involves partnering with entities users already trust and aligning on mission <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>. Alma actively asks users about their trusted information sources to explore potential collaborations <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
*   **Community and New Data**: As the community grows, there's user interest in how others eat and a desire to learn from shared habits <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>. Since major LLM companies are "hoovering up" existing online data, Alma focuses on leveraging its users to create valuable, net new data <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>.