---
title: Comparisons with diffusion models
videoId: ExfMg4v5DMA
---

From: [[hu-po]] <br/> 

Initially, the speaker questioned whether [[Diffusion Models and ControlNet | diffusion models]] were still the primary focus, highlighting a new paper, "Drag Your GAN," which suggested a potential shift back towards GAN-based research <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.

## Diffusion Models vs. Generative Adversarial Networks (GANs)

While [[Comparison of diffusion models and consistency models | diffusion models]] are noted as "a little bit more popular now," generative GANs are "making a little bit of a comeback" <a class="yt-timestamp" data-t="02:21:57">[02:21:57]</a>.

### Generation Process
[[Diffusion Models and ControlNet | Diffusion models]] iteratively denoise randomly sampled noise to create photorealistic images <a class="yt-timestamp" data-t="02:22:22">[02:22:22]</a>. This process begins with "a bunch of gaussian noise," resembling "snow on a CRT TV," and the model "creates the image" by "pulling the image out of the universal entropy" <a class="yt-timestamp" data-t="02:22:44">[02:22:44]</a>. In contrast, GANs generally "one shot generate the entire image" from a low-dimensional latent vector <a class="yt-timestamp" data-t="02:23:01">[02:23:01]</a>, <a class="yt-timestamp" data-t="03:14:46">[03:14:46]</a>.

### Speed
A common criticism of [[Diffusion Models and ControlNet | diffusion models]] is their slowness, as they "require multiple noising steps," potentially up to "a thousand steps" <a class="yt-timestamp" data-t="03:12:26">[03:12:26]</a>. Although in practice, this is often "usually like 10 steps" <a class="yt-timestamp" data-t="03:13:39">[03:13:39]</a>. GANs, however, do not require this iterative process, offering a faster, single-shot generation <a class="yt-timestamp" data-t="03:14:46">[03:14:46]</a>.

### Controllability
Recent [[Diffusion Models and ControlNet | diffusion models]] have demonstrated "expressive image synthesis conditioned on text inputs," which was a key factor in launching the "generative AI revolution" <a class="yt-timestamp" data-t="03:30:27">[03:30:27]</a>. Despite this, the paper claims that natural language "does not enable fine-grained control" over image attributes <a class="yt-timestamp" data-t="03:42:42">[03:42:42]</a>. The speaker, however, expresses a belief that fine-grained control *is* possible with natural language and that the future of image editing will be "audio based," allowing users to verbally describe complex manipulations <a class="yt-timestamp" data-t="03:45:00">[03:45:00]</a>, <a class="yt-timestamp" data-t="03:53:01">[03:53:01]</a>.

### Image Quality
[[Diffusion Models and ControlNet | Diffusion models]] are acknowledged for enabling "image synthesis at a high quality" <a class="yt-timestamp" data-t="03:13:11">[03:13:11]</a>.

## Potential Future Work
The "Drag Your GAN" paper explicitly focuses on GANs, but the speaker speculates that the core approach could be extended to [[latent diffusion models and their internal representations | diffusion models]] <a class="yt-timestamp" data-t="03:52:51">[03:52:51]</a>. This would involve treating the diffusion model's latent feature map similarly to a GAN's latent code <a class="yt-timestamp" data-t="03:55:10">[03:55:10]</a>. However, this extension would likely lead to "very slow" performance due to the multi-step nature of [[Diffusion Models and ControlNet | diffusion models]] <a class="yt-timestamp" data-t="03:55:31">[03:55:31]</a>.

The speaker also suggests that future research could focus on adapting this point-based image editing to [[Rectified Flow in Diffusion Models | diffusion models]] or even video generation <a class="yt-timestamp" data-t="01:53:35">[01:53:35]</a>, <a class="yt-timestamp" data-t="01:53:40">[01:53:40]</a>.