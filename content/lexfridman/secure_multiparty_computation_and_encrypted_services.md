---
title: Secure multiparty computation and encrypted services
videoId: 4zrU54VIK6k
---

From: [[lexfridman]] <br/> 

Secure multiparty computation (SMPC) and encrypted services represent a groundbreaking approach in the world of data science and cryptography, facilitating the secure use of sensitive data without compromising privacy. This approach holds the promise of transforming how we handle personal data, perform computations, and offer services over the internet, all while maintaining stringent privacy standards.

## What is Secure Multiparty Computation?

Secure multiparty computation enables multiple parties to jointly compute a function over their inputs while keeping those inputs private from each other. This computation model allows for the sharing of ownership over data in such a way that no single party can learn the input of the other parties just by looking at their own share. The concept can be described as follows:

> [!info] Secure Multiparty Computation
>
> Secure multiparty computation allows for encrypted computation, meaning multiple individuals can combine their data to compute a function without revealing their private inputs to each other, thus providing privacy-preserving joint computation <a class="yt-timestamp" data-t="00:28:13">[00:28:13]</a>.

### Example of Secure Multiparty Computation

Consider a number five, which can be split into two shares, say two and three. Two friends, Mary Ann and Bobby, each hold one share, thus sharing ownership of the original number (five). They can perform computations while the number remains encrypted; for instance, multiplying each share by two results in an encrypted product of ten. These computations can be done without either party knowing the input data from the other party, preserving the privacy of the data while achieving the desired computation <a class="yt-timestamp" data-t="00:30:02">[00:30:02]</a>.

## Encrypted Services and Their Implications 

Encrypted services extend the concept of secure data handling across various applications, allowing services to be provided over encrypted data. A notable example is the encrypted messaging service like WhatsApp, where messages are encrypted on the sender's device and only decrypted on the recipient's device <a class="yt-timestamp" data-t="00:55:04">[00:55:04]</a>.

With advancements in machine learning, encrypted computation, and differential privacy, similar encryption principles could be applied to a broader range of services, such as medical diagnostics or personalized recommendations. These services could benefit from accessing personal data without compromising user privacy.

### Envisioning Encrypted Medical Services

Imagine a scenario where a patient can receive a medical diagnosis without revealing their medical records to their doctor. By utilizing encrypted services, the patient's symptoms and medical history remain private, with computations performed through a secure multi-party protocol. The output, whether a diagnosis or treatment recommendation, is returned to the patient, maintaining confidentiality throughout the process <a class="yt-timestamp" data-t="00:58:56">[00:58:56]</a>.

## Challenges and Opportunities

Despite their potential, SMPC and encrypted services do present challenges, particularly in terms of computational complexity and the need for robust network infrastructure. These services currently experience a performance slowdown compared to their plaintext counterparts, but with continued technological advancements and greater adoption, these hurdles are expected to be addressed <a class="yt-timestamp" data-t="00:33:26">[00:33:26]</a>.

The transformative potential of secure multiparty computation and encrypted services lies in their ability to offer remarkable privacy enhancements and new capabilities in data-sharing applications. They provide a pathway to a future where sensitive data can be utilized to its fullest extent without compromising individual privacy. By opening up access to previously inaccessible datasets, these technologies could revolutionize fields such as healthcare, personalized marketing, and more, enabling innovations that benefit society as a whole.