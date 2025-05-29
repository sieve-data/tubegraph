---
title: Challenges and solutions for adopting causal ML in different fields
videoId: _mJclm_aJlc
---

From: [[causalpython]] <br/> 

Causal machine learning (ML) holds significant promise for making a distinctive impact in practical applications, particularly in fields like medicine, marketing, and business decision-making <a class="yt-timestamp" data-t="01:45:10">[01:45:10]</a>. While the academic community has developed powerful methods and tools, the real challenge lies in translating these into actionable insights and tools that can be widely adopted by practitioners <a class="yt-timestamp" data-t="03:00:23">[03:00:23]</a>.

## The Importance of Real-World Impact

A primary driver for many researchers in causal ML is to make a profound impact on people's lives beyond theoretical statistical challenges <a class="yt-timestamp" data-t="01:42:57">[01:42:57]</a>. This includes improving treatment selection in medicine, optimizing business operations, and enhancing public sector resource allocation <a class="yt-timestamp" data-t="02:47:58">[02:47:58]</a>. The vision is to develop, implement, and evaluate new AI algorithms to improve decision-making <a class="yt-timestamp" data-t="02:29:56">[02:29:56]</a>.

## [[challenges_in_implementing_causal_analysis_in_practice|Challenges in Adopting Causal ML]]

Despite its potential, several significant [[challenges_in_implementing_causal_analysis_in_practice|challenges]] hinder the widespread adoption of causal ML in practice:

*   **Language Barrier and Communication Gap** <a class="yt-timestamp" data-t="03:29:39">[03:29:39]</a>: Expecting domain experts, such as medical professionals or managers, to understand complex statistical and mathematical concepts behind causal ML is unrealistic <a class="yt-timestamp" data-t="05:51:30">[05:51:30]</a>. They have full schedules and different training backgrounds <a class="yt-timestamp" data-t="02:29:39">[02:29:39]</a>. The community often speaks a "hermetic" language <a class="yt-timestamp" data-t="06:42:07">[06:42:07]</a>.
*   **Complexity of Methods** <a class="yt-timestamp" data-t="05:05:07">[05:05:07]</a>: Explaining complex causal machine learning methods (e.g., S-learner, T-learner, double robust learner) in an easily digestible manner is difficult, especially to those without a solid technical background <a class="yt-timestamp" data-t="05:05:07">[05:05:07]</a>.
*   **Data Scarcity** <a class="yt-timestamp" data-t="02:26:26">[02:26:26]</a>: Unlike large tech companies, many small to medium enterprises (SMEs) do not have billions of customers or large datasets, making it challenging to apply data-hungry neural networks <a class="yt-timestamp" data-t="02:26:26">[02:26:26]</a>.
*   **Building Trust in AI Systems** <a class="yt-timestamp" data-t="02:28:23">[02:28:23]</a>: Users need to trust these systems, which was a significant hurdle in the early days of AI <a class="yt-timestamp" data-t="02:28:23">[02:28:23]</a>.
*   **Lack of Uncertainty Quantification** <a class="yt-timestamp" data-t="09:27:00">[09:27:00]</a>: Many machine learning methods for causal inference do not yet provide reliable uncertainty quantification, which is crucial for real-world decision-making, particularly in medicine where point estimates alone are insufficient for treatment recommendations <a class="yt-timestamp" data-t="09:27:00">[09:27:00]</a>.

## Strategies and Solutions for Adoption

To overcome these [[challenges_in_implementing_causal_analysis_in_practice|challenges]], a multi-faceted approach is required:

### 1. Bridging the Communication Gap
*   **Speak their language**: Instead of expecting medical professionals or business leaders to learn the technical language of causal ML, the community must translate its methods and language into terms understandable by practitioners <a class="yt-timestamp" data-t="03:07:07">[03:07:07]</a>.
*   **Go to them**: Researchers need to actively engage with domain experts and explain how causal ML can solve their specific problems and enhance their day-to-day business <a class="yt-timestamp" data-t="02:32:00">[02:32:00]</a>.
*   **Simple Analogies**: Use intuitive analogies to explain complex concepts. For example, explaining causal ML to managers as having "two crystal balls" (one for decision A, one for decision B) to see future outcomes allows them to pick the best decision, moving beyond mere correlation <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>.

