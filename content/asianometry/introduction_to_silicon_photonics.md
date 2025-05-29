---
title: Introduction to Silicon Photonics
videoId: 29aTqLvRia8
---

From: [[asianometry]] <br/> 

Silicon photonics is a technology that applies modern nanoscale CMOS processes to the optical realm, allowing for the manipulation and transmission of light using silicon [00:00:14]. This technology is gaining traction in the contemporary technology world [00:00:25].

## What is Photonics?
Photonics, in this context, refers to technologies that transmit and manipulate light in the form of photons, or light particles [00:01:00]. This field is closely related to optical data transmission [00:01:07].

Historically, networking companies used electrical signals sent through copper wire [00:01:11]. However, electrons moving through wires interact with other atoms, leading to slowdowns and heat generation [00:01:16]. By the 1990s, networking companies faced challenges handling exploding data traffic [00:01:24]. They revolutionized long-distance communications by switching to optical fiber, which uses light to efficiently transmit data [00:01:30]. Light travels through optical fiber at the speed of light, enabling super high-frequency transmissions and thus higher data volumes [00:01:40]. Engineers later advanced this by sending multiple signals through the same fiber using different, non-interfering light wavelengths [00:01:52]. Today, optical fiber technologies dominate long-distance communication, with over 2 billion kilometers deployed globally [00:02:03].

## Silicon's Role
The nanoelectronics industry has used silicon for decades due to its abundance, low cost, and ability to facilitate massive scale [00:02:18]. Silicon has enabled technologies like billions of transistors on a single wafer and entire systems on chips that are faster, smaller, and cheaper [00:02:29]. Engineers have long sought to apply the vast scale of modern CMOS manufacturing processes, including EDA and PDK tools, to the photonics world [00:02:41].

A key motivation for silicon photonics is to replace the electrons and wires currently used for communication between transistors on traditional chips with optical fibers and light [00:02:53].

## Components of a Monolithic Silicon Photonics System
Dreams of a monolithic silicon chip—where all components are made of a single material system to transmit and manipulate light—date back to the 1970s [00:03:08]. Such a system would ideally have five core components:
1.  **Light Source:** Typically a laser [00:03:21].
2.  **Routes and Pathways:** Passive structures to manipulate light (bend, guide, filter, couple, split, combine) within the integrated chip, similar to optical fiber [00:03:24].
3.  **Modulator:** Converts digital electronic signals into digital optical signals [00:03:45].
4.  **Photodetector:** Converts digital optical signals back into digital electronic signals [00:03:52].
5.  **CMOS Electronics:** Traditional electronics that accompany the photonics components, serving support functions like encoding and decoding data [00:04:14].

A component that combines modulator and photodetector functionality is called a **transceiver** [00:04:01]. In data centers, transceivers sit at each end of an optical cable, converting data between light and electrical forms [00:04:06].

## [[Challenges in Silicon Photonics Development | Challenges in Developing Pure Silicon Photonics]]
Despite the vision of a monolithic silicon chip, two major issues hinder the production of a fully integrated photonics device from pure silicon using standard manufacturing methods [00:03:31]:

1.  **Light Emission:** Silicon on its own cannot emit light [00:04:41]. Crystalline silicon has an "indirect band gap," which prevented its use for early LEDs and means it cannot "lase" (produce laser light) [00:04:44]. Without lazing, pure silicon cannot be used as a light source [00:04:56]. Researchers have had to modify silicon, for example, by implanting boron, to force it to emit light and create efficient room-temperature silicon-based LEDs [00:05:02]. However, [[Commercial Applications of Silicon Photonics | commercial]] silicon-based lasers are still in development [00:05:15].
2.  **Modulation:** Silicon's crystal structure does not exhibit the Pockel's effect [00:05:20]. The Pockel's effect allows an electric field to control how fast light travels through an object by changing its refractive index [00:05:24]. Lasers typically lase continuously, and a modulator's purpose is to convert this continuous output into a digital signal [00:05:36]. Without the ability to control light's progress through silicon using electrical fields, converting digital electrical signals into digital light signals is not possible [00:05:51].

These fundamental issues make it challenging to produce a fully integrated photonics device from pure silicon using the same methods as traditional [[Advancements in semiconductor technology | semiconductor]] manufacturing [00:06:01]. Early optics researchers thus focused on other materials like gallium arsenide and indium phosphide [00:06:15].

## Evolution of Silicon Photonics
[[Evolution and uses of silicon wafers in technology | Silicon photonics]] as it is known today began in the mid-1980s with Richard Soref's work [00:06:25]. In 1987, he co-authored a paper demonstrating how silicon could be manipulated to adjust its refractive index [00:06:30]. This enabled the replication of a p-n junction, a basic building block of [[Advancements in semiconductor technology | semiconductor]] electronic devices, using a photonic passive structure called a waveguide [00:06:38]. This development kickstarted the [[Future Potential of Silicon Photonics Technology | silicon photonics industry]], which then focused on building a practical photonic system with a viable light source and modulator [00:06:52].

### Overcoming Light Source Challenges
A silicon-based laser is considered the "holy grail" of silicon photonics [00:07:08]. Since a pure silicon laser remains elusive, engineers have developed workarounds [00:07:12]:
*   Using an external laser positioned outside the chip, which also helps prevent the chip from overheating [00:07:19].
*   Bonding a pre-made laser from a different material, such as indium phosphide, onto the silicon—a technique known as hybrid integration [00:07:31]. Most [[Commercial Applications of Silicon Photonics | commercial]] silicon photonics providers currently use one of these two methods [00:07:38].

