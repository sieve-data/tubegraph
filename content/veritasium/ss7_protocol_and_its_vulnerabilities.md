---
title: SS7 protocol and its vulnerabilities
videoId: wVyu7NB7W6Y
---

From: [[veritasium]] <br/> 

**Signaling System No. 7 (SS7)** is a protocol that serves as the backbone for 2G and 3G telecommunications, widely in use today for routing calls and messages [07:02]. While designed to be secure, it has significant vulnerabilities that can be exploited for call interception, SMS interception, and location tracking [07:05].

## History of Phone System Exploitation
Before SS7, telephone networks relied on different methods for connecting calls, some of which were susceptible to exploitation.

### Early Manual Connections
Until the mid-1920s, most phones lacked dialing capabilities [02:24]. When a receiver was lifted, a voltage drop alerted an operator at the telephone exchange, who would then manually connect the call after being told the desired recipient [02:29]. This labor-intensive process, requiring hundreds of connections per hour, led to a prediction in 1910 that the telephone system would soon need to employ every working-age woman in the country as an operator [03:03]. By 1950, over a million operators were employed in the US alone [03:14].

### Rotary Dial Automation
To reduce costs, companies sought to automate call connection [03:19]. The rotary dial telephone was a solution, sending electrical pulses down the phone line to match each dialed number (e.g., two pulses for the number two) [03:23]. These pulses were known as control signals [04:06]. However, as transmission lines increased in length, capacitance and resistance caused signals to distort, preventing pulses from triggering switches at the exchange, making automated long-distance calls almost impossible [04:08].

### Touch-Tone Telephones and Frequency Exploitation
Phone lines were built to carry sounds within the human voice range (300 to 3,400 Hertz) [04:31]. This led to the introduction of the touch-tone or push-button telephone, which used combinations of two tones (specific frequencies for horizontal and vertical axes) to uniquely identify each button [04:42]. By sending control signals within the voice band, telephone networks could receive them using existing systems regardless of distance [05:06].

This innovation created an opportunity for early hackers like Steve Jobs and Steve Wozniak, who created a "blue box" in the 1970s [01:24]. Long-distance calls were expensive then, costing up to $25 a minute (adjusted for inflation) for a call from New York to London [01:15]. Jobs and Wozniak's device hacked the telephone network, allowing them to trick the company into connecting calls for free [01:26].

They exploited a vulnerability where a central node and a remote node in a long-distance call setup would send a 2600 Hertz tone to determine if a line was free [05:21]. By dialing a toll-free 1-800 number to enter a local node, they would then send a 2600 Hertz tone into the phone [05:39]. This tricked the remote node into thinking the call had been disconnected, causing it to restart playing the 2600 Hertz tone [05:49]. Since Jobs and Wozniak were still on the line, when they stopped playing the tone, the remote node assumed a new call was being placed [05:57]. By following a key pulse tone with the desired phone number and an ending start tone, they could connect to any long-distance number for free, as the home node still believed it was connected to a toll-free number [06:06]. Some even used a toy whistle from a Cap'n Crunch cereal box, which happened to make the 2600 Hertz frequency, to mimic this tone [06:28]. [[history_of_phone_system_hacks | This type of exploitation of phone systems]] was known as "phreaking" [15:26].

## Introduction of SS7
The vulnerabilities in the tone-based signaling system led telephone companies to develop a new signaling protocol [06:38]. Their solution was to use a separate digital line to carry control signals, preventing network control via voice line tones [06:43]. This new protocol was named Signaling System No. 7, or SS7 [06:57].

## SS7 Vulnerabilities
Despite its original design, SS7 is not as secure as once thought, primarily due to changes in the telecommunications landscape [07:05].

### The "Walled Garden" Approach and its Breakdown
When SS7 was introduced in 1980, mobile phones were rudimentary, mainly used as car phones [08:42]. The telecommunications landscape was dominated by a few large, reputable operators with established relationships and mutual interests in network integrity [10:26]. SS7 was designed as a "walled garden" – a closed network with few barriers once inside [10:11]. Telcos would typically establish agreements with two providers (one primary, one backup) in each country to provide global roaming coverage [09:59]. They would only accept messages from Global Titles (GTs) with which they had agreements, using these unique addresses to identify request origins [10:06]. This system allowed telcos to communicate for roaming purposes, where a foreign network could reach out to a home network to validate a customer and confirm payment willingness, all exchanged over SS7 [09:01].

