---
title: Troubleshooting issues in PDF document generation
videoId: 70hk3h7f_o8
---

From: [[theaccountantguy]] <br/> 
## Troubleshooting Issues in PDF Document Generation

When [[using_pdfoutputcom_to_generate_pdf_documents_in_bulk | generating PDF documents]] using PDF output, several common issues may arise, primarily related to template and database configuration, as well as regeneration of existing documents. This guide outlines how to identify and resolve these issues.

### Common Troubleshooting Scenarios

#### Unmapped Properties Between Database and Template

A frequent issue occurs when the names of fields in your Notion database do not exactly match the placeholder text in your template <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

*   **Cause**: If a database column name, such as "total amount", has a space, but the corresponding placeholder in the template (`{total amount}`) does not, it will not be automatically mapped <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>. Adding extra commas or spaces can also cause mismatches <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
*   **Identification**:
    *   During the mapping step (Step 2), you will see elements listed as "unmatched" <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.
    *   You can use the "Filter unmapped properties" option to quickly identify any properties that are not mapped <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
*   **Solution**: Manually select and match the similar names between the Notion database properties (on the left) and the template elements (on the right) <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. Ensure that your template placeholder names precisely match your database column names, avoiding extra spaces or punctuation <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.

#### Regenerating Existing PDF Documents

When [[exporting_and_tracking_generated_pdf_documents | exporting and tracking generated PDF documents]], PDF output adds a "PDF status" column to your database to indicate that a PDF document has been generated for a particular row <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.

*   **Issue**: If the checkbox in the "PDF status" column for a specific row is ticked, the system assumes the PDF has already been generated <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
*   **Solution**: To regenerate a PDF for a specific row, you must first untick the checkbox in the "PDF status" column for that row <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.

#### Watermarks on Generated PDFs

*   **Issue**: PDF documents generated on the free plan will include a watermark <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
*   **Solution**: To remove watermarks from your generated PDFs, you need to upgrade to a paid plan <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. This can be done via the "Upgrade" section in the sidebar <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>. For more information, refer to [[options_for_upgrading_pdf_output_features_and_settings | Options for Upgrading PDF Output Features and Settings]].

### Getting General Assistance

If you encounter other issues or difficulties not covered above, PDF output provides several avenues for support:

*   **Help Section**: The "Help" section in the sidebar offers a complete demonstration setup video that can assist with troubleshooting <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.
*   **Feedback Option**: Use the "Feedback" option in the sidebar to report specific issues. You can select the type of issue from a drop-down menu to send feedback directly to support <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.
*   **Direct Contact**: For specific solutions or assistance with particular use cases, you can reach out via email at notionformyuse@gmail <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.