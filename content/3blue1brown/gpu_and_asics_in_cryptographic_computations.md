---
title: GPU and ASICs in cryptographic computations
videoId: S9JGmA5_unY
---

From: [[3blue1brown]] <br/> 

Cryptographic computations, particularly those involving [[hash_functions_and_SHA256 | cryptographic hash functions]] like [[hash_functions_and_SHA256 | SHA-256]] used in [[digital_signatures_and_cryptography | digital signatures]] and [[mining_and_the_proof_of_work_concept_in_the_bitcoin_protocol | Bitcoin mining]], require immense processing power to perform repeated calculations or "guesses" [00:00:21] [00:00:27]. This is often in the context of breaking [[256_bit_security_concept | 256-bit security]], which would require, on average, 2 to the 256 guesses [00:00:33].

## General Purpose Graphics Processing Units (GPUs)

Graphics Processing Units (GPUs) are capable of running numerous computations in parallel at high speeds [01:09:00] [01:12:00]. When specially programmed to run a [[hash_functions_and_SHA256 | cryptographic hash function]] repeatedly, a high-performing GPU can achieve a rate of a little less than a billion hashes per second [01:15:00] [01:20:00]. For conceptual scale, a computer packed with multiple GPUs could potentially reach a hashing rate of 4 billion hashes per second [01:27:00] [01:30:00].

## Application-Specific Integrated Circuits (ASICs)

While GPUs are powerful, [[mining_and_the_proof_of_work_concept_in_the_bitcoin_protocol | Bitcoin mining]] operations primarily utilize Application-Specific Integrated Circuits (ASICs) [03:46:00] [03:50:00]. ASICs are hardware components specifically engineered for a singular purpose, such as running a high volume of [[hash_functions_and_SHA256 | SHA-256]] hashes for [[mining_and_the_proof_of_work_concept_in_the_bitcoin_protocol | Bitcoin mining]], and are not designed for general computation [03:58:00] [04:03:00] [04:07:00] [04:11:00].

### Efficiency Gains of ASICs
ASICs offer significant efficiency improvements compared to GPUs [04:07:00]. They can be approximately 1,000 times more efficient than a GPU for their specific task [03:50:00] [03:55:00]. This enhanced efficiency is achieved by eliminating the need for general computing capabilities and designing the integrated circuits solely for one task [04:07:00] [04:11:00].

### ASICs in Bitcoin Mining
The collective hashing power of all [[mining_and_the_proof_of_work_concept_in_the_bitcoin_protocol | Bitcoin]] miners combined is about 5 billion billion hashes per second [03:32:00] [03:37:00]. This immense rate is largely due to the widespread use of ASICs, which are purpose-built for [[bitcoin_mining_efficiency_and_technology | Bitcoin mining]], rather than a vast number of GPU-packed machines [03:46:00] [03:50:00].