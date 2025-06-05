---
title: Simplified nutrition tracking
videoId: Ghc-qalQFLw
---

From: [[aidotengineer]] <br/> 

Alma's core belief is that eating well shouldn't be difficult, and good health stems from simple, personalized nutrition <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. Historically, understanding one's eating habits has been challenging despite numerous apps available <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. The problem identified is an imbalance: users are required to share extensive information but receive little meaningful feedback <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. Alma believes that [[AI in personalized nutrition | AI]] can solve this, creating a unique "nutrition companion" <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

## Alma's Vision for AI Nutrition

Alma's vision for an [[AI in personalized nutrition | AI]] nutrition companion rests on three core pillars <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>:

1.  **Simple Nutrition Tracking**
    *   The goal is to make nutrition tracking easy, natural, and feel like texting a friend <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. This avoids the laborious task of searching through endless product lists or relying on inaccurate photo recognition <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
2.  **Building User Context**
    *   Once tracking is easy, the information gathered is used to build a strong context around the user, including their flavor profile, interests, habits, and hobbies <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. This context helps steer them toward their stated goals <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
3.  **Connecting Users with Goals**
    *   In the second half of the year, Alma plans to use this information to connect users with specific products, restaurants, and meals that will help them achieve their nutritional goals <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

## Key Learnings in Building the AI Nutrition Companion

Alma gained several key insights during its beta phase and development:

*   **Importance of User Feedback**: Real-time, in-the-moment feedback from users is paramount <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. Alma implemented a "How did Alma do?" prompt after every interaction to gather this crucial data <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
*   **Constraining Large Language Models (LLMs)**: Giving LLMs open-ended, very large tasks results in high error rates <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. It's vital to constrain the LLM to very specific tasks <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. Alma addresses this by breaking down information processing into multiple steps, sending partial results to the user as they become available. For example, when a user tracks a banana, Alma first recognizes the food item, extracts it, sends it to the app, and then processes further details like caloric content from a USDA database in subsequent steps <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. This makes the experience feel faster and more interactive for users <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   **User Value for Features**: Even seemingly minor features, like "streaks," can be highly valued by users <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>. When a streak bug occurred, users actively voiced their concern, highlighting the importance of doubling down on features that users find engaging <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
*   **Building Continuous Context**: [[AI in personalized nutrition | AI]] agents benefit significantly from continuously building context about the user <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. Alma incorporates a "About You" knowledge data set that is updated with novel information from user interactions, making Alma smarter over time and reducing the need for users to reiterate information <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.
*   **Proactive Engagement**: Proactive outreach is crucial because users only open the app to ask questions so often <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. Alma detects insights about user eating habits and proactively surfaces unknown information, such as the increased vitamin C absorption when blueberries are paired with dark chocolate <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.
*   **Multimodality**: While some modalities (like voice) are personally preferred for their efficiency in tracking meals <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>, users appreciate the option to use voice, photo, or text depending on the context <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. Providing multiple modalities that make sense for users is essential <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.

## Future Focus Areas

Looking forward, Alma is doubling down on three key areas <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>:

*   **Brand and Design**: Code is becoming a commodity, and a user-centric product with visually appealing design is crucial for standing out <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.
*   **Trust and Partnerships**: Earning user trust, especially as a new entity, involves partnering with organizations and individuals that users already trust and who share an aligned mission <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>. Alma actively asks users who they trust for information and seeks partnerships <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
*   **Community and New Data**: As the community grows, there's interest in how others eat and learning from their habits <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>. Alma is focusing on features that leverage the community to create net new, valuable data, recognizing that major LLM companies are already "hoovering up" online data <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.

The development of the [[alma_score_for_food_quality_assessment | Alma score for food quality assessment]], a metric out of 100 developed with academic advisor Dr. Eric Prim, also emerged from user feedback indicating a desire to understand holistic eating quality beyond just calories and macros <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.