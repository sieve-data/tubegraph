---
title: Planning and preparing before coding with Cursor AI
videoId: gqUQbjsYZLQ
---

From: [[gregisenberg]] <br/> 

When embarking on development with AI tools like [[building_ai_apps_with_cursor | Cursor]], it's crucial to adopt a structured approach rather than immediately diving into coding [00:02:29]. This preparation can save countless hours and lead to more effective results [00:00:39].

## The Importance of Planning

Taking an idea and transforming it into functional code quickly is one of the amazing capabilities of AI tools like [[building_ai_apps_with_cursor | Cursor]] [00:00:05]. However, achieving the best results requires understanding and applying [[cursor_ai_best_practices | best practices]] [00:00:16], which fundamentally begin with thorough planning [00:02:29]. Even if you're not a seasoned developer, adopting a "developer mindset" by planning your project is essential [00:02:40].

Planning ensures you provide the AI model with as much context as possible [00:03:01]. Remember, you are the "boss," and the AI is merely a "co-pilot" [00:03:09]. This strategic approach is often referred to as the "measure twice, cut once" strategy [00:03:28].

## Practical Planning Steps

### Sketching and Wireframing

Before writing any code, visualize what you intend to build [00:02:48]. This can be done through:
*   **Sketches**: Use tools like Figma, Paint, or even simple pen and paper to draw out your ideas [00:02:50]. An example shared was a hand-drawn sketch on an iPad for a web3 client's portfolio page, which was then uploaded to ChatGPT for structural planning even before [[building_ai_apps_with_cursor | Cursor]] existed [00:04:11].
*   **V0**: If you're not using tools like Figma, consider starting with V0 [00:05:53]. V0 is excellent for visualizing your potential app or Minimum Viable Product (MVP) [00:06:04] and is built on Shadcn UI, allowing for aesthetically pleasing designs [00:07:48]. You can even drag and drop your hand-drawn wireframes into V0 to start [00:08:35]. Spend ample time in V0, using at least 10-15 prompts, to refine your vision as much as possible [00:10:31]. Once you have a clear visualization from V0, you can then transfer that code to [[building_ai_apps_with_cursor | Cursor]] or Claude for further development [00:07:30]. The initial step to effectively use [[building_ai_apps_with_cursor | Cursor]] is to *not* immediately go to [[building_ai_apps_with_cursor | Cursor]] [00:10:46].

This process of explaining your thoughts, similar to "rubber ducking" in programming, can lead to important realizations before you start coding [00:05:32].

### Utilizing Cursor.directory for Initial Setup

A critical step for anyone using [[building_ai_apps_with_cursor | Cursor]], especially beginners, is to leverage `cursor.directory` [00:11:14]. This website provides pre-written prompts tailored for specific technologies (e.g., Next.js, Python, React) [00:11:42].

**How to Use `cursor.directory`**:
1.  **Find Relevant Prompts**: Search for the technologies you are using (e.g., Next.js) [00:11:42].
2.  **Copy the Prompt**: Select the prompt that best aligns with your project [00:11:55]. These prompts usually define the AI's role and best practices for the chosen technology (e.g., "You are an expert in TypeScript, Node.js, Next.js, etc.") [00:11:59]. This helps [[building_ai_apps_with_cursor | Cursor]] avoid outdated information [00:12:14].
3.  **Create `.cursor_rules` File**: In the root directory of your project, create a new file named `.cursor_rules` [00:12:39].
4.  **Paste and Save**: Paste the copied prompt into the `.cursor_rules` file and save it [00:13:37].

Now, every time you interact with [[building_ai_apps_with_cursor | Cursor]] through the composer or side AI chat, it will be aware of your codebase's foundation based on this `.cursor_rules` file, leading to significantly better results [00:13:50]. If your specific technology isn't listed, you can copy existing prompts and ask other AI models like Claude or ChatGPT to adapt them for your technologies [00:14:37].

## Leveraging Other AI Models

Even when using [[building_ai_apps_with_cursor | Cursor]], there will be instances where it gets stuck on a bug [00:26:16]. In such cases, it's beneficial to consult other AI models like Claude, V0, or even ChatGPT [00:27:08].

**Debugging Strategy**:
*   **Provide Context**: When moving a bug to another AI, don't just copy-paste the error. Include the solutions that [[building_ai_apps_with_cursor | Cursor]] attempted but failed, along with the output you're getting versus what you expect [00:27:48]. This additional context significantly improves the chances of a successful resolution [00:27:37].

## General Best Practices and Learning

### Explaining and Teaching Code

AI models are excellent at explaining existing code and teaching programming concepts [00:29:26].
*   **Documentation**: They can automatically generate documentation for your code, saving developers time [00:29:30].
*   **Learning**: As a non-developer or beginner, you can use [[building_ai_apps_with_cursor | Cursor]] to understand specific code snippets or concepts. For example, by selecting a code component and asking, "Explain this code to me like a beginner. I want to know the flow logic and overall how things work" [00:30:31]. If a term is unclear (e.g., `use client` directive), you can ask the AI to explain it further [00:31:16]. This iterative process fosters learning and helps you understand common programming patterns [00:32:04].

### Tagging Documentation (Docs)

Keeping your AI models informed with the latest and most accurate information is crucial, as their training data might be outdated [00:21:03].
*   **Add Docs to Cursor**: Within [[building_ai_apps_with_cursor | Cursor]]'s composer view, you can add documentation links (`add doc`) [00:20:31]. For instance, you can paste the URL for Next.js documentation (`nextjs.org/docs`) and name it "Next.js Docs" [00:20:44].
*   **Benefits**: This gives [[building_ai_apps_with_cursor | Cursor]] access to the most up-to-date "source of truth" for the technologies you're using [00:21:13]. When you encounter issues, tagging these docs enables [[building_ai_apps_with_cursor | Cursor]] to debug with current information, simplifying the process [00:23:10]. For beginners, reviewing these linked documents can help them understand the language and ecosystem of different frameworks like Superbase or Next.js [00:23:55].

### Duplicating and Reusing Functionality

When building, if you have existing functionality on one page that you want to replicate with a slight modification on another, leverage the AI by referencing the existing code [00:35:50]. Provide the AI with the working code and explain the desired changes [00:35:55]. The more context you provide, the better the AI's output will be [00:36:05].

### Using Starter Templates

For serious development, consider starting with a pre-built template or starter kit [00:36:56]. Many repetitive functionalities like landing pages, payment integrations (e.g., Stripe), database setup, and authentication (e.g., Google Auth, 2FA) are often needed [00:37:20].
*   **Benefits**: Instead of building these from scratch each time, a template provides a boiler-plate foundation [00:37:42]. This saves significant time, especially since complex aspects like authentication and database setup can be challenging [00:38:36].
*   **Finding Templates**: You can find free templates on platforms like GitHub (e.g., "Next.js starter template" or "React starter template") [00:38:13]. Download the code and use it as your starting point in [[building_ai_apps_with_cursor | Cursor]] [00:38:24].

By embracing these planning and preparation strategies, users can overcome common challenges and build more robust applications with AI tools like [[building_ai_apps_with_cursor | Cursor]] [00:18:28].