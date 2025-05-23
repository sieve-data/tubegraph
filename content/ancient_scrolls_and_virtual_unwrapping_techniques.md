---
title: Ancient Scrolls and Virtual Unwrapping Techniques
videoId: qcvMjoJdck4
---

From: [[dwarkesh | The Dwarkesh Podcast]]

The Vesuvius Challenge, also referred to as the Scroll Prize, is an open competition aimed at deciphering ancient papyrus scrolls carbonized by the eruption of Mount Vesuvius in AD 79 [[impact_of_ai_on_future_technology_and_society | impact of AI on future technology and society]], [[open_source_ai_models_and_their_implications | open source AI models and their implications]]. Organized by Nat Friedman and Daniel Gross [[impact_of_ai_on_future_technology_and_society | impact of AI on future technology and society]], the challenge seeks to utilize modern imaging and machine learning techniques to read these fragile artifacts without physically unrolling them.

## Historical Background: The Herculaneum Papyri

### The Eruption of Mount Vesuvius and Herculaneum
In AD 79, Mount Vesuvius erupted, destroying nearby towns including the well-known Pompeii. Another town, Herculaneum, described as a more affluent area akin to Beverly Hills compared to Pompeii, was also buried. Herculaneum was covered by approximately 20 meters of volcanic mud and ash, a very thick layer that preserved it for centuries.

### The Villa of the Papyri
Within Herculaneum, a particularly enormous villa, once owned by the father-in-law of Julius Caesar, housed a vast library of papyrus scrolls alongside beautiful statues and art. This library is unique as it is the only one from antiquity to have survived, albeit in a badly damaged, carbonized state. In the Mediterranean climate, papyrus scrolls typically rot and decay quickly, requiring recopying every 100 years or less; it's estimated that less than 1% of all writing from that period survives [[historical_influences_on_leadership_and_innovation | historical influences on leadership and innovation]].

### Discovery and Initial Challenges
The buried towns were forgotten until the 1700s. In 1750, a farm worker digging a well struck a marble paving stone from this villa, about 60 feet down. A Swiss engineer subsequently began digging tunnels from the well shaft, uncovering treasures. During these early excavations, lumps resembling charcoal were found; many were discarded until writing was noticed on one, revealing them to be hundreds, possibly thousands, of papyrus scrolls. It's believed that only about a third of the villa has been excavated [[the_evolution_and_future_of_the_tech_industry | the evolution and future of the tech industry]]. Excavations in the 1990s revealed it was a seaside villa and uncovered two additional floors not previously explored by the 18th-century tunnels. The majority of scrolls found so far were in one small room, believed to be the working library of the Epicurean philosopher Philodemus. Historians hypothesize that the main library, potentially containing Latin literary and historical texts, has not yet been found. Firsthand accounts describe discoveries of other scrolls, including a case of Latin scrolls, that were accidentally destroyed during extraction attempts.

## Early Attempts at Decipherment

### Destructive Physical Methods
Initial attempts to read the fragile, carbonized scrolls often resulted in their destruction, turning them to ash upon handling. Methods included cutting them down the middle with daggers, using rose water or oils to soften them, and even pouring mercury into them in an attempt to separate layers. Hundreds of scrolls were destroyed through such efforts, which continued even into the 2000s.

### Piaggio's Unrolling Machine
An Italian monk named Piaggio, under Vatican care, devised a machine to unroll the scrolls very slowly, at about half a centimeter per day. This method successfully unrolled a few scrolls, typically 15-30 feet long, revealing Greek philosophical texts in the Epicurean tradition by Philodemus. Currently, there are over 600 roughly intact scrolls that remain unopened.

## Modern Approaches: Virtual Unwrapping

### Pioneering Work by Dr. Brent Seales
Professor Brent Seales from the University of Kentucky has been a key figure in developing non-destructive methods to read these scrolls. His field is now known as "virtual unwrapping" [[challenges_and_opportunities_in_deploying_ai_at_scale | challenges and opportunities in deploying AI at scale]]. Seales initially successfully applied these techniques to the En-Gedi scroll, a carbonized scroll found in Israel, which used ink with a high X-ray contrast, making it easier to read. The En-Gedi scroll was found to contain an early part of the Book of Leviticus.

