---
title: history of convolutional neural networks
videoId: u6aEYuemt0M
---

From: [[lexfridman]] <br/> 

Convolutional neural networks (CNNs) have played a pivotal role in advancing the field of computer vision. The evolution of these networks highlights significant milestones and breakthroughs in artificial intelligence, particularly in their application to image classification tasks. Here, we trace the historical development and key contributions that shaped CNNs and their current ubiquitous presence.

## Early Inspiration and Models

The concept of convolutional operation within neural networks is heavily inspired by biological processes. In the 1960s, experiments by Hubble and Wiesel aimed to understand the computations in the visual cortex of cats. Their work demonstrated how neurons in the visual fields responded to specific patterns of light, which later inspired the model of simple and complex cells used in early CNNs <a class="yt-timestamp" data-t="01:31">[00:01:31]</a>.

One of the earliest models that attempted to incorporate these insights into a computational framework was the Neocognitron, developed by Kunihiko Fukushima in the 1980s. This model introduced a hierarchical, layered structure similar to the visual cortex, where simple cells detected basic visual features that were spatially combined by complex cells <a class="yt-timestamp" data-t="02:08">[00:02:08]</a>.

However, the Neocognitron did not initially utilize backpropagation for learning, relying instead on unsupervised learning methods to tune certain parameters.

## Key Breakthroughs and Advancements

### Introduction of Backpropagation

The significant shift came in the 1990s with Yann LeCun's work, which integrated backpropagation into training convolutional neural networks. This approach allowed for supervised learning, which facilitated the end-to-end training of networks. The introduction of backpropagation marked a considerable improvement, laying the foundation for more robust and efficient CNN architectures <a class="yt-timestamp" data-t="03:02">[00:03:02]</a>.

### Emergence of AlexNet (2012)

A watershed moment for convolutional neural networks occurred in 2012 with the development of AlexNet by Alex Krizhevsky, Ilya Sutskever, and Geoffrey Hinton. This model harnessed the power of GPUs for training on the large-scale ImageNet dataset, demonstrating the feasibility of scaling up neural networks for complex image processing tasks. AlexNet significantly outperformed previous architectures in the ImageNet Large Scale Visual Recognition Challenge (ILSVRC), reducing the top-5 error rate drastically <a class="yt-timestamp" data-t="10:58">[00:10:58]</a>.

### VGGNet and GoogleNet (2014)

The following years saw incremental improvements with architectures such as VGGNet, which emphasized simplicity by using smaller 3x3 convolutional filters throughout the network. GoogleNet introduced a more complex architecture with inception modules that efficiently used computational resources by exploiting spatial hierarchies within the data <a class="yt-timestamp" data-t="38:52">[00:38:52]</a>.

### Residual Networks (2015)

A significant advancement in CNN architectures came with the introduction of Residual Networks (ResNets) by Kaiming He and colleagues. ResNets addressed the degradation problem by introducing shortcut connections, allowing gradients to backpropagate more effectively without vanishing or exploding. The concept of residual learning enabled the training of much deeper networks, leading to substantial improvements in performance across various visual recognition tasks <a class="yt-timestamp" data-t="43:00">[00:43:00]</a>.

### Applications Beyond Image Classification

Today, CNNs are applied to a wide range of tasks beyond simple image classification. They have been integrated into systems for object detection, semantic segmentation, image captioning, and even areas outside computer vision such as genomics and speech processing <a class="yt-timestamp" data-t="59:30">[00:59:30]</a>.

## Impact and Current Trends

The success of CNNs has catalyzed the rapid development and application of deep learning technologies. Frameworks such as TensorFlow have democratized access to state-of-the-art architectures, allowing researchers and practitioners to leverage CNNs across various domains.

The continual refinement and exploration of new architectures and training regimes, such as convolutional networks with dilations, recurrent feedback loops, and pruning techniques for efficiency, continue to push the boundaries of what CNNs can achieve <a class="yt-timestamp" data-t="72:00">[01:12:00]</a>.

> [!info] Conclusion
>
> The historical trajectory of convolutional neural networks is a testament to the symbiotic relationship between theoretical neuroscience, algorithmic advancements, and computational innovations. As we look toward the future, CNNs remain a cornerstone of deep learning, influencing cutting-edge research and technological developments across numerous fields.