---
title: Water usage in data centers
videoId: tJYSzc7YkY0
---

From: [[asianometry]] <br/> 

Data centers, the backbone of our digital world, consume vast amounts of resources. While their significant energy demands are well-known <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>, their reliance on water is also substantial and closely linked to energy consumption <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. A single data center with 15 megawatts of IT capacity is estimated to use between 80 to 130 million gallons of water annually <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. This is comparable to the water usage of three hospitals or two 18-hole golf courses <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. The current [[ai_boom_and_data_center_demands | AI boom]] is accelerating the construction of large data centers globally, intensifying these demands <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

## Types of Data Centers

[[energy_efficiency_in_ai_data_centers | Data centers]] vary in size and function, from small closet-sized setups to massive, custom-built facilities spanning entire football fields <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. They are generally classified by floor space, number of servers, or power consumption <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. The largest facilities, known as "hyperscale" data centers, house around 5,000 servers and can be 10,000 square meters in size <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. These are often built by global operators like Google or Meta for applications such as Gmail or Facebook <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

A key metric for a data center's [[energy_efficiency_in_ai_data_centers | energy efficiency]] is Power Usage Effectiveness (PUE) <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. PUE is calculated by dividing the total energy delivered by the energy consumed by ICT equipment <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. A PUE of 1.0 signifies 100% efficiency, with all energy used by ICT <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. Larger data centers tend to have lower PUEs; hyperscale facilities from Google and Microsoft claim PUEs of 1.1 or 1.2, while smaller data centers might have a PUE of 2.5 <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. This difference is largely due to the more efficient [[cooling_systems_in_data_centers | cooling systems]] that hyperscale data centers can implement, including advanced airflow modeling or liquid cooling <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

## Cooling Systems

Nearly all electricity consumed by a data center is converted into heat <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. Even when not at full capacity, data centers draw 60-100% of their maximum power, generating significant heat <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. Electronic equipment must be kept cool to prevent long-term damage, with hard drives needing to stay around 45 degrees Celsius (113 degrees Fahrenheit) and solid-state chips up to 85 degrees Celsius <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

Maintaining stable temperature and humidity is the role of the [[cooling_systems_in_data_centers | cooling system]] <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. Most data centers use air cooling in a raised-floor system, where cold air from Computer Room Air Conditioners (CRACs) is directed into cold aisles to absorb heat from servers <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. The heated air then rises and is re-collected to be sent to fluid heat exchangers <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

A common [[cooling_systems_in_data_centers | cooling system]] involves two fluid loops: a process loop (often water and glycol) that takes heat from the data room, and a condenser loop (water-based) that transfers heat to the outside <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. This dual-loop system prevents contamination and offers flexibility, despite being more expensive <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. Cooling towers then cool the water in the condenser loop by evaporating some of it, releasing energy <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>. Approximately 1% of the water evaporates for every 10 degrees Fahrenheit (5.6 degrees Celsius) of cooling, depending on ambient conditions <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. This evaporated water must be replaced with new, "make-up" water <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.

## Energy Usage and Indirect Water Footprint

The second, and often larger, way data centers consume water is indirectly through electricity generation <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. In 2022, data centers accounted for 1% to 1.3% of global electricity consumption <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. Thermoelectric power generation (coal, natural gas, nuclear), which boils water to spin turbines, requires significant water <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. In 2021, 73% of US power came from thermoelectric means <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.

A study by the Berkeley National Laboratory indicates that water usage from energy generation can be 2-3 times greater than the water directly consumed by data center [[cooling_systems_in_data_centers | cooling systems]] <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>. While evaporative cooling towers consume thousands of gallons directly, switching to air conditioning systems would increase power usage and, consequently, indirect water consumption <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. Although companies like Apple are working towards using more renewable energy or offsetting their use <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>, most data centers draw power from their local grid <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.

## The Big Companies and Water Usage

Major tech companies report significant water consumption for their data centers:

*   **Google**: Used approximately 4.3 billion gallons of water for cooling in 2022 <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. They state that 25% of the water used is [[water_recycling_and_reuse_technologies_in_semiconductor_manufacturing | reclaimed wastewater]] or seawater <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.
*   **Digital Realty**: A real estate investment trust specializing in data centers, reported that about 36% of their water comes from municipal non-drinkable sources <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. Roughly half of their 2022 water consumption occurred in areas experiencing water strain <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.
*   **AWS**: Their 2022 Sustainability Report noted that 20 of their global data centers use [[water_recycling_and_reuse_technologies_in_semiconductor_manufacturing | recycled water]] for cooling, with 16 in Virginia, 2 in California, and 2 in Singapore <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
*   **Microsoft**: Committed to being water positive, sponsoring projects that replenish more water than they consume and providing water access to a million people <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>. However, their 2022 water consumption jumped 34% from 2021 <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>, likely due to ChatGPT and other generative AI products <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.

