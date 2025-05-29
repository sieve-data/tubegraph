---
title: Analysis of COVID19 spread rates and mortality
videoId: mCa0JXEwDEk
---

From: [[khanacademy]] <br/> 

This article aims to help estimate the actual daily new COVID-19 cases in a given area, based on analysis by Thomas Pueyo, as published in a Medium blog post. <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>

## Discrepancy Between Reported and Actual Cases

The number of COVID-19 cases reported in the news is based on individuals who have been tested. <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a> However, many people might not have symptoms yet, or their symptoms are not severe enough to warrant a test. <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a> Consequently, the [[difference_between_reported_and_actual_covid19_cases | actual cases are likely far larger than the number of confirmed cases]]. <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>

### Hubei Province Example

A diagram from Thomas Pueyo's blog post illustrates this discrepancy using data from Hubei province, where Wuhan is located. <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>
*   The vertical axis represents the number of cases per day. <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>
*   On January 23rd, the yellow bar shows about 300 confirmed new cases (people tested positive). <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>
*   The gray bar, representing the actual number of new cases that day, was close to 2,500, roughly eight times higher. <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>

The actual number of cases was determined in hindsight: when someone tested positive, they were asked when they first got symptoms. <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a> For example, if someone tested positive on January 23rd but reported symptoms on January 13th, they were counted as an actual new case on January 13th. <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>

#### Impact of Wuhan Shutdown
Wuhan was shut down on January 23rd. <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a> Before the shutdown, as city officials started to see confirmed cases, the actual cases were far higher. <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a> The shutdown [[effective_measures_to_control_covid19_spread | significantly slowed down the spread rate]]. <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a> A few days later, the actual cases (calculated in hindsight) began to flatten and then decrease. <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a> However, confirmed new cases continued to rise due to a delay between symptom onset and testing. <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>

This chart represents the number of *new* cases per day, not the total number of cases. <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>
*   As of January 22nd, summing the gray bars (actual cases) yields approximately 12,000 cases. <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>
*   Summing the yellow bars (confirmed cases) for the same period yields roughly only 444 confirmed cases. <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>
This shows that before the shutdown, the actual number of cases was significantly higher than the confirmed cases, even with reasonably good Chinese testing. <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>

### Impact of Testing Limitations
The ratio of actual to confirmed cases is likely even higher in many other geographies, as they are [[impact_of_testing_limitations_on_reported_covid19_cases | not testing as well as the Chinese did]]. <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a> As of March 3rd, countries like the United States were not performing well in terms of tests per million citizens, leading to a significant understatement of actual cases. <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>

## Estimating Actual Cases Using Deaths

To [[estimating_actual_covid19_cases_using_mortality_data | estimate the actual number of cases]] in an area, one can use the number of deaths, estimates of mortality rate, time from infection to death, and the virus's spread rate. <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a> This approach uses Thomas Pueyo's analysis. <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>

### Key Parameters

1.  **Mortality Rate:** A working estimate is a 1% mortality rate. <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a> Reported rates vary, from as low as 0.6% in South Korea to about 5% in places like Iran. <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a> Higher rates are often observed where hospital systems are overwhelmed, while lower rates might not fully account for future mortality. <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>
2.  **Time from Infection to Death:**
    *   Incubation period (infection to symptoms): Approximately 5 days. <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>
    *   Symptoms to death: Approximately 15 days. <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>
    *   Total time from infection to death: Roughly 20 days. <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>
3.  **Days to Doubling (Spread Rate):** This indicates how long it takes for the infection to double in the population, heavily influenced by population density and interaction. <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a> A lower doubling rate means faster spread. <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a> For a conservative estimate, assuming a doubling rate of five days is used, which might be conservative for places like the United States where actions are less stringent than in China, South Korea, or Japan. <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>

### [[reallife_calculations_and_examples_of_statistical_measures | Real-Life Calculation Example]]

Let's assume one death is reported in a region today. <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>

*   Based on a 20-day infection-to-death period, that person likely contracted the virus about 20 days ago. <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>
*   If the mortality rate is 1%, then for that one death to occur, approximately 100 people were infected 20 days ago. <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a> (If the mortality rate were 0.5%, it would imply 200 infected; if 5%, it would imply 20 infected.) <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>
*   Using a five-day doubling rate:
    *   20 days ago: 100 infected <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>
    *   15 days ago (5 days later): 200 cases <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>
    *   10 days ago (another 5 days later): 400 cases <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>
    *   5 days ago (another 5 days later): 800 cases <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>
    *   Today (another 5 days later): Approximately 1,600 cases. <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>

This calculation demonstrates that the data reported (especially where testing is limited) significantly lags the actual circumstances. <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a> For instance, in Santa Clara County, California, with reported cases under 100, two deaths suggest the actual number of infected persons is likely at least ten times higher, possibly between one to three thousand people. <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>

> [!warning]
> The data we receive is lagging the actual situation on the ground, particularly in places with limited testing. <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>

## Conclusion

The situation is serious, and the mortality rate can change based on the healthcare system's capacity. <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>
*   Social isolation and precautions can lower the spread rate, preventing hospitals from being overwhelmed and keeping the mortality rate as low as possible. <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>
*   Complacency due to lagging reported data (especially with limited testing) could lead to overwhelming hospital systems in a few weeks, which would cause the mortality rate to increase. <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>