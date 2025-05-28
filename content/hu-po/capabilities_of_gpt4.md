---
title: Capabilities of GPT4
videoId: 0s67_7zy_04
---

From: [[hu-po]] <br/> 

This article explores the capabilities of [[GPT4 ensemble of models | GPT4]] through direct comparisons with PDF summarizer tools, namely ChatPDF and PDFGPT. The evaluation highlights [[GPT4 ensemble of models | GPT4]]'s robust general knowledge and ability to process complex queries without prior exposure to specific documents.

## Initial Comparisons with PDF-Specific Tools

The initial tests involved comparing [[GPT4 ensemble of models | GPT4]] against PDFGPT and ChatPDF using a generic deep learning summary paper <a class="yt-timestamp" data-t="01:17:29">[01:17:29]</a>. The goal was to observe how the responses differed when the PDF-specific tools were given the document, versus [[GPT4 ensemble of models | GPT4]] relying on its generalist knowledge <a class="yt-timestamp" data-t="01:37:08">[01:37:08]</a>.

### Defining Deep Learning
When asked "what is deep learning in two sentences?", [[GPT4 ensemble of models | GPT4]] provided a succinct and correct definition <a class="yt-timestamp" data-t="04:21:00">[04:21:00]</a>. ChatPDF's answer was very similar to [[GPT4 ensemble of models | GPT4]]'s <a class="yt-timestamp" data-t="05:06:00">[05:06:00]</a>, while PDFGPT gave a more paper-specific answer, including a reference to page 33 <a class="yt-timestamp" data-t="06:41:00">[06:41:00]</a>.

### Types of Supervised Learning
For the query "what are the different types of supervised learning?", [[GPT4 ensemble of models | GPT4]] provided the best answer, distinguishing between regression and classification <a class="yt-timestamp" data-t="08:56:00">[08:56:00]</a>. PDFGPT attempted to draw from the paper, listing supervised, semi-supervised, and unsupervised learning, and mentioning deep reinforcement learning <a class="yt-timestamp" data-t="09:32:00">[09:32:00]</a>. ChatPDF gave a less accurate answer, listing model architectures instead of learning paradigms <a class="yt-timestamp" data-t="10:40:00">[10:40:00]</a>.

### Key Difference: Traditional ML vs. Deep Learning
When asked "what is a key difference between traditional ML and DL?", [[GPT4 ensemble of models | GPT4]] accurately described the role of feature engineering in traditional ML versus automatic feature learning in deep learning <a class="yt-timestamp" data-t="14:04:00">[14:04:00]</a>. Both PDFGPT and ChatPDF were also able to find and reiterate this specific point from the paper, suggesting they performed a similarity search <a class="yt-timestamp" data-t="15:36:00">[15:36:00]</a>, <a class="yt-timestamp" data-t="16:44:00">[16:44:00]</a>.

### Optimization Methods
For "what are different optimization methods for DL?", [[GPT4 ensemble of models | GPT4]] provided the most comprehensive list of methods, including SGD, momentum, AdaGrad, RMSProp, Adam, Adamax, and Adam AMSGrad <a class="yt-timestamp" data-t="46:36:00">[46:36:00]</a>. ChatPDF listed the five methods mentioned in the paper in the exact order <a class="yt-timestamp" data-t="43:52:00">[43:52:00]</a>. PDFGPT, however, gave a more generic response, failing to list the specific optimization methods from the paper <a class="yt-timestamp" data-t="44:11:00">[44:11:11]</a>. This suggested that ChatPDF might have a higher threshold for similarity lookup compared to PDFGPT <a class="yt-timestamp" data-t="44:53:00">[44:53:00]</a>.

## Handling Obscure Information and Hallucinations

To further test [[GPT4 ensemble of models | GPT4]]'s capabilities, questions about more obscure or specific details from the papers were posed.

