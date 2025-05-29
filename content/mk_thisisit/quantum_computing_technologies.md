---
title: Quantum computing technologies
videoId: XwSWdmmlwQQ
---

From: [[mk_thisisit]] <br/> 

## Introduction to Spintronics

Traditional electronics relies on the negative or positive charge of an electron for power [01:07:12]. However, electrons possess an additional property: spin [01:16:16]. Spin results from the electron's rotational motion around its axis, similar to Earth rotating around its axis, which produces a magnetic moment [01:50:50]. This magnetic moment can be utilized to record information [02:00:00]. This entire field is known as spintronics [01:22:00].

### Spintronics for Information Recording
Magnetic memories currently use materials with more electrons oriented in one spin direction compared to the opposite direction [02:06:03]. This magnetism stems from unpaired magnetic moments or spins [02:15:06]. Magnetic recording has been in use for many years, with historical examples like Franz Joseph's voice recorded on a magnetic disc [02:22:07]. Modern hard drives in data centers, used by services like Google or for streaming movies, rely on this technology, showcasing a huge recording density [02:34:00].

### Spintronics for Information Processing
Beyond recording, the ambition is to use these spins for information processing [02:54:00]. This is the second branch of spintronics [03:01:03]. An electron spin can exist in a quantum dot, which was the subject of this year's Nobel Prize in chemistry [03:07:07]. Scientists can control the number of electrons in these quantum dots, potentially down to a single electron [03:22:00]. When two electrons in adjacent quantum dots interact, it constitutes information processing [03:27:00]. The change in spin direction after interaction signifies a calculation being performed [03:42:00]. If isolated from the environment, these interactions are governed by the laws of quantum mechanics [03:51:00]. This forms a model of a [[Quantum computers and their challenges | quantum computer]] [03:58:00].

The idea to use individual spins for information processing is about 30 years old [04:17:00]. Currently, collaborations like Intel's with Delft University of Technology are working to scale this to thousands of bits for [[Quantum computing and its applications in science and technology | quantum calculations]] [04:25:00]. Professor Tomasz Diem is considered a creator of this branch of physics [01:30:00, 01:33:00, 04:46:00]. Early work in spintronics, involving semiconductors with magnetic ions, dates back to Professor Gałązka in the last century [05:25:00, 05:28:00]. The concept was to combine semiconductors (like silicon) with magnetic materials (like iron) to utilize both their electronic and magnetic properties [05:31:00]. By applying voltage to a magnetic semiconductor, its magnetic properties, used for information recording and processing, can be changed [07:04:00].

## Evolution of Computing and the Need for New Architectures

### Transistor Miniaturization and Moore's Law
Modern electronics and computers are based on the number of transistors [07:46:00]. The number of transistors on a given surface area has increased dramatically over the last several decades, growing by 10 million times [08:20:00]. Currently, several billion transistors can be placed on one square centimeter, compared to several thousand previously [08:28:00]. This progress in electronics is significantly greater than advancements in other fields like car fuel efficiency (four times reduction) or solar cell efficiency (several times increase since the 1970s) [08:39:00, 08:55:00].

However, transistors are now reaching sizes of 5 nanometers, a record for modern phones [09:13:00]. To put this in perspective, a human hair has a cross-section 10,000 times larger than 5 nanometers [09:22:00]. This extreme miniaturization means that spaces between components are counted in atoms, indicating that the limits of current technology are being reached [08:05:00, 09:38:00]. The speed of computers, which initially grew rapidly from megahertz to gigahertz, has now plateaued [09:44:00].

Moore's Law, which states that the number of transistors on a unit area doubles every year and a half, held true for about 40 years [12:24:00, 12:37:00]. While physicists and engineers strive to keep Moore's Law alive, it is showing signs of saturation as physical limits are approached [12:57:00, 13:07:00]. This exponential growth led to a 10 million-fold increase in transistors per unit area over 70 years [13:43:00].

### Limitations of Classical Computing
The current computer architecture, developed during World War II, is over 75 years old and is ceasing to be applicable [10:06:00, 10:13:00]. Transistors themselves were patented in 1924 by Juliusz Lilienfeld, originating from a Polonized Jewish family from Lviv [10:26:00, 10:41:00]. Miniaturization not only increased the number of transistors but also made them faster and more energy-efficient, drastically reducing their price (100 times smaller than printing a single letter in a book) [11:12:00, 11:36:00].

### Changing Information Carriers
Due to these limitations, new architectures are being considered, and a change in the information carrier may be necessary [14:00:00, 14:09:00]. While classical computing uses the electron's charge [14:15:00], information transfer has already shifted from using electrons via wires to photons (light, optical fibers, microwave radiation) [14:23:00, 14:42:00]. The question now is whether the same can be done for information processing [14:49:00]. Spintronics suggests that spins could be better for information processing [15:01:00].

