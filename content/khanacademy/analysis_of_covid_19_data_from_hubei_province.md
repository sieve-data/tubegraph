---
title: Analysis of COVID 19 data from Hubei province
videoId: mCa0JXEwDEk
---

From: [[khanacademy]] <br/> 

This analysis aims to help estimate the actual number of new COVID-19 cases per day in a given area, drawing on data and insights from Hubei province, where Wuhan is located <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. The information is based on analysis by Thomas Pueyo, published in a blog post on Medium <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## Confirmed vs. Actual Cases

The number of reported COVID-19 cases, often seen on the news, reflects only those who have been tested and confirmed positive <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. This reported figure likely significantly understates the true number of cases, as many individuals may not yet show symptoms or their symptoms are not severe enough to warrant a test <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. Therefore, the actual number of cases is likely far larger than the number of confirmed cases <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>, highlighting the [[difference_between_confirmed_and_actual_covid_19_cases | difference between confirmed and actual COVID-19 cases]].

Thomas Pueyo's diagram, a screenshot from his blog post, illustrates this discrepancy in Hubei province <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. The vertical axis represents the number of cases, and the horizontal axis represents "per day" <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

*   **Yellow Bar**: Indicates the number of confirmed new cases for a given day (people tested and positive) <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
*   **Gray Bar**: Represents the actual number of new cases for that same day <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

For instance, on January 23rd, the confirmed new cases were about 300, while the actual new cases were closer to 2,500 – roughly eight times higher <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

### How Actual Cases Were Determined

Chinese officials were able to determine the "actual" number of cases in hindsight <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. When someone tested positive, they were asked when they first experienced symptoms <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. If, for example, symptoms began 10 days prior, that individual would be counted as an actual new case on that earlier date <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

## [[impact_of_shutdowns_on_covid_19_case_spread | Impact of Shutdowns]] in Hubei

Wuhan, in Hubei province, was shut down on January 23rd <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

*   **Pre-Shutdown**: As city officials began to see confirmed cases, the actual cases were already significantly higher <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
*   **Post-Shutdown**: The shutdown significantly slowed down the spread rate of the virus <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. A few days later, the actual cases (calculated in hindsight) began to flatten out and then decline <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.
*   **Delay in Confirmed Cases**: Despite the actual cases decreasing, the confirmed new cases continued to rise due to a delay <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>. This delay represents the approximate time between symptom onset and testing <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   **Consequences of No Shutdown**: Had the shutdown not occurred, the exponential growth of the virus would have continued <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

## Cumulative Cases

The displayed graph shows the number of *new* cases per day <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. To determine the *total* number of cases at a given point in time, one would need to sum up the daily bars (gray for actual, yellow for confirmed) <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

As of January 22nd (before the city shutdown):
*   **Total Actual Cases**: Approximately 12,000 cases <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
*   **Total Confirmed Cases**: Roughly only 444 cases <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.

This highlights that even with "reasonably good testing" by Chinese officials, the actual number of cases was far higher than the confirmed cases suggested before the city went into shutdown <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. The ratio between actual and confirmed cases is likely even higher in geographies with less robust testing <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

## Estimating Actual Cases Based on Hubei Insights

The method for [[estimating_actual_covid_19_cases_based_on_deaths | estimating actual COVID-19 cases based on deaths]] involves considering:
*   Mortality rate <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>
*   Time from infection to death <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>
*   How fast the virus spreads (days to double) <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>

### Key Estimates Used:
*   **Mortality Rate**: Assumed to be 1% for calculation simplicity and as a good estimate <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>. This rate can vary significantly based on [[factors_influencing_covid_19_mortality_rate | factors influencing COVID-19 mortality rate]], such as the healthcare system's capacity <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.
*   **Time from Infection to Death**: Roughly 20 days <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. This is broken down as:
    *   5 days from infection to symptom onset <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
    *   15 days from symptom onset to death (in fatal cases) <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.
*   **Days to Double (Spread Rate)**: Assumed to be 5 days, though this is conservative and heavily dependent on population behavior and density <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

### Example Scenario: One Death in a Region
If one death is reported in a region today <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>:
1.  **Infection Date**: Given the 20-day infection-to-death period, that person likely contracted the virus approximately 20 days ago <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
2.  **Initial Infections**: With a 1% mortality rate, it's possible that 100 people were infected on that day (20 days ago), with the reported death being the one in a hundred who succumbed to the illness <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.
3.  **Current Infections (Doubling)**: If the infection rate doubles every five days, then from those initial 100 cases:
    *   15 days ago (after 5 days): 200 cases <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.
    *   10 days ago (after 10 days): 400 cases <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.
    *   5 days ago (after 15 days): 800 cases <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.
    *   Today (after 20 days): Approximately 1,600 cases <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>.

This demonstrates how the reported data, especially with limited testing, significantly lags the actual situation on the ground <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>. Taking proactive measures like social isolation and precautions is crucial to lower the spread rate, prevent overwhelming hospital systems, and keep the mortality rate as low as possible <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.