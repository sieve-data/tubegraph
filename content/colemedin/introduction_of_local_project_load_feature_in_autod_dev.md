---
title: Introduction of local project load feature in Autod Dev
videoId: nkqQfABopyc
---

From: [[colemedin]] <br/> 

[[autod_dev | Autod Dev]], formerly known as Bolt.new, has introduced a highly requested feature allowing users to load existing local projects into the platform. This enables continuous work on projects directly within [[autod_dev | Autod Dev]] <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Key Feature: Local Project Loading

This feature allows users to import local project folders into [[autod_dev | Autod Dev]], making it a more mature project <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

### Implementation and Credit
The ability to load local projects was a highly requested community feature and is now available <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. Edward, one of [[autod_dev | Autod Dev]]'s core maintainers, is credited with implementing this functionality <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

### How to Import a Project
1.  **Select "Import Folder"**: From the [[ui_changes_and_new_features_in_autod_dev | Autod Dev UI]], click on the "Import Folder" option <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
2.  **Choose Project**: Select the local project folder you wish to upload <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. Projects previously built and exported from [[autod_dev | Autod Dev]], or those coded elsewhere, can be imported <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.
3.  **Upload**: Once selected, click "Upload" to load the files into the platform <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

### Functionality Post-Import
After importing, [[autod_dev | Autod Dev]] understands all the files, retaining the necessary context for further interaction <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. For example, users can ask it to "describe these files" and it will comprehend the project structure <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. The AI can then work with these files as if they were coded within the same conversation, allowing for extensions and improvements <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. Users may need to explicitly tell the AI to run installation and execution commands (e.g., `npm install`, `npm run dev`) for the project to run within the environment <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

### Limitations
While powerful, there are limitations:
*   **Project Size**: Users cannot load massive projects, as this may crash the site during file import <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. It's recommended to keep projects to less than 100 files <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
*   **Irrelevant Folders**: Avoid importing large, unnecessary folders like `node_modules`. Although [[autod_dev | Autod Dev]] has an ignore setup for such folders (e.g., GitHub, node modules), they still need to be processed on the frontend before filtering, which can be inefficient <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. Keeping imports "nimble" is key for optimal performance <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

## Related [[ui_changes_and_new_features_in_autod_dev | UI Changes and Features]]

Along with local project loading, several other [[ui_changes_and_new_features_in_autod_dev | UI changes]] and new features have been implemented:
*   **Chat Import/Export**: Users can now import existing chats and export them from the coding view <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
*   **Chat History Search**: The chat history now includes a search function <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
*   **Collapsible Model Settings**: Model settings can be collapsed to provide more UI space <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **Conversation Management**:
    *   **Revert to Message**: Allows users to revert code to earlier versions or specific messages in the conversation <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
    *   **Fork Chat**: Users can fork a chat from a specific message point <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   **Prompt Enhance Feature**: This feature has received enhancements <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.

## [[roadmap_and_development_progress_of_autod_dev | Roadmap]] Context

The local project load feature is a completed high-priority item on the [[roadmap_and_development_progress_of_autod_dev | Autod Dev roadmap]] <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>. Other related high-priority features currently in progress include:
*   **Loading GitHub Projects**: This feature will allow users to load Git repositories into [[autod_dev | Autod Dev]], similar to local projects <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
*   **Attaching Images to Prompts**: This feature is nearing completion and will enable users to upload images with their prompts, particularly useful for models that support image comprehension like Claude or GPT-4o <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.

This progress on high-priority features is crucial for [[autod_dev | Autod Dev]]'s continued development and vision <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

## Conclusion

The introduction of the local project load feature significantly enhances [[autod_dev | Autod Dev]]'s capabilities, moving it closer to becoming the best open-source AI coding assistant <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. The continuous contributions from the community, especially Edward's work on this and other features, are driving this progress <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.