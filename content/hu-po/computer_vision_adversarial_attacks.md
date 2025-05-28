---
title: computer vision adversarial attacks
videoId: pR2et-guixM
---

From: [[hu-po]] <br/> 

[[computer_vision_deep_dive | Computer vision]] adversarial attacks have existed for some time, demonstrating that neural networks operate in ways that are not always intuitive to humans <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. These attacks highlight the fragility of artificial intelligence systems <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

## How They Work
Neural networks, particularly those used for classification, create decision boundaries in very high-dimensional latent spaces that are difficult for humans to parse <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. An adversarial attack involves making small, often imperceptible, perturbations to an input image. While these changes may appear as noise to the human eye, they can cause a convolutional neural network (confnet) to entirely misclassify the image <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. The network's scanning of the image, including different textures, shapes, and edges, adds up to a consensus, and the adversarial perturbation changes enough of these inputs to alter that consensus dramatically <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

Image models operate on discrete inputs, as pixels are discretized into 256 bins for red, green, and blue values, resulting in millions of possible pixel values <a class="yt-timestamp" data-t="00:29:30">[00:29:30]</a>.

## Famous Examples

### Panda to Gibbon
One of the earliest and most well-known examples involved a picture of a panda <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. Adding a small amount of carefully crafted noise, which appears like static to a human, could transform the classification from "panda" to "gibbon" with high confidence <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. This "noise" is actually a step in the high-dimensional manifold towards the "gibbon" area in the network's latent space <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

### Stop Signs
Around 2016, when autonomous vehicles were a hot topic, researchers realized that object detectors in these vehicles were vulnerable. Adding specific bars or "crap" to a stop sign could prevent the vehicle's system from detecting it as a stop sign <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

### Banana to Toaster
A prominent example involved stickers placed on real-world objects <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. A picture of a banana, correctly classified as such by a VGG16 convnet, could be misclassified as a toaster simply by attaching a specially designed sticker to it <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. This demonstrates how even minor visual changes can completely alter the object's classification to the neural network <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.

## Vulnerability and Specificity
Early [[computer_vision_deep_dive | computer vision]] adversarial attacks were often very specific and brittle <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>. An adversarial attack for a convnet would typically only work for:
*   A specific model <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>
*   The same model architecture, but *not* if trained on different data <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>
*   A specific model architecture trained on a specific dataset <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>

This characteristic made them less practical as an attack vector initially <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>. In contrast, newer [[interpretable_and_universal_adversarial_prompts | universal and transferable adversarial attacks]] for language models represent a significant advancement, as they are designed to work across different models, even black-box ones <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>. The vulnerability of these attacks relative to model size is not yet fully understood <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.