However, the landscape has dramatically shifted [10:39]. Now, there are over 1,200 operators and 4,500 networks, many needing SS7 access, including virtual network operators and mass-text services [10:43]. Not all these new players are trustworthy; some sell services, can be bribed, or hacked [10:57]. This means there are "thousands of ways into SS7 at reasonable effort or cost" [11:12].

### Cost of SS7 Access
Buying a single SS7 connection can cost a few thousand dollars per month [11:24]. A valuable US-based GT was observed being leased illegally for $13,000 a month [11:47]. Accessing a trusted GT grants access to all the GTs with which it has partnerships [11:37]. Security specialists like Karsten Nohl pay for SS7 access to conduct security tests and simulate real hacker positions [11:56].

## SS7 Attack Methodology
Cybersecurity specialists Karsten Nohl and Alexandre De Oliveira outlined three steps to spy on a target using SS7 [08:27]:

1.  **Infiltrate SS7:** This involves gaining access to the network, often by leasing a trusted Global Title (GT) [08:30].
2.  **Gain Trust (IMSI Harvesting):** Even with a trusted GT and a phone number, a unique 15-digit identifier called the International Mobile Subscriber Identity (IMSI), belonging exclusively to the SIM card, is needed for unique identification [12:20]. Messages like "send routing info" or "send routing info for SM" are used to collect the IMSI [12:55]. Networks have firewalls to deny suspicious requests, so obtaining the IMSI is crucial to appear trusted [13:07].
3.  **Attack:** Once trusted, various attacks can be launched.

### Call Interception and Rerouting
Attackers can seize control of a target's phone number [16:18]. By tricking the network into thinking the target's phone is roaming, the attacker can rewrite the number being called to a number they control [16:49]. This rerouting is a powerful function; for example, a call intended for Linus was rerouted to the interviewer's phone, and Linus's phone did not ring [14:03]. The attacker can even act as a middleman, rerouting a call to themselves while simultaneously dialing the real number for the target, allowing them to record the conversation [17:55]. At its simplest, only the target's phone number is needed for this type of attack [17:48].

### SMS Interception
Similar to call interception, attackers can trick the network into believing the target is roaming, rerouting their text messages to the attacker's GT [18:15]. This allows the attacker to steal one-time passwords (OTPs) used in two-factor authentication (2FA) [18:26]. This type of attack works until the subscriber interacts with their phone network, which reconnects the phone to the correct GT [18:31]. However, only a few seconds are needed to receive the OTP and hack into an account [18:39].

The process demonstrated involved obtaining a username/password (e.g., via a data dump or keylogger) and then, when the system requests a 2FA code to verify the number, intercepting that SMS code via SS7 [18:50]. The attacker receives the code, inputs it, and gains access to the account, while the target never receives the message or knows it was intercepted [19:18].

### Location Tracking
SS7 attacks can also be used to track a target's location, without relying on GPS (SS7 predates public GPS use) [20:52].
One method is to identify the cell tower the target is connected to [21:34]. In urban areas with many towers, this can pinpoint a location to within a hundred meters [21:40]. This is useful for determining if someone is at home or work [21:47].
Another method involves using the IMSI number harvested in step two to send a command deeper into the network, targeting the switching center where the device is connected [20:33]. This command, routinely used for legitimate purposes like call routing or emergency services, can be exploited to track location [20:42].

#### "Anytime Interrogation"
A command called "anytime interrogation request" used to allow requests for location over SS7 without even knowing the IMSI, with networks providing it with no questions asked [25:35]. Experts state there is no legitimate purpose for one network to send this command to another network to interrogate customers [25:53].

## Real-World Impacts of SS7 Vulnerabilities
[[impact_of_mobile_phone_security_breaches | Mobile phone security breaches]] involving SS7 have had serious consequences.