Dynamic random-access memories (DRAM) and cache memories in microprocessors utilize electron charge, storing information by charging or discharging capacitors [15:21:00, 15:31:00]. However, these memories require constant power to retain information, losing data when disconnected [15:38:00]. The goal is to limit the energy needed for information storage and processing [15:55:00]. This is where magnetic materials, traditionally used in disk memories, could be applied to fast cache memories using spins [16:03:00].

## [[Quantum computing and its applications in science and technology | Quantum Computing]] Technologies

### Principles of Quantum Computing
One of the most important branches of semiconductor physics, representing the latest face of magnetism, is the model of a [[Quantum computers and their challenges | quantum computer]] [04:05:00]. This involves controlling individual spins in quantum dots, where their interaction performs calculations [03:22:00, 03:51:00].

### [[Quantum computers and their challenges | Challenges in Quantum Computing]]
A significant challenge in [[Quantum computers and their challenges | quantum computer]] development is decoherence, the process by which quantum phenomena like diffraction and interference disappear due to interaction with the environment [21:38:00, 22:16:00, 23:21:00, 24:05:00]. This interaction can be caused by thermal noise from neighboring atoms or electromagnetic signals in the air [23:00:00]. When noises appear, they disturb the electron, slightly changing its wavelength and causing quantum interference to fade [23:58:00].

Two primary difficulties currently prevent the widespread construction of large [[Quantum computers and their challenges | quantum computers]]:
1.  **Nonlocality of quantum mechanics:** Quantum mechanics states that an electron in one place can affect electrons in another, even without direct interaction, making it hard to control individual quantum elements without disturbing others (crosstalk) [20:00:00, 20:21:00, 20:27:00, 24:22:00].
2.  **Interaction with the environment (noise):** This interaction disrupts the quantum evolution of spins, leading to errors in calculations [24:25:00]. While error correction methods exist, they require even more qubits, posing a fundamental difficulty [24:34:00].

### Different Approaches to Quantum Computers
There are various ideas and principles on which [[Quantum computers and their challenges | quantum computers]] are built [18:30:00]. Current [[Quantum computers and their challenges | quantum computers]] are still "mini" versions, typically with 20-40 bits [19:10:00, 19:13:00].

Methods mentioned include:
*   **Quantum Dots:** Utilizing single spins in quantum dots for processing [03:07:07, 18:28:00, 19:24:00]. These might offer better control over individual dots without disturbing the rest of the system [20:36:00]. Intel is currently focusing on this approach [28:32:00].
*   **Superconductors:** Currently the most advanced approach for [[Quantum computers and their challenges | quantum computers]] [19:44:00, 19:51:00, 19:56:00, 19:26:00]. However, the nonlocality of quantum mechanics makes it difficult to scale up the number of superconducting elements without interference [20:21:00].
*   **Trapped Ions:** Using ions held in electromagnetic traps [18:41:00].
*   **[[Quantum computers and cold atoms | Neutral Atoms]] on Networks:** Employing neutral atoms arranged in grids [18:43:00].

### Current State and Future Outlook
Despite the challenges, significant investments are being made. For example, Europe has allocated about a billion euros for the development of [[Quantum computing and its applications in science and technology | quantum computing]] [00:37:00, 20:51:00]. A center in Poznań is currently acquiring a [[Quantum computers and their challenges | quantum computer]] for 15 million euros, with the decision on which technology to purchase pending [18:51:00, 19:05:00]. Experts are still uncertain which method will ultimately dominate [[Quantum computing and its applications in science and technology | quantum computing]] in the future [18:19:00, 21:13:00].

## Role of Topology in Quantum Computing

Topology, distinct from geometry, focuses on properties that remain unchanged under continuous deformation [25:41:00, 26:26:00]. For instance, a bun is topologically distinct from a doughnut, which has a hole [26:39:00]. In physics, this applies to the arrangement of spins [26:58:00]. If spins are arranged in a non-trivial topological way (i.e., with a non-zero topological index), the structure becomes more stable and less susceptible to disturbances [27:08:00, 27:28:00]. This stability allows for even smaller memory units [27:22:00].

