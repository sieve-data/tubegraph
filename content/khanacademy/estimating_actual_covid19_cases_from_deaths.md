---
title: Estimating actual COVID19 cases from deaths
videoId: mCa0JXEwDEk
---

From: [[khanacademy]] <br/> 

The goal of this analysis is to estimate the actual number of new COVID-19 cases per day in a given area, as opposed to the reported numbers, based on an analysis by Thomas Pueyo <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## [[differences_between_reported_and_actual_covid19_cases | Reported vs. Actual Cases]]

The number of COVID-19 cases reported daily on the news is based on individuals who have been tested <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. This reported number likely significantly understates the actual cases, as many people may not have symptoms severe enough to get tested, or may not have symptoms yet <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

### Hubei Province Example

A diagram from Thomas Pueyo's analysis, based on data from Hubei province (where Wuhan is located), illustrates this disparity <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>:
*   On January 23rd, the confirmed new cases (yellow bar) were approximately 300 <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
*   However, the actual number of new cases (gray bar) for that same day was close to 2,500, roughly eight times higher <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

The actual numbers were determined in hindsight by asking confirmed positive individuals when they first experienced symptoms. If symptoms began 10 days prior, they were counted as an actual new case on that earlier date <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

The shutdown of Wuhan on January 23rd showed an effect: while confirmed cases continued to rise due to delays in testing and symptom onset, the actual cases, calculated in hindsight, began to flatten out and then decrease a few days later <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

> [!INFO] Cumulative Cases
> As of January 22nd, before the city shutdown, the cumulative actual cases (sum of gray bars) were approximately 12,000, while the cumulative confirmed cases (sum of yellow bars) were only about 444 <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. This highlights a significant lag in confirmed numbers.

### [[impact_of_testing_on_reported_covid19_case_numbers | Impact of Testing]]

The ratio of actual to confirmed cases can be even higher in areas with less extensive testing. For example, as of March 3rd, the United States was performing significantly fewer tests per million citizens compared to other countries, leading to a greater understatement of actual cases <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

## Estimating Actual Cases Using Deaths

To estimate the actual number of cases, an analysis uses reported deaths along with estimations of the mortality rate, [[time_from_infection_to_death_estimation_in_covid19_cases | time from infection to death]], and how fast the virus spreads <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

### Key Estimation Factors

1.  **Mortality Rate**:
    *   A mortality rate of **1%** is a reasonable estimate, falling between reports as low as 0.6% (South Korea) and as high as 5% (Iran) <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
    *   Higher rates often occur when hospital systems are overwhelmed, while lower rates might not fully account for all potential mortality <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
    *   Factors such as the strain on the healthcare system can influence [[factors_influencing_covid19_mortality_rates | COVID-19 mortality rates]] <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>.

2.  **[[time_from_infection_to_death_estimation_in_covid19_cases | Time from Infection to Death]]**:
    *   This is the time between when someone is infected and when they unfortunately pass away <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
    *   It's estimated as:
        *   **5 days** from infection to showing symptoms (incubation period) <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
        *   **15 days** from showing symptoms to death <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.
    *   Total: **20 days** from infection to death <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

3.  **Days to Doubling**:
    *   This refers to the time it takes for the number of infections to double in the population <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
    *   It is heavily dependent on population density, interaction levels, and preventative measures <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
    *   A conservative estimate, especially for areas not taking significant action, is **5 days to double** <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

### Estimation Process Example

Consider a scenario where one death is reported in a region today <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.

1.  **Infection Time**: Given the 20-day [[time_from_infection_to_death_estimation_in_covid19_cases | time from infection to death]], that person likely contracted the virus approximately 20 days ago <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
2.  **Initial Infections**: Assuming a 1% mortality rate, that one death implies that approximately **100 people** were infected 20 days ago <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. This is because the person who died represents 1% of a larger infected group (1 death / 0.01 mortality rate = 100 infections). If the mortality rate was 0.5%, it would imply 200 infected, or 5% implying 20 infected <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.
3.  **Projected Current Cases**: If the infection rate doubles every five days (5 days to double):
    *   20 days ago: 100 cases
    *   15 days ago (after 5 days): 200 cases <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>
    *   10 days ago (after another 5 days): 400 cases <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>
    *   5 days ago (after another 5 days): 800 cases <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>
    *   **Today (after another 5 days): 1600 cases** <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>

> [!WARNING] Lagging Data
> This calculation demonstrates that one reported death can indicate approximately 1600 actual active cases in the region today, underscoring how much the reported data lags behind the real situation, especially in areas with limited testing <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>.

## Conclusion

The significant disparity between reported and actual cases highlights the seriousness of the situation. It emphasizes the importance of social isolation and preventative measures to slow the spread rate. By doing so, the healthcare system can avoid being overwhelmed, which in turn helps keep the [[factors_influencing_covid19_mortality_rates | mortality rate]] as low as possible <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>. Complacency due to lagging reported data could lead to overwhelming hospitals and an increase in the mortality rate <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.