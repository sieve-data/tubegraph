---
title: Challenges and considerations in stock trading using AI
videoId: EONHTpg_fag
---

From: [[everyinc]] <br/> 

The use of Artificial Intelligence (AI) models like Gemini in stock trading presents both exciting opportunities and significant challenges, as demonstrated by an experiment aiming to replicate a highly successful Nvidia investment [00:00:10]. While AI offers powerful analytical capabilities, limitations in data access, real-time information, and the AI's inherent caution can complicate its practical application in financial decision-making [01:24:04].

## The AI-Assisted Stock Picking Process

The core idea was to find an investment as successful as a past Nvidia trade, which saw a share price increase from $33 in January 2019 to $800 [00:00:00]. This involved downloading earnings call transcripts from 2022 and 2023 and loading them into Gemini [00:00:17].

The initial investment strategy involved identifying companies that had:
1.  Suddenly traded down for a temporary, exogenous reason [00:07:50].
2.  Were not yet massive but had the potential to become a "10-bagger" (e.g., market cap between a few billion and $100 billion) [00:10:07].
3.  Were in positive gross profit to avoid "total bozo risk" [00:10:49].
4.  Possessed an extremely scalable business model [00:54:38].
5.  Sat at a key bottleneck in their value chain [00:45:13].

Using a stock screener (TradingView), initial filters were applied for market cap, positive gross profit, and a six-month performance showing a significant downturn (e.g., down 20%) while still maintaining positive long-term growth (e.g., five-year performance at or above zero) [00:10:00].

### Initial AI Filtering Attempts

When presented with a list of filtered stocks, Gemini initially suggested companies like Bill Holdings Incorporated, Clavio, and Appen [00:14:30]. However, the AI's responses were highly cautious:
> "Good caveat, it's important to remember that past performance is not indicative of future results and finding the next 10 bagger is extremely difficult. While your Nvidia trade was successful, replicating that exact scenario is unlikely." <a class="yt-timestamp" data-t="01:14:05">[01:14:05]</a>
The AI consistently emphasized the difficulty and unlikelihood of successful replication, and its initial suggestions did not meet the desired "artificially depressed" criteria [01:18:50].

## [[challenges_in_building_ai_tools|Challenges and Limitations of AI in Investment]]

The experiment highlighted several significant challenges when using AI for stock trading:

*   **AI's Cautiousness and Liability Aversion:** Gemini and ChatGPT demonstrated a strong reluctance to provide direct investment advice or make definitive decisions [01:17:04]. This stems from concerns about liability, as highlighted by Gemini's disclaimers [01:18:40]. This forced users to "roleplay" or apply persona prompts (e.g., "pretend you're Warren Buffett") to elicit more direct guidance [01:19:00]. This cautiousness limits the AI's practical utility for direct decision-making.
*   **Lack of Real-time Data Access:** AI models often lack access to the most current financial data [01:31:06]. This proved a critical hurdle, as stock prices and market conditions change rapidly [01:32:03]. The reliance on external screeners and manual data input means the AI cannot truly assess current market sentiment or price-in events [01:36:36].
*   **Difficulty in Accessing Large Contextual Data:** While Gemini 1.5 Pro boasts a "million token context window" [00:03:15], the practical challenge lies in feeding it enough relevant data. Attempting to load multiple years of earnings call transcripts from a company like GoGo revealed that readily accessible, bulk content is often hard to find or download [01:30:30]. This issue is exacerbated by content providers potentially restricting AI indexing [01:24:37].
    *   This leads to a "broken internet" where valuable content is not easily accessible to AI models, limiting their ability to leverage their large context windows effectively [01:24:51].
*   **Generic Recommendations:** When prompted for less obvious choices or highly specific criteria (e.g., companies with extremely scalable business models outside software), AI often reverted to generic suggestions or well-known large-cap companies (e.g., Amazon, Netflix, Google, Microsoft, Visa) [01:57:52]. This indicates a challenge in the AI's ability to identify truly undervalued or niche opportunities that fit complex criteria without extensive human guidance and refinement.

## Human Element and Investor Psychology

The experiment underscored the persistent importance of human judgment and the psychological [[challenges_and_strategies_for_ai_startups|challenges and strategies for AI startups]] in investment:

