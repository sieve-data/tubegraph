---
title: The spread and influence of Unix in academia and industry
videoId: HADp3emVABg
---

From: [[asianometry]] <br/> 

The creation and emergence of the operating system Unix was a pivotal moment in technology history <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This article explores [[the_origins_and_development_of_unix | the rise and fragmentation of Unix]] <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

## Beginnings

In 1965, scientists at Bell Labs, MIT, and General Electric collaborated on "Multiplexed Information and Computing Service," or Multics <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. This project aimed to create a general-purpose utility for time-sharing on computer systems <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. Since computers were extremely expensive, time-sharing operating systems allowed multiple users to efficiently share resources <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. Multics experimented with concepts like arbitrary file names, directory structures, and a virtual memory system, which allowed secondary storage to function as main memory <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. This was a significant improvement over existing file systems and remains in use today <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

However, Multics became too ambitious, leading Bell Labs to withdraw in 1969 due to a lack of a workable product <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. Despite this, scientists Ken Thompson, Dennis Ritchie, Rudd Canaday, Doug McIlroy, and J.F. Ossanna at the Bell Labs Computing Science Research Center continued their work <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. After losing access to the GE 635 computer, Ken Thompson rewrote his game "Space Travel" for an unused PDP-7 minicomputer in 1969 <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>. This led him to implement a new file system, along with utilities for copying, printing, deleting, and editing files, and a simple command interpreter (shell) <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

The concept of the "file" coalesced as an interface for data operations, abstracting away hardware differences <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. By the end of summer 1969, the system was a separate entity from the original GECOS operating system <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. In 1970, team member Brian Kernighan suggested the name "Unics," which eventually became "Unix" <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.

Unix was rewritten for the DEC PDP-11, a newer, more affordable minicomputer <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>. The request for the PDP-11 was approved because it had a compelling use case: creating and editing text files <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>. Unix, now with a text editor and the typesetting markup language "roff," was adopted by the Bell Labs Patent Department due to its ability to handle line-numbered pages <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. It quickly grew from supporting three typists to becoming a popular homegrown product across Bell Labs <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.

## Why Unix Spread

Unix was initially intended as an internal Bell Labs tool, but its popularity quickly spread <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a> due to several key factors:

1.  **Cost-Effectiveness**: Unix ran on relatively humble hardware, such as the PDP-11/40, which cost $50,000-$150,000 in 1977 dollars <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>. This was significantly cheaper than mainframes, which could cost half a million dollars or more <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
2.  **Portability and Modifiability**: Unix was the first operating system written in a higher-level programming language, "C" <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>. Dennis Ritchie produced "C" from "B," which Ken Thompson created by porting BCPL <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. Programming in C was much easier than in assembly language, making Unix easy to port to different hardware architectures and simpler to modify and enhance <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
3.  **Low Acquisition Cost**: [[the_role_of_att_consent_decree_in_unixs_distribution | Unix did not cost an arm and a leg to acquire]] <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. AT&T and Bell Labs sold the Unix source code to non-profits like universities for only a few hundred dollars <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. Unlike other software companies that zealously guarded their source code, Unix allowed users to see and modify the code <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.

### The [[the_role_of_att_consent_decree_in_unixs_distribution | AT&T Consent Decree]]

This open distribution was not out of generosity, but a result of [[the_role_of_att_consent_decree_in_unixs_distribution | the 1956 AT&T Consent Decree]] <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. This anti-trust settlement mandated that in exchange for a legal monopoly on the US telephone system, AT&T had to make its inventions available to the academic community for free or under fair terms <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>. The decree also barred AT&T from entering the computer business, rendering Unix commercially useless for them <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. This decree had previously facilitated the spread of the transistor and now did the same for Unix <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.

AT&T managers, wary of violating the decree, shied away from providing support to licensees <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>. This unintentionally encouraged university students to collaborate and implement desired features themselves <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. By the early 1970s, Unix had spread worldwide to universities in Australia, the United Kingdom, Belgium, and the Netherlands <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.

## Berkeley Unix