### Fukushima and CNNs
When asked "when did Fukushima first describe the CNN?", the paper suggested 1988 <a class="yt-timestamp" data-t="19:55:00">[19:55:00]</a>. ChatPDF correctly retrieved 1988 from the PDF <a class="yt-timestamp" data-t="21:50:00">[21:50:00]</a>, while PDFGPT failed to find the information, possibly because the term "CNN" was not in the same sentence as the date in the paper <a class="yt-timestamp" data-t="21:12:00">[21:12:00]</a>. Crucially, [[GPT4 ensemble of models | GPT4]] responded with 1979-1980 <a class="yt-timestamp" data-t="20:46:00">[20:46:00]</a>. A quick internet search revealed that the paper "Neocognitron" describing a convolutional neural network was published in 1980 <a class="yt-timestamp" data-t="23:21:00">[23:21:00]</a>. This highlights [[GPT4 ensemble of models | GPT4]]'s extensive knowledge base, even correcting an inaccuracy in the provided PDF <a class="yt-timestamp" data-t="23:56:00">[23:56:00]</a>.

### AlexNet Innovations
When asked about "what new types of architecture design did AlexNet introduce?", [[GPT4 ensemble of models | GPT4]] correctly identified dropout and ReLU activation <a class="yt-timestamp" data-t="27:00:00">[27:00:00]</a>. PDFGPT also correctly identified Local Response Normalization (LRN) and dropout <a class="yt-timestamp" data-t="27:15:00">[27:15:00]</a>. ChatPDF identified ReLU and dropout but missed LRN <a class="yt-timestamp" data-t="27:45:00">[27:45:00]</a>.

### Parametric ReLU (PReLU) Proposer
For the highly specific query "who proposed the parametric ReLU and when?", [[GPT4 ensemble of models | GPT4]] provided the full names of the proposers (Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun) and the correct publication year (2015), even including the paper title <a class="yt-timestamp" data-t="38:50:00">[38:50:00]</a>. Both PDFGPT and ChatPDF correctly extracted "Kim et al. in 2015" from the paper, but did not provide the full list of authors <a class="yt-timestamp" data-t="39:31:00">[39:31:00]</a>, <a class="yt-timestamp" data-t="40:59:00">[40:59:00]</a>. This demonstrated [[GPT4 ensemble of models | GPT4]]'s ability to provide more detailed and accurate information beyond what was explicitly stated in the document.

### Stanford Question Answering Dataset (SQuAD) Link
In a test of very niche information, asking for "a link to the Stanford Question Answering dataset (SQuAD)" from the deep learning paper, both PDFGPT and ChatPDF successfully provided the exact link found in the paper <a class="yt-timestamp" data-t="53:02:00">[53:02:00]</a>, <a class="yt-timestamp" data-t="53:15:00">[53:15:00]</a>. Remarkably, [[GPT4 ensemble of models | GPT4]] also knew the precise link, despite not being fed the document <a class="yt-timestamp" data-t="53:31:00">[53:31:00]</a>.

### Obscure Archeological Field Notes
Using a second, "extremely obscure" computational archeology paper <a class="yt-timestamp" data-t="56:54:00">[56:54:00]</a>, a question was posed: "who and when were the original field notes for Tiwanaku in Bolivia recorded for the ashlars?". ChatPDF correctly identified JP Protein (mid-1990s), Leonce Agron (1848), and Max Uhle (1893) <a class="yt-timestamp" data-t="59:23:00">[59:23:00]</a>. PDFGPT, unfortunately, "died" during this test <a class="yt-timestamp" data-t="59:58:00">[59:58:00]</a>. [[GPT4 ensemble of models | GPT4]] came "disgustingly close," identifying Max Uhle and his date (1895 vs. 1893 in paper) and other researchers not in the paper, but missing the other two names mentioned in the paper <a class="yt-timestamp" data-t="01:01:03">[01:01:03]</a>.