*   **Refining the Investment Thesis:** The human users continuously refined their investment thesis based on the AI's responses and their own market understanding [01:32:51]. The three-part "Nvidia trade" thesis evolved to emphasize exogenous shocks, bottleneck positions, and extreme scalability, guiding subsequent AI prompts [01:05:25].
*   **The Difficulty of "Doing Nothing":** A critical insight was the psychological pressure to make a trade, even when no suitable opportunity aligned with the refined strategy [01:22:51]. As a good investor, one must be "really good at doing nothing" [01:23:04], waiting for the "fat pitches" – opportunities that obviously fit the strategy [01:23:36].
*   **"YOLO Trades" for Content:** The decision to invest in 23andMe, despite significant uncertainty and negative indicators, was acknowledged as a "YOLO trade" for "the content" [01:48:46], highlighting the emotional and external pressures that can override sound strategy. This demonstrated the human tendency to deviate from strategy even when armed with AI insights.

## The "Fat Pitch" Investment Strategy

The ideal investment was described as a "fat pitch" – a company:
1.  Experiencing a temporary depression due to an exogenous shock (e.g., the trade war for Nvidia, Apple's privacy changes for Meta) [00:42:53].
2.  Well-positioned to benefit from a rapidly adopted new technology wave [00:44:00].
3.  Possessing an extremely scalable business model that can grow significantly without hitting bottlenecks (e.g., Nvidia's fabless model, Meta's ad revenue scalability) [00:54:57].
4.  Sitting at a key bottleneck in its value chain, allowing it to capture the lion's share of new market opportunities [01:01:16].

## The Ultimate Investment Decision: Alphabet (Google)

After rejecting 23andMe due to its precarious financial and legal challenges [01:55:00], the team decided to invest in Alphabet (Google) based on the refined thesis [01:08:10].

The justification for Google as a "fat pitch" included:
*   **Exogenous Shock:** Recent negative perception due to Gemini's public issues [01:30:28] and earnings disappointment related to increased capex for AI integration [01:31:22]. This created a perception of Google being "incredibly corporate, woke, unable to get out of its own way" [01:32:05].
*   **Scalable Business Model:** Google was noted for having "one of the most scalable business models ever conceived" [01:32:54]. Despite increased AI-related costs, Google's internal semiconductor design and cloud infrastructure give it a structural advantage [01:33:15].
*   **Tailwind from Technology Wave:** Google is positioned to benefit significantly from the AI wave, particularly in [[the_role_of_ai_in_financial_analysis_and_trading|AI-based search]] and [[use_of_ai_in_writing_and_investment|LLM-generated experiences]] [01:33:47]. The perceived temporary challenges are akin to past rocky periods faced by Microsoft or Apple, which they overcame to grow strongly in subsequent technology waves [01:34:10].

A $1,087 investment was made into Google, rolling over initial winnings from a small 23andMe trade [01:35:16].

## Broader Implications for AI and Content

The experiment also illuminated broader implications for content and AI development:

*   **Value of Accessible Content:** The roadblocks encountered in accessing readily available data (like earnings call transcripts or analyst reports) highlight a significant opportunity for content publishers [01:24:51]. If AI models could seamlessly access and process large volumes of licensed content (e.g., through paid APIs), it would greatly enhance their utility [01:25:01].
*   **New Revenue Streams for Content Creators:** This could create new revenue streams for publishers and content creators, as users would be willing to pay for their AI models to access specific, valuable datasets [01:25:21]. This shifts the focus from human consumption of entire books to AI models extracting relevant insights from them [01:25:31].
*   **The "Golden Age" of LLM Use:** There's a concern that the increasing caution and "milk toast" responses from large-scale LLMs, due to liability and regulation, might limit their usefulness [01:27:06]. This could open opportunities for developers to build models "willing to return riskier results" or operate with fewer restrictions, potentially leading to a "Golden Age of LLM use" before excessive lockdown [01:27:18].

## Conclusion

While AI like Gemini offers a powerful tool for sifting through data and identifying trends, its current application in active stock trading is limited by data access, real-time information gaps, and an inherent reluctance to provide direct, actionable advice. The experiment showcased that effective AI-assisted trading still requires significant human strategic refinement, market understanding, and the discipline to wait for truly opportune "fat pitches." The true potential of AI in investment, particularly leveraging its massive context windows, remains tied to the future of content accessibility and the regulatory environment governing AI recommendations.