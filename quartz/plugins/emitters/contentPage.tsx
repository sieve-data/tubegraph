import path from "path"
import { QuartzEmitterPlugin } from "../types"
import { QuartzComponentProps } from "../../components/types"
import HeaderConstructor from "../../components/Header"
import BodyConstructor from "../../components/Body"
import { pageResources, renderPage } from "../../components/renderPage"
import { FullPageLayout } from "../../cfg"
import { pathToRoot } from "../../util/path"
// Import your new layout and potentially other components if needed
import {
  defaultContentPageLayout,
  sharedPageComponents,
  indexPageLayout,
} from "../../../quartz.layout" // UPDATED
import { Content } from "../../components"
import chalk from "chalk"
import { write } from "./helpers"
import { BuildCtx } from "../../util/ctx"
import { Node } from "unist"
import { StaticResources } from "../../util/resources"
import { QuartzPluginData } from "../vfile"
import { Fragment } from "preact/jsx-runtime"

async function processContent(
  ctx: BuildCtx,
  tree: Node,
  fileData: QuartzPluginData,
  allFiles: QuartzPluginData[],
  opts: FullPageLayout, // This will now vary
  resources: StaticResources,
) {
  const slug = fileData.slug!
  const cfg = ctx.cfg.configuration
  const externalResources = pageResources(pathToRoot(slug), resources)
  const componentData: QuartzComponentProps = {
    ctx,
    fileData,
    externalResources,
    cfg,
    children: [],
    tree,
    allFiles,
  }

  const content = renderPage(cfg, slug, componentData, opts, externalResources)
  return write({
    ctx,
    content,
    slug,
    ext: ".html",
  })
}

export const ContentPage: QuartzEmitterPlugin<Partial<FullPageLayout>> = (userOpts) => {
  // Options for default content pages
  const defaultOpts: FullPageLayout = {
    ...sharedPageComponents,
    ...defaultContentPageLayout,
    pageBody: Content(),
    ...userOpts,
  }

  // Empty component for hiding content
  const EmptyBody = () => <Fragment />

  // Options specifically for the index.md page
  const indexOpts: FullPageLayout = {
    ...sharedPageComponents,
    ...indexPageLayout, // Use your custom layout here
    pageBody: EmptyBody, // Or a custom body component if index needs it
    ...userOpts, // Allow user overrides for index page as well
  }

  // Components need to be a superset of all components used by any layout this emitter handles.
  // Destructure from defaultOpts, assuming it's a superset or very similar.
  // If customIndexPageLayout uses vastly different components, you might need to adjust this.
  const Head = defaultOpts.head! // Assuming head is shared or taken from default
  const Header = HeaderConstructor()
  const Body = BodyConstructor()
  const Footer = defaultOpts.footer! // Assuming footer is shared or taken from default

  return {
    name: "ContentPage",
    getQuartzComponents() {
      // Return all components that *might* be used by either layout.
      // renderPage will pick the correct ones based on the `opts` passed to it.
      const allComponents = [
        Head,
        Header,
        Body,
        ...defaultOpts.header,
        ...indexOpts.header, // Combine and let renderPage pick
        ...defaultOpts.beforeBody,
        ...indexOpts.beforeBody,
        defaultOpts.pageBody,
        // indexOpts.pageBody, // pageBody component itself
        ...defaultOpts.afterBody,
        ...indexOpts.afterBody,
        ...defaultOpts.left,
        ...indexOpts.left,
        ...defaultOpts.right,
        ...indexOpts.right,
        Footer,
      ]
      // Simple way to get unique components if there's overlap (e.g., by name, if components have names)
      // Or just ensure your components are robust enough to be included even if not used by a specific layout.
      // For now, let's assume Quartz handles any redundancy or you manage it in your layout definitions.
      // A more robust way to get unique components by reference:
      const uniqueComponents = [...new Set(allComponents.flat().filter(Boolean))]
      return uniqueComponents
    },
    async *emit(ctx, content, resources) {
      const allFiles = content.map((c) => c[1].data)
      let containsIndex = false

      for (const [tree, file] of content) {
        const slug = file.data.slug!

        if (slug === "index") {
          containsIndex = true
          // Process index.md with indexOpts
          yield processContent(ctx, tree, file.data, allFiles, indexOpts, resources)
        } else if (slug.endsWith("/index") || slug.startsWith("tags/")) {
          // Skip folder index pages (e.g., folder/index.md) and tag pages,
          // as they are likely handled by FolderContentIndex or TagContentIndex emitters.
          continue
        } else {
          // Process other content pages with defaultOpts
          yield processContent(ctx, tree, file.data, allFiles, defaultOpts, resources)
        }
      }

      if (!containsIndex && !content.some((c) => c[1].data.slug === "index")) {
        // Check if index was actually processed
        console.log(
          chalk.yellow(
            `\nWarning: you seem to be missing an \`index.md\` home page file at the root of your \`${ctx.argv.directory}\` folder (\`${path.join(ctx.argv.directory, "index.md")} does not exist\`). This may cause errors when deploying.`,
          ),
        )
      }
    },
    async *partialEmit(ctx, content, resources, changeEvents) {
      const allFiles = content.map((c) => c[1].data)
      const changedSlugs = new Set<string>()
      for (const changeEvent of changeEvents) {
        if (!changeEvent.file) continue
        if (changeEvent.type === "add" || changeEvent.type === "change") {
          changedSlugs.add(changeEvent.file.data.slug!)
        }
      }

      for (const [tree, file] of content) {
        const slug = file.data.slug!
        if (!changedSlugs.has(slug)) continue

        if (slug === "index") {
          yield processContent(ctx, tree, file.data, allFiles, indexOpts, resources)
        } else if (slug.endsWith("/index") || slug.startsWith("tags/")) {
          continue
        } else {
          yield processContent(ctx, tree, file.data, allFiles, defaultOpts, resources)
        }
      }
    },
  }
}