### Princess Latifa Abduction
In 2018, Princess Latifa Al Maktoum of Dubai, who claimed her father held her in solitary confinement, attempted to escape [07:10]. Her escape yacht captain was the victim of a coordinated SS7 attack aimed at pinpointing his location and, by extension, the princess's [08:00]. Attackers leased multiple GTs in different countries [22:48]. Within a five-minute window, they sent at least seven requests to get the captain's IMSI from his US-based operator, followed by at least four location requests [22:54]. While many requests were blocked by firewalls, requests from a sixth GT (a nearby US one) likely were not stopped, indicating a successful breach [23:10]. An investigative journalist described this as a "textbook example of telco penetration risks," illustrating a classic sophisticated attack pattern with multiple GTs in multiple countries [23:35]. Although other surveillance tools like Pegasus spyware and spotter planes were also used, SS7 was a contributing factor [23:48].

### Financial Fraud and Cyber Espionage
Criminals have used SS7 to intercept SMS 2FA codes and empty millions of dollars from bank accounts [24:06]. For some, SS7 is a first step in more complex attacks [24:13]. The NSO Group, an Israeli cyber-surveillance firm known for Pegasus spyware, acquired an SS7 tracking company in 2014 [24:16]. Pegasus is a "zero-click" hack, gaining complete access to targeted phones without user interaction, embedding itself and erasing traces of entry, though such exploits can cost over $4 million [24:24]. Before committing resources to costly software exploits, NSO gathers basic data like device type and software version using SS7 [24:40].

### Prevalence of Attacks
One expert tested a foreign network and found 20 to 30 VIPs, including the country's chief of cybersecurity, under constant surveillance [24:55]. Another expert provided evidence of over 2.5 million tracking attempts per year [25:08]. While these targets are generally people of interest to state agencies, millions of malicious SS7 requests are sent annually [25:15].

## Addressing SS7 Vulnerabilities
The SS7 research disclosed in 2014 by Karsten Nohl and Tobias Engel was a "wake-up call" to the industry [26:03]. They publicly exposed these vulnerabilities, demonstrating how easily a "ragtag gang of hackers" could perform SS7 hacking [26:05]. After their conference, all German telcos immediately began refusing "anytime interrogation" requests, as it was widely abused [26:34].

However, while "anytime interrogation" was stopped, over 150 other messages still need to be secured to make SS7 completely safe [26:47].

### Reasons for Continued Use
Despite its known vulnerabilities, SS7 remains in widespread use because it is the backbone of 2G and 3G communications [26:59]. Phasing out 2G and 3G causes problems; for instance, cars in the EU since 2018 are equipped with mandatory emergency call buttons that trigger in an accident, using 2G and 3G SIM cards that rely on SS7 to cut costs [27:10]. Legacy support for 2G/3G is also critical for situations where 4G connectivity drops [27:27].

There has not been a global push to replace SS7 with its two newer, more secure versions, the latest of which was introduced with 5G [27:41]. This is due to "first mover disadvantage" – networks gain nothing by adopting the technology first, preferring to be the last to join when everyone else is already connected to reap full benefits [27:54]. The inertia makes moving on "extremely difficult" [28:28]. Experts predict it could take another 10, 15, or even 20 years until SS7 networks are finally switched off unless major events put it back on the public radar [28:35].

## [[steps_individuals_can_take_to_protect_against_ss7_attacks | Steps Individuals Can Take to Protect Against SS7 Attacks]]
On a personal level, protection against SS7 attacks is limited, especially for location tracking, as long as a SIM card is used [29:06].

*   **Two-Factor Authentication (2FA) Alternatives:** If possible, choose alternatives to SMS-based 2FA, such as Authenticator apps or hardware tokens, to prevent message interception [29:11].
*   **Encrypted Calling Services:** For concerns about phone tapping, use encrypted internet-based calling services like Signal or WhatsApp [29:21].

While these attacks mainly target "people of interest" (e.g., to state agencies), SS7 represents a significant privacy intrusion with millions of abuse cases monthly [29:27]. For some, privacy and the ability to form thoughts without observation are prerequisites for democracy [29:32].