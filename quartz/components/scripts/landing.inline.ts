document.addEventListener("nav", async (e: CustomEventMap["nav"]) => {
  console.log("navved")
  const currentSlug = e.detail.url

  // Only run on the landing page
  if (currentSlug !== "/" && currentSlug !== "index") {
    console.log("Not on landing page, slug:", currentSlug)
    return
  }

  console.log("Setting up channel selector...")
  await setupChannelSelector()
  await setupCreateGraphButton()
})

async function setupChannelSelector() {
  const channelSelect = document.getElementById("channel-select") as HTMLSelectElement

  if (!channelSelect) {
    console.log("Channel select element not found!")
    return
  }

  console.log("Channel select found, adding event listener...")

  channelSelect.addEventListener("change", async (e) => {
    console.log("changed")
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

    // Instead of a custom event, trigger a fake "nav" event to re-render the graph
    // This will use the existing graph rendering logic
    const navEvent = new CustomEvent("nav", {
      detail: { url: "index" },
    })
    document.dispatchEvent(navEvent)
  })
}

async function setupCreateGraphButton() {
  const createButton = document.getElementById("add-video") as HTMLButtonElement

  if (!createButton) {
    console.log("Create Graph button not found!")
    return
  }

  console.log("Create Graph button found, adding event listener...")

  createButton.addEventListener("click", async (e) => {
    e.preventDefault()

    // Get input values
    const channelInput = document.getElementById("channel-input") as HTMLInputElement
    const sortBySelect = document.getElementById("sort-by") as HTMLSelectElement
    const vidDurationInput = document.getElementById("vid-duration") as HTMLInputElement

    if (!channelInput || !sortBySelect || !vidDurationInput) {
      console.error("Required form elements not found!")
      return
    }

    const username = channelInput.value.trim()
    const sortBy = sortBySelect.value as "views" | "upload_date"
    const minVidDuration = parseInt(vidDurationInput.value) || 1

    // Validate inputs
    if (!username) {
      alert("Please enter a channel username")
      return
    }

    // Show loading state on button
    const originalText = createButton.textContent
    createButton.textContent = "Creating Graph..."
    createButton.disabled = true

    try {
      await createTubegraphPages(username, minVidDuration, sortBy)

      // Success feedback
      createButton.textContent = "Graph Created!"
      createButton.style.backgroundColor = "#22c55e"

      // Reset form
      channelInput.value = ""
      vidDurationInput.value = "1"
      sortBySelect.value = "views"

      // Reset button after delay
      setTimeout(() => {
        createButton.textContent = originalText
        createButton.style.backgroundColor = ""
        createButton.disabled = false
      }, 3000)
    } catch (error) {
      console.error("Error creating tubegraph:", error)

      // Error feedback
      createButton.textContent = "Error - Try Again"
      createButton.style.backgroundColor = "#ef4444"

      // Reset button after delay
      setTimeout(() => {
        createButton.textContent = originalText
        createButton.style.backgroundColor = ""
        createButton.disabled = false
      }, 3000)
    }
  })
}

async function createTubegraphPages(
  username: string,
  minVidDuration: number,
  sortBy: "views" | "upload_date",
) {
  const api_key = "MCmpv1nyARO6vKq5xJqfCgTDCVrGevkxO7qT9jlhatY"

  // Submit the job
  const response = await fetch("https://mango.sievedata.com/v2/push", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-API-Key": api_key,
    },
    body: JSON.stringify({
      function: "sieve-demos/tubegraph-entry",
      inputs: {
        username: username,
        min_vid_duration: minVidDuration * 60,
        sort_by: sortBy,
      },
    }),
  })

  if (!response.ok) {
    throw new Error(`API request failed: ${response.status} ${response.statusText}`)
  }

  const result = await response.json()
  const jobId = result.id
  console.log("Job submitted with ID:", jobId)

  // Poll for job completion
  const getJobStatus = async (jobId: string) => {
    const endpoint = `https://mango.sievedata.com/v2/jobs/${jobId}`

    const headers = {
      "X-API-Key": api_key,
    }

    const response = await fetch(endpoint, { headers })
    const data = await response.json()
    console.log("Job status:", data.status)
    return data
  }

  // Poll until job is finished
  let jobData
  do {
    await new Promise((resolve) => setTimeout(resolve, 2000)) // Wait 2 seconds between polls
    jobData = await getJobStatus(jobId)
  } while (jobData.status !== "finished")

  console.log("Job completed:", jobData)

  // Replace the contents of add-channel with the result
  const addChannelDiv = document.querySelector(".add-channel") as HTMLElement
  if (addChannelDiv) {
    addChannelDiv.innerHTML = jobData.outputs[0].data.result
  }

  return jobData.outputs[0].result
}

function getChannelDisplayName(channelPath: string): string {
  const channelMap: Record<string, string> = {
    "DwarkeshPatel/DwarkeshPatel": "Dwarkesh Podcast",
    "lexfridman/lexfridman": "Lex Fridman",
    "hubermanlab/hubermanlab": "Huberman Lab",
    "awdii/awdii": "Awdii",
  }
  return channelMap[channelPath] || channelPath
}
