---
title: Snapshotting in AI sandboxes
videoId: wsFd22SL1s8
---

From: [[aidotengineer]] <br/> 

Snapshotting in AI sandboxes is a crucial capability that allows AI agents to save their progress and revert to previous states, significantly enhancing reliability and efficiency in complex workflows <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. Arachis, an open-source sandboxing service for AI agents, offers out-of-the-box support for this feature <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

## Motivation for Snapshotting
AI agents frequently encounter failures when tackling large, multi-step tasks, such as creating complex applications <a class="yt-timestamp" data-t="00:32:39">[00:32:39]</a>. Even with detailed, step-by-step plans, multi-stage processes can fail, especially late in a deep execution flow <a class="yt-timestamp" data-t="00:32:59">[00:32:59]</a>.
Instead of restarting from scratch after a failure, agents need the ability to:
*   Backtrack to the last successful checkpoint <a class="yt-timestamp" data-t="00:33:10">[00:33:10]</a>.
*   Replan their approach <a class="yt-timestamp" data-t="00:33:12">[00:33:12]</a>.
*   Attempt the task again <a class="yt-timestamp" data-t="00:33:15">[00:33:15]</a>.

This capability to fail and backtrack is central to achieving more reliable, higher-order complex task execution by agents, enabling them to explore multiple paths in parallel <a class="yt-timestamp" data-t="00:33:17">[00:33:17]</a>.

## Arachis's Snapshotting Capabilities
Arachis supports snapshot and restore functionalities, allowing agents to checkpoint their progress by snapshotting the sandbox <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. If an agent fails in a multi-step flow, it can restore an old snapshot <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

The process of snapshotting involves saving the entire running state of a sandbox <a class="yt-timestamp" data-t="00:33:30">[00:33:30]</a>. This includes:
*   The guest memory <a class="yt-timestamp" data-t="00:33:34">[00:33:34]</a>.
*   The read-write (RW) part of the overlay file system <a class="yt-timestamp" data-t="00:33:36">[00:33:36]</a>.

Any files created by the sandbox or agent, any processes spawned, and even windows opened in the GUI will be restored exactly as they were <a class="yt-timestamp" data-t="00:33:41">[00:33:41]</a>. This offers the same semantic as closing and opening a laptop lid <a class="yt-timestamp" data-t="00:33:44">[00:33:44]</a>.

## Technical Details: How Snapshotting Works
[[MicroVMs for secure AI sandboxing | MicroVMs]], which Arachis uses as its runtime, provide a way to perform fast snapshots by simply dumping the entire guest memory <a class="yt-timestamp" data-t="00:21:43">[00:21:43]</a>. This is significantly easier than with [[Stateful Agents and AI Memory Management | containers]] or GVisor <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a>. With [[microvms_for_secure_ai_sandboxing | microVMs]], virtual memory can be allocated, dumped for snapshotting, and then restored to bring the VM back <a class="yt-timestamp" data-t="00:21:55">[00:21:55]</a>.

The snapshotting process in Arachis involves four key steps <a class="yt-timestamp" data-t="00:34:42">[00:34:42]</a>:
1.  **Pause VM:** The VM is paused by calling the `pause` API on the Virtual Machine Monitor (VMM) <a class="yt-timestamp" data-t="00:34:44">[00:34:44]</a>.
2.  **Snapshot API:** The `snapshot` API is called to dump the guest memory <a class="yt-timestamp" data-t="00:34:50">[00:34:50]</a>.
3.  **Persist Read-Write Layer:** The thin read-write overlay file system, which contains all files created by the sandbox or agent, is manually persisted out-of-band <a class="yt-timestamp" data-t="00:34:55">[00:34:55]</a>.
4.  **Resume VM:** The VMM is resumed, allowing the sandbox to continue its operations <a class="yt-timestamp" data-t="00:35:08">[00:35:08]</a>.

Snapshotting is designed to be very fast, taking single-digit seconds, with continuous improvements aimed at reducing this time <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

### File System Management
Arachis utilizes an overlay file system for storage, where a shared base layer (root FS) is protected and shared across sandboxes <a class="yt-timestamp" data-t="00:25:03">[00:25:03]</a>. Each sandbox receives its own read-write layer where new files are created <a class="yt-timestamp" data-t="00:25:14">[00:25:14]</a>. When a snapshot is taken, only this read-write layer is persisted, ensuring efficient storage and sharing <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>.

## API Usage
Arachis provides a simple REST-based API that includes a `snapshots` resource <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>. This allows for easy snapshotting and restoration of VMs <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

Using the Python SDK, snapshotting is a straightforward process <a class="yt-timestamp" data-t="00:35:54">[00:35:54]</a>:
1.  Initialize the sandbox manager with the Arachis host IP <a class="yt-timestamp" data-t="00:36:01">[00:36:01]</a>.
2.  Start a sandbox using `start_sandbox` <a class="yt-timestamp" data-t="00:36:17">[00:36:17]</a>.
3.  Execute commands and observe output <a class="yt-timestamp" data-t="00:36:19">[00:36:19]</a>.
4.  Call `snapshot` with a `snapshot_id` to save the state <a class="yt-timestamp" data-t="00:36:26">[00:36:26]</a>.
5.  To restore, call `restore` with the VM name and the saved `snapshot_id` <a class="yt-timestamp" data-t="00:36:38">[00:36:38]</a>.

## Demo Example
A demonstration showcased Claude Desktop creating a Google Docs clone using Arachis <a class="yt-timestamp" data-t="00:37:04">[00:37:04]</a>. The process included:
1.  Creating the Google Docs clone within the [[building_ai_sandboxes_from_scratch | Linux sandbox]] <a class="yt-timestamp" data-t="00:37:46">[00:37:46]</a>.
2.  Taking a snapshot of this initial version <a class="yt-timestamp" data-t="00:37:51">[00:37:51]</a>.
3.  Adding a new feature, dark mode, to the clone <a class="yt-timestamp" data-t="00:37:58">[00:37:58]</a>.
4.  Restoring the old checkpoint to revert to the version without dark mode <a class="yt-timestamp" data-t="00:38:21">[00:38:21]</a>.

This demonstrated how snapshotting allows agents to backtrack and iterate on development without manual intervention or extensive prompting <a class="yt-timestamp" data-t="00:38:38">[00:38:38]</a>.

## Ongoing Work and Future Enhancements
Current and future work on Arachis regarding snapshots includes:
*   **Faster Boot Times:** Aiming for boot times under 1 second <a class="yt-timestamp" data-t="00:39:14">[00:39:14]</a>.
*   **Enhanced Persistence:** Moving to Btrfs, a file system optimized for incremental snapshots, to provide first-class support for snapshots and persistence <a class="yt-timestamp" data-t="00:39:24">[00:39:24]</a>.
*   **Dynamic Resource Management:** Implementing dynamic memory management (ballooning or hot-plugging/removal of memory at runtime) to [[scaling_ai_agents_in_production | bin-pack]] more sandboxes onto a single server <a class="yt-timestamp" data-t="00:39:35">[00:39:35]</a>.