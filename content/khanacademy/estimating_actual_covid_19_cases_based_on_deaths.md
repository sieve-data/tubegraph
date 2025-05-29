---
title: Estimating actual COVID 19 cases based on deaths
videoId: mCa0JXEwDEk
---

From: [[khanacademy]] <br/> 

The goal of this analysis, based on a blog post by Thomas Pueyo, is to estimate the actual number of new COVID-19 cases per day in a given area <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Reported vs. Actual Cases

The numbers of COVID-19 cases reported daily on the news represent only the confirmed cases, which are based on individuals who have been tested <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. Many people may not have symptoms or have symptoms not severe enough to warrant testing, meaning the [[difference_between_confirmed_and_actual_covid_19_cases | actual cases]] are likely much larger than the confirmed numbers <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

### Hubei Province Data
Graphical data from [[analysis_of_covid_19_data_from_hubei_province | Hubei province]], where Wuhan is located, illustrates this disparity <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
For instance, on January 23rd, 2020:
*   **Confirmed new cases (yellow bar)**: Approximately 300 individuals tested positive <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
*   **Actual new cases (gray bar)**: Close to 2,500, roughly eight times higher than confirmed cases <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

Chinese officials were able to determine the actual number of cases in hindsight by asking confirmed positive individuals when they first experienced symptoms <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. If someone reported symptoms 10 days prior, they were counted as an actual new case on that earlier date <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

Wuhan implemented a shutdown on January 23rd <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. While city officials began seeing confirmed cases rise, the actual cases were already far higher <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. Following the shutdown, the actual cases started to flatten and then decrease, indicating a significant slowing of the spread rate <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. However, confirmed new cases continued to increase due to a delay between symptom onset and testing <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

By January 22nd, before the city went into shutdown:
*   Total actual cases: Approximately 12,000 <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
*   Total confirmed cases: Approximately 444 <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.

The ratio of actual to confirmed cases may be even higher in areas not performing as much testing as China did <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>. For example, the United States, as of March 3rd, was not performing as well in terms of tests per million citizens, leading to a significant understatement of actual cases <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

## Factors for Estimating Actual Cases
To estimate the actual number of cases, three key factors are considered <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>:
1.  **Mortality Rate**: Assumed to be 1% <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
    *   Reports vary from 0.6% in South Korea to about 5% in Iran <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
    *   Higher rates often occur when the hospital system is overwhelmed, while lower rates might not fully account for all potential mortality <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>. This highlights the [[factors_influencing_covid_19_mortality_rate | factors influencing COVID 19 mortality rate]].
2.  **Time from Infection to Death**: Estimated at 20 days <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
    *   This is broken down into an incubation period (infection to symptoms) of roughly 5 days <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
    *   And the time from symptom onset to death (in fatal cases) of roughly 15 days <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.
3.  **Days to Doubling**: Assumed to be 5 days for the infection to double in the population <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
    *   This rate is highly dependent on population density and interaction <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
    *   A lower doubling rate indicates faster spread, while higher rates (more days to double) suggest effective precautions <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.
    *   A 5-day doubling rate is considered conservative, especially in regions not taking significant action <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>.

## Estimating Actual Cases from a Single Death
Using these estimates, one can infer the actual number of cases:
1.  **One Death Today**: If there is one reported death today, that individual likely contracted the virus approximately 20 days ago, based on the estimated time from infection to death <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
2.  **Initial Infections**: Given a 1% mortality rate, this one death suggests that approximately 100 people were infected 20 days ago (1 death / 0.01 mortality rate = 100 infections) <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.
    *   If the mortality rate were 0.5%, it would imply 200 initial infections <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.
    *   If it were 5%, it would imply 20 initial infections <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.
3.  **Exponential Growth**: Assuming the infection doubles every 5 days:
    *   **20 days ago**: 100 infected <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.
    *   **15 days ago** (after 5 days): 200 cases <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.
    *   **10 days ago** (after another 5 days): 400 cases <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.
    *   **5 days ago** (after another 5 days): 800 cases <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.
    *   **Today** (after another 5 days): Approximately 1,600 cases <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>.

This estimation suggests that one death today could indicate around 1,600 actual active cases in the population.

## Implications and Takeaways
The data reported often lags behind the actual situation, especially in regions with limited testing capabilities <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>. For example, in Santa Clara County, California, with only under 100 reported cases, the actual number of infected persons is likely at least ten times higher, possibly between 1,000 and 3,000, based on recent deaths <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.

It is crucial to take the situation seriously because the [[factors_influencing_covid_19_mortality_rate | mortality rate]] can increase if the healthcare system becomes overwhelmed <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>. By practicing social isolation and taking precautions, the spread rate can be lowered, preventing hospitals from being overwhelmed and keeping the mortality rate as low as possible <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>. Complacency due to lagging reported data could lead to overwhelming the hospital system in a few weeks, which would likely increase the mortality rate <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.