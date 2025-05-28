---
title: Moving computation from cloud to edge
videoId: WbLQqPw_n88
---

From: [[lexfridman]] <br/> 

## Introduction
In recent years, the landscape of computation has seen a significant shift from centralized cloud computing to distributed, edge-based processing. This shift is primarily driven by the need for improved communication, enhanced privacy, reduced latency, and the computational demands of modern applications like [[computation_and_intelligence | AI]], robotics, and healthcare systems. As we delve into this shift, we will explore the rationale behind moving computation to the edge, the advantages it holds, and the challenges it presents.

## The Rationale for Edge Computing

### Communication Challenges
One of the primary reasons for shifting computation to edge devices is the limitation in communication infrastructure. In many parts of the world, reliable high-bandwidth communication networks are unavailable or may not be feasible due to infrastructural constraints. By processing data locally on devices, the reliance on stable communication networks is minimized, addressing the tethering issues of cloud computing <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

### Privacy and Security Concerns
Applications that handle sensitive data significantly benefit from edge computing. For instance, in healthcare, where patient data is highly sensitive, processing information locally on devices ensures better privacy and security compared to sending data to the cloud <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.

### Latency Reduction
Interactive applications such as autonomous navigation, robotics, and real-time AI applications require minimal latency. Processing data locally on the device—such as a robot or a self-driving car—enables real-time decision-making, which is crucial in scenarios where reaction times are critical (e.g., obstacle detection in self-driving cars) <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.

## Challenges of Edge Computing

### Power Consumption
One of the significant challenges of edge computing is managing power consumption. Devices like smartphones or small robots have limited energy capacities due to size, weight, and cost constraints. Processing data locally can consume substantial power, sometimes equivalent to—or even surpassing—the device's total power budget <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.

### Need for Specialized Hardware
Transitioning computation to the edge often requires specialized hardware that can provide the necessary speed and efficiency. Traditional transistors are no longer becoming smaller or faster, necessitating the development of custom hardware designed explicitly for AI and robotic tasks <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.

### Data Movement
Another challenge involves reducing data movement, which is a significant cost in terms of energy. Efficient designs must minimize data transfers within devices by using memory hierarchies and custom data flows to keep power consumption low <a class="yt-timestamp" data-t="00:20:38">[00:20:38]</a>.

## Advantages of Edge Computing

### Parallelism
Edge devices can offer significant parallel processing capabilities. Many algorithms, particularly in AI, exhibit parallelism that can be exploited to improve processing speeds and efficiency on edge devices <a class="yt-timestamp" data-t="00:21:02">[00:21:02]</a>.

### Hardware Acceleration
By designing hardware acceleration strategies tailored for specific applications, edge devices can perform complex computations more efficiently than general-purpose processors. This leads to significant reductions in both latency and energy consumption <a class="yt-timestamp" data-t="00:34:06">[00:34:06]</a>.

### Flexibility
Despite the demanding nature of edge computing applications, flexible hardware architectures can support various algorithms and data processing needs without requiring a one-to-one mapping to cloud resources. This adaptability is crucial for future-proofing edge technology <a class="yt-timestamp" data-t="00:57:01">[00:57:01]</a>.

## Conclusion

The move from cloud to edge computing represents a transformative change in how data is processed across numerous applications. While there are challenges to overcome, especially concerning power consumption and data management, the benefits of low latency, heightened privacy, and reduced communication dependence are compelling. As hardware and algorithmic innovations continue to advance, the scope and capability of edge computing will only expand, paving the way for more sophisticated, real-time applications to flourish without the constraints of cloud-based processing. This shift aligns closely with the overarching goals of [[decentralizing_compute_power | decentralizing compute power]] and optimizing technology for a wide range of settings and applications.