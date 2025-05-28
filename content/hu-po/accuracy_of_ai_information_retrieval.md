---
title: Accuracy of AI information retrieval
videoId: 0s67_7zy_04
---

From: [[hu-po]] <br/> 

This article explores the accuracy and utility of specialized PDF summarizer AI tools, specifically **PDFGPT.io** and **ChatPDF.com**, in comparison to a generalist AI model like **GPT-4**. The evaluation uses two distinct academic papers: a generic deep learning survey and an obscure computational archaeology paper.

## Initial Observations on Processing <a class="yt-timestamp" data-t="02:25:00">[02:25:00]</a>

Upon uploading, both PDFGPT.io and ChatPDF.com processed the documents very quickly, leading to a suspicion that they may not be scraping the entire PDF for text initially. It's suggested they might acknowledge the upload and then process the document in the background, or perform a [[Advancements in AI context length and retrieval | similarity search]] based on queries rather than reading the entire document upfront <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>, <a class="yt-timestamp" data-t="02:42:42">[02:42:42]</a>.

## User Interface and Feature Comparison

*   **PDFGPT.io**: Features a user interface that displays the PDF alongside the chat, allowing for direct visual reference <a class="yt-timestamp" data-t="03:03:00">[03:03:00]</a>. It also provides clickable references to specific page numbers in the PDF where information was sourced <a class="yt-timestamp" data-t="06:49:00">[06:49:00]</a>, <a class="yt-timestamp" data-t="17:51:00">[17:51:00]</a>.
*   **ChatPDF.com**: Does not display the PDF directly in the interface once uploaded, requiring separate viewing <a class="yt-timestamp" data-t="03:18:00">[03:18:00]</a>. References are embedded directly within the answer text <a class="yt-timestamp" data-t="18:01:00">[18:01:00]</a>.

## Comparative Performance on Information Retrieval

The evaluation involved asking specific questions derived from the content of the uploaded PDFs and comparing the answers from PDFGPT.io, ChatPDF.com, and GPT-4.

### Test 1: "What is deep learning?" <a class="yt-timestamp" data-t="03:39:00">[03:39:00]</a>

*   **GPT-4**: Provided a general, accurate definition <a class="yt-timestamp" data-t="04:21:00">[04:21:00]</a>.
*   **ChatPDF.com**: Offered a definition very similar to GPT-4's, suggesting a reliance on general knowledge rather than specific PDF content <a class="yt-timestamp" data-t="05:06:00">[05:06:00]</a>.
*   **PDFGPT.io**: Provided a definition more specific to the paper, including direct citations to page numbers, indicating it pulled information directly from the PDF <a class="yt-timestamp" data-t="06:38:00">[06:38:00]</a>.
    *   **Verdict**: PDFGPT.io was superior in leveraging the PDF content.

### Test 2: "What are the different types of supervised learning?" <a class="yt-timestamp" data-t="08:32:00">[08:32:00]</a>

*   **GPT-4**: Gave a succinct and correct answer, identifying regression and classification <a class="yt-timestamp" data-t="09:06:00">[09:06:00]</a>.
*   **ChatPDF.com**: Despite a mistyped query ("soy provised"), ChatPDF struggled, listing [[Model Architecture and Data Quality in AI | model architectures]] (e.g., CNN, RNN) rather than types of supervised learning <a class="yt-timestamp" data-t="10:40:00">[10:40:00]</a>.
*   **PDFGPT.io**: Provided the types of learning as categorized in the paper: supervised, semi-supervised, and unsupervised, also mentioning deep reinforcement learning <a class="yt-timestamp" data-t="09:32:00">[09:32:00]</a>.
    *   **Verdict**: PDFGPT.io was better at extracting paper-specific information. GPT-4 provided the most generally correct answer.

### Test 3: "What is a key difference between traditional ML and DL?" <a class="yt-timestamp" data-t="13:18:00">[13:18:00]</a>

*   All three models (GPT-4, PDFGPT.io, ChatPDF.com) accurately identified feature extraction as a key difference, demonstrating effective [[Advancements in AI context length and retrieval | similarity search]] and information retrieval <a class="yt-timestamp" data-t="14:04:00">[14:04:00]</a>, <a class="yt-timestamp" data-t="15:36:00">[15:36:00]</a>, <a class="yt-timestamp" data-t="16:44:00">[16:44:00]</a>.

### Test 4: "When did Fukushima first describe the CNN?" <a class="yt-timestamp" data-t="19:57:00">[19:57:00]</a>

