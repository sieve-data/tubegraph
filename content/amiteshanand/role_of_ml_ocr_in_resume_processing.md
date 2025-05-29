---
title: Role of ML OCR in resume processing
videoId: ji_hECcyTjs
---

From: [[amiteshanand]] <br/> 

ML OCR (Mistral OCR) plays a crucial role in the described job finder application by efficiently processing resumes <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. It is an LLM-based model designed to read documents and images with high efficiency <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>, <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

## Key Capabilities and Performance

ML OCR performs better than other competitive OCR models and frameworks, showcasing an overall benchmark score of 94.89 <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>, <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. Its multilingual capability is particularly strong, with a score of 99.0 <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>, making it a highly effective tool for text extraction <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

## Integration in the Job Finder App

In the context of the job finder application built with [[using_agent_development_kit_to_create_a_job_finder_app | Google Agent Development Kit]], ML OCR is specifically used to read and analyze uploaded resumes <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>, <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

### OCR Tool Definition

Within the agent workflow, ML OCR is defined as an "OCR tool" <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>, utilizing its latest model <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. The process for resume processing involves:
1.  Uploading a PDF <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
2.  Obtaining a signed URL for the document <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
3.  Processing the OCR on the document <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.

### OCR Agent

An "OCR agent" is the first sub-agent in the sequential agent workflow <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>, <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. Its primary instruction is to "extract text from a given PDF file path" using the ML OCR tool, returning only the plain text content without any explanations or commentary <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>, <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>. The response is prefixed with "OCR" for easy identification <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

After processing a resume, the OCR agent successfully extracts information such as technical skills, education, skill sets, projects, and achievements from the uploaded PDF <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>. This extracted text, referred to as "OCR output," then serves as input for subsequent agents in the workflow, such as the query preparation agent <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.