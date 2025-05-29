---
title: Vertical integration and business strategy in tech companies
videoId: TRZqE6H-dww
---

From: [[asianometry]] <br/> 

In 1995, over 30 companies competed to build graphics chips for personal computers, but within six years, only three remained, with Nvidia clearly leading <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This consolidation highlights the critical role of strategic business decisions, including partnerships and vertical integration, in determining market dominance.

## Early Graphics Hardware Landscape

The concept of separate hardware handling complex 3D graphics tasks existed before Nvidia's founding <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. Early examples include Atari video game consoles in the 1970s and commercial video cards in the 1980s <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. The IBM Professional Graphics Controller (PGA), released in 1984, utilized an onboard Intel 8088 microprocessor to offload video tasks from the CPU, though its high cost ($4,000-$5,000) and IBM PC exclusivity limited its market success <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

In the late 1980s, Silicon Graphics Inc. (SGI) emerged as a dominant graphics player, refining the concept of a graphics pipeline to translate coordinates to 2D pixel space <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. SGI released OpenGL in 1992, a public 3D graphic standard (API) with 120 commands, which became widely adopted and a critical factor in graphics hardware <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. While SGI hardware dominated the profitable graphics workstation space, it did not seriously pursue the consumer market <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

### The Rise of Consumer Graphics Demand

Consumer interest in graphics surged with Microsoft Windows 3.1 in 1990, featuring a graphical user interface <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>. This interest exploded in 1993 with the release of the 3D game *Doom* by id Software, followed by *Quake* in 1996 <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. *Quake* offered full real-time 3D rendering and online multiplayer, but many PCs struggled to run it at full specifications without additional hardware <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

To address this, id Software's John Carmack rewrote *Quake* to support OpenGL, creating *GLQuake* <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. This spurred innovation in consumer video cards. 3dfx, a graphics chip startup, developed a wrapper to make OpenGL compatible with its proprietary Glide graphics API and launched the Voodoo video card, taking advantage of a drop in RAM prices <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. Voodoo cards, designed by 3dfx in America and manufactured in Taiwan, were sold to board partners for resale <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>. The Voodoo card was the first consumer card capable of running *GLQuake* well (640x480, 16-bit color at 30 frames per second) and retailed for about $200 <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>. Crucially, it only offered 3D acceleration, requiring a separate card for 2D <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>. At its peak, 3dfx held 80% of the 3D acceleration graphics card market <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.

## Nvidia's Strategic Evolution

Nvidia was founded in 1993 by Jensen Huang (CEO), Chris Malachowsky, and Curtis Priem, with the aim of creating microprocessors for high-quality 3D graphics <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. Facing a downturn in Silicon Valley and competing with many other graphics chip startups, Nvidia secured $2.5 million in early funding <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

### Early Partnerships and Product Setbacks

Jensen Huang pursued three crucial early partnerships:
1.  **Manufacturing**: In 1994, Nvidia partnered with SGS Thompson Microelectronics (now STMicroelectronics) for chip manufacturing, with Nvidia focusing on design <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.
2.  **Board Sales**: A deal with Diamond Multimedia Systems ensured that Diamond would buy Nvidia's chips for their multimedia accelerator boards <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.
3.  **Content/Brand**: A partnership with Sega, a popular video game company, allowed Nvidia to use Sega's brand name for its product launch as Sega sought to port its arcade and console games to PCs <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.

Nvidia's first product, the NV1, launched in May 1995. It was a multimedia PCI card combining graphics, sound, and Sega gamepad support, aiming to converge multiple multimedia functions into one board <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>. Although technically impressive, the NV1 tried to do too much, resulting in compromises, and critically, it was not compatible with leading graphics APIs like OpenGL or 3dfx's Glide <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. The NV1 was a flop, discontinued in late 1996 <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. A planned advanced NV2 for Sega's next console also fell through <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.

### The "Change Everything" Pivot

Inspired by Samsung's Lee Kun-hee's "change everything" philosophy, Nvidia's leadership pivoted after the NV1 failure <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>. They bet on three key rising trends:

#### 1. Embracing Microsoft Direct3D
Nvidia decided to bet its future on Microsoft's Direct3D, despite its initial struggles and criticism from developers like John Carmack, who called it "horribly broken" <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>. Bill Gates himself advocated for Direct3D, promising improvements and support <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>. Nvidia believed Direct3D's tight integration with Windows would make it the dominant 3D graphics API <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.

#### 2. [[ykks_strategy_of_vertical_integration_and_market_adaptation | Vertical Integration]] of Device Driver Development
Nvidia decided to take control of writing their own device drivers for their hardware <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>. Previously, board partners (OEMs) wrote most drivers, leading to mismatched incentives as drivers are complex and critical to device experience <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>. By bringing driver development in-house, Nvidia aligned proper incentives, allowed sufficient time for quality development, and could aggregate and respond to issues from all its board partners <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>. This commitment to high-performing drivers became a cornerstone of Nvidia's future success <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.

Nvidia's second (or third) product, the Riva 128, launched in 1997 when the company had less than six weeks of cash left <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>. The Riva 128 was specifically designed to accelerate Direct3D and, critically, supported both 3D and 2D graphics – a functionality 3dfx's Voodoo lacked <a class="yt-timestamp" data-t="00:13:29">[00:13:29]</a>. It retailed for about $140 and sold well, with Diamond Multimedia reselling it as the Diamond Viper 330 <a class="yt-timestamp" data-t="00:13:47">[00:13:47]</a>.

