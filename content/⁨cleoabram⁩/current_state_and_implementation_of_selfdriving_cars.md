---
title: Current state and implementation of selfdriving cars
videoId: Hr6GPYCHTfA
---

From: [[⁨cleoabram⁩]] <br/> 

Initially, there was a degree of skepticism about the arrival of self-driving cars, with predictions often pushing their availability further into the future <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. However, recent developments, particularly in San Francisco, reveal that fully driverless vehicles are already picking up passengers <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. These are not the futuristic, go-anywhere cars often envisioned in science fiction <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>, but rather represent two distinct approaches to deploying self-driving technology in the near future <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

## [[levels_of_autonomous_driving_technology | Levels of Autonomous Driving]]

The journey to full autonomy is a gradual process, not a sudden switch <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. This progression has been happening for decades <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>:

*   **Mid-1900s:** Basic cruise control introduced <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
*   **Early 2000s:** Car assistance in key moments, like emergency braking <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
*   **Later Developments:** Continuous support features like lane centering and adaptive cruise control <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.

To categorize this progression, the industry has defined [[levels_of_autonomous_driving_technology | levels of self-driving-ness]] <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>:

*   **Level 0:** Momentary help <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
*   **Level 1:** More continuous support <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
*   **Level 2:** Newer systems like highway piloting, representing the current limit for most easily purchasable cars <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>, <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>. At these levels, humans remain largely in charge <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

Higher levels envision scenarios where the car takes full charge, initially in specific situations or areas <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>, and eventually anywhere, at any time <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>. While the ultimate "sci-fi" level (Level 5) is still distant and its predictions seem unreliable <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>, <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>, significant progress is being made within the current capabilities of full self-driving, albeit with constraints <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

These constraints include:
*   Training vehicles to drive in less complex situations, like highways <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
*   Operating in more complex areas, but only after being specifically trained for those locations, meaning they cannot simply be dropped into a new city <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

## Two Visions for Self-Driving Implementation

The current landscape of self-driving technology is characterized by two significant divides <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>, which define the competing visions for its near future:

### Divide 1: Where to Use Them?

*   **Less Complex Situations, Anywhere:** Focusing on environments like highways, where the driving tasks are simpler and more predictable <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
*   **More Complex Situations, Geographically Constrained:** Concentrating on urban environments that are highly complex, but limiting operations to specific, pre-mapped, and thoroughly trained areas <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.

### Divide 2: Whether to Carry People?

This second divide leads to two primary implementation models for advanced self-driving systems:

#### 1. Robotaxis: Cities, with People (e.g., Cruise)

Companies like Cruise operate driverless taxi services in complex urban environments, such as San Francisco <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>, <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. Users can request a car via an app, and a vehicle arrives with no human driver inside <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

*   **Real-World [[challenges_and_considerations_in_deploying_selfdriving_vehicles | Challenges]]:**
    *   **Human-Machine Interaction:** Unexpected nuances arise when technology meets the real world <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>. For instance, passengers falling asleep in the car <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. Customer support can intervene via audio to assist <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.
    *   **Interactions with Authorities:** Humorous, yet clumsy, incidents have occurred, such as a driverless car attempting to find a safe place to pull over after an interaction with police, who initially expected a human driver <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>, <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>. The vehicle's advanced detection systems for sirens and lights work perfectly, but the human element of understanding the interaction created confusion <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.
*   **Future Robotaxi Design:** The next generation of robotaxis, like the Cruise "Origin," will remove elements meant for human drivers, such as steering wheels and brake pedals, as drivers cannot take control of these vehicles anyway <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>, <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>.

#### 2. Autonomous Trucking: Highways, No People

This vision focuses on long-distance autonomous trucking, where goods are moved without human involvement <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>, <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>. These trucks are already being used for deliveries <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.

*   **Benefits:** Autonomous trucks do not require sleep, drink, or get distracted, offering a more efficient and potentially safer method of transport <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>. Their impact is compared to the efficiency gains of an excavator over a hundred people with shovels <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.
*   **Societal Impact:** While less directly experienced by consumers, this technology could profoundly reshape global goods movement <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

## Conclusion

The [[the_future_impact_of_selfdriving_technology_on_society_and_transportation | future impact of self-driving technology]] is not just a distant sci-fi concept but is actively being shaped in the "messy middle" of current implementation <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>. These two distinct approaches—urban robotaxis and long-haul autonomous trucking—represent the near-term futures of self-driving cars that will likely change daily life in the next few years <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.

Autonomous vehicles offer the potential to mitigate the risks associated with human driving, which currently involves significant hazards <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>, <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>. They also promise to return valuable time to individuals, a profound benefit in modern life <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>. Understanding these [[levels of autonomous driving technology | levels]] and approaches provides a clearer perspective on the current state and future direction of self-driving technology <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>.