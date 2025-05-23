function activateTimestampLinks(player: any) {
  document.addEventListener("click", (e) => {
    const link = (e.target as HTMLElement).closest<HTMLAnchorElement>("a.yt-timestamp[data-t]")
    if (!link) return

    e.preventDefault()

    const stamp = link.dataset.t
    if (!stamp) return

    const [h = "0", m = "0", s = "0"] = stamp.split(":")
    const secs = +h * 3600 + +m * 60 + +s

    console.log("→ seeking to", secs, "s")
    player.seekTo(secs, true)
  })
}

function loadYT() {
  if (!(window as any).YT) {
    const tag = document.createElement("script")
    tag.src = "https://www.youtube.com/iframe_api"
    document.head.appendChild(tag)
  }
}

document.addEventListener("nav", () => {
  console.log("loaded nav")
  loadYT()
  ;(window as any).onYouTubeIframeAPIReady = () => {
    const iframe = document.querySelector<HTMLIFrameElement>("iframe.youtube-player")
    if (!iframe) return

    const player = new (window as any).YT.Player(iframe, {
      events: {
        onReady() {
          console.log("YT player ready")
          activateTimestampLinks(player) // ← the helper above
          // tidy-up when Quartz swaps pages
          window.addCleanup?.(() =>
            document.querySelectorAll<HTMLAnchorElement>(".yt-timestamp").forEach((l) => {
              l.onclick = null
            }),
          )
        },
      },
    })
  }
})
