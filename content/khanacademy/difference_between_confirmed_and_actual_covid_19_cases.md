---
title: Difference between confirmed and actual COVID 19 cases
videoId: mCa0JXEwDEk
---

From: [[khanacademy]] <br/> 

The goal is to [[estimating_actual_covid_19_cases_based_on_deaths | estimate the actual new COVID-19 cases per day]] in a given area <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. The information presented is based on analysis by Thomas Puello, published in a blog post on Medium <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## The Discrepancy

While news reports provide daily confirmed COVID-19 cases, these numbers are based only on individuals who have been tested <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. Many people may not have symptoms severe enough to warrant a test, or they may not have symptoms yet <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. Consequently, the actual number of cases is likely far greater than the confirmed count <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

### Case Study: Hubei Province

Data from [[analysis_of_covid_19_data_from_hubei_province | Hubei province]], where Wuhan is located, graphically illustrates this difference <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

*   On January 23rd, the yellow bar represented approximately 300 confirmed new cases (people tested positive) <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
*   The gray bar for the same day showed the actual number of new cases to be around 2,500, which is roughly eight times higher <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

Chinese officials were able to determine these "actual" figures in hindsight <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. When someone tested positive, they were asked when they first experienced symptoms. If symptoms began 10 days prior, that case was retroactively added as an actual new case for that earlier date <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

Prior to Wuhan's shutdown on January 23rd <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>:
*   As of January 22nd, the cumulative actual cases totaled approximately 12,000 <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
*   The cumulative confirmed cases for the same period were only about 444 <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.

This demonstrates that even with reasonably good testing, the actual number of cases was significantly higher than the confirmed cases would suggest <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. After the shutdown, the actual cases started to flatten and decline, though confirmed cases continued to rise due to a delay between symptom onset and testing <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

## Limitations in Testing

The disparity between actual and confirmed cases is likely even greater in many other geographies, such as the United States, which did not perform testing as extensively as China did early on <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>. As of March 3rd, the United States was not performing well in terms of tests per million citizens <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. This lack of widespread testing means that reported cases significantly understate the true number of actual cases <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

## Estimating Actual Cases Based on Deaths

To [[estimating_actual_covid_19_cases_based_on_deaths | estimate the actual number of cases]], analysis can look at the number of deaths, mortality rate, time from infection to death, and how quickly the virus spreads <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.

Key estimates used in this analysis:
*   **Mortality Rate**: Assumed to be 1% <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>. This rate can vary, from as low as 0.6% in South Korea to about 5% in Iran, often influenced by whether the hospital system is overwhelmed <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
*   **Time from Infection to Death**: Roughly 20 days <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. This is broken down into:
    *   Incubation period (infection to symptoms): Approximately 5 days <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
    *   Symptoms to death: Approximately 15 days <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.
*   **Days to Doubling**: Assumed to be 5 days <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. This rate depends heavily on population density and interactions; lower doubling rates indicate faster spread <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. This estimate is considered conservative, especially for areas like the United States that had not yet taken significant action <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.

### Example Calculation

Consider a scenario where one death is reported in a region today <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
1.  **Infection Date**: Given the 20-day average time from infection to death, that person was likely infected 20 days ago <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
2.  **Actual Cases 20 Days Ago**: Assuming a 1% mortality rate, if one person died, it implies that approximately 100 people were infected on that day (1% of 100 is 1) <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
3.  **Compounding Effect**: If the infection doubles every five days, the number of actual cases would increase as follows <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>:
    *   20 days ago: 100 infected <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>
    *   15 days ago (after 5 days): 200 cases <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>
    *   10 days ago (after another 5 days): 400 cases <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>
    *   5 days ago (after another 5 days): 800 cases <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>
    *   Today (after another 5 days): Approximately 1,600 cases <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>

This calculation, based on a single death, suggests that today there could be roughly 1,600 actual cases <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>. This highlights how much the reported data lags the true situation on the ground, especially in regions with limited testing <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>. For example, in Santa Clara County, California, with two reported deaths and under 100 reported cases, the actual number of infected persons was estimated to be at least ten times higher, possibly between 1,000 and 3,000 people <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.

## Implications

It is crucial to take the situation seriously because the [[factors_influencing_covid_19_mortality_rate | mortality rate]] can increase if the hospital system becomes overwhelmed <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>. Social isolation and proper precautions can lower the [[impact_of_shutdowns_on_covid_19_case_spread | spread rate]], prevent overwhelming hospitals, and help keep the mortality rate as low as possible <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>. Complacency due to lagging reported data and insufficient testing risks overwhelming the hospital system, which would lead to a higher mortality rate <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.