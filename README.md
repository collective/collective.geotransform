# collective.geotransform

GEO stands for "Gracefully E-mail Obfuscation". This package implements the solution exposed in this post of A List Apart, authored by Roel Van Gils:

http://www.alistapart.com/articles/gracefulemailobfuscation/

collective.geotransform uses plone.transformchain to transform the response output from Zope before it reaches your browser. It searches for all "mailto:" occurrences inside the response and transforms them into encoded harmless links.
It also searches for plain email addresses (without links) inside the response and transforms them into encrypted spans.
This codification is done via a simple base64 encoding, but enough to fool a spam robot.

This is the form of the encoded mailto link:

```html
<a rel="nofollow" href="geomailto:dmljdG9yLmZlcm5hbmRlejJAdXBjbmV0LmVz">Link text</a>
```

While this is the form of the encoded span for plain email address:

```html
<span class="geomailaddress">dmljdG9yLmZlcm5hbmRlejJAdXBjbmV0LmVz</span>
```

On the browser side, the encoded links and spans are decoded to their original form by using a Javascript that restores them to normal "mailto:" links and decrypted plain text emails.

Authenticated responses are NOT affected by this transform. Only anonymous responses are modified.


## Compatibility

The versions 3.x (build from the master-branch) are compatible with Plone 6 / Python 3 only.

Other branches / versions support old Plone versions:

- Plone 5: versions 2.x
- Plone 4: versions 1.x


## Installation

Add `collective.geotransform` to the dependencies of your project (with pip, uv or buildout), restart Plone, then activate the add-on in the Add-ons control panel.


## TODO

- Accessibility form and validators
