---
title: History and evolution of the Cray Supercomputer
videoId: SOQ6F7HMfSc
---

From: [[asianometry]] <br/> 

Computer designer [[seymour_crays_career_and_contributions_to_supercomputing | Seymour Cray]] had a singular focus: to build the biggest computer in the world, stating his five-year goal as such and his one-year goal as one-fifth of that [00:00:09]. His lifelong quest was dedicated to making the biggest supercomputers [00:00:23].

## Beginnings

[[seymour_crays_career_and_contributions_to_supercomputing | Seymour Cray]] Jr. was born in Chippewa Falls, Wisconsin, in 1925, the son of a civil engineer [00:00:43]. His father encouraged his love for science and engineering, and the young Cray excelled in chemistry, electrician work, and radio [00:00:53]. After serving as an army electrician, Cray attended the University of Minnesota, earning a bachelor's in electrical engineering and a master's in applied math [00:01:04].

In 1950, Cray joined Engineering Research Associates (ERA) in St. Paul, Minnesota [00:01:16].

### ERA's Origins
During World War II, the US Navy had an elite code-breaking division called the Communications Supplementary Activity - Washington (CSAW), which secretly designed machines to break Axis naval codes, primarily to track German submarines [00:01:24]. After the war, with budget cuts, the Navy needed to continue breaking codes, especially Soviet ones, but couldn't afford to retain their employees [00:01:41]. To solve this, the Navy collaborated with investment banker John Parker to establish ERA as a for-profit company that would hire the old team at higher salaries [00:01:51].

ERA operated largely in secret from an old glider factory, initially producing code-breaking machines [00:02:02]. The team soon shifted towards general-purpose computers, leveraging emerging technologies like [[history_and_evolution_of_hard_disk_drives | magnetic drum memory]] [00:02:10]. One of their early products was the ERA 1101, a commercialized version of a device sold to a precursor of the NSA [00:02:19]. Minnesota in the 1950s became a premier computing center, often considered "Silicon Valley before Silicon Valley existed," due to a strong military presence [00:02:28].

### Working With Cray at ERA
At 25, [[seymour_crays_career_and_contributions_to_supercomputing | Cray]] proved to be a talented and quiet worker with unwavering confidence, incredible focus, rigid discipline, and a brilliant understanding of binary numbers [00:02:40]. He was tasked with designing the control system for ERA's next computer, the ERA 1103, which required comprehensive knowledge of the computer's internal workings to break down software instructions into execution steps [00:02:58]. Cray successfully completed the work and quickly rose to supervise a team [00:03:20].

Like [[history_of_sun_microsystems | An Wang]] of Wang Labs, Cray's genius could make him a challenging boss [00:03:25]. He preferred working alone, often spending late evenings in the workshop, and would reassign tasks and complete them himself if he felt someone wasn't performing adequately — a process employees called "being scrayed" [00:03:30]. Despite this, Cray was generally liked and respected by his colleagues, viewed as eccentric and enigmatic [00:03:44].

### Remington Rand Acquisition
In December 1951, John Parker, ERA's president and original investor, sold the company to Remington Rand without informing employees, causing anger among key staff like William Norris, who was then VP of Operations [00:03:58]. Remington Rand, primarily a typewriter and shaver company, had previously acquired the Eckert–Mauchly Computer Corporation [00:04:20].

J. Presper Eckert and John Mauchly were renowned for creating ENIAC, the first programmable digital computer, and EDVAC, which pioneered the stored program computer design that underpins the [[technological_innovations_and_challenges_in_supercomputer_design | Von Neumann architecture]] [00:04:32]. Eckert also created the Moore School Lectures, which popularized the [[technological_innovations_and_challenges_in_supercomputer_design | Von Neumann architecture]] [00:04:47]. The UNIVAC I, another Eckert–Mauchly creation, gained fame for accurately predicting Dwight Eisenhower's victory in the 1952 US presidential election [00:04:59].

