---
title: Using ICE for connectivity in WebRTC
videoId: WmR9IMUD_CY
---

From: [[fireship]] <br/> 

[[introduction_to_webrtc | WebRTC]] enables the exchange of real-time audio and video streams entirely within the browser, establishing a [[building_a_peertopeer_video_chat_app | peer-to-peer connection]] without the need for a third-party server or native application for media transmission <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>, <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>. However, connecting peers directly can be challenging due to common networking obstacles <a class="yt-timestamp" data-t="01:10:04">[01:10:04]</a>.

## The Challenge of Peer-to-Peer Connectivity

Most devices in the real world operate behind firewalls, and their IP addresses frequently change due to Network Address Translation (NAT) <a class="yt-timestamp" data-t="01:01:82">[01:01:82]</a>. This dynamic environment complicates establishing direct [[building_a_peertopeer_video_chat_app | peer-to-peer connections]] <a class="yt-timestamp" data-t="01:07:05">[01:07:05]</a>.

## Interactive Connectivity Establishment (ICE)

To overcome these challenges, a standard called Interactive Connectivity Establishment (ICE) assists clients in coordinating the discovery of their public-facing IP addresses <a class="yt-timestamp" data-t="01:13:30">[01:13:30]</a>.

### ICE Candidates

Both peers involved in a [[building_a_peertopeer_video_chat_app | peer-to-peer connection]] generate a list of ICE candidates <a class="yt-timestamp" data-t="01:23:71">[01:23:71]</a>. Each ICE candidate contains a potential IP address and port pair that one peer can use to connect to another <a class="yt-timestamp" data-t="01:26:01">[01:26:01]</a>, <a class="yt-timestamp" data-t="08:19:15">[08:19:15]</a>.

### Role of STUN Servers

[[introduction_to_webrtc | WebRTC]] generates ICE candidates by making a series of requests to a STUN (Session Traversal Utilities for NAT) server <a class="yt-timestamp" data-t="01:31:71">[01:31:71]</a>, <a class="yt-timestamp" data-t="04:58:14">[04:58:14]</a>. STUN servers are readily available for free from reliable sources like Google, so there is no need to set one up independently <a class="yt-timestamp" data-t="01:36:58">[01:36:58]</a>, <a class="yt-timestamp" data-t="05:04:15">[05:04:15]</a>.

## Exchanging ICE Candidates During Signaling

During the [[signaling_process_and_stp_in_webrtc | signaling process]], ICE candidates are saved in a database (such as Firestore when [[setting_up_firebase_for_signaling_in_video_chat_apps | Firebase]] is used as a signaling server) where they can be read by the other peer <a class="yt-timestamp" data-t="01:43:08">[01:43:08]</a>, <a class="yt-timestamp" data-t="03:08:42">[03:08:42]</a>.

The `RTCPeerConnection` object automatically begins generating ICE candidates when its local description is set <a class="yt-timestamp" data-t="08:13:21">[08:13:21]</a>. It's crucial to establish a listener for the `onicecandidate` event *before* making this call <a class="yt-timestamp" data-t="08:26:15">[08:26:15]</a>. When an ICE candidate event is fired, the candidate data is written to the appropriate collection (e.g., `offerCandidates` or `answerCandidates`) in the database <a class="yt-timestamp" data-t="08:34:64">[08:34:64]</a>, <a class="yt-timestamp" data-t="10:05:85">[10:05:85]</a>.

The [[signaling_process_and_stp_in_webrtc | signaling server]] allows the two parties to securely exchange this connection data, but it never touches the actual media transmitted between the peers <a class="yt-timestamp" data-t="00:53:23">[00:53:23]</a>.

Once ICE candidates are exchanged, an algorithm automatically determines the best candidate, enabling real-time media flow between the peers <a class="yt-timestamp" data-t="01:48:07">[01:48:07]</a>, <a class="yt-timestamp" data-t="03:27:07">[03:27:07]</a>.

### WebRTC's Background Handling

The [[introduction_to_webrtc | WebRTC]] API handles the complex [[building_a_peertopeer_video_chat_app | peer-to-peer networking]] and media streaming in the background, making it appear "magical" to the developer <a class="yt-timestamp" data-t="02:07:95">[02:07:95]</a>, <a class="yt-timestamp" data-t="10:59:00">[10:59:00]</a>. The majority of the development work involves simply [[signaling_process_and_stp_in_webrtc | signaling]] the necessary data, including ICE candidates, between the two users <a class="yt-timestamp" data-t="10:55:00">[10:55:00]</a>.