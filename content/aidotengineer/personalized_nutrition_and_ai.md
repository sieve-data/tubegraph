---
title: Personalized nutrition and AI
videoId: Ghc-qalQFLw
---

From: [[aidotengineer]] <br/> 

Alma is an AI-powered nutrition companion built on the belief that eating well should be simple and personalized, leading to good health <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. Existing nutrition apps often demand extensive information from users while providing minimal value in return, indicating a fundamental imbalance in the current approach <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. Alma aims to leverage AI to address this challenge, offering a unique and effective nutrition companion <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## Core Vision of Alma

Alma's vision for an AI nutrition companion is built on three core pillars <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>:

1.  **Simplified Nutrition Tracking**
    The goal is to make nutrition tracking effortless and natural, akin to texting a friend, rather than requiring users to search through endless product lists or rely on unreliable photo recognition <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
2.  **Contextualized User Guidance**
    Once tracking is easy, the system builds robust context around the user, including their flavor preferences, interests, habits, and hobbies. This rich context allows Alma to guide users effectively towards their personal nutrition goals <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. This involves deep [[customization_and_personalization_in_speech_ai | customization and personalization]].
3.  **Personalized Recommendations**
    The ultimate goal, planned for the second half of the year, is to connect users with specific products, restaurants, and meals that align with their objectives, facilitating goal achievement <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

### The Alma Score

Through [[user_feedback_and_ai_development | user feedback]], Alma discovered that users desire more than just calorie and macronutrient data; they seek a holistic understanding of their food quality and overall well-being <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. Recognizing that 1,000 calories can vastly differ in nutritional quality <a class="yt=" data-t="00:02:24">[00:02:24]</a>, Alma developed the "Alma score" concept in collaboration with academic adviser Dr. Eric Prim of Harvard University <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. The Alma score is a simple metric out of 100 designed to guide users towards foods scientifically proven to be beneficial for health, while gently nudging them away from less healthy options <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

## Key Lessons in Building AI for Nutrition

Building Alma provided several crucial lessons, particularly concerning [[building_user_experiences_with_ai | building user experiences with AI]]:

### Prioritizing User Feedback

While evaluations are considered, nothing surpasses real-time, in-the-moment [[user_feedback_and_ai_development | user feedback]] for guiding AI development <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. Alma implemented a feature asking "How did Alma do?" after every interaction, which was instrumental in measuring accuracy and improvement <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

### Constraining Large Language Models (LLMs)

Open-ended, large tasks given to LLMs result in extremely high error rates <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. It is vital to constrain LLMs to very specific tasks <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. Alma addresses this by breaking down the information relay process into distinct steps. For example, when a user logs a banana, the system first recognizes and extracts "banana," then sends it to the client app, which then processes it through various steps, including matching with a USDA database for caloric content <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. This multi-step process makes the user experience feel much faster and more interactive <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

### The Power of Streaks

Even seemingly minor features like "streaks" proved highly valued by users. A bug that broke user streaks caused significant outrage within the user community, highlighting the importance of such engagement features <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.

### Building Continuous Context for Personal AI Agents

For [[personal_private_ai_agents | personal AI agents]], continuously building context is critical. Users become frustrated if they repeatedly have to reiterate information <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. Alma addresses this by automatically adding novel pieces of information from user interactions to a personalized knowledge dataset <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>. Users can view, delete, or add to this information, ensuring Alma becomes smarter with every interaction <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.

### Proactive Insights

AI agents shouldn't solely rely on users initiating interactions. Proactive engagement, such as Alma detecting insights about a user's eating habits and surfacing unknown facts (e.g., pairing blueberries with dark chocolate enhances vitamin C absorption), enhances the learning experience <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.

### Embracing Multimodality

Instead of focusing on a single "winning" modality (e.g., voice), Alma discovered that users value the flexibility of [[multimodal_interaction_with_nutrition_apps | multimodal interaction]] <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. Users appreciate the ability to track food via voice, photo, or text, depending on their current context, making the experience seamless and convenient <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.

## Future Direction for AI in Personalized Nutrition

Alma's future strategy is based on three key learnings for the evolving AI space:

1.  **Brand and Design are Paramount**
    As code becomes a commodity, a strong brand and a user-centric, visually appealing design are crucial for a product to stand out <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>. This aligns with principles of [[effective_design_of_ai_in_products | effective design of AI in products]].
2.  **Trust and Partnerships**
    For new products, earning user trust involves identifying and partnering with entities users already trust, especially if there's an aligned mission <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>. Alma actively seeks to understand where users get their information and who they trust to foster beneficial partnerships <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>. This is a crucial element of [[customer_success_with_ai_solutions | customer success with AI solutions]].
3.  **Community and Net New Data**
    As communities grow, there's a natural curiosity about how others eat. Alma is focusing on features that allow users to learn from each other's habits <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>. Furthermore, with larger LLM companies "hoovering up" online data, it's essential for smaller players to leverage their users and members to create truly valuable and interesting "net new data" <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.