Given Eckert and Mauchly's strong credentials, ERA employees accepted the acquisition [00:05:09]. The arrangement dictated that Eckert–Mauchly would focus on the business computer market, while ERA would concentrate on scientific computing [00:05:13].

### Tensions Remain
Despite the division, tensions persisted. In the early days of computing, business and scientific needs required distinct computer designs [00:05:24]. Business computers performed simple operations (addition, subtraction, multiplication) with low accuracy but on a large scale, processing thousands of rows of data [00:05:34]. Scientific computing, conversely, demanded complex calculations with high accuracy (up to 20-30 decimal points) and could take hours to produce a single line of output [00:05:50].

The Eckert–Mauchly team in Philadelphia viewed the Minnesota-based ERA team as mere "farmers" who didn't work on state-of-the-art technology [00:06:04]. Conversely, the Minnesota team saw the Philadelphians as theoreticians focused solely on speed, even at the cost of reliability [00:06:13].

Tensions worsened in 1955 when Rand merged with Sperry Corporation to become Sperry Rand, consolidating the two independent units into one Univac division [00:06:22]. William Norris, the division's new general manager, openly criticized the Philadelphia team, stating, "You people run a laboratory and ERA runs a business" [00:06:36]. Sperry's top management believed they were acquiring a market leader, but UNIVAC, despite its potential to become what IBM eventually did, lacked the necessary capital for R&D and to support the capital-intensive equipment leasing business model of the time [00:06:52].

### Control Data Corporation
By 1957, William Norris, fed up with Sperry Rand, left to found a new company, Control Data Corporation (CDC) [00:07:17]. Although a significant risk, Norris was prepared to return to his Nebraska farm if it failed [00:07:29]. He invited several ERA coworkers to join him, and [[seymour_crays_career_and_contributions_to_supercomputing | Cray]] accepted, having noted his project being categorized as "999 Miscellaneous and Other" by the accounting system [00:07:35].