### Modulator Advancements
Silicon modulators have been studied since the beginning, with breakthroughs in shrinking device size and increasing throughput throughout the 1980s and 1990s [00:07:43].
*   In 2004, Intel announced the first silicon-based high-speed optical modulator with over 1 gigahertz bandwidth [00:07:55]. This system utilized a Mach-Zehnder interferometer (MZI), which works by splitting light into two wavelengths and recombining them to represent digital signals [00:08:07].
*   In 2012, Intel announced its first fully integrated [[Advancements in semiconductor technology | CMOS silicon photonics]] transceiver with four channels, each at 25 gigabits per second, fabricated with a 90-nanometer process [00:08:20]. This design used a ring modulator, which offers size advantages over the MZI [00:08:34].

These [[Advancements in semiconductor technology | advancements]] allowed the silicon photonics industry to move out of the laboratory, even without a pure silicon-based laser [00:08:41].

## [[Commercial Applications of Silicon Photonics | Commercial Applications]]
The silicon photonics industry found its first major [[Commercial Applications of Silicon Photonics | commercialization opportunity]] in data centers [00:08:50]. Hyperscalers (e.g., Alibaba, AWS, Google, Microsoft) offer immense cloud computing scalability and invest tens of billions annually in data centers [00:09:02]. The volume of data transmitted within a single hyperscaler data center is enormous [00:09:14].

Silicon photonics enables the integration of transceiver functionality directly onto the chip, replacing legacy components [00:09:46]. This integration leads to savings in cost, power, and labor, and helps address bandwidth bottlenecks [00:09:52]. Today, companies like Intel, Cisco, and Macom sell millions of units annually, and photonic components are expected to continue gaining market share from traditional optics and copper wire [00:09:59].

### [[Future Potential of Silicon Photonics Technology | Future Potential]]
While data centers are the largest short-term market for silicon photonics, there is also potential in the sensor and LiDAR markets [00:10:12]. LiDAR (Light Detection and Ranging) uses light to create 3D images of environments, similar to radar but offering higher resolutions due to smaller optical light waves [00:10:21]. LiDAR is crucial for autonomous driving, but current systems are expensive (up to $70,000) and bulky [00:10:35]. A silicon photonics-based LiDAR system could integrate many discrete optical components onto a single chip, drastically reducing costs and size [00:10:51]. Companies like Mobileye (an Intel subsidiary), PointCloud, Aeva, Voyant Photonics, and Analog Photonics are actively pursuing this space [00:11:04].

## Manufacturing Considerations
Silicon photonics products typically use silicon-on-insulator (SOI) wafers [00:11:26]. These wafers have special layers, often silicon dioxide, in addition to silicon [00:11:29]. The contrasting refractive indices of these layers help confine light [00:11:35].

Because of this, silicon photonics requires a slightly different fabrication process, which is a few years behind the "leading edge" of [[Advancements in semiconductor technology | semiconductor manufacturing]] [00:11:41]. This positions it as a specialty node, offering opportunities for foundries not competing at the most advanced nodes (e.g., 3 nanometers) [00:11:47].
*   **GlobalFoundries** is considered a market leader in this space, having acquired relevant IP from IBM's microelectronics division in 2014 [00:11:54].
*   **Intel** has been a pioneer in silicon photonics R&D for a long time and is expected to offer its IP and capabilities as it expands its foundry business [00:12:16].
*   **TSMC** has historically had less presence in this area [00:12:28]. Recently, their strategy appears to focus on building integration schemes that allow silicon photonics chiplets to work seamlessly with [[Advancements in semiconductor technology | traditional semiconductors]] [00:12:35].

## Market [[Challenges in Silicon Photonics Development | Challenges]] and [[Future Potential of Silicon Photonics Technology | Future Outlook]]
One of the [[Challenges in Silicon Photonics Development | challenges]] for the silicon photonics industry is market volume [00:12:47]. The biggest market, transceivers, is estimated to sell 50 to 75 million units annually [00:12:51]. This translates to about 40,000 to 60,000 200mm SOI wafers per year for the entire industry, which is less than a month's production for a typical megafab [00:13:00]. For large foundries like TSMC, the volume might not justify the investment [00:13:17]. This highlights a challenge: even if silicon photonics captures the entire transceiver and LiDAR markets, it needs other large markets to achieve its full potential [00:13:24].

Despite hundreds of millions of dollars poured into R&D, silicon photonics has yet to go mainstream [00:13:35]. Some startups aim to replace copper wiring on chips with optical fiber to create a silicon photonics microprocessor, potentially disrupting [[Advancements in semiconductor technology | traditional semiconductors]] [00:13:45]. However, this presents new [[Challenges in Silicon Photonics Development | challenges]]:
*   Modern transistors have feature sizes of a few nanometers, while photonic components cannot be smaller than the wavelengths of light they carry, topping out around one micrometer [00:14:01].
*   At a 7-nanometer node, one square micrometer can house over a hundred transistors, making the space occupied by larger photonic components a significant "opportunity cost" [00:14:19].

This size disparity pushes the industry towards packaging solutions that pair photonics and traditional chiplets rather than highly integrated monolithic silicon photonics [00:14:27], which may explain TSMC's integration strategy [00:14:38].

Silicon photonics is a futuristic technology aiming to change current paradigms [00:15:20]. However, it is a technology in search of a [[Commercial Applications of Silicon Photonics | commercial market]] large and valuable enough to fulfill its potential [00:15:27]. Without such a market, it risks facing a similar fate to the MEMS industry, which, despite selling millions of units, sees the majority of its value accrue to packaging rather than the chip itself, stifling innovation and limiting its financial potential [00:14:50].