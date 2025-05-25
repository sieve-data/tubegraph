// quartz/components/ChannelLoader.tsx
import { QuartzComponentConstructor } from "./types"

export default (() => {
  /** The UI that ends up in the HTML */
  function ChannelLoader() {
    return (
      <button id="counter-btn" class="q-btn">
        Count me
      </button>
    )
  }

  /** Styles (optional) */
  ChannelLoader.css = `
    .q-btn {
      padding: .6rem 1rem;
      border-radius: .5rem;
      background-color: black,
      color: white;
      font-weight: 600;
      cursor: pointer;
    }
  `

  /** Runs once the page’s DOM is ready */
  ChannelLoader.afterDOMLoaded = `
    let clicks = 0
    document.getElementById('counter-btn')?.addEventListener('click', () => {
      clicks++
      alert(\`You clicked \${clicks} time(s)!\`)
    })
  `
  return ChannelLoader
}) satisfies QuartzComponentConstructor
