---
title: Snapshotting in AI sandboxes
videoId: wsFd22SL1s8
---

From: [[aidotengineer]] <br/> 

Snapshotting is a crucial feature in [[building_ai_sandboxes | AI sandboxes]] that enables [[stateful_ai_agents | AI agents]] to manage multi-step workflows and recover from failures <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. Arachis, an open-source code execution and computer use sandboxing service, offers out-of-the-box support for this functionality <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

## Why Snapshotting is Needed

[[Stateful AI Agents | AI agents]] often struggle with large, complex tasks, such as creating an entire application, as they may fail partway through <a class="yt-timestamp" data-t="00:32:39">[00:32:39]</a>. If a multi-stage plan fails, agents shouldn't have to restart from scratch <a class="yt-timestamp" data-t="00:33:08">[00:33:08]</a>. Snapshotting allows agents to:
*   **Checkpoint Progress** <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>
*   **Backtrack** to the last successful state <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a> <a class="yt-timestamp" data-t="00:33:10">[00:33:10]</a>
*   **Replan** and continue the workflow <a class="yt-timestamp" data-t="00:33:12">[00:33:12]</a>
This capability leads to more reliable execution of complex tasks <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. At scale, it allows agents to explore multiple paths in parallel <a class="yt-timestamp" data-t="00:33:24">[00:33:24]</a>.

## How Snapshotting Works in Arachis

Arachis leverages [[microvms_in_ai_sandboxes | microVMs]] to provide fast snapshotting capabilities <a class="yt-timestamp" data-t="00:21:43">[00:21:43]</a>.

### Key Components Saved
A snapshot saves the entire running state of an [[ai_sandbox_security | AI sandbox]] <a class="yt-timestamp" data-t="00:33:30">[00:33:30]</a>, including:
*   **Guest Memory**: This includes the state of any processes spawned or even GUI windows opened <a class="yt-timestamp" data-t="00:33:34">[00:33:34]</a> <a class="yt-timestamp" data-t="00:33:51">[00:33:51]</a>.
*   **File System**: Specifically, the read-write layer of the overlay file system, which contains any new files created by the agent <a class="yt-timestamp" data-t="00:25:33">[00:25:33]</a> <a class="yt-timestamp" data-t="00:33:36">[00:33:36]</a>. The base read-only file system layer is shared and protected <a class="yt-timestamp" data-t="00:25:24">[00:25:24]</a>.

### Technical Steps for Snapshotting
The process involves four main steps <a class="yt-timestamp" data-t="00:34:42">[00:34:42]</a>:
1.  **Pause the VM**: The virtual machine is temporarily paused <a class="yt-timestamp" data-t="00:34:44">[00:34:44]</a>.
2.  **Dump Guest Memory**: The snapshot API is called to save the entire guest memory <a class="yt-timestamp" data-t="00:34:50">[00:34:50]</a>. This is more straightforward with [[microvms_in_ai_sandboxes | microVMs]] compared to containers <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a>.
3.  **Persist Read-Write Layer**: The stateful read-write overlay file system is manually persisted <a class="yt-timestamp" data-t="00:34:57">[00:34:57]</a>.
4.  **Resume the VM**: The virtual machine is resumed, continuing its operations from where it paused <a class="yt-timestamp" data-t="00:35:08">[00:35:08]</a>.

```go
func SnapshotVM(vm_id string, snapshot_id string) error {
    // Pause the VM
    // ...
    // Make sure to resume before exiting the function
    defer vm.Resume()

    // Create a copy of the stateful disk (read-write layer of overlay FS)
    // ...

    // Call snapshot API to dump guest memory
    // ...
}
```
<a class="yt-timestamp" data-t="00:35:17">[00:35:17]</a>

### Performance
Snapshots in Arachis are very fast, currently completing in single-digit seconds, with ongoing efforts to reduce this time further <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

## Arachis API for Snapshotting
Arachis provides a simple REST-based API for managing snapshots <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.

Using the Python SDK, snapshotting is a single command <a class="yt-timestamp" data-t="00:36:26">[00:36:26]</a>:
```python
# Snapshot a VM
manager.snapshot(vm_name="my_vm", snapshot_id="snapshot_id")
```
<a class="yt-timestamp" data-t="00:36:28">[00:36:28]</a>

To restore a VM from a snapshot:
```python
# Restore a VM
manager.restore(vm_name="my_vm", snapshot_id="snapshot_id")
```
<a class="yt-timestamp" data-t="00:36:38">[00:36:38]</a>

## Demonstration
In a demonstration, an [[ai_sandbox_security | AI sandbox]] was used to create a Google Docs clone <a class="yt-timestamp" data-t="00:37:28">[00:37:28]</a>. A snapshot of the initial working clone was taken <a class="yt-timestamp" data-t="00:37:53">[00:37:53]</a>. A new "dark mode" feature was then added <a class="yt-timestamp" data-t="00:38:03">[00:38:03]</a>. Critically, the system allowed for a restoration to the previous snapshot, effectively reverting the changes and removing the dark mode, without having to re-create the entire application <a class="yt-timestamp" data-t="00:38:19">[00:38:19]</a> <a class="yt-timestamp" data-t="00:38:25">[00:38:25]</a>.

## Future Work
Ongoing work in Arachis aims to further enhance snapshotting and persistence <a class="yt-timestamp" data-t="00:39:24">[00:39:24]</a>. This includes moving to `butterfs`, a file system designed for incremental snapshots <a class="yt-timestamp" data-t="00:39:27">[00:39:27]</a> <a class="yt-timestamp" data-t="00:34:21">[00:34:21]</a>. Additionally, [[memory_management_in_ai | dynamic memory management]] and resource management, such as hot plugging or removing memory at runtime, are being explored to allow for more [[scaling_ai_agents_in_production | sandboxes]] to be binned on a single server <a class="yt-timestamp" data-t="00:39:40">[00:39:40]</a>.