## Water Sources and Scarcity

The majority of water directly withdrawn and used for data center cooling by these companies is drinkable water from local supplies <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>. With 40-50% of the global population living in areas with water scarcity <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>, and many data centers needing to be near population centers, this creates a new competing demand for water <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

Arizona, a leading state for data center development (including Microsoft, PayPal, and Meta) <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>, experiences drought conditions and relies heavily on the Colorado River for water <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>. Meta has responded by funding water restoration projects in the Colorado and Salt River basins, sourcing water via long-term storage credits to avoid municipal supply impact, and leveraging direct free cooling to cut water usage by 60% <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.

## Solutions for Water Reduction

### Free Cooling

"Free cooling" involves using nature to cool data centers, avoiding large HVAC systems or extensive water evaporation <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.
Direct free cooling, like leaving windows open, is the simplest method <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>. However, outside air often contains impurities, requiring dehumidification, air filtration, and cleaners, which can offset cost benefits depending on the location <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. Studies in Europe show direct free-cooling can lead to energy savings of about 5.4-7.9% <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. In Australia, savings can reach 60% in southern capital cities <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>. The significant advantages of cold climates have led Nordic governments to actively pursue data center investments <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>.

### Waterside Free Cooling

Data centers located near cold water bodies can use this water for cooling <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>. Google's Hamina data center in Finland, a converted paper mill, uses existing pipes to take in fresh seawater <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>. Due to the two-loop cooling system, the seawater does not mix with the fluid directly cooling the data center, and is cooled before being returned to the sea <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>. Microsoft's "Project Natick" also explored underwater data centers for cooling benefits <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.

### Heat Recapture

Another strategy is to recover and reuse the heat generated by data centers <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>. Recaptured heat can be used for water desalination, pre-heating water in thermoelectric plants, direct power generation, or district heating for homes <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. Heat from air-cooled data centers can be captured at 35-45 degrees Celsius <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>. Space and water heating is the largest energy use in homes, accounting for about 6% of America's total energy consumption <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.

The main challenge is that heat cannot be efficiently moved as far as electricity, requiring demand sources (households) to be relatively close to the data center <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>. Infrastructure, such as district heating networks, is also a barrier in many cities <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>. Nordic countries have made significant progress in this area <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>. Adopting liquid cooling solutions alongside heat recapture would be beneficial, as liquid is more efficient at capturing and transferring heat than air, reducing overall energy consumption and improving processor performance <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>.

### Temperature Ranges

Optimizing operating temperatures can also reduce cooling needs <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>. The American Society of Heating, Refrigerating and Air-Conditioning Engineers (ASHRAE) recommends a data center temperature range of 15 to 32 degrees Celsius <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>. While some operators run cooler assuming better electronics performance, raising a data center's temperature by even 1-2 degrees can yield significant financial benefits <a class="yt-timestamp" data-t="00:13:26">[00:13:26]</a>. Google's tests have shown their data centers can operate at higher temperatures, though some contradictory observations exist regarding hard drive performance at cooler temperatures <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>.

## The [[ai_boom_and_data_center_demands | AI Boom]]

The ongoing [[ai_boom_and_data_center_demands | AI boom]] is leading to faster ramp-up and increased energy usage for massive data centers <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>. Bob Blue, CEO of Dominion Energy, serving the Northern Virginia data center cluster, noted a significant increase in demand requests:
> For some context, historically, a single data center typically had a demand of 30 megawatts or greater. However, we're now receiving individual requests for demand of 60 megawatts to 90 megawatts or greater, and it hasn't stopped there. We get regular requests to support larger data center campuses that include multiple buildings and require total capacity ranging from 300 megawatts to as many as several gigawatts. <a class="yt-timestamp" data-t="00:14:34">[00:14:34]</a>

SemiAnalysis estimates that AI could propel data center energy consumption to 4.5% of global energy generation by 2030, implying a similar increase in water consumption <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>. Nvidia's upcoming GPU products are increasingly power-hungry, and training and deploying leading-edge AI models will drive maximum power and water consumption <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>.

## Conclusion

The future of compute and AI will demand significantly more electricity and water <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>. This demand begins at the [[semiconductor_water_usage_and_challenges | semiconductor fabrication]] stage; for instance, TSMC in Taiwan is projected to account for 12.5% of Taiwan's total energy consumption by 2025 <a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>. After chips are fabricated, they are run at full tilt in data centers, generating heat that requires even more energy to remove <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>.

To address these growing demands, future data centers must rapidly adopt a combination of strategies:
*   Free-cooling <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a>
*   Waste heat recovery <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>
*   Renewable energy sources like solar <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>

The swiftness of this transition is crucial for both environmental sustainability and financial viability <a class="yt-timestamp" data-t="00:16:22">[00:16:22]</a>.