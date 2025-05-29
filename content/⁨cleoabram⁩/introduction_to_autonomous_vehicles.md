---
title: Introduction to autonomous vehicles
videoId: Hr6GPYCHTfA
---

From: [[⁨cleoabram⁩]] <br/> 

Autonomous vehicles, commonly known as self-driving cars, are an advanced form of transportation technology that can operate without human input. While many anticipate a futuristic, fully autonomous vehicle capable of driving anywhere at any time, the [[current_state_and_implementation_of_selfdriving_cars | current state of implementation]] is more nuanced and involves a "messy middle" of development and deployment <a class="yt-timestamp" data-t="02:31:00">[02:31:00]</a> <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>.

## Current State of Driverless Technology

Contrary to previous predictions that self-driving cars were always "a few years away," driverless taxis are already operational and picking up people in cities like San Francisco <a class="yt-timestamp" data-t="00:35:00">[00:35:00]</a> <a class="yt-timestamp" data-t="01:29:00">[01:29:00]</a> <a class="yt-timestamp" data-t="04:05:00">[04:05:00]</a>. These vehicles, such as those operated by Cruise, function as "robotaxis" where users can request a ride and find nobody inside the car upon arrival <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a> <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a> <a class="yt-timestamp" data-t="01:26:00">[01:26:00]</a>.

## Evolution and [[levels_of_autonomous_driving_technology | Levels of Autonomous Driving Technology]]

The journey towards full autonomy is a long road with gradual advancements <a class="yt-timestamp" data-t="02:31:00">[02:31:00]</a>. This progression can be categorized into various [[levels_of_autonomous_driving_technology | levels of self-driving-ness]]:

*   **Level 0: Momentary help** <a class="yt-timestamp" data-t="03:12:00">[03:12:00]</a> – Examples include basic cruise control from the mid-1900s <a class="yt-timestamp" data-t="02:38:00">[02:38:00]</a>.
*   **Level 1: More continuous support** <a class="yt-timestamp" data-t="03:15:00">[03:15:00]</a> – Such as emergency braking in the early 2000s <a class="yt-timestamp" data-t="02:43:00">[02:43:00]</a>.
*   **Level 2: Highway piloting systems** <a class="yt-timestamp" data-t="03:18:00">[03:18:00]</a> – This level includes continuous support like lane centering or adaptive cruise control, which matches the speed of the car in front <a class="yt-timestamp" data-t="02:48:00">[02:48:00]</a>. Most readily available cars today are at this limit, with humans still largely in charge <a class="yt-timestamp" data-t="03:24:00">[03:24:00]</a> <a class="yt-timestamp" data-t="03:35:00">[03:35:00]</a>.
*   **Higher Levels (3-5)**:
    *   **Level 3/4**: The idea is that the car would be fully in charge but only in certain situations or areas, with humans initially monitoring <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a> <a class="yt-timestamp" data-t="03:45:00">[03:45:00]</a>.
    *   **Level 5**: The final level envisions a car in charge anywhere, anytime, even if the passenger is asleep <a class="yt-timestamp" data-t="03:50:00">[03:50:00]</a>. While many headlines focus on reaching this "sci-fi level," it is not yet close to being achieved <a class="yt-timestamp" data-t="04:21:00">[04:21:00]</a> <a class="yt-timestamp" data-t="04:29:00">[04:29:00]</a>.

## Current Approaches and the "Messy Middle"

The current focus in the development of [[current_state_and_implementation_of_selfdriving_cars | self-driving cars]] is on full self-driving within specific constraints <a class="yt-timestamp" data-t="04:36:00">[04:36:00]</a>. Two distinct visions are competing for the future of self-driving:

