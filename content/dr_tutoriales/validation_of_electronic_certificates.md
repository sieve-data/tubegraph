---
title: Validation of electronic certificates
videoId: qI-57MxCitM
---

From: [[dr_tutoriales]] <br/> 

To validate electronic certificates, particularly those associated with an electronic ID (DNIe), specific software and hardware are required, along with an initial activation process. This guide outlines the steps to prepare your computer and validate your electronic certificate.

## Activating Your Electronic ID (DNIe)

Before beginning the installation and validation process, you need a PIN key for your electronic ID card <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. This code is typically issued on the day you receive your DNI <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

If you do not have this code, you can obtain it from an automatic machine at the nearest police station <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. The process involves logging in with your ID card to these machines to register and receive the code <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

> [!NOTE] Further details on [[how_to_activate_an_electronic_id | activating an electronic ID]] are available in a separate tutorial mentioned in the video's first comment <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

## [[process_of_downloading_and_installing_the_digital_certificate | Setting Up the Installation Environment for Digital Signatures on Windows]]

The [[installation_environment_for_digital_signatures_on_windows | installation environment for digital signatures on Windows]] requires two main software components: one from the government headquarters (likely for general ID card services) and one for electronic signature installation <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. These links are typically provided in the video's description or comments <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

### Checking Your Computer's Bit Version

Before downloading, determine if your Windows system is 64-bit or 32-bit <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>:
1.  Open File Explorer <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
2.  Navigate to "This PC" <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
3.  Right-click on "This PC" and select "Properties" <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.
4.  Look for "System type" to see if it's a 64-bit or 32-bit operating system <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

### Software Installation Steps

1.  **Download and Install the FNMT Configurator:**
    *   Download the appropriate version (e.g., 64-bit for Windows) from the provided link <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.
    *   Run the installer, accept the conditions, and proceed with the installation to the default directory <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
    *   This component is essential for various options related to digital certificates <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

2.  **Download and Install the "Self-Signature" Application:**
    *   Download the latest version (e.g., 1.82 for 64-bit systems) from the electronic signature link <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
    *   After the FNMT configurator is installed, run the self-signature installer <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
    *   Accept the terms and conditions <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
    *   During installation, you may have the option to configure Firefox to rely on its root certificate <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. Ensure this option is selected if you use Firefox <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
    *   Complete the installation <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>. Once installed, you will see the self-signature application icon on your desktop <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.

## Required Hardware: ID Card Reader

To validate your digital certificate, you will need an ID card reader <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. This device reads the chip embedded in your ID card <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. A recommended reader model can be found via a link in the video's first comment, often available on platforms like Amazon <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

### Connecting the ID Card Reader
1.  Insert your ID card into the reader, ensuring the chip is correctly aligned to be read by the device <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
2.  Connect the reader to your computer via its USB port <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. You should hear a connection sound, indicating the device is reading the ID <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.

## Validating Your Electronic Certificate

To verify that your electronic ID card and its certificates are working correctly:

1.  Access the certificate validation link, typically provided in the video's first comment <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>. This link is often associated with the FNMT (Fábrica Nacional de Moneda y Timbre) service <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
2.  Click on the option to "validate certificate" <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
3.  On the validation page, click "Select Certificate" <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
4.  Open the "self-signature" application that was previously installed <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.
5.  The self-signature application will read the electronic certificates stored on your ID card <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.
6.  You will see a list of different certificates associated with your name, including authentication and signature certificates <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.
7.  Select one of the signature certificates, such as the DNI electronic signature <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
8.  Enter your secret PIN code <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.
9.  If successful, the system will confirm that the certificate is valid, displaying your name, surname, and ID card details <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.

This process confirms the proper functioning and validity of your electronic ID's digital certificates. For information on [[using_digital_signatures_in_pdf_files | using digital signatures in PDF files]], the validation page might provide further details or a downloadable PDF guide <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.