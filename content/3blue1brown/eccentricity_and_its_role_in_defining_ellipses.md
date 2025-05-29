---
title: Eccentricity and its role in defining ellipses
videoId: pQa_tWZmlGs
---

From: [[3blue1brown]] <br/> 

Ellipses are a family of curves whose specific shape can be precisely quantified <a class="yt-timestamp" data-t="00:01:59"></a>.

## Defining an Ellipse

There are at least three primary geometric definitions for an ellipse:
*   **Stretched Circle** One way is to imagine taking a circle and stretching it out in one dimension <a class="yt-timestamp" data-t="00:00:55"></a>. For example, if points are represented as (x,y) coordinates, one could multiply only the x-coordinate by a special factor <a class="yt-timestamp" data-t="00:00:59"></a>.
*   **Two Thumbtacks and String** This classic construction involves looping a string around two thumbtacks stuck into paper, pulling it taut with a pencil, and tracing <a class="yt-timestamp" data-t="00:01:08"></a>. The resulting curve is the set of all points where the sum of the distances from the pencil point to the two thumbtack points (called foci) remains constant <a class="yt-timestamp" data-t="00:01:22"></a>. This "constant focal sum property" defines the ellipse <a class="yt-timestamp" data-t="00:01:36"></a>.
*   **Slicing a Cone** An ellipse can also be defined by slicing a cone with a plane at an angle smaller than the cone's slope <a class="yt-timestamp" data-t="00:01:42"></a>. The intersection curve formed by this plane and the cone is an ellipse <a class="yt-timestamp" data-t="00:01:50"></a>, which is why ellipses are often referred to as a [[ellipses_and_conic_sections | conic section]] <a class="yt-timestamp" data-t="00:01:54"></a>.

## The Role of Eccentricity

The specific shape of an ellipse, ranging from a perfect circle to something infinitely stretched, is typically quantified by a number called its eccentricity <a class="yt-timestamp" data-t="00:02:03"></a>. The term "squishification" can be used as a conceptual shorthand for eccentricity <a class="yt-timestamp" data-t="00:02:07"></a>.

*   A perfect circle has an eccentricity of 0 <a class="yt-timestamp" data-t="00:02:16"></a>.
*   As an ellipse becomes more "squished," its eccentricity approaches the number 1 <a class="yt-timestamp" data-t="00:02:16"></a>.

### Examples of Eccentricity
*   Earth's orbit has a very low eccentricity of 0.0167, indicating it is very close to being a circle <a class="yt-timestamp" data-t="00:02:23"></a>.
*   Halley's comet has an orbit with a high eccentricity of 0.9671, signifying a very "squished" orbit <a class="yt-timestamp" data-t="00:02:33"></a>.

### Eccentricity in Different Definitions
The eccentricity of an ellipse can be determined differently depending on how the ellipse is defined:
*   **Thumbtack Definition** In the thumbtack definition, where an ellipse is based on the constant sum of distances from any point to the two foci, eccentricity is determined by how far apart the two thumbtacks (foci) are <a class="yt-timestamp" data-t="00:02:40"></a>. Specifically, it is the distance between the foci divided by the length of the ellipse's longest axis <a class="yt-timestamp" data-t="00:02:51"></a>.
*   **Cone Slicing Definition** When slicing a cone, the eccentricity is determined by the slope of the plane used for the slicing <a class="yt-timestamp" data-t="00:03:00"></a>.

## Equivalence of Definitions

A key mathematical question is why these three distinct definitions produce precisely the same family of shapes <a class="yt-timestamp" data-t="00:03:10"></a>. The intersection curve from slicing a cone, for instance, is an ellipse—a symmetric shape, not a lopsided "egg" <a class="yt-timestamp" data-t="00:03:31"></a>.

The equivalence, especially between the cone slicing and thumbtack constructions, can be demonstrated through an ingenious proof involving the introduction of two spheres, known as Dandelin spheres <a class="yt-timestamp" data-t="00:04:00"></a>. These spheres are sized to be tangent to the cone along circles of points and tangent to the slicing plane at single points, which turn out to be the foci of the ellipse <a class="yt-timestamp" data-t="00:04:42"></a>. This proof shows that any point on the intersection curve maintains a constant sum of distances to these two focal points, thus satisfying the thumbtack definition <a class="yt-timestamp" data-t="00:09:02"></a>. This demonstrates that slicing a cone results in a curve with the constant focal sum property <a class="yt-timestamp" data-t="00:09:18"></a>. This proof was first discovered by Germenal Dandelin in 1822 <a class="yt-timestamp" data-t="00:09:29"></a>.

This kind of proof highlights a common feature in mathematics: that sometimes there isn't a single most fundamental way to define something, and showing equivalences between definitions is what truly matters <a class="yt-timestamp" data-t="00:10:24"></a>.