### Z-Corp Z310 Rapid Prototyping Printer
When asked "what is a z-corp z310?", both ChatPDF and PDFGPT provided descriptions based directly from the paper <a class="yt-timestamp" data-t="01:03:21">[01:03:21]</a>, <a class="yt-timestamp" data-t="01:04:00">[01:04:00]</a>. However, [[GPT4 ensemble of models | GPT4]] again demonstrated superior general knowledge, identifying the printer, its manufacturer (Z Corp, acquired by 3D Systems in 2012), and its powder-based technology <a class="yt-timestamp" data-t="01:05:07">[01:05:07]</a>.

### University Housing Specific Facilities
For the query "what university houses the School of Art and Architecture as well as the Young Research Library?", ChatPDF stated it did not contain the information, but then revealed it performed an internet search to find the answer (UCLA) <a class="yt-timestamp" data-t="01:11:04">[01:11:04]</a>. PDFGPT successfully found the information within the PDF <a class="yt-timestamp" data-t="01:12:12">[01:12:12]</a>. As expected, [[GPT4 ensemble of models | GPT4]] also knew the answer directly, reinforcing its vast knowledge base <a class="yt-timestamp" data-t="01:13:37">[01:13:37]</a>.

## Implications for Information Consumption

The consistent performance of [[GPT4 ensemble of models | GPT4]] across diverse and obscure queries raises significant questions about the future of information consumption and knowledge acquisition <a class="yt-timestamp" data-t="01:14:16">[01:14:16]</a>. As [[GPT4 ensemble of models | GPT4]] and future iterations (GPT5, GPT6, GPT7, GPT8) continue to advance, the necessity of humans directly reading papers or books might diminish <a class="yt-timestamp" data-t="01:14:48">[01:14:48]</a>. This could lead to:

*   **Replacement of Traditional Reading**: Asking [[GPT4 ensemble of models | GPT4]] questions about books or papers might replace the act of reading them directly <a class="yt-timestamp" data-t="01:15:04">[01:15:04]</a>.
*   **Changes in Document Format**: If AI becomes the primary consumer of academic papers, their format might evolve to be more consumable by Large Language Models (LLMs) rather than humans <a class="yt-timestamp" data-t="01:15:42">[01:15:42]</a>.
*   **API Design Shifts**: Similar to document formats, [[exploring_functionality_and_limitations_of_aidriven_coding_tools | API design]] might prioritize ease of use for LLMs over human readability <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a>.

This shift signifies that generalist AI, like [[GPT4 ensemble of models | GPT4]], is increasingly outperforming task-specific AI <a class="yt-timestamp" data-t="01:08:02">[01:08:02]</a>.

## Conclusion

Based on the comparisons, [[GPT4 ensemble of models | GPT4]] consistently demonstrated superior capabilities compared to the PDF-specific tools [[Comparisons with proprietary models like ChatGPT and Bard | ChatPDF and PDFGPT]] <a class="yt-timestamp" data-t="01:17:02">[01:17:02]</a>.

*   **[[Comparisons with proprietary models like ChatGPT and Bard | ChatPDF]]**: Did not error out, provided more succinct answers, and sometimes performed internet searches to answer questions beyond the PDF's scope <a class="yt-timestamp" data-t="01:17:16">[01:17:16]</a>.
*   **[[Comparisons with proprietary models like ChatGPT and Bard | PDFGPT]]**: Featured a better user interface (showing the PDF alongside the chat) and clickable references <a class="yt-timestamp" data-t="01:17:30">[01:17:30]</a>. However, it was sometimes verbose and prone to "airing out" or crashing <a class="yt-timestamp" data-t="01:17:42">[01:17:42]</a>.

Ultimately, for most queries, [[GPT4 ensemble of models | GPT4]] proved to be the most reliable and knowledgeable tool, often providing correct and comprehensive answers without needing the specific PDF in question <a class="yt-timestamp" data-t="01:18:03">[01:18:03]</a>.