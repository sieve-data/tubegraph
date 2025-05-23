() => {
    // Storyboard Get
    const resp = ytplayer.config.args.raw_player_response;
    const storyboards = resp.storyboards;
    const specRend = storyboards.playerStoryboardSpecRenderer;
    const spec = specRend.spec;

    const parts = spec.split("|")
    const base_n = (n) => parts[0].replace('L$L/$N',`L${n}/M0`);

    const signs = parts.map(p => p.split("rs$")[1]).filter(p => !!p).map(p => "rs%24" + p);

    // Output
    urls = []
    for (let i = 0; i < signs.length; i++) {
        let url = `${base_n(i)}&sigh=${signs[i]}`
        urls.push(url)
    }
    return urls
}