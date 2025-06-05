---
title: Marching Cubes Algorithm for Medical Imaging
videoId: SmyPTnlqhlk
---

From: [[fireship]] <br/> 

The Marching Cubes algorithm is a procedure designed to extract a polygonal mesh of an isosurface from a three-dimensional discrete scalar field <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. This specific [[Data Structures and Algorithms | algorithm]] was created and patented in 1987 by two programmers at General Electric <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. It has significantly impacted medicine by enabling doctors to visualize data from CT and MRI scans, potentially saving countless lives <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

## How it Works

The process begins with a 3D scalar field, which could represent data obtained from an MRI machine <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. In this field, each point in the 3D space is represented by a single number, or scalar <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.

The algorithm operates by:
1.  **Forming a Cube**: Starting with a single point, it considers its eight neighboring locations to form an imaginary cube <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.
2.  **Bit Interpretation**: The values within this cube are treated as bits in an 8-bit integer <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.
3.  **Polygon Selection**: This interpretation results in 256 different possibilities, each pointing to a pre-calculated array of polygons <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.
4.  **Mesh Generation**: The algorithm "marches" through each point in the scalar field, applying this process to create a complete 3D mesh <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. This mesh can then be used in 3D software <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.

## Impact

The Marching Cubes algorithm was groundbreaking because it allowed slices of data produced by MRI machines to be rendered into a coherent 3D representation <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.