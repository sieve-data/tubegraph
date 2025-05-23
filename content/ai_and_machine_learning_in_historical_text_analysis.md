---
title: AI and Machine Learning in Historical Text Analysis
videoId: qcvMjoJdck4
---

From: [[dwarkesh | The Dwarkesh Podcast]]

The Vesuvius Challenge is an ambitious project aimed at deciphering ancient papyrus scrolls carbonized by the eruption of Mount Vesuvius in AD 79. [[historical_influences_on_leadership_and_innovation | Organized by Nat Friedman, former CEO of GitHub]], in collaboration with Professor Brent Seales of the University of Kentucky and others, the challenge leverages advanced imaging techniques and artificial intelligence, particularly machine learning, to read texts that have been inaccessible for nearly two millennia.

## Historical Context: The Lost Library of Herculaneum

### The Eruption and Discovery
In AD 79, the eruption of Mount Vesuvius buried nearby towns, including the well-known Pompeii and the wealthier Herculaneum. [[impact_of_plagues_on_human_history | Herculaneum was entombed under approximately 20 meters of volcanic mud and ash. ]] One particularly large villa in Herculaneum, once owned by Julius Caesar's father-in-law, housed a significant library of papyrus scrolls. These scrolls were carbonized by the heat of the eruption.

The villa and its library were rediscovered in 1750 when a farm worker digging a well struck a marble paving stone 60 feet down. Subsequent tunneling, led by a Swiss engineer, uncovered treasures and hundreds, possibly thousands, of these carbonized scrolls. [[impact_of_plagues_on_human_history | This find is remarkable as it represents the only library from antiquity to have survived]], albeit in a damaged state, as papyrus typically rots quickly in the Mediterranean climate. [[historical_influences_on_leadership_and_innovation | It's estimated that less than 1% of all writing from that period has survived]].

### Early Attempts at Unrolling
Initial efforts to read the scrolls were often destructive. [[the_impact_of_modern_technology_on_warfare_and_strategy | The fragile, carbonized papyri would turn to ash when handled]]. Methods like cutting them down the middle were tried, resulting in further damage. An Italian monk named Piaggio later devised a machine to unroll the scrolls very slowly, successfully revealing Greek philosophical texts by Philodemus. However, many scrolls were destroyed even into the 20th century by physical unrolling attempts. Approximately 600 relatively intact scrolls remain unopened.

Nat Friedman simulated the carbonization process using a Dutch oven, heating modern papyrus scrolls to 500°F for several hours, noting their extreme fragility and tendency to crumble.

## Modern Approaches: Virtual Unwrapping and AI

### Pioneering Virtual Unwrapping
Professor Brent Seales at the University of Kentucky has been a pioneer in "virtual unwrapping." His initial success came with the En-Gedi scroll, found in Israel. Using 3D X-ray (CT) scans, his team was able to segment the layers of the scroll and, because the ink had a high X-ray contrast against the papyrus, they could read the text, which turned out to be a portion of the Book of Leviticus.

### Challenges with the Herculaneum Scrolls
Applying these techniques to the Herculaneum scrolls proved more difficult due to two main factors:
1.  **Ink Visibility**: The ink used on the Herculaneum papyri is carbon-based, similar to the carbonized papyrus itself. This means it has very similar X-ray absorption properties to the papyrus, making it nearly invisible in standard X-ray scans.
2.  **Scroll Condition**: The scrolls are highly distorted and damaged from the volcanic event, making the segmentation of individual layers complex.

In 2019, Dr. Seales' team took some Herculaneum scrolls to the Diamond Light Source, a particle accelerator in Oxford, England, to create incredibly high-resolution 3D X-ray scans at eight-micron voxel size.

### The Machine Learning Breakthrough for Ink Detection
Despite the low contrast, Dr. Seales' lab made significant progress by applying machine learning models, specifically convolutional neural networks (CNNs), to identify ink. [[open_source_ai_models_and_their_implications | These models can detect subtle patterns in the X-ray absorption data that are not visible to the human eye. ]]

To train these models, the team used:
1.  **Broken-off fragments** of the papyri where some lettering is visible.
2.  **Infrared imaging** (around 930 nanometers) of these fragments to enhance the visibility of the ink, creating ground truth data.
3.  **CT scans of these fragments** were then aligned with the infrared images to provide training data for the ML models.

A remaining challenge is adapting models trained on fragments (where ink is often next to air) to the interior of a scroll (where ink is pressed against another layer of papyrus).

## The Vesuvius Challenge Prize

Nat Friedman, along with Daniel Gross, launched the Vesuvius Challenge, an open competition with a prize (mentioned as a quarter of a million dollars) for the first team to read substantial amounts of text from one of the scanned Herculaneum scrolls without physically opening it. The goal is to accelerate the process by bringing many smart minds to the problem. [[ai_scalability_and_breakthroughs | Data and Technical Details for Participants]]

### Data and Technical Details for Participants
*   The scans are high-resolution, with 8-micrometer voxels.
*   Data is provided as TIFF files for each cross-sectional slice of the scroll, with each slice being over 100 megabytes.
*   Approximately 6-8 voxels span the thickness of a single papyrus layer.
*   Dr. Seales' PhD students have demonstrated ink recognition at this 8-micron resolution.

Friedman estimates a 50% chance that the problem will be solved within the year due to this open competition format.

## Potential Impact of Success

The successful deciphering of these scrolls holds immense potential:
*   **Vast Expansion of Ancient Texts**: If all 600-800 unopened scrolls in the collection could be read, it is estimated this would roughly double the total body of texts currently available from antiquity. Friedman mentions this could be equivalent to "multiple Shakespeares" in terms of volume.
*   **Unknown Content**: While some unrolled scrolls contained works by the Epicurean philosopher Philodemus, the unopened scrolls could contain lost epic poems, historical texts, or even unique insights like contemporaneous mentions of early Christianity. [[artificial_intelligence_vs_human_intelligence | Some scrolls found were already hundreds of years old at the time of the eruption, and there's speculative hope some texts from the Library of Alexandria might be present. ]]
*   **Further Excavation**: Only about a third of the villa has been excavated. Historians hypothesize that the main library, possibly containing Latin literary texts, may still be undiscovered in the unexcavated portions. Success in reading even one scroll could catalyze funding for scanning the remaining known scrolls and for further archaeological excavation at Herculaneum.

The Vesuvius Challenge represents a confluence of archaeology, advanced physics (particle accelerators), and cutting-edge artificial intelligence to potentially unlock a treasure trove of lost knowledge from the ancient world.