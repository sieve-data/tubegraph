---
title: Role of Linux Kernel in Operating Systems
videoId: ShcR4Zfc6Dw
---

From: [[fireship]] <br/> 

The [[Linux kernel and its role | Linux kernel]] is a fundamental component of the [[Introduction to Linux | Linux]] operating system, analogous to the "engine in your car" <a class="yt-timestamp" data-t="07:10:43">[07:10:43]</a>. It serves as the bridge between hardware and software, managing crucial system resources <a class="yt-timestamp" data-t="01:41:26">[01:41:26]</a>.

## Origin and Purpose
On August 25, 1991, Linus Torvalds, a 21-year-old graduate student in Helsinki, announced his project for a free operating system, which he initially considered just a hobby <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. This hobby project eventually evolved into one of the most significant endeavors in computing history <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

While many operating systems were developed for profit, [[Introduction to Linux | Linux]] emerged as a revolution founded on the principle that software should be free and open <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

By the early 1990s, the GNU Project had developed many applications to replace Unix, but it lacked an essential operating system kernel <a class="yt-timestamp" data-t="01:35:10">[01:35:10]</a>. It was at this opportune time that Linus Torvalds was developing his hobby operating system, which would fulfill this missing component <a class="yt-timestamp" data-t="01:50:58">[01:50:58]</a>.

### Naming
Initially, Linus Torvalds intended to name his project "FreeAX" because "Linux" seemed too egotistical <a class="yt-timestamp" data-t="01:56:49">[01:56:49]</a>. However, the administrator of the FTP server where the project was hosted changed the name to "Linux" without Torvalds' consent, and the name ultimately stuck <a class="yt-timestamp" data-t="02:02:11">[02:02:11]</a>.

## Role in the Operating System
A complete operating system requires a kernel to function as an intermediary between the hardware and software layers <a class="yt-timestamp" data-t="01:41:26">[01:41:26]</a>. Its primary responsibilities include:
*   Allocating CPU resources <a class="yt-timestamp" data-t="01:41:26">[01:41:26]</a>
*   Managing memory resources <a class="yt-timestamp" data-t="01:41:26">[01:41:26]</a>
*   Enabling software applications to run <a class="yt-timestamp" data-t="01:41:26">[01:41:26]</a>

## Integration with GNU and the Birth of [[Linux System Architecture and Components | GNU/Linux]]
Initially, the [[Linux kernel and its role | Linux kernel]] was released under a proprietary license with restrictions on commercial use <a class="yt-timestamp" data-t="02:08:43">[02:08:43]</a>. However, by the end of 1992, it was re-released under the GNU General Public License (GPL) <a class="yt-timestamp" data-t="02:14:04">[02:14:04]</a>. This change allowed for the creation of a complete operating system known today as [[Linux System Architecture and Components | GNU/Linux]], combining the [[Linux kernel and its role | Linux kernel]] with the tools developed by the GNU Project <a class="yt-timestamp" data-t="02:18:43">[02:18:43]</a>.

## Impact on [[Linux Distributions and their Origins | Linux Distributions]]
The [[Linux kernel and its role | Linux kernel]]'s open nature offered developers the freedom to build custom operating systems that resembled Unix but without the legal entanglements associated with Unix's proprietary code <a class="yt-timestamp" data-t="02:29:43">[02:29:43]</a>. This flexibility led to the proliferation of [[Linux Distributions and their Origins | Linux distributions]] (distros) <a class="yt-timestamp" data-t="02:37:55">[02:37:55]</a>.

A [[Linux Distributions and their Origins | Linux distro]] is a complete operating system built upon the [[Linux kernel and its role | Linux kernel]], typically including various packages, libraries, a package manager, and potentially a graphical user interface (GUI) system <a class="yt-timestamp" data-t="02:46:27">[02:46:27]</a>. Today, there are nearly a thousand different [[Linux Distributions and their Origins | Linux distros]], each customized for specific purposes, user types, or device categories <a class="yt-timestamp" data-t="03:09:07">[03:09:07]</a>.

As a free "engine," the [[Linux kernel and its role | Linux kernel]] empowers developers to create diverse systems, fostering innovation within the open-source ecosystem <a class="yt-timestamp" data-t="07:23:25">[07:23:25]</a>. This philosophy is considered the "free market at its finest" by its proponents <a class="yt-timestamp" data-t="07:39:15">[07:39:15]</a>. Even Microsoft now fully supports [[Introduction to Linux | Linux]] through its WSL (Windows Subsystem for Linux) project <a class="yt-timestamp" data-t="07:42:07">[07:42:07]</a>.

### Creation of Git
In 2005, the source code for [[Introduction to Linux | Linux]] was managed using BitKeeper, a proprietary version control system <a class="yt-timestamp" data-t="08:01:03">[08:01:03]</a>. Due to controversies surrounding its proprietary nature, Linus Torvalds developed Git, a distributed version control system, to manage the [[Linux kernel and its role | Linux kernel]]'s source code <a class="yt-timestamp" data-t="08:06:01">[08:06:01]</a>.