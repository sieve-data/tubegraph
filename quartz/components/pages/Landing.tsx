import { i18n } from "../../i18n"
import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "../types"

const Landing: QuartzComponent = ({ cfg }: QuartzComponentProps) => {
  // If baseUrl contains a pathname after the domain, use this as the home link

  return (
    <main style={{}}>
      <h1>Welcome to Tubegraph.</h1>
    </main>
  )
}

export default (() => Landing) satisfies QuartzComponentConstructor
