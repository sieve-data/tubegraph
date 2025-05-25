// @ts-ignore – Quartz’ bundler handles .inline.ts files
import ytScript from "./scripts/youtube-player.inline"
import { QuartzComponentConstructor, QuartzComponentProps } from "./types"

export default (() => {
  function YouTubePlayer({ fileData }: QuartzComponentProps) {
    // 1️⃣  read it from front-matter, else use a sensible default
    const videoId = fileData.frontmatter?.videoId ?? "QFzgSmN8Ng8"

    return (
      <iframe
        id="main-yt"
        className="youtube-player"
        // use the page’s real origin so the JS API works in prod too
        src={`https://www.youtube.com/embed/${videoId}?enablejsapi=1`}
        style={{ width: "100%", aspectRatio: "16/9" }}
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowFullScreen
      />
    )
  }

  // Quartz will inline this once the DOM is ready
  YouTubePlayer.afterDOMLoaded = ytScript
  return YouTubePlayer
}) satisfies QuartzComponentConstructor
