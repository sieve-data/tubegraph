---
title: Estimating actual COVID19 cases using mortality data
videoId: mCa0JXEwDEk
---

From: [[khanacademy]] <br/> 

This article aims to provide an estimate of the actual daily new COVID-19 cases in a given area, based on [[analysis_of_covid19_spread_rates_and_mortality | analysis]] by Thomas Pueyo, whose blog post on Medium provides the underlying data and [[analysis_of_covid19_spread_rates_and_mortality | analysis]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>, <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## Reported vs. Actual Cases
The reported number of COVID-19 cases, often seen in news updates, only reflects individuals who have been tested <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. The actual number of cases is likely far greater than the confirmed cases, as many people may not have symptoms or their symptoms are not severe enough to warrant testing <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>, <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. This highlights a significant [[difference_between_reported_and_actual_covid19_cases | difference between reported and actual COVID-19 cases]] <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

### Hubei Province Example
A diagram from Thomas Pueyo's blog, illustrating the situation in Hubei province (where Wuhan is located), demonstrates this disparity <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>, <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
*   On January 23rd, the confirmed new cases (yellow bar) were approximately 300 <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>, <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>, <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
*   However, the actual new cases (gray bar) for the same day were close to 2,500 <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>, <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>, roughly eight times higher <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

Chinese officials were able to determine the actual number of cases in hindsight by asking confirmed positive individuals when they first experienced symptoms <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>, <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. This allowed them to construct the "gray bars" indicating true new cases on specific past dates <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>, <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

When Wuhan was shut down on January 23rd <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>, actual cases were already far higher than confirmed cases <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>, <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. The shutdown significantly slowed the spread rate <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>, <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. A few days later, the actual cases began to flatten and decrease, though confirmed new cases continued to rise due to a reporting delay <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>, <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>, <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

This chart represents *new* cases per day <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>, not total cases. To find the total number of cases at a given point, one would sum the daily bars <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>, <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. For instance, as of January 22nd:
*   Total actual cases: Approximately 12,000 <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>, <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
*   Total confirmed cases: Roughly 444 <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>, <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

This shows that before the shutdown, actual cases were significantly higher than what confirmed cases indicated <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>, <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

### Impact of Testing Limitations
The ratio of actual to confirmed cases is likely even higher in areas not testing as extensively as China <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>, <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. For example, as of March 3rd, the United States was not performing well in terms of total tests performed per million citizens, leading to a significant understatement of actual cases <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>, <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>, <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>. This highlights the [[impact_of_testing_limitations_on_reported_covid19_cases | impact of testing limitations on reported COVID19 cases]].

## Estimation Methodology
To estimate the actual number of cases, Thomas Pueyo's [[analysis_of_covid19_spread_rates_and_mortality | analysis]] uses:
1.  The number of deaths <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
2.  Estimations of the mortality rate <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
3.  Time from infection to death <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
4.  The rate at which the virus spreads <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>, <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.

### Parameter Assumptions
*   **Mortality Rate**: A 1% mortality rate is used for calculation simplicity and is a reasonable estimate <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>, <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>. Reported rates vary from 0.6% (South Korea) to 5% (Iran), with higher rates often observed where hospital systems are overwhelmed <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>, <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>, <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
*   **Time from Infection to Death**: This is estimated at approximately 20 days <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>, <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>, based on:
    *   Incubation period (infection to symptom onset): Roughly 5 days <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>, <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>, <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.
    *   Time from symptom onset to death: Approximately 15 days <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>, <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>, <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.
*   **Days to Doubling**: This refers to how long it takes for the infection to double in the population <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>, <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. This rate depends heavily on population density and interaction <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. For estimation, a conservative doubling rate of 5 days is assumed <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>, <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>, especially in regions like the United States that have not taken as stringent actions as China or South Korea <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.

## Estimating Actual Cases: A Real-Life Example
Let's consider an example of a single reported death in a region today <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>, <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
1.  **Origin of Infection**: Given the 20-day average time from infection to death, this person likely contracted the virus approximately 20 days ago <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>, <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>, <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
2.  **Initial Actual Cases**: Assuming a 1% mortality rate, one death implies that approximately 100 people were infected on that day (20 days ago) <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>, <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>, <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. This is a conservative estimate, assuming these were the only cases at that time <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>, <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.
3.  **Exponential Growth**: If the infection rate doubles every 5 days:
    *   15 days ago (5 days after initial infection): Cases double to 200 <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>, <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.
    *   10 days ago (10 days after initial infection): Cases double again to 400 <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>, <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>, <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
    *   5 days ago (15 days after initial infection): Cases double to 800 <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>, <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>, <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.
    *   Today (20 days after initial infection): Cases double to approximately 1,600 <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>, <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>, <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.

This demonstrates that one death today could imply approximately 1,600 actual active cases in the community from that original infection point, illustrating the significant lag in reported data <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>, <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

For instance, in Santa Clara County, California, with under 100 reported cases, two deaths (one recent, one 5 days prior) suggest the actual number of infected persons is likely at least a factor of ten more, potentially 1,000 to 3,000 people <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>, <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>, <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>, <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>, <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.

## Implications and Takeaway
The significant disparity between reported and actual cases underscores the seriousness of the situation <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>, <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>. The mortality rate itself can increase if the hospital system becomes overwhelmed <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>, <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>. By engaging in social isolation and taking proper precautions, the spread rate can be lowered, preventing the healthcare system from being overwhelmed and keeping the mortality rate as low as possible <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>, <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>, <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>. Conversely, complacency due to lagging reported data (especially in areas with limited testing) could lead to an overwhelmed hospital system in a few weeks, potentially causing a higher mortality rate <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>, <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>, <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>. These are [[effective_measures_to_control_covid19_spread | effective measures to control COVID-19 spread]].