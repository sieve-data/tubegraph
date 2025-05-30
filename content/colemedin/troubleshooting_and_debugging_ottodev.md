---
title: Troubleshooting and debugging oTToDev
videoId: 5I9VgwauuzU
---

From: [[colemedin]] <br/> 

Debugging [[ottodev_open_source_ai_coding_assistant | autod Dev]] can involve a range of issues, including problems with API keys or the preview not showing <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>. Understanding where to find helpful error messages is crucial for self-troubleshooting or getting better support from the community <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.

## Identifying Error Messages

A common, unhelpful error message displayed in the UI is "There was an error processing your request" <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>. More specific and helpful error messages can be found elsewhere <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.

### Backend Errors (500 Internal Server Error)
If you encounter an internal server error (a 500 error), the detailed output will appear in the terminal where you initially started [[ottodev_open_source_ai_coding_assistant | autod Dev]] <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>. This output provides much more useful information than the generic UI message <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.

### Frontend Errors (400 Errors)
For issues occurring on the frontend (like 400 errors), you should check your browser's developer tools <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.
1.  Right-click anywhere on the page and select "Inspect" <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>.
2.  Navigate to the "Console" tab within the developer tools <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.
This console will display error messages related to frontend problems <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.

### Bolt Terminal Output
The [[New features in oTToDev | Bolt terminal]] provides real-time output of the commands the large language model (LLM) is running <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. This is a significant addition as it allows you to see if a command failed, which previously would have made [[ottodev_open_source_ai_coding_assistant | autod Dev]] appear broken, rather than indicating a bad command from the LLM <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. You can also see output from the [[New features in oTToDev | Bolt terminal]] in your main terminal, including indications of backend (500) or frontend (400) errors <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>.

## Common Troubleshooting Scenarios

### Blank Preview
A blank preview often indicates that the LLM has "hallucinated" something in the code, file structure, or commands, rather than an issue with [[ottodev_open_source_ai_coding_assistant | autod Dev]] itself <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>. This can be resolved by using a larger, more capable model <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.

### Missing API Key Header
If you encounter an "x API key header missing" error, restarting your container or site will typically fix the issue <a class="yt-timestamp" data-t="00:13:25">[00:13:25]</a>.

### Poor Results
If "everything works but the results are bad" <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>, this often means you are using a smaller large language model that is prone to making mistakes <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>. While smaller local LLMs can be useful for testing or quick interactions, using a larger model is recommended for building substantial applications to achieve better results <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>.

## Community Support

For further assistance, you can share error messages in the "automator Think Tank" community or in the YouTube comments <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>. A pinned comment in the issues and troubleshooting category within the community provides further guidance <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.