Furthermore, the velocity vector of electrons in condensed matter can also exhibit different topological classes [27:37:00, 27:48:00]. When materials with different topological indexes are combined, stable "edge states" are created at their interface [28:01:00, 28:11:00, 28:18:00]. These edge states are insensitive to disturbances, making them ideal information carriers [28:20:00, 28:23:00]. Microsoft is investing in the idea of topological [[Quantum computing and its applications in science and technology | quantum computers]], believing these materials will be better for [[Quantum computing and its applications in science and technology | quantum calculations]] due to their low sensitivity to noise, thereby mitigating decoherence [28:34:00, 28:46:00, 28:55:00].

## Quantum Metrology

Metrology is the science of measurement, focused on precisely measuring various quantities [30:04:00, 34:04:00]. The drive for standardization in the 19th century, crucial for the industrial revolution, led to the establishment of physical standards like the meter and kilogram in Paris [29:13:00, 29:32:00, 30:00:00]. However, it was later discovered that the world could be described with much greater precision using physical constants [30:15:00]. These constants, like the speed of light, maintain their value across vast spans of time and space [30:24:00].

A unit of time, not based on Earth's rotation but on the frequency of light emitted during intra-atomic transitions (specifically, the cesium atom), was introduced years ago [30:43:00, 30:58:00, 31:04:00]. This allows for extremely high accuracy in time measurement, which is fundamental to technologies like GPS [31:08:00, 31:17:00, 31:28:00]. GPS relies on four atomic clocks on satellites, and while relativistic corrections are needed, this precision allows for location determination with accuracy down to several meters [31:33:00, 31:40:00, 31:46:00, 31:55:00].

The quantum Hall phenomenon allows for the transfer of quantum properties from the microscopic world to macroscopic units [32:10:00, 32:40:00]. Now, fundamental units are not meter and kilogram but electron charge and Planck's constant [32:21:00, 32:23:00, 32:58:00]. The kilogram, ampere, and other units can now be expressed using the cesium atom's standard second, the Josephson phenomenon (for voltage), and the quantum Hall phenomenon [32:29:00, 32:36:00, 32:52:00, 33:13:00]. This translation from the microscopic, atomic world of electron charge (10^-19 coulombs) to macroscopic quantities (like amperes in a car battery) allows for the creation of units more precise than any existing before [33:39:00, 33:47:00, 33:55:00]. This precise measurement opens up new possibilities for applications [34:32:00].

## Science Funding and Research in Poland

Poland has received significant subsidies from the European Union, offering a chance to be a leader in science [34:50:00, 35:17:00]. Laboratories, including those researching topological matter, are financed by European funds such as the European Intelligent Development fund [35:22:00].

Scientific projects in Poland are generally very good, and the obtained results are fantastic, showing significant progress [36:03:00, 36:08:00, 36:10:00, 36:17:00, 37:11:00]. This progress is also evident in the growing number of European Research Council grants received by Polish institutions, which is a key metric for assessing university quality in Europe [37:13:00, 37:20:00, 37:32:00].

However, despite European grants, the financing of science in Poland remains low compared to the global average (around 3% of GDP, while Poland struggles to reach 2%) [37:37:00, 37:45:00]. There are high expectations for increased funding [37:57:00]. Assessing scientific units by the number of grants obtained is suggested as a good measure, as it reflects expert evaluation of research quality and plans, rather than automatic metrics [38:11:00, 38:16:00]. For competitions to be effective, approximately one in four grant applications should win [39:01:00].

Groundbreaking fundamental research is being undertaken in Poland [39:08:00, 39:14:00]. An example is Professor Bartosz Grzybowski, who developed an algorithmic approach to chemistry [39:35:00, 39:39:00]. His work predicts chemical reactions needed to obtain compounds and has described how the first organic materials might have formed, which is a significant contribution to understanding the origin of life [39:49:00, 40:04:00, 40:10:00, 40:25:00, 40:29:00].

## Nobel Prize in Science

Poland has not received a scientific Nobel Prize in physics or chemistry for almost a century [40:47:00, 40:49:00]. While Poland has two Nobel laureates in poetry, this highlights the gap in scientific awards [41:11:00]. Countries like Japan, while large and innovative, also took many years to win scientific Nobel Prizes [41:37:00].

Professor Paczyński, an astronomer who has since passed away, was considered to have a real chance at a Nobel Prize for his astronomical research, particularly on microlensing, an idea continued by his students [41:58:00, 42:04:00, 42:06:00, 42:13:00, 42:18:00]. Another potential candidate is Wojciech Żurek for his contributions to [[Quantum computing and its applications in science and technology | quantum computing]], particularly his discovery of decoherence as the boundary between quantum and classical worlds [22:28:00, 22:30:00, 22:33:00, 42:47:00, 42:50:00]. While nominations are made, and shortlists exist (300 proposals per field annually), receiving the prize is highly competitive and often unexpected [42:26:00, 42:32:00, 42:48:00].