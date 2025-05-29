---
title: Guido van Rossums insights on Python 40
videoId: -DVyjdw4t9I
---

From: [[lexfridman]] <br/> 

## Introduction

The conversation with [[guido_van_rossums_view_on_human_nature | Guido van Rossum]], the creator of the [[development_history_of_python | Python programming language]], sheds light on the possibility of a Python 4.0 release and the lessons learned from the transition to Python 3.0. The experiences with Python's evolution, the insights on community and language development, and the philosophical approach to making fundamental changes to a widely-used programming language were key elements discussed [02:00:25](https://www.youtube.com/watch?v=02:00:00).

## Reflections on Python 3 Transition

Guido van Rossum recalls the transition from Python 2 to 3 as a period filled with "pain and joy, suffering, and triumph" [00:00:15](https://www.youtube.com/watch?v=00:00:00). The move to Python 3.0 involved significant challenges as users had to adapt to new features and changes that were not backward-compatible with Python 2. This transition presented valuable lessons on managing expectations and the complexities involved in evolving a widely-used language.

> [!info] Transition Challenges
> 
> The transition to Python 3.0 taught the community the difficulties of maintaining backward compatibility while introducing significant improvements [02:24:01](https://www.youtube.com/watch?v=02:24:00).

## The Possibility of Python 4.0

As of now, the Python community and core development team have agreed that there won't be a Python 4.0 in the near future. If it were to happen, they would plan the transition very differently, taking into account lessons learned from the Python 3 shift [02:23:48](https://www.youtube.com/watch?v=02:23:00).

Guido emphasizes that any move to Python 4.0 would require a significant reason and a well-considered strategy to avoid past mistakes. One potential catalyst for Python 4.0 could be the removal of the global interpreter lock (GIL), which might necessitate changes that are not backward-compatible [02:24:48](https://www.youtube.com/watch?v=02:24:00).

## Features That Could Necessitate Python 4.0

### Consideration for No-GIL Python

One of the envisioned features that may necessitate a Python 4.0 is the removal of the GIL. This change could lead to a version of Python that provides better multi-threading capabilities. However, Guido van Rossum notes that the removal of the GIL would significantly change the binary interface for C extensions, a critical aspect for the scientific community using Python for machine learning and data science [02:26:21](https://www.youtube.com/watch?v=02:26:00).

### Transition Strategy

The introduction of Python 4.0, especially with no GIL, would require an extended transition strategy with considerable overlap between Python 3.x and 4.x to allow third-party extensions to adopt the new APIs and adapt to the changes [02:30:31](https://www.youtube.com/watch?v=02:30:00).

> [!info] Community Adaptation
>
> The transition to Python 4.0 would demand cooperation and adaptation from the vast ecosystem of third-party packages and extensions that form a critical part of Python's appeal [02:30:03](https://www.youtube.com/watch?v=02:30:00).

## Conclusion

Guido van Rossum's reflections and insights highlight the complexity of transitioning a major programming language to a new version. The lessons from Python 3.0 emphasize the importance of community, careful planning, and the significance of backward compatibility. The possibility of a Python 4.0, governed by thoughtful planning and collaboration within the community, illustrates the evolving nature of programming languages and the challenges of innovation in widely-used technological ecosystems.

To learn more about the broader Python community and its development history, refer to the related topics such as [[python_programming_and_community | Python programming and community]] and [[development_history_of_python | development history of Python]].