*   **PDFGPT.io**: Failed to find the information, likely due to the exact phrase "CNN" not being in the sentence containing the 1988 date <a class="yt-timestamp" data-t="21:12:00">[21:12:00]</a>.
*   **ChatPDF.com**: Correctly found the 1988 date from the PDF <a class="yt-timestamp" data-t="21:46:00">[21:46:00]</a>.
*   **GPT-4**: Provided a date (1979-1980) that contradicted the PDF's 1988 date <a class="yt-timestamp" data-t="20:40:00">[20:40:00]</a>. However, an external web search confirmed GPT-4's date was *actually correct* regarding the original Neocognitron paper, revealing an inaccuracy in the survey PDF itself <a class="yt-timestamp" data-t="23:30:00">[23:30:00]</a>.
    *   **Verdict**: This highlights that generalist AIs might sometimes correct inaccuracies in the source material due to their broader [[Data Curation and Model Evaluation in AI | training data]].

### Test 5: "What new types of architecture/design did AlexNet introduce?" <a class="yt-timestamp" data-t="25:36:00">[25:36:00]</a>

*   **GPT-4**: Identified larger/deeper networks, ReLU activation, and Dropout regularization <a class="yt-timestamp" data-t="26:30:00">[26:30:00]</a>.
*   **PDFGPT.io**: Identified Local Response Normalization (LRN) and Dropout <a class="yt-timestamp" data-t="27:13:00">[27:13:00]</a>.
*   **ChatPDF.com**: Identified deeper/wider models, convolutional layers, ReLU, and Dropout, but missed LRN <a class="yt-timestamp" data-t="27:58:00">[27:58:00]</a>.
    *   **Verdict**: PDFGPT.io extracted both specific mentions from the paper.

### Test 6: "Who proposed the Parametric ReLU and when?" <a class="yt-timestamp" data-t="37:51:00">[37:51:00]</a>

*   **GPT-4**: Accurately provided the full names (Kaiming He, et al.) and the publication year (2015), along with the paper's title <a class="yt-timestamp" data-t="38:50:00">[38:50:00]</a>.
*   **PDFGPT.io & ChatPDF.com**: Both correctly cited "Kim et al. in 2015" as found in the paper <a class="yt-timestamp" data-t="39:31:00">[39:31:00]</a>, <a class="yt-timestamp" data-t="40:59:00">[40:59:00]</a>.
    *   **Verdict**: GPT-4 demonstrated superior external knowledge, providing more comprehensive authorship details. The PDF bots faithfully reproduced the information as presented in the document, even if less complete.

### Test 7: "What are different optimization methods for DL?" <a class="yt-timestamp" data-t="43:13:00">[43:13:00]</a>

*   **GPT-4**: Provided the most comprehensive list of optimization methods, including several not explicitly listed in the paper <a class="yt-timestamp" data-t="46:36:00">[46:36:00]</a>.
*   **ChatPDF.com**: Accurately listed the five specific methods mentioned in the paper (SGD, AdaGrad, AdaDelta, RMSprop, Adam) in the exact order <a class="yt-timestamp" data-t="43:52:00">[43:52:00]</a>. This suggests ChatPDF has a higher [[Data Curation and Model Evaluation in AI | similarity threshold]] for information retrieval <a class="yt-timestamp" data-t="44:53:00">[44:53:00]</a>.
*   **PDFGPT.io**: Gave a more generic and less specific answer, suggesting a lower [[Data Curation and Model Evaluation in AI | similarity threshold]] where it stops searching once it finds something "kind of similar" <a class="yt-timestamp" data-t="45:47:00">[45:47:00]</a>.
    *   **Verdict**: GPT-4 was the best source for general knowledge. ChatPDF was best at extracting specific lists from the paper.

### Test 8: "Can you provide a link to the Stanford Question Answering Dataset (SQuAD)?" <a class="yt-timestamp" data-t="52:22:00">[52:22:00]</a>

*   **PDFGPT.io & ChatPDF.com**: Both found the exact specific link within the PDF <a class="yt-timestamp" data-t="53:02:00">[53:02:00]</a>, <a class="yt-timestamp" data-t="53:15:00">[53:15:00]</a>.
*   **GPT-4**: Surprisingly, GPT-4 *also* knew the exact, obscure link without being provided the PDF, demonstrating its vast [[Data Curation and Model Evaluation in AI | training data]] and knowledge base <a class="yt-timestamp" data-t="53:31:00">[53:31:00]</a>.
    *   **Verdict**: All performed well, but GPT-4's ability to recall such niche information without the document was particularly striking.

### Test 9 (Obscure Paper): "Who and when recorded the original field notes for ashlars in Tiwanaku, Bolivia?" <a class="yt-timestamp" data-t="58:29:00">[58:29:00]</a>

