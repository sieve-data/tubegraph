---
title: Building and deploying custom AI front ends
videoId: 2Ai7_5G70xY
---

From: [[colemedin]] <br/> 

[[integrating_ai_with_front_ends | Integrating AI with front ends]] is a crucial step in [[embedding_and_production_deployment_of_ai_agents | embedding and production deployment of AI agents]]. While AI agents can be run locally or accessed via API endpoints, creating a custom front end provides a user-friendly interface for interaction <a class="yt-timestamp" data-t="03:20">[03:20]</a>. This article details the process of [[creating_custom_frontends_for_ai_agents | creating custom front ends for AI agents]] and then [[deploying_ai_applications_to_the_cloud | deploying AI applications to the cloud]] for production use.

## The Need for Custom Front Ends
Although platforms like Agent Zero offer an instant front end for any locally running AI agent <a class="yt-timestamp" data-t="03:24">[03:24]</a>, there's a strong case for building custom interfaces. A custom front end allows for tailored user experiences and specific functionalities that might not be available in general-purpose platforms <a class="yt-timestamp" data-t="03:33">[03:33]</a>.

## Technologies Used
The custom front end discussed here was developed as part of a series focusing on [[building_productiongrade_ai_agents | building production-grade AI agents]] <a class="yt-timestamp" data-t="15:16">[15:16]</a>. It began with Lovable for initial development and was then improved using Bolt.DIY, leveraging Gemini for enhancements <a class="yt-timestamp" data-t="15:27">[15:27]</a>. The resulting application is built with Vite and React <a class="yt-timestamp" data-t="16:18">[16:18]</a>.

## Connecting the Front End to the AI Agent
For the front end to communicate with the deployed AI agent, it needs to know the agent's API endpoint. This is managed using environment variables within the front end's codebase <a class="yt-timestamp" data-t="15:37">[15:37]</a>. An AI IDE like Windsurf can assist in defining these variables <a class="yt-timestamp" data-t="15:42">[15:42]</a>.

Key environment variables for the front end include:
*   `VITE_API_URL`: Points to the AI agent's API endpoint hosted in the cloud <a class="yt-timestamp" data-t="16:03">[16:03]</a>.
*   `VITE_SUPERBASE_URL` and `SUPERBASE_PUBLIC_KEY`: For Superbase integration, if used <a class="yt-timestamp" data-t="17:41">[17:41]</a>.

These variables allow the front end to be configured differently, enabling it to connect to specific instances of AI agents, such as those customized for different clients or departments <a class="yt-timestamp" data-t="15:53">[15:53]</a>.

## Deploying the Custom Front End
The process of [[deploying_ai_applications_without_coding | Deploying AI applications without coding]] can be simplified with the right tools. For the front end, a platform like Render is suitable due to its ease of use and free tier <a class="yt-timestamp" data-t="10:01">[10:01]</a>.

### Steps for Deployment on Render:
1.  **Choose Service Type**: Since Vite generates static content, the front end is deployed as a "static site" on Render, unlike the AI agent backend which is a "web app" <a class="yt-timestamp" data-t="16:32">[16:32]</a>.
2.  **Connect to GitHub**: Link the Render service to the GitHub repository containing the front end code <a class="yt-timestamp" data-t="16:51">[16:51]</a>. Render can automatically recognize the project as Node.js <a class="yt-timestamp" data-t="17:01">[17:01]</a>.
3.  **Configure Build Commands**: Set the install command to `npm install` and the build command to `npm run build` <a class="yt-timestamp" data-t="17:05">[17:05]</a>. The publish directory is typically `dist` for Vite projects <a class="yt-timestamp" data-t="17:13">[17:13]</a>.
4.  **Set Environment Variables**: Input the required environment variables, such as `VITE_API_URL`, `VITE_SUPERBASE_URL`, and `SUPERBASE_PUBLIC_KEY` <a class="yt-timestamp" data-t="17:19">[17:19]</a>.
5.  **Deploy**: Initiate the deployment. Render will pull the code, run the build commands, and serve the static site <a class="yt-timestamp" data-t="18:04">[18:04]</a>. This process is typically very fast for React/Vite applications, often taking around 30 seconds <a class="yt-timestamp" data-t="18:08">[18:08]</a>.

### Testing the Deployment
Once deployed, the front end's URL can be accessed to verify functionality. By sending a test message, it can be confirmed that both the front end and the AI agent (backend) hosted on Render are working perfectly together <a class="yt-timestamp" data-t="18:25">[18:25]</a>.

This streamlined process allows for [[deploying and testing AI agents quickly | deploying and testing AI agents quickly]] with their custom front ends, making the entire solution available in the cloud within minutes <a class="yt-timestamp" data-t="18:47">[18:47]</a>.