CDC launched in July 1957 with employees, a vague plan for computers, and limited funds from friends [00:07:51]. With no plant or product, CDC raised capital through an IPO, literally selling shares on the street for a dollar each [00:07:59]. The company gained unexpected publicity when sports columnist Sid Hartman mentioned their venture [00:08:15]. Many prominent local investors declined, believing CDC had "not a ghost of a chance" against IBM [00:08:31]. Notably, [[seymour_crays_career_and_contributions_to_supercomputing | William Norris's]] nephew by marriage, Warren Buffett, also declined due to a lack of understanding [00:08:41]. Years later, those initial $1 shares became significantly more valuable, enriching 300 initial investors and creating wealth in Minnesota [00:08:53].

## The CDC 1604

[[seymour_crays_career_and_contributions_to_supercomputing | Cray]], as the most technical person at CDC, convinced his cofounders to build scientific computers rather than entering the commercial market [00:09:07]. His rationale was that clientele like universities and nuclear weapons research labs were less concerned with marketing or client service and programmed their own software [00:09:16]. They demanded immense compute power [00:09:26]. Simulating nuclear weapon detonations, which involved stepping through equations every micro-second, required the biggest and fastest computers available [00:09:31].

Cray believed he could build such a computer cost-effectively using transistors [00:09:54]. He discovered cheap, reject bipolar transistors from a local electronics shop that outputted a weak signal [00:10:04]. Cray ingeniously paired them in a Darlington pair, using the second transistor to amplify the first's output, demonstrating that with the right design, substandard components could still achieve the desired goal [00:10:10].

In 1958, with money running low, Bill Norris secured a deal with the US Navy for what would become the CDC 1604 computer [00:10:29]. Building it at scale required buying a factory and hiring engineers [00:10:40]. Managers, including Norris, halved their salaries, and engineers resorted to using free sales samples from transistor companies [00:10:45].

The CDC 1604 launched in 1960, priced at $990,000 (about $10.4 million today) [00:10:55]. At 0.2 megahertz, it was the most powerful commercially available computer of its time—a supercomputer [00:11:06].

### Supercomputers in the Era
The term "supercomputer" is fluid, referring to a computer that pushes the boundaries of computing and leads its field [00:11:13]. Control Data was not the sole player in fast computers for niche customers [00:11:23]. UNIVAC released the Livermore Automatic Reaction Calculator (LARC) in 1960, which helped Edward Teller simulate the hydrogen bomb and was the world's most powerful computer from 1960 to 1961 [00:11:27]. The LARC spurred IBM to build the IBM 7030 STRETCH supercomputer, designed by Gene Amdahl, which held the crown for world's most powerful until 1964 [00:11:45].

However, the LARC and STRETCH were largely made-to-order products, with UNIVAC producing only two LARC units [00:12:01]. Control Data, with the 1604, turned the supercomputer into a commercially successful category [00:12:07]. The 1604 was sold to institutions like the University of Illinois, Lockheed, and the State of Israel [00:12:13]. CDC began turning a profit, challenging older computer giants like Rand and IBM, with its stock rising from $1 to $9 [00:12:20].

## The CDC 6600

After the 1604, [[seymour_crays_career_and_contributions_to_supercomputing | Cray]] and CDC debated their next move [00:13:34]. While some favored iterating on the 1604 architecture to attack the business data processing market, Cray was solely focused on building the fastest possible machine [00:13:39]. The scientific community was beginning to adopt [[technological_innovations_and_challenges_in_supercomputer_design | Finite Element Analysis]], a new computational modeling method that involved breaking down complex systems into millions of simpler elements for simulation [00:13:00]. This method implied an infinite need for compute power, which Cray aimed to fulfill [00:13:25].

Cray threatened to leave CDC if he couldn't pursue his vision, leading Norris to agree to split the teams [00:13:44]. The 35-year-old Cray and his team were allowed to open their own lab in his hometown of Chippewa Falls, Wisconsin, to work on the 6600, a machine designed to be 15 times faster than the 1604 [00:13:55].

### Technological Innovations of the CDC 6600
Initial designs for the CDC 6600 resembled the 1604, using ferrite magnetic cores for memory, magnetic tape for secondary storage, and germanium transistors for compute, all within air-cooled pluggable building blocks [00:14:16]. However, [[seymour_crays_career_and_contributions_to_supercomputing | Cray]] made significant changes:
*   **Transistors**: He sourced [[technological_innovations_and_challenges_in_supercomputer_design | silicon planar transistors]] from Fairchild, which were five times faster than germanium, immediately boosting speed [00:14:43].
*   **Module Design**: Cray abandoned the building-block approach due to extensive back panel wiring causing noise, limiting I/O, and increasing data transmission time [00:14:54]. He switched to denser, more complex "cordwood modules," which had shorter wires for improved speed but were harder to repair and required freon gas cooling instead of air [00:15:12].
*   **Parallelism**: The 6600 implemented parallelism, offloading housekeeping functions [00:15:30]. It featured 11 individual computers sharing central memory, with 10 handling secondary tasks like peripherals, leaving the eleventh dedicated solely to high-speed math [00:15:44].
*   **Simplified ISA**: The 6600's CPU featured a simplified Instruction Set Architecture (ISA), stripping out instructions unrelated to scientific computing (e.g., those for large data handling relevant to commercial users) [00:16:01]. This simplification allowed the computer to "pipeline" tasks, breaking down large jobs into smaller ones for simultaneous processing by peripheral computers [00:16:28].

CDC delivered the first 6600 to Lawrence Livermore in 1964 [00:16:43]. Its speed—three times faster than the IBM 7030—shocked IBM. Chairman Thomas J. Watson Jr. questioned how "34 people - including the janitor" could beat the world's largest technology company. The answer was IBM's reluctance to sacrifice compatibility for speed [00:16:48].

## Discontent and the Birth of Cray Research

Despite the success of splitting teams, discontent at Control Data persisted [00:17:13]. Norris and other managers expanded CDC's business by making its own peripherals and software, and by purchasing Commercial Credit, a consumer finance company, to fund its computer leasing strategy [00:17:19]. This strategy, though seemingly smart, eventually backfired when Commercial Credit faced difficulties [00:17:30].

Over a hundred CDC 6600s were sold, including to the Atomic Energy Commission [00:17:49]. Each cost $8 million ($23 million today), limiting the market to only about 50 customers worldwide [00:17:54]. [[seymour_crays_career_and_contributions_to_supercomputing | Cray]] viewed this limited market as a feature, preferring to know his customers personally [00:18:05]. However, CDC's management increasingly believed that peripherals and services, not hardware, were the company's future [00:18:15].

CDC followed the 6600 with the 7600, hailed as the world's fastest computer and five times faster than its predecessor [00:18:22]. Despite costing only twice as much, it sold poorly due to frequent breakdowns and a weak economy [00:18:34]. The subsequent 8600 supercomputer, built with discrete transistors, aimed for an 8-nanosecond clock cycle, requiring wires shorter than 2.5 meters and extremely dense component packing [00:18:41]. Cray struggled with cooling the dense components, eventually deciding to scrap the design and start over—his characteristic "Cray way" [00:18:58].

By 1971, CDC was embroiled in an expensive antitrust lawsuit against IBM, and cash flow was low [00:19:10]. Cray was asked to cut expenses by 10%, but unwilling to do so, he cut his own salary to minimum wage ($1.25 an hour) [00:19:19]. This didn't resolve the issue, and Norris informed Cray that a complete redesign of the 8600 was impossible as two systems had already been pre-sold [00:19:28]. In 1972, Cray decided to leave and establish his own company, Cray Research [00:19:39].

## Cray Research & the Cray-1

[[seymour_crays_career_and_contributions_to_supercomputing | Seymour Cray]] founded Cray Research with $2.5 million, 20% of which was his own money, supplemented by bank loans [00:19:44]. The company's goal was to build the biggest computer, one at a time, like a master artisan, focusing on research rather than mass manufacture [00:19:53]. In a show of goodwill, Norris and Control Data invested a quarter million dollars in the new company, which Norris called "heart money" [00:20:09].

For his first computer, the Cray-1, [[seymour_crays_career_and_contributions_to_supercomputing | Cray]] aimed for revolutionary performance by turning to vector processing [00:20:19]. Most CPUs of the time used scalar processing, handling single data items one at a time, requiring many instructions for repetitive tasks [00:20:30]. Vector processing machines, however, shortcut this by processing single-dimension arrays of data (vectors) with significantly fewer instructions [00:21:01].

Control Data also explored vector processing with its STAR-100, but it was overly complicated, failed to meet promises, shipped four years late, and sold only three units [00:21:20]. [[seymour_crays_career_and_contributions_to_supercomputing | Cray]] studied the STAR-100, identifying its flaws: slow scalar processing bottlenecked performance, and vector processing implementation had a hitch where loading and storing vectors took too long, negating the speed benefits [00:21:37]. To address this, Cray introduced "vector registers," very fast intermediate memory systems that functioned like cache memory to improve speed [00:22:12].

[[seymour_crays_career_and_contributions_to_supercomputing | Seymour]] also adopted [[technological_innovations_and_challenges_in_supercomputer_design | integrated circuits]] for the first time, allowing for greater density and reduced wiring, making the Cray-1 significantly smaller than its predecessors [00:22:20]. While ICs were mature (about 14 years old), this reflected Cray's principle of choosing older, more reliable technologies, often "a decade behind" [00:22:31]. For memory, however, he broke this principle, using bipolar semiconductor memory chips to replace older core memory, which were cheaper, denser, and consumed less power [00:22:44]. The Cray-1's 12.5-nanosecond clock cycle made it five times faster than the CDC 7600, necessitating wires shorter than four feet [00:22:57].

The Cray-1 also featured an iconic circular shape for its cooling system, enhanced with aesthetic flair to differentiate it from other computers, and even included cushions [00:23:08].

### The Cray-1's Stir
The Cray-1's flashy design and world-beating speed created a huge stir upon its release in 1976 [00:23:22]. One hundred Cray-1 units were sold to various government and university labs, including the National Center for Atmospheric Research and the Department of Defense [00:23:29]. Cray Research saw massive revenue growth—150% from 1978 to 1979, and another 50% the following year [00:23:38]. Orders came in so fast (one per month, significant for an $8 million product) that a large backlog developed [00:23:44].

IBM didn't even attempt to compete [00:23:54]. Control Data, Cray's former employer, was caught off guard [00:23:57]. While they tried to produce vector computers like the Cyber-205, they had become bloated and complicated, unable to keep pace [00:24:03]. Control Data suffered significant financial losses and eventually sold off its assets in pieces, with its most profitable business by the mid-1980s being Ticketron [00:24:10].

## The Fruits of Success and New Dilemmas

[[seymour_crays_career_and_contributions_to_supercomputing | Cray's]] desire to build the fastest computer from a "clean piece of paper" drove his work [00:24:24]. Even as the Cray-1 neared completion, he shifted his focus to the Cray-2, aiming for a clock speed three to six times faster [00:24:30]. This new machine presented challenges, with wire lengths limited to 40 centimeters, leading to the same heating issues Cray faced with the 8600 [00:24:44].

However, Cray found himself unable to focus solely on solving these problems because his business demanded his attention [00:24:55]. To fund early development, Cray Research had an IPO, bringing new responsibilities [00:25:00]. The company's success led to headaches; each Cray-1 was hand-wired and custom-made—a year-long process—requiring a rapid increase in staff to address the backlog [00:25:08]. From 1978 to 1980, the company grew from 300 to 500 employees, eventually employing over 5,000 people in Chippewa Falls, Wisconsin [00:25:24].

### The Same Dilemma
[[seymour_crays_career_and_contributions_to_supercomputing | Cray]] initially pursued scientific computing because users wrote their own software, allowing him to focus solely on hardware [00:25:38]. But times changed; customers now sought software portability, exemplified by the popularity of the Unix operating system, and lacked the budget to rewrite software for each new machine [00:25:46]. Customers increasingly preferred a better Cray-1 rather than a radically different Cray-2 that would necessitate extensive software changes—a repeat of the Control Data and 1604 dilemma [00:25:57].

Cray Research's management, led by CEO John Rollwagen, again adopted a dual approach [00:26:13]. They extended the Cray-1 line with the 1S, a powerful but not radically different computer [00:26:18]. Meanwhile, [[seymour_crays_career_and_contributions_to_supercomputing | Seymour Cray]] stepped down as Chairman in 1981, becoming an independent contractor to focus on the Cray-2 [00:26:28]. He moved to Boulder, Colorado, seeking peace for his work [00:26:37].

### The Cray X-MP Upstages
The Cray-2 eventually launched in 1985 after three false starts on its cooling system [00:26:43]. It famously featured a massive liquid immersion cooling system, making it resemble an aquarium [00:26:49]. Despite this, memory latency hindered its full potential [00:26:53].

To many's surprise, Cray's Cray-2 was upstaged by another computer from a separate team: the Cray X-MP supercomputer [00:27:00]. Led by Les Davis and Steve Chen, the X-MP introduced parallel processing with four CPUs and new solid-state storage semiconductors [00:27:09]. Released in 1983, the X-MP became the world's fastest supercomputer, 2-5 times faster than the 1S, without the radical design changes of the Cray-2 [00:27:24]. It sold exceptionally well compared to the Cray-2; by 1989, only 24 Cray-2 units were sold, versus nearly 200 units of the X-MP and its successor, the Y-MP [00:27:42].

### New Pressures
In the 1970s, Cray had no direct competitors in its unique market segment [00:27:56]. However, throughout the 1980s, new supercomputer rivals emerged [00:28:02]. Japanese companies like Fujitsu, Hitachi, and NEC leveraged Japan's growing advantages in [[technological_innovations_and_challenges_in_supercomputer_design | VLSI semiconductor]] production to create compelling supercomputers [00:28:06]. While Cray still dominated with 56% market share of traditional supercomputers in 1988, Japanese companies collectively held 37% and were gaining ground [00:28:18].

Simultaneously, supercomputer startups such as Thinking Machines and nCUBE explored new approaches beyond vector computing, most notably Massively Parallel Systems (MPPs) [00:28:29]. These systems coordinated many commercial microprocessors to achieve millions or billions of floating-point operations per second [00:28:43]. Using off-the-shelf microprocessors offered a much better price-to-performance ratio [00:28:52]. This combined competition from startups, Japanese firms, and even Control Data's supercomputer spinoff, ETA Systems, pressured Cray to refine its approach and product lineup [00:28:57].

## Cray Leaves Cray
The unexpected success of the X-MP eventually created new challenges for Cray Research [00:29:09]. Designer Steve Chen, hailed as the "next [[seymour_crays_career_and_contributions_to_supercomputing | Seymour Cray]]," had an aggressive vision for the MP line beyond the Y-MP, which included 64 processors, custom [[technological_innovations_and_challenges_in_supercomputer_design | integrated circuits]], and optical interconnects [00:29:14]. By 1987, Cray Research was already invested in developing [[seymour_crays_career_and_contributions_to_supercomputing | Seymour Cray's]] next machine, the Cray-3, and the Y-MP, in addition to three existing products, leaving no funds for Chen's ambitious plans [00:29:23].

Cray Research scaled back the MP line that year, leading Steve Chen to quit and start his own company, Supercomputer Systems [00:29:51]. Supercomputer Systems raised $150 million from investors like IBM, Ford, and Boeing but went bankrupt in 1993 [00:30:02].

In 1989, Cray Research could no longer accommodate its founder. [[seymour_crays_career_and_contributions_to_supercomputing | Seymour Cray]] joined a spinoff called Cray Computer Corporation (CCC) in Colorado to work on the future Cray-3 [00:30:12]. Cray Research continued with the existing Cray X-MP architecture and ecosystem [00:30:25].

The Cray-3 was designed to use [[technological_innovations_and_challenges_in_supercomputer_design | gallium arsenide semiconductors]] for switching performance far exceeding silicon, necessitating significant chipmaking equipment investment [00:30:32]. However, the Cray-3 soon fell behind [00:30:42]. By 1991, customers began canceling orders due to cratering defense demand after the [[soviet_computer_development_history | fall of the Soviet Union]] [00:30:48]. CCC sold only one system before filing for bankruptcy in 1995, and an announced Cray-4 never materialized [00:30:53]. [[seymour_crays_career_and_contributions_to_supercomputing | Seymour Cray's]] cherished approach of designing "big iron" supercomputers from a "clean sheet of paper" was no longer financially viable [00:30:59].

[[seymour_crays_career_and_contributions_to_supercomputing | Seymour Cray]] formed a new company, SRC Computers, to explore parallel designs, but he passed away in 1996 at age 71 from car accident injuries [00:31:11]. Cray Research was eventually sold to Silicon Graphics and, after moving between owners, is now part of Hewlett Packard Enterprise as Cray Inc. [00:31:24].

## Conclusion

Advancements in [[technological_innovations_and_challenges_in_supercomputer_design | semiconductor technologies]] have made past supercomputers seem comically slow [00:31:34]. In 2010, electrical engineer Chris Fenton emulated the Cray-1A supercomputer using a Xilinx Spartan-3E 1600 development board, even housing it in a miniature Cray-1 package; this emulation now resides in the Computer History Museum and inspired the video [00:31:40].

Today's leading-edge semiconductor makers face similar challenges to those [[seymour_crays_career_and_contributions_to_supercomputing | Cray]] encountered with his supercomputers, including thermal problems, interconnect issues, and slowdowns due to memory retrieval [00:31:59]. However, unlike [[seymour_crays_career_and_contributions_to_supercomputing | Seymour Cray]], the modern [[technological_innovations_and_challenges_in_supercomputer_design | semiconductor industry]] cannot simply "throw it all out and start anew with a fresh sheet of paper" [00:32:12].