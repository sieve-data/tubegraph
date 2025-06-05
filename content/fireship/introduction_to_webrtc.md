---
title: Introduction to WebRTC
videoId: WmR9IMUD_CY
---

From: [[fireship]] <br/> 

WebRTC enables the exchange of real-time audio and video streams entirely within a web browser <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It is an API that allows for establishing a peer-to-peer connection between two or more browsers <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. This means audio and video media can be exchanged directly without the need for a third-party server or native application <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## How WebRTC Works: The Signaling Process

The initial setup of a WebRTC connection involves a process called [[signaling_process_and_stp_in_webrtc | signaling]] <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. This process facilitates the secure exchange of connection data between peers, but the signaling server itself never touches the actual media transmitted <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

The steps involved in [[signaling_process_and_stp_in_webrtc | signaling]] are:
1.  **Offer Creation**: The first peer creates an "offer" to connect <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. This generates an [[signaling_process_and_stp_in_webrtc | Session Description Protocol (SDP)]] object <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. The [[signaling_process_and_stp_in_webrtc | SDP]] contains information about the peer-to-peer connection, such as video codecs and timing <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. This data is saved on a server <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
2.  **Answer Creation**: A second peer reads the offer from the server and creates an [[signaling_process_and_stp_in_webrtc | SDP]] "answer" <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. This answer is then written back to the same server <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

## How WebRTC Works: Connectivity (ICE)

Establishing a direct peer-to-peer connection can be complex due to real-world networking challenges like firewalls and constantly changing IP addresses from Network Address Translation (NAT) <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. To overcome this, WebRTC uses a standard called [[using_ice_for_connectivity_in_webrtc | Interactive Connectivity Establishment (ICE)]] <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

Key components of [[using_ice_for_connectivity_in_webrtc | ICE]]:
*   **[[using_ice_for_connectivity_in_webrtc | ICE Candidates]]**: Both peers generate a list of [[using_ice_for_connectivity_in_webrtc | ICE candidates]], which are potential IP address and port pairs that another peer can use to connect <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.
*   **STUN Server**: WebRTC generates these candidates by making requests to a STUN (Session Traversal Utilities for NAT) server <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. STUN servers help clients discover their public-facing IP addresses <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. Many free STUN server options are available from reliable sources like Google <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
*   **Candidate Exchange**: Each peer saves their [[using_ice_for_connectivity_in_webrtc | ICE candidates]] in a database, which the other peer can read <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. An algorithm then automatically determines the best candidate for the connection <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>, allowing real-time media to flow between the peers <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

## Implementing WebRTC in Practice

A peer-to-peer video calling application can be built from scratch using [[building_a_peertopeer_video_chat_app | vanilla JavaScript]] and [[setting_up_firebase_for_signaling_in_video_chat_apps | Firebase]] as the [[signaling_process_and_stp_in_webrtc | signaling]] server <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>. [[setting_up_firebase_for_signaling_in_video_chat_apps | Firebase]] is well-suited for a [[signaling_process_and_stp_in_webrtc | signaling]] server because it allows real-time listening for database updates <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

### Key API and State Management
*   **`RTCPeerConnection`**: This JavaScript object is central to WebRTC, handling the negotiation process <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a> and emitting events for database updates and media stream management <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. It also generates the [[using_ice_for_connectivity_in_webrtc | ICE candidates]] <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>, for which it requires configuring STUN servers <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
*   **Streams**: `localStream` and `remoteStream` objects represent the video streams from the webcams of each user <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

### Core Implementation Steps

1.  **Accessing Webcam**:
    *   Obtain a stream from the user's webcam using `navigator.mediaDevices.getUserMedia` <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>, setting `video` and `audio` to `true` <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. This prompts the user for permission <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
    *   Once the `MediaStream` object is resolved, populate video elements in the DOM by setting `videoElement.srcObject` to the stream <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.

2.  **Managing Streams with `RTCPeerConnection`**:
    *   Add tracks from the `localStream` to the `RTCPeerConnection` using `peerConnection.addTrack` <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.
    *   Listen for incoming tracks on the `RTCPeerConnection` by setting up an `onTrack` event handler <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. When a remote track comes in, add it to the `remoteStream` <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

3.  **Signaling with Firestore (Caller's Perspective)**:
    *   **Create Call Document**: A "call" document in Firestore is created to manage offer and answer details, along with sub-collections for "offer candidates" and "answer candidates" <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. Firestore can generate a unique ID for this document <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.
    *   **Generate Offer**: Await `peerConnection.createOffer()` to get an offer description <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.
    *   **Set Local Description**: Set the generated offer as the `localDescription` on the `peerConnection` <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.
    *   **Save Offer to Database**: Convert the [[signaling_process_and_stp_in_webrtc | SDP]] value from the offer description to a plain JavaScript object and write it to the call document in Firestore <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
    *   **Listen for [[using_ice_for_connectivity_in_webrtc | ICE Candidates]] (Local)**: Set up a listener for the `onicecandidate` event on the `peerConnection` *before* setting the local description <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>. When a candidate is generated, write its data to the "offer candidates" collection <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.
    *   **Listen for Answer (Remote)**: Use Firestore's `onSnapshot` method on the call document to listen for real-time changes <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>. If an answer is received and the `peerConnection` doesn't have a `currentRemoteDescription`, set the received answer as the `remoteDescription` <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
    *   **Listen for [[using_ice_for_connectivity_in_webrtc | ICE Candidates]] (Remote)**: Listen to updates on the "answer candidates" sub-collection <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. When a new document is added, create an `RTCIceCandidate` and add it to the `peerConnection` <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.

4.  **Signaling with Firestore (Answerer's Perspective)**:
    *   **Reference Call Document**: The answerer references the call document in Firestore using the unique ID created by the caller <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.
    *   **Listen for [[using_ice_for_connectivity_in_webrtc | ICE Candidates]] (Local)**: Set up the `onicecandidate` event listener to update the "answer candidates" collection whenever a new candidate is generated <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.
    *   **Fetch Offer & Set Remote Description**: Fetch the call document's data to get the offer, then use it to set the `remoteDescription` on the `peerConnection` <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.
    *   **Generate Answer & Set Local Description**: Generate an answer locally <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a> and set it as the `localDescription` <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.
    *   **Update Answer in Database**: Convert the answer to a plain object and update it on the call document in Firestore for the caller to listen to <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>.
    *   **Listen for [[using_ice_for_connectivity_in_webrtc | ICE Candidates]] (Remote)**: Set up a listener on the "offer candidates" collection. When a new candidate is added, create an `RTCIceCandidate` and add it to the `peerConnection` <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.

WebRTC abstracts the complicated peer-to-peer networking and media streaming complexities <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>, making the vast majority of the development work revolve around [[signaling_process_and_stp_in_webrtc | signaling]] data between users <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.