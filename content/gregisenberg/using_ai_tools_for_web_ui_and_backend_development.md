---
title: Using AI tools for web UI and backend development
videoId: sCFS_U7d9Do
---

From: [[gregisenberg]] <br/> 

VZ is an AI assistant specifically designed for web development, aimed at helping users create high-quality web products quickly [01:08:11]. It focuses on working with JavaScript, HTML, CSS, and various new frameworks and libraries [01:29:07]. The goal is to streamline the process of getting high-quality code and ultimately, high-quality products [01:37:37].

## [[design_and_user_interface_considerations_for_ai_applications | VZ for Web UI Development]]

VZ excels at generating user interfaces. It can be used for both creating great UIs and performing backend work by adding interactivity [03:02:40].

### Tips for Maximizing UI Output

*   **Start with Screenshots**: Providing screenshots is highly effective, especially if you have a specific vision for the UI, similar to iterating on a music player design [03:11:00].
*   **Creative Modes**:
    *   **Opinionated**: If you have a clear idea, steer VZ with specific requests [03:33:00].
    *   **Exploratory**: If unsure, let the AI generate initial designs and iterate from there. For example, a simple request to "build a page where I can post a link...and it'll send it to Slack" resulted in a ready-to-use component in one shot [03:40:00].
*   **Iterative Prompting**: Refine designs through multiple prompts. For a music player UI, prompts included:
    *   "Make it have warmer Grays, use a Sanda font from Google fonts with next font" [04:56:00].
    *   "Make the UI have a tighter information density" [05:12:00].
    *   "The time playing bar should be longer, the search input should have an actual input in it, add more realistic fake data for the songs" [05:18:00].
    *   "Less vertical spacing between the rows, each row should have the album art to the left of it" [05:44:00].
*   **Leverage Tailwind CSS Knowledge**: VZ "thinks in Tailwind" [06:03:00]. Explicitly stating Tailwind classes (e.g., "make it size four") can directly guide VZ to specific visual outcomes [06:09:00].
*   **Incorporate Imagery and Typography**: Once images are added, web design significantly improves. Typography and imagery are crucial for a polished look [07:48:00].
*   **Use Natural Language**: Communicate with VZ as you would with a human designer, e.g., "make the playing track a little less wide" [08:04:00].
*   **Apply [[basics_of_web_technologies_and_their_importance_in_ai_tools | Foundational Web Design Knowledge]]**: If you have pre-existing web design or CSS knowledge, you can guide VZ more effectively (e.g., asking for "tabular nums" for number alignment) [08:25:00].
*   **Ensure Responsiveness**: Requesting VZ to "make the table mobile responsive" can quickly adapt designs for different screen sizes [08:47:00].
*   **Fork and Customize**: Designs can be "forked" and further refined, such as adjusting color schemes (e.g., experimenting with darker Grays) [09:34:00].

### [[importance_of_foundational_web_design_knowledge_when_using_ai_tools | Learning Web Design with VZ]]

While pre-existing knowledge helps, it's not a requirement to use VZ effectively [10:59:00]. AI assistants can help users discover the right questions to ask [11:15:00].

*   **Ask for Design Advice**: You can prompt VZ for guidance on improving designs, such as "I'm a novice at web design... what can I try to make things look a little better? Any common practices or patterns?" [11:42:00].
*   **Key Design Principles Suggested by VZ**:
    *   Consistent color scheme (2-3 main colors) [12:13:00].
    *   White space, padding, and margins to allow elements "room to breathe" [12:29:00].
    *   Readable fonts (sans-serif for better readability) [12:33:00].
    *   Consistent, aligned, and organized layout [12:48:00].
    *   Responsiveness [12:51:00].
    *   High-quality images [13:02:00].
*   **Utilize Design Inspiration Sites**: Websites like Godly.website and Patterns offer design inspiration that can be used as starting points or referenced in VZ prompts [14:17:00].
*   **Shad CN UI Foundation**: VZ is built on Shad CN UI, a system for building component libraries. This means the code VZ generates is real, production-ready React components that can be customized for unique branding [16:11:00]. VZ understands this language, allowing specific component requests like a "date picker" [17:09:00].

## [[using_ai_tools_for_saas_development | VZ for Backend Development]]

VZ goes beyond just UI and can assist with backend development, crucial for [[harnessing_ai_tools_for_modern_business_development | modern business development]] [03:02:40].

*   **Implementing Logic**: After designing the UI, VZ can help implement backend logic. For instance, transforming a settings page UI into a functional admin portal with CRUD (Create, Read, Update, Delete) actions [19:39:00].
*   **API Integration**: VZ can swap mock data with real API calls by taking an external API as input [20:50:00].
*   **Database Schema and ORM**: You can provide VZ with your database schema (e.g., PostgreSQL) and ask it to generate ORM (Object-Relational Mapping) code (e.g., for Drizzle or Prisma in JavaScript/TypeScript) [21:08:00]. It can even help design backend structures for speed, like suggesting the use of indexes on databases for faster queries [21:16:00].
*   **Underrated Capability**: The ability to build out the backend after UI design is often overlooked but crucial for developing full applications [22:01:00].

## General Outlook on AI Tools for Development

AI tools are transformative for the development ecosystem, augmenting rather than replacing human work [26:44:00]. They act as a "knowledgeable super senior engineer" guiding developers with best practices and helping solve issues [27:28:00]. This empowerment means that developers can now build virtually anything they can imagine, whether it's an iOS app using Swift or an Android app using Kotlin [27:45:00]. It's encouraged to try these tools to rethink one's relationship with application building [27:05:00].

VZ can be tried at vz.dev, which offers a free tier [28:27:00].