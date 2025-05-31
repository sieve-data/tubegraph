---
title: Generative AI tools in Creative Cloud
videoId: lwtU_NfFH8o
---

From: [[redpointai]] <br/> 

Adobe's approach to [[ai_transformation_in_creative_workflows | AI transformation in creative workflows]] is deeply integrated across its product suite, with a particular focus on generative AI tools within Creative Cloud [00:00:17]. Alexandre Cen, Adobe's VP of Generative AI and Sensei, highlights how the company leverages its extensive user base and proprietary data to refine its AI models and redefine content creation [00:00:07].

## Adobe's AI Strategy and Product Integration
Adobe's AI capabilities span its three main business units: Creative Cloud, Document Cloud, and Experience Cloud [00:02:53]. AI is a core component of products within each unit [00:03:02].

### Creative Cloud
The Creative Cloud, which includes applications like Photoshop, Illustrator, and Adobe Express, utilizes AI extensively [00:03:02]. Models are trained on Adobe's internally developed Sensei platform [00:03:32]. Existing AI-powered features in Photoshop include:
*   Auto masking [00:03:52]
*   Content-aware fill [00:03:54]
*   Object detection [00:03:56]
*   Neural Filters [00:03:57]

### Document Cloud
In the Document Cloud, particularly Acrobat, AI powers features like "Liquid Mode," which reflows documents for easier reading on mobile phones [00:04:06]. This is particularly useful for quickly consuming academic papers or archives [00:04:15].

### Experience Cloud
The Experience Cloud incorporates AI for various functions, such as anomaly detection in analytics, and content generation for marketing and branding within Adobe Experience Manager (CMS) [00:04:29].

## The Firefly Suite: Embracing Large Models
Adobe decided to fully embrace large models, including diffusion models and Large Language Models (LLMs), observing the significant improvements in content generation and summarization quality [00:05:00]. This led to the creation of the Firefly Suite of models, launched in March [00:05:12].

Even in its beta phase, Firefly has seen tremendous success, with over a billion images generated across multiple platforms [00:05:24]. These include the Firefly website, deep integration into Photoshop (Generative Fill), and integration into Adobe Express [00:05:29]. Firefly is slated for integration across all Adobe products, including Illustrator [00:05:47].

## AI's Impact on Creative Workflows
Adobe views [[ai_transformation_in_creative_workflows | AI transformation in creative workflows]] as a continuation of historical technological disruptions that have made content creation cheaper and more accessible [00:07:25]. While concerns about job security for creators arise with each wave, the demand for content always increases exponentially, surpassing the decrease in creation costs [00:08:35].

Adobe believes that content will increasingly be "touched by AI" [00:09:12]. While it won't be fully automated, creators will remain in control of both the creation and curation processes [00:09:18]. By embracing AI, creative professionals can become 10x more productive and creative [00:09:03]. For instance, even simple selections in Photoshop already use AI (Gans or selection models), and features like Generative Fill directly create pixels during the editing process [00:09:44].

## User Experience and Design Decisions
Integrating AI into complex tools like Photoshop, which has decades of accumulated features, requires careful user experience design [00:10:49]. Adobe's design philosophy has evolved:

### Intent-Driven Editing
Initially, with features like Neural Filters and "Smart Portrait," Adobe introduced "intent-driven editing" using sliders to control AI-generated changes, such as making a person smile or age them [00:11:15]. This offered a more user-friendly paradigm compared to manual pixel manipulation [00:12:17].

### Prompt-Based Interfaces
Prompt-based user interfaces significantly lower the barrier to entry, allowing users to express their desired outcome in natural language [00:12:45]. However, Adobe's professional users expect more control than just a prompt [00:13:09].

### A Hybrid Approach
Adobe anticipates a mix of language, pointing, and sliders for the future of human-computer interaction in creativity [00:13:19]. The goal is to provide more control mechanisms to help users achieve their precise artistic vision [00:14:24].

### Tailored Experiences for Different Segments
Adobe customizes the AI experience for its diverse user base [00:17:36]:
*   **Consumers (firefly.adobe.com)**: Features an inspiration stream for remixing existing prompts, curated by the community [00:18:56]. Adobe also introduced an "Adobe Style Engine" that allows users to select styles, lighting conditions, and composition rules through curated options, simplifying the prompt [00:20:20]. Prompt auto-completion models will also be integrated [00:21:26].
*   **Communicators/Marketers (Adobe Express)**: Templates are the primary gateway, with generative capabilities baked directly into templates [00:21:50]. This allows for quick creation of social content [00:22:08].
*   **Creative Professionals (Photoshop)**: The "Generative Fill" feature is integrated into a contextual bar that appears near selections [00:22:30]. Users don't always need to type a prompt; the rest of the image can serve as an implied prompt to generate matching content [00:22:50]. This co-pilot experience aims to help users reach their desired destination sooner [00:16:24].
*   **Enterprises**: AI capabilities are introduced in context within tools like Adobe Experience Manager (AEM) [00:23:41]. This includes contextual recommendations for auto-generating text that respects brand voice and guidelines [00:23:57]. The focus is on enabling content velocity while maintaining brand compliance [00:25:10].