#### 3. Outsourcing Manufacturing to TSMC (Betting on Moore's Law)
To maintain a relentless pace and keep up with competition, Nvidia ended its partnership with SGS Thompson in 1998 and formed a new one with Taiwan Semiconductor Manufacturing Company (TSMC) <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>. Nvidia management was concerned that SGS Thompson, being a manufacturer, ultimately had opposing interests <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>. TSMC, on the other hand, advocated for its partners by pledging never to compete with them, aligning their success with their partners' increased chip sales <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>.

This partnership allowed Nvidia to focus entirely on design, optimizing for speed and rapid iteration <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>. Nvidia organized its teams into three groups: one for the upcoming design, one for a refresh of last year's design, and one for next year's design <a class="yt-timestamp" data-t="00:16:02">[00:16:02]</a>. They adopted advanced chip design processes, including computer-aided design, verification, and validation, with extensive simulations to prevent costly bugs <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>. The result was a relentless six-month product cycle, delivering a new chip generation every half-year <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>. This brutal pace ground down most competitors, leaving only ATI able to keep up its own release cycle <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>.

## 3dfx's Misguided [[ykks_strategy_of_vertical_integration_and_market_adaptation | Vertical Integration]]

Despite holding the market lead in 1998 with their Voodoo graphics set, 3dfx struggled to produce a proper 3D/2D follow-up <a class="yt-timestamp" data-t="00:17:11">[00:17:11]</a>. Their first attempt, the Rush chipset (mid-1997), performed poorly <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>. It took over a year to release the competitive Banshee in September 1998, delaying their entire product lineup <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>. Their 3D-only Voodoo 2 still sold well, maintaining a third of the high-end market <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>.

However, 3dfx made a massive misstep by attempting their own [[ykks_strategy_of_vertical_integration_and_market_adaptation | vertical integration]] expansion into manufacturing and direct sales <a class="yt-timestamp" data-t="00:18:05">[00:18:05]</a>. In December 1998, 3dfx acquired boardmaker STB for $141 million and announced that their chips would only be available in their own name-branded boards <a class="yt-timestamp" data-t="00:18:34">[00:18:34]</a>. This directly competed with their old customers (board partners), many of whom defected to Nvidia <a class="yt-timestamp" data-t="00:18:45">[00:18:45]</a>. 3dfx's management had no prior manufacturing experience, and STB's Mexico-based facilities could not compete with Asian manufacturers <a class="yt-timestamp" data-t="00:18:54">[00:18:54]</a>. The manufacturing division became a cash burn, and 3dfx eventually dissolved, selling its assets to Nvidia in 2000 <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>.

## Intel's Entry and Market Consolidation

Intel, the industry's dominant force at the time, predicted in 1996 that 80% of PCs would have 3D graphics by the end of the millennium and that they would dominate the space by 1998 <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>. This prediction even led Microsoft to cancel its own line of graphics hardware <a class="yt-timestamp" data-t="00:19:24">[00:19:24]</a>.

Intel released the Intel 740 card in 1998, but it did not sell well <a class="yt-timestamp" data-t="00:19:29">[00:19:29]</a>. It used the AGP port format, which Intel was trying to popularize, while most of the market stuck with the PCI standard <a class="yt-timestamp" data-t="00:19:36">[00:19:36]</a>. Although the card performed well in speed tests, real-world performance lagged <a class="yt-timestamp" data-t="00:19:45">[00:19:45]</a>. Intel, accustomed to a 1-2 year CPU development cycle, could not keep up with the graphics market's rapid pace <a class="yt-timestamp" data-t="00:19:55">[00:19:55]</a>.

While the Intel 740 was discontinued, Intel continued to develop integrated graphics processors (IGPs) <a class="yt-timestamp" data-t="00:20:07">[00:20:07]</a>. By leveraging its CPU monopoly, Intel built massive market share in IGPs, which use a portion of system memory instead of dedicated memory <a class="yt-timestamp" data-t="00:20:16">[00:20:16]</a>. Although these IGPs were not top-of-the-line, Intel's entry effectively wiped out the market for low-margin, low-performance graphics needs, leaving the rest of the industry caught in the middle and causing them to shrink or fail <a class="yt-timestamp" data-t="00:20:34">[00:20:34]</a>.

## Conclusion

By the early 2000s, the graphics card market had drastically consolidated from over 30 companies to just three: Nvidia and ATI (a clear duopoly), with Intel dominating the low-end integrated graphics space <a class="yt-timestamp" data-t="00:20:50">[00:20:50]</a>. ATI was later acquired by AMD in 2006 for $5.6 billion <a class="yt-timestamp" data-t="00:21:05">[00:21:05]</a>.

The history of this consolidation provides a powerful lesson in [[ykks_strategy_of_vertical_integration_and_market_adaptation | vertical integration]] and business strategy. Nvidia's choice of an adjacent expansion into device drivers added significant business value and created a lasting competitive edge <a class="yt-timestamp" data-t="00:21:27">[00:21:27]</a>. In contrast, 3dfx's expansion into manufacturing and direct sales destroyed value, burned cash, and alienated key customers <a class="yt-timestamp" data-t="00:21:44">[00:21:44]</a>.

Nvidia has since looked beyond just graphics chipsets, coining the phrase "general processing unit" (GPU) in 1999 <a class="yt-timestamp" data-t="00:21:56">[00:21:56]</a>. They began popularizing the concept of general-purpose computing, envisioning new applications beyond video game graphics, a vision that would materialize in the years to follow <a class="yt-timestamp" data-t="00:22:04">[00:22:04]</a>.