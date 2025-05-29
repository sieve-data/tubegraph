---
title: Installation environment for digital signatures on Windows
videoId: qI-57MxCitM
---

From: [[dr_tutoriales]] <br/> 

To set up an environment for [[using_digital_signatures_in_pdf_files | digital signatures]] on a Windows computer, several components are required, including specific software installations and a physical ID card reader <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. This process involves obtaining a PIN, downloading necessary software, and verifying the setup <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

## Initial Requirements

Before beginning the software installation, an essential **PIN key** linked to your ID card (DNI) is needed <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. This PIN is typically issued when the DNI is first obtained <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. If the PIN is not available, it can be acquired from the nearest police station using automatic machines <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. The process involves logging in with your ID card to these machines to sign up and retrieve the code <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

## Software Downloads

Two primary links are required for the installation: one from the government headquarters and another for the [[using_digital_signatures_in_pdf_files | electronic signature]] installation <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

### Determining System Bit Version

Before downloading, it's crucial to determine if your Windows operating system is 64-bit or 32-bit to ensure compatibility <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
To check this:
1.  Open File Explorer <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
2.  Navigate to "This PC" <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
3.  Right-click on "This PC" and select "Properties" <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.
4.  The system type (e.g., "64-bit operating system") will be displayed <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

### Required Software Components

*   **FNMT Configurator**: This configurator is installed first <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. The installation involves accepting terms and choosing a directory <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.
*   **Self-Signature Software**: This software is also downloaded and installed <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a> <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. It is crucial for the [[process_of_downloading_and_installing_the_digital_certificate | validation of electronic certificates]] <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. During its installation, there is an option to configure it for Firefox, which should be selected if Firefox is used <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. Once installed, the self-signature software will be visible on the computer <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.

## Hardware Requirement: ID Card Reader

To [[validation_of_electronic_certificates | validate]] the [[process_of_downloading_and_installing_the_digital_certificate | digital certificate]] on the ID card, a physical ID card reader is necessary <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.
The process involves:
1.  Inserting the ID card into the reader, ensuring the chip is correctly aligned to be read <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
2.  Connecting the reader to the computer via a USB port <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. A sound confirms successful connection and the device reading the ID <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.

## Certificate Validation

To verify the functionality of the setup, a specific link for certificate validation can be used <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. This step leverages the FNMT software to confirm the certificate <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.

1.  Access the validation link <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
2.  Click to validate the certificate <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. This may open a PDF with instructions <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
3.  Select "Select Certificate" and open the previously installed self-signature software <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
4.  The self-signature software will read the [[validation_of_electronic_certificates | electronic certificates]] stored on the ID card <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.
5.  Different certificates associated with the individual's name will appear, including authentication and [[options_for_signing_pdfs_including_text_and_image_signatures | signature]] certificates <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
6.  Choose the DNI electronic signature certificate, enter the secret PIN code, and the system will confirm the certificate's validity, displaying the name, surname, and ID card details <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.