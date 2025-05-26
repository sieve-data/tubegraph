import { QuartzComponentConstructor } from "./types"
import landingStyle from "./styles/landing.scss"
import Graph from "./Graph"
// @ts-ignore
import script from "./scripts/landing.inline"

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
    <a href={"/huberman/huberman"}>
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
        <div class="content-container">
          <div class="landing-header">
            <p class="header-text">
              Build a Knowledge Graph of{" "}
              <b>
                <i>Any</i>
              </b>{" "}
              Youtube Channel.
            </p>
            <p class="page-subhead"></p>
          </div>

          <div class="issue-container">{Object.values(CHANNEL_CARDS)}</div>

          {/* Add the Graph section with dropdown */}
          <div class="graph-section">
            <div class="graph-controls">
              <label for="channel-select" class="channel-select-label">
                Select Channel:
              </label>
              <select id="channel-select" class="channel-select">
                <option value="DwarkeshPatel/DwarkeshPatel">Dwarkesh Podcast</option>
                <option value="lexfridman/lexfridman">Lex Fridman</option>
                <option value="hubermanlab/hubermanlab">Huberman Lab</option>
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
  LandingComponent.afterDOMLoaded = script

  return LandingComponent
  //@ts-ignore
}) satisfies QuartzComponentConstructor
