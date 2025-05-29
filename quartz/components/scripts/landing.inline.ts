document.addEventListener("nav", async (e: CustomEventMap["nav"]) => {
  console.log("navved")
  const currentSlug = e.detail.url

  // Only run on the landing page
  if (currentSlug !== "/" && currentSlug !== "index") {
    console.log("Not on landing page, slug:", currentSlug)
    return
  }

  // Check if mobile and handle graph section accordingly
  const isMobile = document.documentElement.clientWidth <= 800
  const graphSectionContainer = document.getElementById("graph-section-container")

  if (isMobile) {
    console.log("Mobile device detected, skipping graph setup")
    // Clear any existing graph content on mobile
    if (graphSectionContainer) {
      graphSectionContainer.innerHTML = ""
    }
    return
  }

  // Desktop: Add graph section if it doesn't exist
  if (graphSectionContainer && !graphSectionContainer.hasChildNodes()) {
    await addGraphSection(graphSectionContainer)
  }

  console.log("Setting up channel selector...")
  await setupChannelSelector()
  await setupCreateGraphButton()
})

async function addGraphSection(container: HTMLElement) {
  // Create the graph section HTML
  const graphSectionHTML = `
    <div class="graph-section">
      <div class="add-channel">
        <label for="channel-input" class="channel-select-label">
          Add a Channel:
        </label>
        <input
          id="channel-input"
          class="channel-select"
          placeholder="Channel Username (@)"
        />
        <label for="filter-by" class="channel-select-label">
          Sort By:
        </label>
        <select id="sort-by" class="channel-select drop">
          <option value="views">Views</option>
          <option value="upload_date">Upload Date</option>
        </select>
        <label for="vid-duration" class="channel-select-label">
          Min Vid Duration:
        </label>
        <input
          id="vid-duration"
          class="channel-select min-vid-duration"
          placeholder="1"
          type="number"
        />
        min.
        <button id="add-video" class="add-video">
          Create Graph
        </button>
      </div>
      <div class="graph-controls">
        <label for="channel-select" class="channel-select-label">
          View Graph For:
        </label>
        <select id="channel-select" class="channel-select">
          <option value="dwarkeshpatel/dwarkeshpatel">Dwarkesh Podcast</option>
          <option value="lexfridman/lexfridman">Lex Fridman</option>
          <option value="hubermanlab/hubermanlab">Huberman Lab</option>
          <option value="awdii/awdii">Awdii</option>
        </select>
      </div>
      <div class="graph">
        <h3>Graph</h3>
        <div class="graph-outer">
          <div class="graph-container" data-cfg='{"drag":true,"zoom":true,"depth":1,"scale":1.1,"repelForce":0.5,"centerForce":0.3,"linkDistance":30,"fontSize":0.6,"opacityScale":1,"showTags":true,"removeTags":[],"focusOnHover":true,"enableRadial":true,"rootNode":"dwarkeshpatel/dwarkeshpatel"}'></div>
          <button class="global-graph-icon" aria-label="Global Graph">
            <svg
              version="1.1"
              xmlns="http://www.w3.org/2000/svg"
              xmlnsXlink="http://www.w3.org/1999/xlink"
              x="0px"
              y="0px"
              viewBox="0 0 55 55"
              fill="currentColor"
              xmlSpace="preserve"
            >
              <path
                d="M49,0c-3.309,0-6,2.691-6,6c0,1.035,0.263,2.009,0.726,2.86l-9.829,9.829C32.542,17.634,30.846,17,29,17
                s-3.542,0.634-4.898,1.688l-7.669-7.669C16.785,10.424,17,9.74,17,9c0-2.206-1.794-4-4-4S9,6.794,9,9s1.794,4,4,4
                c0.74,0,1.424-0.215,2.019-0.567l7.669,7.669C21.634,21.458,21,23.154,21,25s0.634,3.542,1.688,4.897L10.024,42.562
                C8.958,41.595,7.549,41,6,41c-3.309,0-6,2.691-6,6s2.691,6,6,6s6-2.691,6-6c0-1.035-0.263-2.009-0.726-2.86l12.829-12.829
                c1.106,0.86,2.44,1.436,3.898,1.619v10.16c-2.833,0.478-5,2.942-5,5.91c0,3.309,2.691,6,6,6s6-2.691,6-6c0-2.967-2.167-5.431-5-5.91
                v-10.16c1.458-0.183,2.792-0.759,3.898-1.619l7.669,7.669C41.215,39.576,41,40.26,41,41c0,2.206,1.794,4,4,4s4-1.794,4-4
                s-1.794-4-4-4c-0.74,0-1.424,0.215-2.019,0.567l-7.669-7.669C36.366,28.542,37,26.846,37,25s-0.634-3.542-1.688-4.897l9.665-9.665
                C46.042,11.405,47.451,12,49,12c3.309,0,6-2.691,6-6S52.309,0,49,0z M11,9c0-1.103,0.897-2,2-2s2,0.897,2,2s-0.897,2-2,2
                S11,10.103,11,9z M6,51c-2.206,0-4-1.794-4-4s1.794-4,4-4s4,1.794,4,4S8.206,51,6,51z M33,49c0,2.206-1.794,4-4,4s-4-1.794-4-4
                s1.794-4,4-4S33,46.794,33,49z M29,31c-3.309,0-6-2.691-6-6s2.691-6,6-6s6,2.691,6,6S32.309,31,29,31z M47,41c0,1.103-0.897,2-2,2
                s-2-0.897-2-2s0.897-2,2-2S47,39.897,47,41z M49,10c-2.206,0-4-1.794-4-4s1.794-4,4-4s4,1.794,4,4S51.206,10,49,10z"
              />
            </svg>
          </button>
        </div>
        <div class="global-graph-outer">
          <div class="global-graph-container" data-cfg='{"drag":true,"zoom":true,"depth":-1,"scale":0.9,"repelForce":0.5,"centerForce":0.2,"linkDistance":30,"fontSize":0.6,"opacityScale":1,"showTags":true,"removeTags":[],"focusOnHover":true,"enableRadial":true}'></div>
        </div>
      </div>
    </div>
  `

  container.innerHTML = graphSectionHTML

  // Trigger graph initialization by dispatching a nav event
  // This will cause the graph script to initialize the newly added graph containers
  setTimeout(() => {
    const navEvent = new CustomEvent("nav", {
      detail: { url: "index" },
    })
    document.dispatchEvent(navEvent)
  }, 100)
}

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

    try {
      await createTubegraphPages(username, minVidDuration, sortBy)

      // Success feedback
      createButton.textContent = "Graph Created!"
      createButton.style.backgroundColor = "#22c55e"

      // Reset form
      channelInput.value = ""
      vidDurationInput.value = "1"
      sortBySelect.value = "views"
    } catch (error) {
      console.error("Error creating tubegraph:", error)

      // Error feedback
      createButton.textContent = "Error - Try Again"
      createButton.style.backgroundColor = "#ef4444"
    }
  })
}