### 2. Demonstrating Practical Value
*   **Augment, don't replace humans**: Causal ML tools should be positioned as decision support systems that empower users and augment their expertise, rather than replacing them <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>. This fosters trust and management buy-in <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>.
*   **Rigorous Field Experiments**: Conducting rigorous field experiments, like those at ABB Hitachi, is crucial to demonstrate the tangible impact of causal ML tools in real-world settings <a class="yt-timestamp" data-t="01:59:00">[01:59:00]</a>. For example, a tool reduced yield loss in semiconductor fabrication by almost 50% <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
*   **Focus on Actionable Insights**: The goal should be to provide insights that allow users to take actionable steps <a class="yt-timestamp" data-t="04:48:00">[04:48:00]</a>.

### 3. Model Development and Software
*   **Develop Reliable Uncertainty Quantification**: This is considered a "holy grail" for bringing causal ML into medical practice, as treatment recommendations require rigorous uncertainty intervals, not just point estimates <a class="yt-timestamp" data-t="09:36:00">[09:36:00]</a>.
*   **Move Beyond Standard Settings**: Develop methods that can handle non-stylized settings, such as time series data, drug combinations (multiple continuous treatments), and complex treatments, extending beyond binary treatments and outcomes <a class="yt-timestamp" data-t="08:06:00">[08:06:00]</a>.
*   **Prioritize Robust, Data-Sparse Models**: For environments with limited data (e.g., SMEs), simpler, robust models like generalized propensity scores with polynomial regression can outperform more complex approaches like neural networks <a class="yt-timestamp" data-t="02:26:26">[02:26:26]</a>.
*   **Develop More Software Packages**: There's a need for more comprehensive Python packages and software tools that address various parts of the causal inference pipeline, such as partial identification <a class="yt-timestamp" data-t="03:07:54">[03:07:54]</a>.

### 4. Education and Mindset
*   **Popularize Concepts**: Continue to popularize causal concepts using less "hermetic" language and create resources like books, speaker series, and summary papers <a class="yt-timestamp" data-t="06:36:00">[06:36:00]</a>.
*   **Provide Role Model Papers**: Offer papers that outline best practices and robustness checks for applying causal inference in specific domains, such as medicine <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>.
*   **Entrepreneurial Mindset in Research**: Researchers should embrace an entrepreneurial mindset, testing ideas early and being willing to abandon those that don't yield satisfying results quickly, rather than being overly attached <a class="yt-timestamp" data-t="02:48:48">[02:48:48]</a>.

## Examples of Successful Adoption

*   **ABB Hitachi**: Implemented a causal ML tool in semiconductor fabrication that reduced yield loss by almost 50% (49%) <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.
*   **Booking.com**: Runs causal machine learning algorithms at a large scale <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>.
*   **Health Insurance in the Middle East**: Collaborated to develop a two-stage causal ML model to identify patients who would most benefit from diabetes prevention programs, optimizing the allocation of limited resources <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>.
*   **Large Media Company**: Framed front-page newspaper optimization as a causal inference task, leading editors to realize that promoting their own curated articles drove long-term impact and revenue <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>.
*   **OECD (Organization for Economic Co-operation and Development)**: Causal ML was used to provide suggestions on how to allocate development aid, a complex problem involving hundreds of stakeholders and countries <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>.

## Cultivating a Collaborative Environment

A key element for consistent success in [[advances in causal machine learning research|causal machine learning research]] and adoption is building a great team <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>. This includes:
*   **Diversity of Backgrounds**: Teams benefit from individuals with diverse backgrounds (mathematics, data science, statistics, computer science, economics) who approach problems differently and bring unique strengths <a class="yt-timestamp" data-t="02:11:00">[02:11:00]</a>. For instance, an economics student once identified a randomization error in a medical experiment that computer scientists missed, while computer scientists are adept at running GPU clusters <a class="yt-timestamp" data-t="02:11:00">[02:11:00]</a>.
*   **Interdisciplinary Collaboration**: Combining expertise, such as fitting complex diffusion models with theoretical rigor and proofs, enhances the quality and applicability of research <a class="yt-timestamp" data-t="02:35:00">[02:35:00]</a>.
*   **Team Spirit**: Fostering an environment for open discussion, like joint lunches and using whiteboards, encourages the flow of ideas and collaboration <a class="yt-timestamp" data-t="02:15:00">[02:15:00]</a>.

By addressing these [[challenges_in_implementing_causal_analysis_in_practice|challenges]] through effective communication, demonstration of value, thoughtful model development, and a strong collaborative mindset, the [[integration_of_causal_thinking_in_machine_learning|integration of causal thinking in machine learning]] can continue to expand its [[impact_of_causal_machine_learning_beyond_academia|impact beyond academia]] and drive real-world outcomes.