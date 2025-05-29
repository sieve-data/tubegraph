---
title: Industrial espionage and the Rubycon incident
videoId: rSpzAVpnXo4
---

From: [[asianometry]] <br/> 

In the early 2000s, reports began to surface of PC motherboards experiencing "leaking or even popping capacitors," leading to computer failures [00:00:02]. This widespread issue became known as the "Capacitor Plague" [00:00:43]. While the exact cause remains debated, one prominent theory links it to an alleged incident of [[technology_transfer_and_espionage_in_east_germany | industrial espionage]] involving the Japanese company Rubycon [00:14:25].

## The Rubycon Story

The narrative of the Rubycon incident was first reported by Dennis Zogbi in the September/October 2002 issue of "Passive Component Industry" magazine [00:07:15]. According to this account:
*   A materials scientist employed by the Japanese electronics company Rubycon Corporation departed to work for Luminous Town Electric, a Taiwanese company with a factory in China [00:07:25].
*   The scientist allegedly replicated Rubycon's proprietary P-50 water-based electrolyte formula [00:07:38].
*   Luminous Town Electric subsequently used this formula in their aluminum electrolytic capacitors (E-caps), which initially appeared to function correctly [00:07:44].
*   Subsequently, some of this scientist's staff members defected from Luminous Town, taking the electrolyte formula with them [00:07:50]. They then sold it either directly to other Taiwanese E-cap companies or to an electrolyte provider who resold it [00:07:54].

The critical flaw in this transfer was that the defecting staffers did not possess the *complete* formula [00:08:04]. Essential additives were missing, which led to a build-up of hydrogen gas within the E-caps, causing them to rupture or burst [00:08:10].

Luminous Town Electric did not deny the accusation of stealing the electrolyte formulation from Rubycon [00:08:28]. Zogbi's story indicated that anywhere from 5 to 11 Taiwanese capacitor producers were affected [00:08:35]. In a 2003 interview, Zogbi stated that "anybody who uses contract manufacturers that outsource to Taiwan was affected by the problem" [00:08:41]. The incident reportedly occurred around mid-2002, though some unsourced accounts suggest it may have happened in 2001 or even 1999 [00:08:51].

Brands of the failing capacitors included generally unknown names like "Tayeh," "Choyo," or "Chhsi," and some were unmarked [00:09:12]. One company, Jackcon Capacitor Electronics, was named, but their managing director stated they had not made capacitors for motherboards in the preceding two years [00:09:24].

### The Electrolyte's Role

The electrolyte is a critical trade secret in capacitor manufacturing, determining its operating conditions, temperature, voltage, and safety [00:12:48]. These are complex chemical formulations [00:12:57]. A 2004 analysis by the Center for Advanced Life Cycle Engineering at the University of Maryland confirmed that the electrolytes in the bulging capacitors lacked a critical additive known as a "depolarizer" [00:13:09].

The absence of a depolarizer caused the electrolyte to become overly alkaline [00:13:29]. This alkalinity, combined with a lack of protective phosphate ions in the aluminum oxide dielectric, led to the dielectric dissolving into the electrolyte [00:13:44]. As the dielectric thinned, capacitance unnaturally increased, a leading indicator of bulging [00:13:56]. This exposed the underlying aluminum foil, allowing impurities to react and create electrons, which then reacted with hydrogen ions in the water-based electrolyte to generate hydrogen gas [00:14:07].

## Fallout and Denials

Several computer manufacturers acknowledged issues with Taiwanese E-cap failures following Zogbi's report [00:10:01].
*   **IBM**, then a PC manufacturer, reported a "minuscule" number of desktop PCs (less than 1%) returned for repair due to capacitor failure [00:10:11]. However, even "less than 1%" of the 148.1 million PCs shipped globally in 2002 by the PC industry (Gartner) could represent a significant number of affected machines [00:10:31].
*   Taiwanese motherboard maker **ABIT** admitted to an E-cap problem and switched from Taiwanese to Japanese suppliers [00:10:59]. ABIT subsequently faced lawsuits for selling defective capacitors, with some linking the start of the "Capacitor Plague" to their 1999 issues [00:11:00]. The costs associated with settling and repairing defective boards may have contributed to ABIT's eventual exit from the motherboard business in 2006 [00:11:17].

