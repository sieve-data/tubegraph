import { QuartzComponentConstructor } from "./types"
import landingStyle from "./styles/landing.scss"
import Graph from "./Graph"
// @ts-ignore
import script from "./scripts/landing.inline"
import { LogoIcon } from "./SieveLogo"

export const CHANNEL_CARDS = {
  dwarkesh: (
    <a href={"/DwarkeshPatel/DwarkeshPatel"}>
      <div class="card card-1">
        <p class="card-title">Dwarkesh Podcast</p>
        <p class="card-subhead">@DwarkeshPatel</p>
        <img src="/static/dwarkesh.png" class="card-illustration-1" />
      </div>
    </a>
  ),
  huberman: (
    <a href={"/hubermanlab/hubermanlab"}>
      <div class="card card-2">
        <p class="card-title">Huberman Lab</p>
        <p class="card-subhead">@hubermanlab</p>
        <img src="/static/huberman.png" class="card-illustration-2" />
      </div>
    </a>
  ),
  lexfridman: (
    <a href={"/lexfridman/lexfridman"}>
      <div class="card card-3">
        <p class="card-title">Lex Fridman</p>
        <p class="card-subhead">@lexfridman</p>
        <img src="/static/lex.png" class="card-illustration-3" />
      </div>
    </a>
  ),
}

export default (() => {
  function LandingComponent(props: any) {
    // Create a Graph component instance with default options
    const GraphComponent = Graph({
      localGraph: {
        rootNode: "DwarkeshPatel/DwarkeshPatel",
        enableRadial: true,
      },
    })

    return (
      <div class="page-body">
        <a className="powered-by-badge" href="https://www.sievedata.com/">
          Powered by
          <div style={{ width: "50%" }}>
            <LogoIcon />
          </div>
        </a>
        <a href="/directory" class="explore-channels">
          Explore Channels
        </a>
        <div class="content-container">
          <div class="landing-header">
            <a href="#" class="pill-link">
              <span class="pill-link__icon" aria-hidden="true">
                🎉
              </span>
              <span class="pill-link__label">Introducing Tubegraph</span>
              <span class="pill-link__arrow" aria-hidden="true">
                <svg
                  width="14"
                  height="14"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                >
                  <polyline points="9 18 15 12 9 6"></polyline>
                </svg>
              </span>
            </a>
            <p class="header-text">
              Build a Knowledge Graph of{" "}
              <b>
                <i>Any</i>
              </b>{" "}
              Youtube Channel.
            </p>
            <p class="page-subhead">Explore concepts, discover connections, and think deeper.</p>
          </div>

          <div class="issue-container">{Object.values(CHANNEL_CARDS)}</div>

          {/* Add the Graph section with dropdown */}
          <div class="graph-section">
            <div class="add-channel">
              <label for="channel-input" class="channel-select-label">
                Add a Channel:
              </label>
              <input
                id="channel-input"
                class="channel-select"
                placeholder={"Channel Username (@)"}
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
                placeholder={"1"}
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
                <option value="DwarkeshPatel/DwarkeshPatel">Dwarkesh Podcast</option>
                <option value="lexfridman/lexfridman">Lex Fridman</option>
                <option value="hubermanlab/hubermanlab">Huberman Lab</option>
                <option value="awdii/awdii">Awdii</option>
              </select>
            </div>
            <GraphComponent {...props} />
          </div>
        </div>
      </div>
    )
  }

  // Combine the CSS resources
  LandingComponent.css = [landingStyle, Graph().css]
  // Include both the Graph's afterDOMLoaded script and our landing script
  LandingComponent.afterDOMLoaded = [Graph().afterDOMLoaded, script]

  return LandingComponent
  //@ts-ignore
}) satisfies QuartzComponentConstructor