## Trust, Safety, and Training Data
[[adobes_integration_of_ai_in_content_creation | Adobe's integration of AI in content creation]] places a high bar on trust and safety, particularly regarding bias, harmful content, and intellectual property (IP) infringement [00:26:19].

### Differentiated Training Data Strategy
A key differentiator for Firefly is its training data source: Adobe Stock content [00:26:38]. This strategy aims to:
*   **Ensure high-quality content**: Training on Adobe Stock provides curated, professional assets [00:27:01].
*   **Establish proper consent**: Adobe has the right to train on data stored in its marketplace [00:27:06].
*   **Reduce IP infringement risk**: Unlike models trained on scraped internet data, Adobe Stock content reduces legal risks [00:27:10].
*   **Minimize harmful content**: Adobe Stock has a rigorous moderation process (both automated and manual) that prevents harmful content from being approved [00:27:23].

### Addressing Bias
While Adobe Stock reduces harmful content, inherent biases can exist in any dataset [00:28:07]. To combat this, Adobe implemented specific debiasing mechanisms:
*   **Internal Testing**: Extensive internal testing with tens of thousands of Adobe employees identified significant bias issues [00:28:29].
*   **Person Detector**: A model identifies person references in prompts, particularly job titles [00:29:21].
*   **Debiasing Distribution**: When a person is referenced, the model introduces a balanced distribution of skin tones, genders, and age groups based on the country of origin of the request [00:29:52]. This ensures a fair representation in generated content [00:30:18].
*   **Toxicity Detectors and Filters**: To ensure Firefly is safe for all ages and to avoid Not Safe For Work (NSFW) content, Adobe employs toxicity detector models, deny lists, block lists, and NSFW filters at the end of the generation process [00:31:05].
*   **Child-Specific Safeguards**: Systems detect prompts referencing children and implement negative prompting to prevent inappropriate content (e.g., children with tobacco) [00:31:24].

### Customer Feedback for Refinement
Adobe uses a robust feedback mechanism on firefly.adobe.com and within Photoshop [00:32:03]. This includes explicit signals (like/dislike, reports) and implicit signals (downloads, saves, shares) [00:34:18]. This feedback loop is crucial for future Firefly models to reinforce preferred generations and avoid disliked content [00:34:40].

## Organizational Structure for AI Development
Adobe employs a hybrid organizational structure for AI development, combining horizontal and vertical teams [00:33:33]:

### Horizontal Layer (Centralized AI)
*   **Adobe Research**: Over 200 researchers and 300 PhD interns work on [[advancements_in_ai_developer_tools | advancements in AI developer tools]] and models across various modalities (images, video, vector, 3D) [00:39:14]. They focus on publishing papers and bringing models closer to production [00:42:03].
*   **Sensei Team**: Provides a distributed training platform for large and small models in a multi-tenant environment [00:42:19]. This team also manages curated, high-quality datasets for training [00:42:29].
*   **Applied Science and Machine Learning Group**: This group refines pre-production models from research, handles final training (the "last 20%"), and prepares them for productization [00:39:38].
*   **Gen Services Team**: Creates efficient services to run these models, focusing on optimized inference [00:43:09]. This "AI Super Highway" provides APIs that product teams can call, ensuring fast response times (e.g., below 15 seconds for a 1K by 1K image) [00:43:50].

### Vertical Layer (Tech Transfer Teams)
Each major product line (Photoshop, Adobe Express, Illustrator) has "Tech transfer subgroups" [00:44:11]. These teams leverage the APIs created by the horizontal "Gen Services" team to build amazing user experiences tailored to their specific product workflows and customer segments [00:45:08]. They are the product experts who know best where to integrate AI for maximum impact [00:44:39].

## The Future of Creative Cloud with AI
Alexandre Cen believes that software companies will increasingly become [[the future of AI platforms in content creation | AI companies]], with AI replacing more of the traditional software stack [00:49:11]. The [[the future of AI in Adobes products | future of AI in Adobe's products]] will see continued innovation in model architectures, as Adobe does not "fall in love with a particular model" but constantly seeks improvements in quality and performance [00:49:32].

The [[future_of_generative_ai_in_media_and_creative_industries | future of generative AI in media and creative industries]] will enable "hyper personalization" [00:50:29]. This addresses the "content velocity" or "content supply chain" problem faced by enterprises, where individualized or segmented communication with customers is too expensive to manage manually [00:50:31]. Generative AI will allow for the creation of infinite, personalized content tailored to individual viewers or segments, enhancing communication between brands and their constituents [00:50:53].

Ultimately, Creative Cloud will evolve to empower visual designers to become "creative directors of these meta experiences" that are hyper-personalizable [00:51:25]. The human-computer interaction will become more fluid and accessible to a wider audience, with AI at its core, but perhaps not explicitly mentioned [00:51:51]. This vision foresees a Creative Suite that enables content creation with much higher creativity and velocity [00:52:14].