---
title: Role of AI in smartphone photography
videoId: yY8OFp0-UZw
---

From: [[asianometry]] <br/> 

Modern smartphones are capable of capturing high-quality images, often on par with standalone cameras <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This capability is a significant selling point for new phones, with camera performance often headlining marketing messages and driving user upgrades <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. Top smartphone manufacturers heavily invest in this area; for instance, Apple employed 800 people dedicated to the iPhone's camera in 2015, and Xiaomi announced hiring thousands for phone cameras in 2021 <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

While [[traditional_vs_digital_cameras | traditional analog cameras]] exposed photographic film to light <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>, today's smartphone cameras work fundamentally differently, relying on a digital camera module with a lens placed on top of an image sensor chip <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

## Overcoming Hardware Limitations with Computational Photography

[[challenges_in_smartphone_camera_engineering | Smartphone cameras]] face inherent physical constraints due to their small size, typically housed in areas 7 to 10 millimeters thick <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. This limits sensor size (around 5x4 mm compared to DSLR sensors at 36x24 mm) <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>, leading to potential issues like motion blur, image noise, and reduced dynamic range <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. Additionally, smartphone optics are smaller and less adjustable, creating [[challenges_in_smartphone_camera_engineering | engineering challenges]] such as a fixed and limited aperture and limited zoom function <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

The increasing computing power of smartphones, which can be as powerful as some laptops <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>, has been crucial in overcoming these physical deficits <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. This has led to the rise of [[computational_photography_techniques | computational photography]], a rapidly growing field responsible for some of the biggest advancements in recent years <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

### The Image Processing Pipeline

When a photo is taken, the camera image sensor, made of photodiodes with color filters, converts photons into electrical charges <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>. Dedicated image processing hardware receives these charges and maps them to colors, using arrangements like the Bayer filter <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>. Since each photodiode only corresponds to one color, algorithms like "demosaicing" fill in the missing color gaps, with two-thirds of the image data essentially being computer-generated <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

Further processing steps include:
*   **White Balance Correction**: Algorithms estimate scene illumination and adjust colors to appear as if lit by neutral white light, preventing unnatural tones <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.
*   **Color Manipulation**: Images may be manipulated based on user settings (e.g., "vivid" mode) or pre-programmed by the vendor to differentiate their photos' look <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.
*   **Noise Reduction**: Algorithms reduce image artifacts while aiming for a balance to avoid an overly smooth or fake appearance <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.

Finally, the image data is resized, RGB values are adjusted for display, and it's saved to a file format <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>.

### Digital Zoom and Multi-Camera Systems

True optical zoom, which involves physically moving the lens, is difficult in thin smartphones <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. Early attempts to implement it resulted in sizable camera bumps and disappointing performance <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.

Most smartphones initially relied on digital zoom, which involves cropping and upscaling the original image, often leading to reduced resolution <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>. To improve this, camera makers employed image algorithms to enhance missing details <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.

The prevailing approach for modern manufacturers is to use multiple rear cameras, such as a wide and a telephoto lens, allowing users to swap between them to achieve zoom <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>. Some high-end phones use a "folded zoom" approach, employing a 45-degree mirror to bend light sideways, enabling zoom without increasing camera thickness <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.

### Low Light and Night Performance

The iPhone 13's low light and nighttime performance showcases how the industry has pushed the boundaries of [[computational_photography_techniques | computational photography]] <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>. Recognizing that the human eye is poor at discerning color in the dark <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>, camera makers aim to create colorful, noise-free low-light photos rather than strictly faithful reproductions of the scene <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>.

While DSLRs traditionally excelled in low light due to larger sensors and adjustable apertures <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>, smartphones adapt [[computational_photography_techniques | burst processing]] <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>. This technique, rooted in astrophotography's image stacking, involves capturing and merging many frames to reduce noise and improve image quality <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>. The smartphone continuously captures frames, and when the shutter is pressed, it selects a key frame and merges others to create a single high-quality image <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>. The 2018 Google Pixel's Night Sight feature was a breakthrough in this area, compensating for jittery hands and moving objects <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>. Burst photography is now used for denoising, increasing resolution, and High Dynamic Range (HDR) compression <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>.

## Direct Applications of AI and Machine Learning

Recent advancements in onboard [[ai_and_ai_chip_boom | AI processor]] technology have significantly boosted imaging performance <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>.

*   **White Balance Correction**: Researchers have collected digital photos, had professional photographers manually white balance them, and then fed this data into a machine learning model. This model creates more effective color constancy algorithms, particularly useful in low-light conditions, and was prominently featured in Google Pixel's Night Sight <a class="yt-timestamp" data-t="00:14:06">[00:14:06]</a>.
*   **Image Sharpening and Upscaling**: To improve digitally zoomed photos, machine learning models are trained with high- and low-resolution imagery data to properly sharpen and enhance blurry edges <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>. [[nvidia_and_ai_chip_competition | Nvidia]] applies a similar concept called Deep Learning Super Sampling (DLSS) to upscale video game assets <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>.
*   **Bokeh Effect**: In traditional smartphone cameras, the entire image is typically in focus. However, [[computational_photography_techniques | computational photography]] allows mobile phones to generate a synthetic bokeh effect (background blur). Modern cameras use a second camera or a dedicated depth sensor to determine subject distance, then introduce depth blur to simulate the effect <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>. This is the basis of iPhone's Portrait Mode, which uses [[ai_and_ai_chip_boom | AI]] to recognize subjects like people or animals and blur the background <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>.

## Conclusion

The evolution of [[smartphone_camera_advancements | smartphone cameras]] reveals the profound role of computer processing and image manipulation in creating modern digital photos <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>. From simple math operations to complex machine learning models, the image data saved and uploaded is heavily "doctored" from what the sensor actually "sees" <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>. While the scene itself is reality, the smartphone camera image increasingly deviates from it <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>, reflecting a user preference for "great-looking" photos, even if they don't perfectly represent the original reality <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>.