import { QuartzComponentConstructor } from "./types"
import landingStyle from "./styles/landing.scss"
import Graph from "./Graph"
// @ts-ignore
import script from "./scripts/landing.inline"
import { LogoIcon } from "./SieveLogo"

const GitHubIcon = ({ className = "w-5 h-5" }: { className?: string }) => (
  <svg
    className={className}
    fill="currentColor"
    viewBox="0 0 24 24"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z" />
  </svg>
)

export const CHANNEL_CARDS = {
  dwarkesh: (
    <a href={"/dwarkeshpatel/dwarkeshpatel"}>
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
        rootNode: "dwarkeshpatel/dwarkeshpatel",
        enableRadial: true,
      },
    })

    return (
      <div class="page-body">
        <a className="powered-by-badge" href="https://www.sievedata.com/">
          <LogoIcon />
        </a>
        <div class="top-right-container">
          <a
            href="https://github.com/sieve-data/tubegraph"
            class="contribute-link"
            target="_blank"
            rel="noopener noreferrer"
          >
            <GitHubIcon />
            Contribute
          </a>
          <a href="/directory" class="explore-channels">
            {"Explore Channels ->"}
          </a>
        </div>

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
                <option value="dwarkeshpatel/dwarkeshpatel">Dwarkesh Podcast</option>
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
