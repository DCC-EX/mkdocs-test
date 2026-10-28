---
icon: material/home

hide:
  - navigation
  - toc
  - footer
  - title
---
<!-- This style block is to "hide" the title, it must be defined in order for MkDocs to work correctly -->
<style>
.md-content__inner h1 {
  font-size: 1px !important;
  line-height: 1px !important;
  margin: 0 !important;
  padding: 0 !important;
  height: 1px !important;
  overflow: hidden;
  color: var(--md-default-bg-color);
}

.homepage_img {
  margin-bottom: 0px !important;
}

.md-typeset ol li, .md-typeset ul li {
    margin-bottom: 0.1em !important;
}

/* Custom container for your styled paragraphs */
.paragraph-bg-box {
    position: relative;
    isolation: isolate;
    padding: 20px;          /* Adds space inside the box so text doesn't touch edges */
    border-radius: 8px;     /* Optional: rounds the corners */
    color: black;
    margin-bottom: 1em;
}

.paragraph-bg-box::before,
.paragraph-bg-box::after {
    position: absolute;
    inset: 0;
    z-index: -1;
    border-radius: inherit;
    background-size: cover;
    background-position: center top;
    background-repeat: no-repeat;
    content: "";
    opacity: 0;
    pointer-events: none;
    transition: opacity 800ms ease-in-out;
}

.paragraph-bg-box::before {
    background-image: var(--home-background-image-a);
}

.paragraph-bg-box::after {
    background-image: var(--home-background-image-b);
}

.paragraph-bg-box.home-background-a::before,
.paragraph-bg-box.home-background-b::after {
    opacity: 1;
}

@media (prefers-reduced-motion: reduce) {
    .paragraph-bg-box::before,
    .paragraph-bg-box::after {
        transition: none;
    }
}

</style>

<div class="paragraph-bg-box">

<img alt="DCC-EX" src="./_static/images/logos/logo_with_border.png" width="200px" class="off-glb" style="display:block; margin-left:auto; margin-right:auto;">

<span style="display:block; margin-left:10%; margin-right:10%; text-align:center; line-height: 240%; margin-top: 1em;">
<span style="font-size: 250%; font-weight:900; text-align:center;">Free and open source control systems for DCC and DC model train enthusiasts</span>
</span>
<br/>

<span style="font-size: 120%; font-weight:700; display:block; margin-left:10%; margin-right:10%;"><span style="font-style:italic;">"This is a team of volunteers who love model railroading, who wanted to design a new highly capable system for model railroads - and they've done it"</span><br/>- Jimmy at 'DIY and Digital Railroad'</span>

<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

</div><br/><br/>

# Home

<div class="grid cards static home-top-row" markdown>

- ## :material-hand-wave-outline: Welcome to DCC-EX

    Our free, open source, [Command Station](./products/ex-commandstation/index.md) software is one of the most comprehensive available, with many *in-built* features which are unavailable or *extras* in most commercial command stations. Including:

    - *WiFi*. Use smart phones &amp; tablets, or commercial and DIY physical throttles, to control your trains and layout.
    - Run either, or both, *DCC* and *DC* trains from the same throttle.
    - Add a *loco roster* and accessories such as turnouts/points, routes, signals, lights, and sounds.
    - *Automate* your trains and *animate* your layout with the powerful [EXRAIL](./enhance/exrail/index.md) scripting.
    - Integrate with [JMRI](https://www.jmri.org/), [iTrain](https://www.berros.eu/en/itrain/) or [RocRail](https://wiki.rocrail.net/) if you prefer to run trains from your computer.

    Our [ready-to-run](./products/ex-csb1/index.md) and [self-build](./diy/diy.md) systems use this same outstanding [**EX-CommandStation**](/products/ex-commandstation/index.md) software. Configuration is easy using our [**EX-Installer**](./prepare-to-use/installer/index.md) app.

    ---
    [![EX-CSB1](./_static/images/ex-csb1/csb1-resin-case-small.png){ align=left width=140px .homepage_img }](./products/ex-csb1/index.md) The [**EX-CommandStation/Booster 1 Express**](./products/ex-csb1/index.md) (**EX-CSB1**) is our flagship, WiFi enabled, *ready-to-run* system and is available for [purchase now](./purchasing/official-sellers.md) from our [official suppliers](./purchasing/official-sellers.md).  
    With your phone, you could be running your trains in less than 5 minutes. *No computer required.*  
    [Read the product page](./products/ex-csb1/index.md) for more information on the **EX-CSB1** .

    ---
    [![diy](./_static/images/mega/mega-small.png){ align=right width=140px .homepage_img }](./diy/diy.md)
    Or you can enjoy [building your own](./diy/diy.md), staggeringly inexpensive, version from readily-available Arduino/MicroController parts.  
    Our flexible designs range from *easy build* systems for beginners (no soldering required) up to very powerful, but more complex, systems for the adventurous.

    ---

    We also have a continually evolving range of additional [products](./products/products.md) to enhance your layout, including an integrated fast clock, turntable controller, and I/O expansion.

- ## :material-help-box-multiple-outline: What is DCC-EX

    <span style="font-size: .75rem;">![DCC-EX](./_static/images/logos/logo_with_border.png){ .off-glb align=right width=80px } **DCC-EX** is world-wide team of dedicated enthusiasts producing free and open source DCC and DC *software* and *hardware* solutions to run your model trains and layout.  
    *Our mission* is to make model trains accessible and affordable to everyone.</span>

    <span style="font-size: .75rem;">Learn more on our [About Us](./about/about.md) page.</span>

    ---

    <span style="font-size: .7rem;">This website contains information ranging from how to run your first train to how to automate a large exhibition layout. Use the navigation buttons or search facility above to find what you need.</span>

    <span style="font-size: .7rem;">As it is still in the process of being migrated from our [old website](https://dcc-ex.com/legacy-docs), if you can't find what you are looking for, try looking in the [old website](https://dcc-ex.com/legacy-docs).</span>

    <span style="font-size: .7rem;">There is also a light/dark mode button beside the search bar.</span>

    <small>This site does not use Third Party Cookies.</small>

</div>