1.  **Geographically Constrained, Complex Areas**: This approach involves training vehicles to operate in complex areas, but only within specific, predefined geographical zones. Cruise's robotaxis in San Francisco are an example of this <a class="yt-timestamp" data-t="05:31:00">[05:31:00]</a> <a class="yt-timestamp" data-t="05:46:00">[05:46:00]</a>.
    *   **Human-Machine Interaction**: Deploying these vehicles reveals "weird nuances between humans and machines" <a class="yt-timestamp" data-t="06:37:00">[06:37:00]</a>. This includes [[challenges_and_considerations_in_deploying_selfdriving_vehicles | challenges]] such as passengers falling asleep in the back <a class="yt-timestamp" data-t="06:50:00">[06:50:00]</a>, or humorous interactions with law enforcement where a driverless car, upon an officer walking away and turning off sirens, proceeds to find a safe place to pull over, as programmed <a class="yt-timestamp" data-t="07:19:00">[07:19:00]</a> <a class="yt-timestamp" data-t="08:06:00">[08:06:00]</a> <a class="yt-timestamp" data-t="08:16:00">[08:16:00]</a>. These are learning experiences that arise when technology meets the real world <a class="yt-timestamp" data-t="07:10:00">[07:10:00]</a> <a class="yt-timestamp" data-t="08:21:00">[08:21:00]</a>.
    *   **Future Designs**: Companies like Cruise are developing future vehicles, such as the "Origin," which will remove elements like steering wheels and brake pedals that are unnecessary without a human driver <a class="yt-timestamp" data-t="10:01:00">[10:01:00]</a>. Currently, passengers cannot take control of these vehicles, as human interference would likely worsen the situation <a class="yt-timestamp" data-t="10:23:00">[10:23:00]</a> <a class="yt-timestamp" data-t="10:33:00">[10:33:00]</a>.

2.  **Less Complex Situations, Anywhere (Autonomous Trucking)**: This approach focuses on deploying self-driving technology in less complex driving environments, such as highways, for long-distance autonomous trucking <a class="yt-timestamp" data-t="04:44:00">[04:44:00]</a> <a class="yt-timestamp" data-t="08:42:00">[08:42:00]</a>. These trucks are already being used for deliveries <a class="yt-timestamp" data-t="09:17:00">[09:17:00]</a>.
    *   **Advantages**: Autonomous trucks offer benefits over human-driven trucks as they "don't sleep, they don't drink, they don't get distracted" <a class="yt-timestamp" data-t="09:14:00">[09:14:00]</a>. This advancement is likened to the difference between a hundred people with shovels and an excavator, fundamentally changing how goods are moved globally <a class="yt-timestamp" data-t="09:34:00">[09:34:00]</a> <a class="yt-timestamp" data-t="09:04:00">[09:04:00]</a>.

## [[the_future_impact_of_selfdriving_technology_on_society_and_transportation | Future Impact of Self-Driving Technology]]

The [[the_future_impact_of_selfdriving_technology_on_society_and_transportation | long-term impact of autonomous vehicles]] could be profound, with future generations potentially viewing human driving as "barbaric" <a class="yt-timestamp" data-t="10:47:00">[10:47:00]</a> <a class="yt-timestamp" data-t="11:07:00">[11:07:00]</a>. The current status quo of human-driven cars involves significant risks, such as putting teenagers behind the wheel of "two-ton death machines" <a class="yt-timestamp" data-t="11:01:00">[11:01:00]</a> <a class="yt-timestamp" data-t="11:12:00">[11:12:00]</a>. Autonomous technology also promises to give people back significant time, potentially an hour or more of their day <a class="yt-timestamp" data-t="11:19:00">[11:19:00]</a> <a class="yt-timestamp" data-t="11:21:00">[11:21:00]</a>.

The most important takeaway is to pay attention to the present "messy middle" of development, as this is where the future is actively being made, rather than waiting for a distant sci-fi version of autonomous technology <a class="yt-timestamp" data-t="11:51:00">[11:51:00]</a> <a class="yt-timestamp" data-t="12:00:00">[12:00:00]</a>.