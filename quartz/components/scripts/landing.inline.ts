document.addEventListener("nav", async (e: CustomEventMap["nav"]) => {
  const currentSlug = e.detail.url

  // Only run on the landing page
  if (currentSlug !== "/") {
    return
  }

  await setupChannelSelector()
})

async function setupChannelSelector() {
  const channelSelect = document.getElementById("channel-select") as HTMLSelectElement

  if (!channelSelect) {
    return
  }

  channelSelect.addEventListener("change", async (e) => {
    const target = e.target as HTMLSelectElement
    const selectedChannel = target.value

    // Update the graph configuration
    const graphContainer = document.querySelector(".graph-container") as HTMLElement
    if (!graphContainer) {
      return
    }

    // Get the current configuration and update the root node
    const currentConfig = JSON.parse(graphContainer.dataset.cfg || "{}")
    const newConfig = {
      ...currentConfig,
      rootNode: selectedChannel,
    }

    // Update the data attribute
    graphContainer.dataset.cfg = JSON.stringify(newConfig)

    // Show loading state
    graphContainer.innerHTML = `
        <div style="display: flex; justify-content: center; align-items: center; height: 100%; color: #666; font-family: var(--bodyFont);">
          <div style="text-align: center;">
            <div style="margin-bottom: 10px;">Loading graph...</div>
            <div style="font-size: 12px; opacity: 0.7;">${getChannelDisplayName(selectedChannel)}</div>
          </div>
        </div>
      `

    // Trigger a custom event that the graph script can listen to
    const graphUpdateEvent = new CustomEvent("graph-update", {
      detail: {
        container: graphContainer,
        rootNode: selectedChannel,
        config: newConfig,
      },
    })
    document.dispatchEvent(graphUpdateEvent)
  })
}

function getChannelDisplayName(channelPath: string): string {
  const channelMap: Record<string, string> = {
    "DwarkeshPatel/DwarkeshPatel": "Dwarkesh Podcast",
    "lexfridman/lexfridman": "Lex Fridman",
    "hubermanlab/hubermanlab": "Huberman Lab",
  }
  return channelMap[channelPath] || channelPath
}
