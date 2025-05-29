---
title: The commercialization and variants of Unix
videoId: HADp3emVABg
---

From: [[asianometry]] <br/> 

Initially, the system later known as Unix was simply a convenient platform for developing software, not primarily intended for commercial gain <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. Its early development and foundations were driven by interest rather than profit <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>.

## Early Spread and Influence

Unix, though intended as an internal tool for Bell Labs, quickly spread throughout the computing communities <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>. Its unexpected popularity stemmed from several factors:
*   **Hardware Accessibility**: Unix was born on relatively humble hardware, like the PDP-11/40, which cost approximately $50,000-$150,000 in 1977, significantly cheaper than mainframes that could cost at least half a million dollars <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
*   **Written in C**: It was the first operating system written in a higher-level programming language, "C," making it easier to port to different hardware architectures, modify, and enhance <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.
*   **Low Acquisition Cost**: Most importantly, Unix did not cost much to acquire. AT&T and Bell Labs sold the Unix source code to non-profits like universities for just a few hundred dollars <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.

This distribution model was largely influenced by the [[the_role_of_att_consent_decree_in_unixs_distribution | 1956 AT&T Consent Decree]], an anti-trust settlement with the US government <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>. This decree mandated that AT&T make its inventions available to the academic community at no charge or license them under fair terms <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>. It also barred AT&T from entering the computer business, rendering Unix not commercially useful for them <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. This unique situation encouraged university students to collaborate and implement desired features due to the lack of official support from AT&T <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. By the early 1970s, Unix had spread globally to universities in Australia, the United Kingdom, Belgium, and the Netherlands <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.

## Berkeley Unix (BSD)

In November 1973, Ken Thompson and Dennis Ritchie presented the first Unix paper, which UC Berkeley Professor Bob Fabry obtained <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. Ken Thompson later joined Berkeley as a visiting professor in 1975 to help install Unix Version 6 on a newly acquired PDP 11/70 minicomputer <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.

Two students, Chuck Haley and Bill Joy, significantly contributed to this Unix variant <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>. They finished a Pascal implementation with excellent error handling and added utilities, including the "ex" text editor, which later evolved into "vim" <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>. Due to the quality of their Pascal compiler, requests for the Berkeley Unix variant grew <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

In early 1977, Bill Joy compiled and distributed 30 copies of the "Berkeley Software Distribution" (BSD) for about $50 per tape <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>. This proved popular, leading to the "Second Berkeley Software Distribution" (2BSD) <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.

A major advancement came in 1978 when DEC introduced the VAX-11/780, a 32-bit computer <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>. Although AT&T released UNIX/32V for it, it lacked support for the VAX's virtual memory capabilities <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>. In December 1979, Bill Joy and Ozalp Babaoglu added virtual memory support, releasing it as 3BSD <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>. This solidified Berkeley's role in coordinating cutting-edge Unix releases <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.

BSD made another significant leap when DARPA chose Unix as its "universal computing environment" to share software across the organization, due to its capability in handling different hardware <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>. In 1980, DARPA contracted Berkeley to add features to 3BSD <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>. This led to the formation of the Computer Systems Research Group (CSRG) and the development of the 4BSD series <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>. Notably, 4.2BSD fully supported the Internet protocol stack TCP/IP, playing a significant role in popularizing the Internet <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>. 4.2BSD was highly popular, with over a thousand licenses issued within a month of its April 1983 release <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>.

## From Hobby to Industry: Commercialization of Unix

The growing potential of Unix indicated a shift towards commercial activity <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>. In the summer of 1982, Bill Joy left the CSRG to co-found [[history_and_formation_of_sun_microsystems | Sun Microsystems]], stating that the academic atmosphere constrained growth and that the work "needed to be a commercial activity" <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.

[[technological_innovations_and_contributions_by_sun_microsystems | Sun Microsystems]] became famous for pioneering and popularizing the workstation computer, which included the Unix OS, scientific/engineering applications, the Motorola 68000 microprocessor, and other off-the-shelf hardware <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>. They developed their own closed-source Unix variant, SunOS, branched from the 4.2BSD version <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>. Sun workstations, while individually less powerful than mainframes, became immensely valuable when networked <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>, leading [[sun_microsystems_business_model_and_initial_success | Sun Microsystems]] to become one of the fastest-growing companies in Silicon Valley <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>.

### Notable Unix Variants and Commercial Ventures:
*   **Mt. Xinu**: A Berkeley-based software company that sold a commercially licensed version of BSD for the DEC Vax minicomputer <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>.
*   **Santa Cruz Operation (SCO)**: Sold Unix variants for x86 computers <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>.
*   **Onyx Systems**: Marketed a Unix variant for Zilog-based Personal Computers <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>.
*   **Microsoft Xenix**: Microsoft's Unix variant for 16-bit microcomputers <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>.
*   **NeXTSTEP**: Steve Jobs' workstation computer startup, NeXT (founded 1985), developed NeXTSTEP, an operating system derived from 4.3BSD Tahoe <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.

## Conclusion

Unix pioneered powerful concepts that contributed to making software the powerhouse industry it is today <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>. By 1983, Unix had completed its awkward growth years, setting the stage for a period of intense competition known as the "Unix Wars" as various entities sought to capitalize on its burgeoning market <a class="yt-timestamp" data-t="00:16:31">[00:16:31]</a>.