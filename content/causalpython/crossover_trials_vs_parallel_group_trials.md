---
title: Crossover trials vs parallel group trials
videoId: nT_yCwXSz54
---

From: [[causalpython]] <br/> 

Clinical trials are designed to evaluate the effectiveness of new treatments, and two common types of experimental designs are parallel group trials and crossover trials <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>. The choice of design significantly impacts how treatment effects are estimated and the precision of the results <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.

## Parallel Group Trials

A parallel group trial is the most common type of clinical trial <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. In this design, patients are randomized to receive either a new treatment or a standard (control) treatment, with each patient receiving only one of the interventions <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. For example, in a stroke prevention trial, half of the subjects might be randomized to a new treatment and the other half to a standard treatment <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. These trials are generally relatively easy to implement <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

### Challenges in Parallel Group Trials

A key challenge in parallel group trials is that the groups are not expected to be perfectly balanced in all factors that could affect the outcome <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>, despite randomization <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>. Statisticians accept this imperfection, and the standard analysis accounts for it, by allowing for factors that are not perfectly balanced to contribute to the estimate of error <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

In a parallel group trial, the control group serves as a substitute for the unobservable counterfactual outcome of the patients receiving the new treatment <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>. Each group effectively acts as a "counterfactual group" for the other <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.

## Crossover Trials

In contrast, crossover trials are designed to have each patient serve as their own control <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>. This design is feasible for chronic diseases where treatments are essentially reversible <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>. For instance, in an asthma trial, patients could receive one beta agonist for a period and then another for a different period, with the order of treatments randomized <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.

### Advantages of Crossover Trials

The primary advantage of a crossover trial is its ability to balance for a vast number of individual characteristics, such as "20,000 genes, all life history to date," because each subject acts as their own control <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>. This leads to significantly narrower confidence intervals compared to parallel group trials <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

### Challenges in Crossover Trials

Even in crossover trials, circumstances can change from one treatment period to another, leading to a "missing element" or random variation that cannot be fully accounted for <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>.

## Comparison and Practical Implications

| Feature               | Parallel Group Trials                                       | Crossover Trials                                                |
| :-------------------- | :---------------------------------------------------------- | :-------------------------------------------------------------- |
| **Patient Role**      | Each patient receives one treatment <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>      | Each patient receives multiple treatments (their own control) <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a> |
| **Applicability**     | Widely applicable (e.g., stroke prevention) <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a> | Chronic diseases with reversible treatments (e.g., asthma) <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a> |
| **Balancing Factors** | Not perfectly balanced by randomization <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>  | Balances numerous intrinsic factors <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>       |
| **Confidence Intervals** | Wider <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>                                           | Much narrower <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>                                         |
| **Complexity**        | Relatively easy to implement <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>                  | Can be very complex (e.g., 7 treatments in 5 periods, 21 sequences) <a class="yt-timestamp" data-t="00:30:54">[00:30:54]</a> |

Ultimately, in clinical trials, the goal is to produce precise answers about what happened on average to patients <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>. While crossover trials offer greater precision by making each patient their own control, practical and ethical considerations, such as the nature of the disease or the logistics of treatment administration, often dictate the feasibility of a particular design <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>.

### Connection to [[n_of_1_trials | N of 1 Trials]]

The concept of a crossover trial, where a subject is tested and retested with different treatments, is closely related to [[n_of_1_trials | N of 1 Trials]] <a class="yt-timestamp" data-t="01:13:16">[01:13:16]</a>. These trials, initially proposed in medicine by researchers at McMaster University (Gordon Guyatt and colleagues), draw inspiration from psychological experiments where individuals are repeatedly tested by giving them stimuli <a class="yt-timestamp" data-t="01:13:28">[01:13:28]</a>. The key insight was randomizing treatments within the same subject to personalize medicine <a class="yt-timestamp" data-t="01:13:50">[01:13:50]</a>.