async function createTubegraphPages(
  username: string,
  minVidDuration: number,
  sortBy: "views" | "upload_date",
) {
  let username_check = username.replace("@", "")

  // Check if the username directory already exists in content
  try {
    const response = await fetch(`/${username_check}`)
    console.log(response)
    if (response.ok || response.status === 403) {
      const addChannelDiv = document.querySelector(".add-channel") as HTMLElement
      if (addChannelDiv) {
        addChannelDiv.innerHTML = `Already Indexed! View <a href="https://tubegraph.vercel.app/${username_check}/${username_check}">here.</a>`
      }
      return
    }
  } catch (error) {
    // If fetch fails, we'll continue with the normal flow
    console.log("Directory check failed, proceeding with creation:", error)
  }

  const api_key = process.env.SIEVE_API_KEY
  console.log(api_key)

  if (!api_key) {
    throw new Error("SIEVE_API_KEY environment variable is not set")
  }

  // Submit the job
  const response = await fetch("https://mango.sievedata.com/v2/push", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-API-Key": api_key,
    },
    body: JSON.stringify({
      function: "sieve-demos/create-tubegraph-pages",
      inputs: {
        username: username,
        min_vid_duration: minVidDuration * 60,
        sort_by: sortBy,
      },
    }),
  })

  // Show loading state on button
  const addChannelDiv = document.querySelector(".add-channel") as HTMLElement
  if (addChannelDiv) {
    addChannelDiv.innerHTML = `Creating Graph... (this will take a couple minutes), feel free to close and come back later.`
  }

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
  if (addChannelDiv) {
    addChannelDiv.innerHTML = jobData.outputs[0].data.result
  }

  return jobData.outputs[0].result
}

function getChannelDisplayName(channelPath: string): string {
  const channelMap: Record<string, string> = {
    "dwarkeshpatel/dwarkeshpatel": "Dwarkesh Podcast",
    "lexfridman/lexfridman": "Lex Fridman",
    "hubermanlab/hubermanlab": "Huberman Lab",
    "awdii/awdii": "Awdii",
  }
  return channelMap[channelPath] || channelPath
}