In November 1973, Ken Thompson and Dennis Ritchie presented the first Unix paper at Purdue University <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. UC Berkeley Professor Bob Fabry obtained a copy, leading several departments to pool resources for a PDP minicomputer <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>. Ken Thompson himself joined Berkeley as a visiting professor in 1975 to help install Unix Version 6 <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.

Students Chuck Haley and Bill Joy became instrumental, finishing Thompson's Pascal implementation, which allowed Unix to support this higher-level language <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>. They also added utilities, including the "ex" (EXtended) text editor, which later became "vim" <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>. The Berkeley variant's Pascal compiler was widely admired for its excellent error handling <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>.

In early 1977, Bill Joy compiled 30 copies of what he called the "Berkeley Software Distribution" or BSD and sent them out for about $50 per tape <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>. A second version, 2BSD, quickly followed <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.

When DEC introduced the VAX-11/780, a 32-bit computer, AT&T's UNIX/32V didn't support its virtual memory capabilities <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>. In a game-changing move, Bill Joy and Ozalp Babaoglu added this virtual memory feature, shipping it in December 1979 as 3BSD <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>. This solidified Berkeley's position as a coordinating gateway for leading-edge Unix releases <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.

### DARPA & the Internet

BSD took a significant leap thanks to DARPA. In 1979, DARPA sought to consolidate its disparate software into a single "universal computing environment" <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>. They chose Unix due to its capable handling of different hardware <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>. In 1980, Fabry received a DARPA contract to add features to 3BSD <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>. He and Bill Joy established the Computer Systems Research Group (CSRG) to coordinate global volunteer contributors on the 4BSD or BSD Unix series <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>.

This new Unix had to support DARPA's protocols, including those for the Internet <a class="yt-timestamp" data-t="00:13:29">[00:13:29]</a>. Notably, 4.2BSD fully supported the [[technological_innovations_and_contributions_by_sun_microsystems | Internet protocol stack TCP/IP]], playing a significant role in popularizing the Internet <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>. 4.2BSD was extremely popular, with over a thousand licenses issued within a month of its April 1983 release, surpassing all previous distributions combined <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>.

## From Hobby to Industry

In summer 1982, Bill Joy announced his departure from CSRG to [[history_and_formation_of_sun_microsystems | co-found Sun Microsystems]] <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>. While his work at BSD was financially rewarding, he felt the academic environment at Berkeley constrained growth, stating it "needed to be a commercial activity" <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>.

[[impact_of_sun_microsystems_on_silicon_valley_and_the_tech_industry | Sun Microsystems]] became famous for pioneering and popularizing the workstation computer <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>. These workstations included Unix OS with scientific/engineering applications, the Motorola 68000 microprocessor, and other off-the-shelf hardware <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>. Sun later developed its own closed-source Unix variant, SunOS, branched from 4.2BSD <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>. While a single Sun workstation couldn't match a mainframe, they were designed to be networked, making them immensely valuable <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>. [[impact_of_sun_microsystems_on_silicon_valley_and_the_tech_industry | Sun Microsystems]] reaped significant benefits, becoming one of the fastest-growing companies in Silicon Valley <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.

[[the_commercialization_and_variants_of_unix | Sun was not the only company to commercialize Unix]] <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>. Other notable Unix-based startups included:
*   **Mt. Xinu**: A Berkeley-based software company that sold a commercially licensed version of BSD for the DEC Vax minicomputer <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>.
*   **Santa Cruz Operation**: Sold Unix variants for x86 computers <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>.
*   **Onyx Systems**: Marketed a Unix variant for Zilog-based Personal Computers <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>.
*   **Microsoft**: Developed Xenix, a Unix variant for 16-bit microcomputers <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>.
*   **NeXT**: Steve Jobs' workstation computer startup, founded in 1985, whose operating system NeXTSTEP was derived from 4.3BSD Tahoe <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.

## Conclusion

Unix pioneered powerful concepts that helped transform software into the powerhouse industry it is today <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>. Its early development was driven by individuals interested in technology rather than profit <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>. However, as the Unix community grew and its potential became evident, the work surrounding Unix transitioned into a commercial activity <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>. By 1983, Unix's formative years concluded, setting the stage for the intense competition known as the "Unix Wars" <a class="yt-timestamp" data-t="00:16:31">[00:16:31]</a>.