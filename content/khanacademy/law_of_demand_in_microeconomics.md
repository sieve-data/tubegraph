---
title: Law of demand in microeconomics
videoId: ShzPtU7IOXs
---

From: [[khanacademy]] <br/> 

The law of demand is a fundamental concept in [[introduction_to_microeconomics_and_macroeconomics | microeconomics]] <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. It states that if the price of a product increases, the [[difference_between_quantity_demanded_and_demand | quantity demanded]] for that product will decrease <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. Conversely, if the price of a product decreases, the [[difference_between_quantity_demanded_and_demand | quantity demanded]] will increase <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. This is generally true, though there are some exceptions <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

## Demand vs. Quantity Demanded

It is crucial to distinguish between the terms "demand" and "[[difference_between_quantity_demanded_and_demand | quantity demanded]]" in economics <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>:

*   **[[difference_between_quantity_demanded_and_demand | Quantity Demanded]]**: Refers to a specific amount of a product that consumers are willing to buy at a given price <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>.
*   **Demand**: In a formal economic sense, "demand" refers to the entire relationship between various prices and the corresponding [[difference_between_quantity_demanded_and_demand | quantities demanded]], assuming [[ceteris_paribus_in_economic_analysis | all else is equal]] <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. This relationship can be represented by a [[demand_schedule_and_its_significance | demand schedule]] or a demand curve <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.

When price changes, and [[ceteris_paribus_in_economic_analysis | everything else remains equal]], it causes a change in the [[difference_between_quantity_demanded_and_demand | quantity demanded]], not a change in demand <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. A change in demand implies a shift in the entire relationship (the curve itself), which is influenced by other factors not related to the product's price <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.

## The Demand Schedule

A [[demand_schedule_and_its_significance | demand schedule]] is a table that illustrates the relationship between the price of a product and its [[difference_between_quantity_demanded_and_demand | quantity demanded]], holding [[ceteris_paribus_in_economic_analysis | all other factors constant]] <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

**Example: "Space Whatever" Ebook**
Consider an ebook titled "Space Whatever" <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>:

| Scenario | Price (P) | Quantity Demanded (QD) |
| :------- | :-------- | :----------------------- |
| A        | $2        | 60,000                   |
| B        | $4        | 40,000                   |
| C        | $6        | 30,000                   |
| D        | $8        | 25,000                   |
| E        | $10       | 23,000                   |

This table explicitly demonstrates the law of demand: as the price increases, the [[difference_between_quantity_demanded_and_demand | quantity demanded]] decreases <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

## The Demand Curve

A demand curve is a graphical representation of the [[demand_schedule_and_its_significance | demand schedule]], plotting the price against the [[difference_between_quantity_demanded_and_demand | quantity demanded]] <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

By convention in economics, price is typically plotted on the vertical (y) axis, and [[difference_between_quantity_demanded_and_demand | quantity demanded]] is plotted on the horizontal (x) axis <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

Using the "Space Whatever" ebook example:

*   **Vertical Axis (Price)**: Ranges from $2 to $10 <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.
*   **Horizontal Axis (Quantity Demanded)**: Ranges up to 60,000 units (in thousands) <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

When these points are plotted and connected, they form a downward-sloping curve, illustrating the inverse relationship between price and [[difference_between_quantity_demanded_and_demand | quantity demanded]] <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>. The curve is continuous, representing that any price point between the plotted scenarios is possible <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.

```mermaid
graph LR
    subgraph Demand Curve for "Space Whatever" Ebook
        direction LR
        P --- Q
        style P fill:#fff,stroke:#333,stroke-width:2px
        style Q fill:#fff,stroke:#333,stroke-width:2px

        subgraph Axes
            Price(Price)
            QuantityDemanded(Quantity Demanded)
        end

        subgraph Points
            A((A: $2, 60k))
            B((B: $4, 40k))
            C((C: $6, 30k))
            D((D: $8, 25k))
            E((E: $10, 23k))
        end

        Price --plots on--> VerticalAxis
        QuantityDemanded --plots on--> HorizontalAxis

        VerticalAxis --- 10 --higher price--> 8 --still higher--> 6 --mid-range--> 4 --lower price--> 2
        HorizontalAxis --- 60 --lower quantity--> 40 --still lower--> 30 --mid-range--> 25 --even lower--> 23

        linkStyle 0 stroke-width:0px; /* Hide default P-Q link */

        A --> B
        B --> C
        C --> D
        D --> E

        classDef invisible stroke-width:0px,fill:none;
        class Price,QuantityDemanded invisible;
    end

    style Price fill:#fff,stroke:#333,stroke-width:2px
    style QuantityDemanded fill:#fff,stroke:#333,stroke-width:2px
```
*Note: Mermaid's graph capabilities are limited for drawing a precise curve or axes with scales. The visual above conceptually represents the downward slope and points.*

## Movement Along vs. Shift of the Curve

*   **Movement along the curve**: When only the price changes (and [[ceteris_paribus_in_economic_analysis | all else is equal]]), the change in [[difference_between_quantity_demanded_and_demand | quantity demanded]] is represented by a movement along the existing demand curve <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.
*   **Shift of the curve**: If other factors influencing demand (e.g., consumer income, tastes, prices of related goods) change, the entire demand relationship shifts, resulting in a new demand curve <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. These [[factors_influencing_changes_in_demand_and_quantity_demanded | factors influencing changes in demand]] will be explored in future discussions <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.