The electrolyte company accused of buying the flawed formula was Lien Yan in Taichung [00:11:30]. Lien Yan denied these accusations, stating that they heavily damaged their business [00:11:39]. They also pointed out that suppliers of several bulged capacitors had never purchased electrolyte from them [00:11:44]. Lien Yan characterized the Rubycon story as "FUD" (fear, uncertainty, and doubt) spread by Japanese companies to regain market share from Taiwan [00:11:49]. Luxon, another major Taiwanese capacitor supplier, issued a statement blaming Lien Yan ("Lenyan") for the problems, emphasizing their self-development of electrolyte to ensure reliability [00:11:55].

> [!quote]
> Luxon definitely understands that the electrolyte is one of the most important materials for aluminum electrolytic capacitors. In order to ensure our reliability and innovative technology Luxon always develops the electrolyte by ourselves. <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>

## Skepticism Regarding a Single Cause

While [[technology_transfer_and_espionage_in_east_germany | industrial espionage]] is a real phenomenon and the Rubycon incident "couldn't *not* be true," the narrator expresses skepticism that the entire "Capacitor Plague" can be attributed solely to a single defector from Rubycon [00:14:32].

Several points contribute to this doubt:
*   **Widespread Nature**: The "Plague" reportedly affected a wide array of electronics beyond PC motherboards, including audio equipment, Samsung monitors, and Xbox consoles [00:15:00]. Attributing all such failures to the Rubycon story might be an oversimplification [00:15:05].
*   **Unrelated Failures**: The original Xbox, released in November 2001, is known for a faulty clock capacitor that typically fails after 6-7 years [00:15:29]. However, this specific capacitor was a PowerStor Aerogel supercapacitor made by Cooper Industries (an American company), not an aluminum E-cap, and thus unrelated to the Rubycon incident [00:15:42].
*   **Inconsistent Timelines**: Zogbi's account places the Rubycon incident in mid-2002 [00:16:39]. Yet, a poor electrolyte E-cap was expected to fail within a year, or even as little as 250 hours of operation, according to Intel in 2002 [00:16:55]. This contradicts reports of "sleeper" E-caps continuing to fail into 2007 [00:17:07].
    *   For instance, a new round of capacitor failures gained prominence in late 2005, affecting Apple, Hewlett-Packard, and especially Dell [00:17:16]. From May 2003 to July 2005, Dell shipped 11.8 million OptiPlex PCs with faulty capacitors that were ten times more prone to bulging, leading to a $300 million payout for replacements in 2007 [00:17:24]. These faulty capacitors originated from Nichicon in Japan, though insiders reportedly told Zogbi in 2005 that they were made by a Taiwanese sub-contractor [00:17:49].
*   **Technological Challenges**: An alternative explanation suggests that the "Plague" might have been an "extended series of unconnected challenges faced by the capacitor industry as a whole" [00:14:53].
    *   The early 2000s saw Intel and AMD aggressively increase single-core clock rates, leading to microprocessors consuming significant power and generating considerable heat [00:19:12]. This coincided with the introduction of new Low-ESR aluminum E-caps using water-based electrolytes in the late 1990s [00:18:56]. The theory posits that the increasingly hot microprocessors caused these new water-based electrolytes to boil, creating gas that ruptured the capacitors [00:19:34]. The transition to multi-core CPUs by AMD and Intel starting in 2005 reduced internal temperatures, and capacitor manufacturers simultaneously improved their aqueous electrolyte formulations, contributing to the end of the "Capacitor Plague" [00:19:49].
*   **Counterfeit Components**: The increasing complexity of the supply chain and the outsourcing of components to no-name suppliers contributed to issues [00:20:07]. When supply disruptions occurred, manufacturers might turn to unauthorized distributors, inadvertently purchasing counterfeit capacitors that would fail prematurely [00:20:25]. A 2014 study of counterfeit Nichicon E-caps found that their water-based electrolyte lacked sufficient ethylene glycol, lowering its boiling point and making it unstable at higher temperatures [00:20:56].

The Rubycon incident story, while intriguing and plausible as a specific event of [[technology_transfer_and_espionage_in_east_germany | industrial espionage]], is viewed by some as an "urban legend" that became associated with a broader technical challenge faced by the capacitor industry [00:21:41]. While aluminum E-caps with water-based electrolytes still exist with longevity concerns, vendors have largely resolved the major issues [00:21:53].