This test used a complex computational archaeology paper.
*   **ChatPDF.com**: Successfully identified J.P. Protzen (mid-1990s), Léonce Agron (1848), and Max Uhle (1893) from the paper <a class="yt-timestamp" data-t="59:23:00">[59:23:00]</a>.
*   **PDFGPT.io**: Crashed and became unresponsive <a class="yt-timestamp" data-t="59:58:00">[59:58:00]</a>.
*   **GPT-4**: Identified Max Uhle (with a slightly different but close date of 1895) and other researchers, again showcasing its broad general knowledge <a class="yt-timestamp" data-t="01:01:03">[01:01:03]</a>.
    *   **Verdict**: ChatPDF was the most reliable of the PDF tools for this obscure query.

### Test 10 (Obscure Paper): "What is a Z-Corp Z310?" <a class="yt-timestamp" data-t="01:02:59">[01:02:59]</a>

*   **ChatPDF.com**: Provided a succinct summary of the printer's technology as described in the PDF <a class="yt-timestamp" data-t="01:03:21">[01:03:21]</a>.
*   **PDFGPT.io**: Provided details from the paper, including its use in creating 3D models <a class="yt-timestamp" data-t="01:04:00">[01:04:00]</a>.
*   **GPT-4**: Provided a much more detailed and externally sourced answer, including manufacturer, acquisition by 3D Systems, and operational details, demonstrating knowledge beyond the specific PDF <a class="yt-timestamp" data-t="01:05:07">[01:05:07]</a>.
    *   **Verdict**: GPT-4 again offered a superior, richer answer due to its vast knowledge base.

### Test 11 (Obscure Paper): "What university houses the School of Art and Architecture as well as the Young Research Library?" <a class="yt-timestamp" data-t="01:09:32">[01:09:32]</a>

*   **ChatPDF.com**: Initially stated it could not find the information in the PDF, but then performed an *internet search* and correctly identified UCLA <a class="yt-timestamp" data-t="01:11:04">[01:11:04]</a>. This unexpected "tool-forming" capability was surprising <a class="yt-timestamp" data-t="01:11:55">[01:11:55]</a>.
*   **PDFGPT.io**: Successfully found the information within the PDF and identified UCLA <a class="yt-timestamp" data-t="01:12:12">[01:12:12]</a>.
*   **GPT-4**: Immediately knew the answer was UCLA <a class="yt-timestamp" data-t="01:13:37">[01:13:37]</a>.
    *   **Verdict**: All eventually provided the correct answer, but ChatPDF's internet search capability was a notable feature.

## Conclusion and Implications

The overall conclusion is that generalist models like [[Safety and helpfulness in AI models | GPT-4]] often outperform specialized PDF AI tools in terms of both accuracy and comprehensiveness of information retrieval <a class="yt-timestamp" data-t="01:17:02">[01:17:02]</a>. GPT-4's vast [[Data Curation and Model Evaluation in AI | training data]] allows it to answer obscure questions, even correcting inaccuracies found in the source PDF.

While PDF-specific tools can excel at extracting precise information directly from the document via [[Advancements in AI context length and retrieval | similarity search]], their utility is questioned when a generalist AI can provide superior or equally good answers without needing to "read" the specific PDF <a class="yt-timestamp" data-t="01:15:19">[01:15:19]</a>. This raises broader implications for the future of information consumption and content creation:

*   **Reading Papers/Books**: The increasing capability of large language models (LLMs) suggests a future where traditional reading might be replaced by asking AI about content <a class="yt-timestamp" data-t="01:15:02">[01:15:02]</a>.
*   **Content Formatting**: The format of academic papers or APIs might evolve to be more consumable by LLMs rather than solely by humans <a class="yt-timestamp" data-t="01:15:42">[01:15:42]</a>, potentially affecting [[evaluation of AI coding through benchmarks | software development]] and [[Benchmarking AI agents with OSWorld and Web Arena | benchmarking AI agents]].
*   **Specialized vs. Generalist AI**: The trend indicates that general AI models, trained on the most extensive data, are becoming more effective than task-specific AIs, leading to a shift in market dynamics and the purpose of niche AI tools <a class="yt-timestamp" data-t="01:07:47">[01:07:47]</a>, <a class="yt-timestamp" data-t="01:08:02">[01:08:02]</a>.
*   **[[Comparisons of Biological and AI Systems | Inference cost and efficiency in AI]]**: While not directly discussed in detail, the underlying [[Inference cost and efficiency in AI | inference cost and efficiency in AI]] for such expansive models is a consideration.

Ultimately, the generalist GPT-4 was deemed the superior tool for information retrieval across a wide range of queries, often making dedicated PDF AI tools redundant for most purposes <a class="yt-timestamp" data-t="01:18:03">[01:18:03]</a>.