### Imaging Technology and Techniques
For the Herculaneum scrolls, Dr. Seales' team took them to a particle accelerator in Oxford, England, called the Diamond Light Source, in 2019. They created incredibly high-resolution 3D X-ray scans using high-energy photons, achieving voxel sizes of eight microns. These scans are represented as TIFF files, with each slice being over 100 megabytes for full scrolls [[data_center_energy_requirements_and_scaling | data center energy requirements and scaling]]. A stack of 100 such slices would be 0.8 millimeters thick.

### Machine Learning for Ink Detection
A primary challenge with the Herculaneum scrolls is that the carbon-based ink used is almost as X-ray absorbent as the papyrus itself, making it nearly invisible in the scans. Additionally, the scrolls are highly distorted and damaged.
Dr. Seales' lab has made progress using machine learning models, specifically convolutional neural networks, to identify ink. The key insight for training these models was to use broken-off fragments of papyrus where lettering is sometimes visible. Infrared imaging (around 930 nanometers) of these fragments can enhance the visibility of the lettering, providing ground truth data [[ai_and_machine_learning_in_historical_text_analysis | AI and machine learning in historical text analysis]]. CT scans of these fragments are then aligned with the infrared images to train the models. This approach has demonstrated success in identifying ink on fragments.

## The Vesuvius Challenge Prize

### Motivation and Goals
Nat Friedman, after learning about Dr. Seales' work, collaborated with him to launch an open competition to accelerate the decipherment process. The Vesuvius Challenge offers a prize for the first person or team to read substantial amounts of text from one of the scanned scrolls without physically opening it. The competition format aims to leverage many smart individuals trying diverse approaches to solve the problem efficiently.

### Technical Hurdles and Data
Participants are provided with Dr. Seales' team's data, tools, and understanding of the materials. Two scrolls have been scanned so far. Key challenges include:
*   **Segmentation:** Identifying individual layers of the tightly wound and distorted scroll.
*   **Ink Detection Generalization:** Applying models trained on fragments (where ink is next to air) to the inside of a scroll (where ink may be next to another layer of papyrus).
The high resolution of the scans (8 micrometers, providing 6-8 voxels across a papyrus layer) is believed to be sufficient for these tasks.

### Potential Discoveries and Impact
If all 600-800 existing unopened scrolls could be read, it is estimated that this would approximately double the total number of texts currently available from antiquity [[ai_for_science_and_societal_challenges | AI for science and societal challenges]]. This is described as a potential gain equivalent to "multiple Shakespeares". The hope is that successfully reading one scroll will catalyze funding for scanning the remaining scrolls (estimated low millions of dollars) and for further excavation of the Villa of the Papyri [[historical_analysis_of_world_war_i_and_world_war_ii | historical analysis of World War I and World War II]].

## The Nature of the Scrolls and Simulation

### Papyrus Manufacturing
Papyrus is made from a grassy reed found on the Nile. The inner core is cut into strips, laid out in two perpendicular layers, pressed, and dried. Sheets are then glued together with flour paste to form a long scroll. Papyrus has a noticeable texture due to its fibers.

### Simulating Carbonization
To better understand the artifacts, Nat Friedman attempted to simulate the carbonization process. Papyrus scrolls were placed in a Dutch oven (to remove oxygen) at 500 degrees Fahrenheit for five to six hours. The resulting carbonized scrolls were incredibly light, fragile, and would readily fall apart or turn to dust if handled. They shrink, blister, and layers can separate or fuse. This experiment helped replicate the challenges faced by early excavators.

## Speculation on Scroll Contents
While some known texts are by Philodemus, the contents of the unopened scrolls are unknown. Potential discoveries include:
*   More Epicurean philosophy.
*   Lost epic poems, stories, or historical texts.
*   Information about early Christianity, such as a contemporaneous mention, which would be considered a very significant find.
*   Older texts: Some scrolls already found were hundreds of years old at the time of the eruption. The villa was constructed about 100 years prior to AD 79. There's speculation, though acknowledged as potentially wishful thinking, that some scrolls evacuated from the Library of Alexandria (burned 80-90 years prior) might have ended up in this prominent villa.

## Future Outlook and Broader Implications
The successful decipherment of even one scroll is hoped to be a catalyst, demonstrating the viability of the techniques and leading to increased funding for scanning the remaining scrolls and for new archaeological excavations at the Villa of the Papyri [[challenges_and_opportunities_in_deploying_ai_at_scale | challenges and opportunities in deploying AI at scale]]. Friedman expresses a 50% chance that the challenge will be solved within the year of its launch, due to the accessibility of data and the potential for someone to be "nerd sniped" by the problem.