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

function initializePlayer() {
  const iframe = document.querySelector<HTMLIFrameElement>("iframe.youtube-player")
  if (!iframe) return false

  const player = new (window as any).YT.Player(iframe, {
    events: {
      onReady() {
        console.log("YT player ready")
        activateTimestampLinks(player)
        // tidy-up when Quartz swaps pages
        window.addCleanup?.(() =>
          document.querySelectorAll<HTMLAnchorElement>(".yt-timestamp").forEach((l) => {
            l.onclick = null
          }),
        )
      },
    },
  })
  return true
}

function waitForIframe(maxAttempts = 10, delay = 100) {
  let attempts = 0

  function tryInitialize() {
    attempts++
    if (initializePlayer()) {
      console.log("YouTube player initialized successfully")
      return
    }

    if (attempts < maxAttempts) {
      setTimeout(tryInitialize, delay)
    } else {
      console.log("YouTube iframe not found after", maxAttempts, "attempts")
    }
  }

  tryInitialize()
}

function waitForYTAPI(callback: () => void, maxAttempts = 50, delay = 100) {
  let attempts = 0

  function checkAPI() {
    attempts++
    if ((window as any).YT && (window as any).YT.Player) {
      console.log("YouTube API is ready")
      callback()
      return
    }

    if (attempts < maxAttempts) {
      setTimeout(checkAPI, delay)
    } else {
      console.log("YouTube API failed to load after", maxAttempts, "attempts")
    }
  }

  checkAPI()
}

document.addEventListener("nav", () => {
  console.log("loaded nav")
  loadYT()

  // Check if YouTube API is already loaded
  if ((window as any).YT && (window as any).YT.Player) {
    console.log("YouTube API already loaded")
    waitForIframe()
  } else {
    // Set up the callback for when API loads
    ;(window as any).onYouTubeIframeAPIReady = () => {
      console.log("YouTube API loaded via callback")
      waitForIframe()
    }

    // Also poll for the API in case the callback doesn't fire
    waitForYTAPI(() => {
      waitForIframe()
    })
  }
})
