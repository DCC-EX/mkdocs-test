# Using Our Logos

We have various logos available for both the DCC-EX brand and our various products.

These are typically created using InkScape in SVG format, which are located in the "image-artefacts" directory.

The generated logos are exported in PNG format with a transparent background, and located in the "docs/_static/images/logos" directory.

## Light and Dark Theme

Due to most logos using a transparent background, there are typically both a light and dark version of each logo available, and a CSS class is required to display the correct one using an [attribute](/contributing/documentation/mkdocs-features.md#attribute-lists).

If a logo has a solid background (for example our main DCC-EX logo), this is not required.

For example, the EX-CommandStation logo has both options:

```markdown
![EX-CommandStation Logo](/_static/images/logos/product-logo-ex-commandstation-only-light.png){ .only-light }
![EX-CommandStation Logo](/_static/images/logos/product-logo-ex-commandstation-only-dark.png){ .only-dark }
```

This renders, and switching your browser between light and dark modes will demonstrate the result:

![EX-CommandStation Logo](/_static/images/logos/product-logo-ex-commandstation-only-light.png){ .only-light }
![EX-CommandStation Logo](/_static/images/logos/product-logo-ex-commandstation-only-dark.png){ .only-dark }

## Branded and Non-Branded Product Logos

In most instances, using our full brand and product logos can cause pages to become too "busy". Users are navigating the DCC-EX website looking at our products, so incorporating our brand along with the product name can cause content and visual overload.

Where possible, use product name logos only, but if a product is being used in isolation from other DCC-EX context, branded logos are also available.

Logo PNG files including the word "only" have no branding.

EX-CommandStation branded logo:

```markdown
![EX-CommandStation Logo](/_static/images/logos/product-logo-ex-commandstation-light.png){ .only-light }
![EX-CommandStation Logo](/_static/images/logos/product-logo-ex-commandstation-dark.png){ .only-dark }
```

![EX-CommandStation Logo](/_static/images/logos/product-logo-ex-commandstation-light.png){ .only-light }
![EX-CommandStation Logo](/_static/images/logos/product-logo-ex-commandstation-dark.png){ .only-dark }

EX-CommandStation product only logo:

```markdown
![EX-CommandStation Logo](/_static/images/logos/product-logo-ex-commandstation-only-light.png){ .only-light }
![EX-CommandStation Logo](/_static/images/logos/product-logo-ex-commandstation-only-dark.png){ .only-dark }
```

![EX-CommandStation Logo](/_static/images/logos/product-logo-ex-commandstation-only-light.png){ .only-light }
![EX-CommandStation Logo](/_static/images/logos/product-logo-ex-commandstation-only-dark.png){ .only-dark }

## Logo Sizing

As you can see by the examples above, the logo sizes can be quite intrusive if use unconstrained.

If sizing needs to be constrained, use an additional [attribute](/contributing/documentation/mkdocs-features.md#attribute-lists) to set the width only (do not set height):

```markdown
![EX-CommandStation Logo](/_static/images/logos/product-logo-ex-commandstation-only-light.png){ .only-light width=400px }
![EX-CommandStation Logo](/_static/images/logos/product-logo-ex-commandstation-only-dark.png){ .only-dark width=400px }
```

![EX-CommandStation Logo](/_static/images/logos/product-logo-ex-commandstation-only-light.png){ .only-light width=400px }
![EX-CommandStation Logo](/_static/images/logos/product-logo-ex-commandstation-only-dark.png){ .only-dark width=400px }

All our product logos are generated with the same dimensions.
