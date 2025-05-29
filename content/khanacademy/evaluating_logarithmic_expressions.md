---
title: Evaluating logarithmic expressions
videoId: Z5myJ8dg_rM
---

From: [[khanacademy]] <br/> 

[[introduction_to_logarithms | Logarithms]] are fundamentally about determining what power a base number must be raised to in order to obtain a specific result <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. This concept is an inverse of finding the result of an exponentiation <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Relationship to Exponents

When considering an exponential expression like $2^4$, the result is $16$ <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. This means $2$ is multiplied by itself four times ($2 \times 2 \times 2 \times 2 = 16$) <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

The question a logarithm answers is: If you start with a base number (e.g., $2$) and want to reach a target number (e.g., $16$), what power ($x$) must the base be raised to? This can be expressed as $2^x = 16$ <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. In this case, $x$ equals $4$ <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

This [[inverse_relationship_between_logarithms_and_exponents | inverse relationship between logarithms and exponents]] is key to [[evaluating_logarithmic_expressions | evaluating logarithmic expressions]] <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## Logarithm Notation

The exponential question ($2^x = 16$) is expressed in [[logarithm_notation | logarithm notation]] as $\text{log}_2(16) = x$ <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. Both statements are equivalent ways of asking the same question: "What power do I need to raise $2$ to, to get $16$?" <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. The answer, as before, is $x = 4$ <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

## Examples of Evaluating Logarithmic Expressions

### Example 1: $\text{log}_3(81)$
To evaluate $\text{log}_3(81)$, we ask: "What power do we have to raise $3$ to, to get to $81$?" <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
We can set this up as an equation: $3^x = 81$ <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
*   $3^1 = 3$ <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>
*   $3^2 = 9$ <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>
*   $3^3 = 27$ <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>
*   $3^4 = 27 \times 3 = 81$ <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>
Therefore, $\text{log}_3(81) = 4$ <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

### Example 2: $\text{log}_6(216)$
To evaluate $\text{log}_6(216)$, we ask: "What power do we have to raise $6$ to, to get $216$?" <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
*   $6^1 = 6$ <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>
*   $6^2 = 36$ <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>
*   $6^3 = 36 \times 6 = 216$ <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>
Thus, $\text{log}_6(216) = 3$ <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.

### Example 3: $\text{log}_2(64)$
To evaluate $\text{log}_2(64)$, we ask: "What power do we have to raise $2$ to, to get $64$?" <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.
*   $2^1 = 2$ <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>
*   $2^2 = 4$ <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>
*   $2^3 = 8$ <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>
*   $2^4 = 16$ <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>
*   $2^5 = 32$ <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>
*   $2^6 = 64$ <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>
Therefore, $\text{log}_2(64) = 6$ <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

## Special Cases

### Example 4: $\text{log}_{100}(1)$
To evaluate $\text{log}_{100}(1)$, we ask: "What power do I have to raise $100$ to, to get $1$?" <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
If we set this equal to $x$, we have $100^x = 1$ <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.
Any non-zero number raised to the power of $0$ is $1$ <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.
So, $x=0$ <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.
This means $\text{log}_{100}(1) = 0$ <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.

This illustrates a general rule:
> [!info] Logarithm of One
> The logarithm of $1$ with any valid base (a base that is not $0$) will always equal $0$ <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.
> $\text{log}_b(1) = 0$ for any $b \neq 0$.