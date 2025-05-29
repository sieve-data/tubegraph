---
title: Privacy preserving AI techniques
videoId: 4zrU54VIK6k
---

From: [[lexfridman]] <br/> 

In this session, Andrew Trask, a renowned figure in the artificial intelligence and machine learning fields, discusses various privacy-preserving AI techniques. The central theme is the possibility of performing data-driven analysis without direct access to the raw data itself. Trask leads an open-source community called OpenMined, focusing on making algorithms and data more [[privacy_and_data_usage_in_ai | privacy-preserving]] through innovative tools and techniques <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Key Question

Trask poses a fundamental question: "Is it possible to answer questions using data that we cannot see?" He introduces this question as a foundation for understanding privacy-preserving AI and demonstrates how this is achievable through various tools and techniques <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

## Challenges in Accessing Data

One of the main challenges highlighted is the difficulty in accessing sensitive data, which is often scarce and regulated. For example, creating a classifier for medical diagnosis requires specific datasets that are not easily accessible, making research in such areas expensive and complicated <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. This issue leads researchers to often focus on more accessible tasks, leaving significant societal problems underexplored <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.

## Techniques in Privacy-Preserving AI

### Remote Execution

Remote execution allows computations to occur on a remote machine where the actual data resides, without giving direct access to the data itself. This is achieved through tools like PySyft, which extends frameworks such as PyTorch with privacy-preserving capabilities <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.

### Private Search and Sampling

By allowing researchers to perform private searches within remote datasets, they can gain insights and create classifiers without needing to download or directly view the data. This method ensures that sensitive data is not unnecessarily exposed <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>.

### Differential Privacy

Differential privacy introduces statistical noise to data queries, ensuring that individual entries cannot be isolated or identified from query results. This technique is critical in providing privacy guarantees in statistical analysis and machine learning, allowing insights without compromising individual privacy <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.

### Secure Multi-Party Computation (MPC)

Secure MPC enables multiple parties to compute a function using their data inputs without revealing their data to one another. This allows for collaborative computations on encrypted data, providing security even when data owners do not trust each other <a class="yt-timestamp" data-t="00:28:09">[00:28:09]</a>.

## Applications and Future Prospects

Trask envisions a future where more complex AI tasks involving sensitive data become more accessible due to these privacy-preserving techniques. This could drastically shift focus and resources onto essential tasks currently neglected due to data accessibility issues <a class="yt-timestamp" data-t="00:33:57">[00:33:57]</a>.

Moreover, Trask envisions potential applications like open data for science, single-use accountability systems, and encrypted services that could revolutionize how sensitive data is used and shared safely <a class="yt-timestamp" data-t="00:46:01">[00:46:01]</a>.

> [!info] OpenMined and Its Mission
> 
> The OpenMined community, consisting of over six thousand members, is actively working to reduce the barrier to entry in privacy-preserving AI. They focus on making sensitive data accessible in a safer manner for significant societal challenges, aligning with [[importance_of_safety_and_ethical_considerations_in_ai_development | ethical considerations in AI development]] <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>.

## Conclusion

The introduction and maturation of privacy-preserving AI techniques have the potential to transform the way sensitive data is accessed and utilized. These techniques provide a pathway towards addressing critical issues without compromising individual privacy, paving the way for safer and more ethical AI applications. As these technologies advance, they offer immense potential for privacy-respectful AI-driven analysis and highlight the need for [[ethical_considerations_for_ai_with_respect_to_privacy_and_trust | ethical considerations and trust in AI]] development.