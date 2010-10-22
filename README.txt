Introduction
============

GEO stands for "Gracefully E-mail Obfuscation". This package implements the solution exposed in this post of List Apart web site authored by Roel Van Gils:

http://www.alistapart.com/articles/gracefulemailobfuscation/ 

collective.geo uses plone.transformchain to transform the response output from Zope before it reaches your browser. It searches for all "mailto:" 
occurences inside the response and transform them into encoded harmless links. This codification is done via a simple base64 encoding, but enough to fool 
a spam robot. This is the form of the encoded mail link:

<a rel="nofollow" href="contact/dmljdG9yLmZlcm5hbmRlejJAdXBjbmV0LmVz">mymail</a>

On the browser side, the encoded links are decoded to their original form by using a Javascript that restore them to normal "mailto:" links.

The text of the link is replaced by the full E-mail specified in the original mailto attribute.

Authenticated responses are NOT affected by this transform. Only anonymous responses are modified. 

Requirements
============
Tested only in Plone 4 although is possible that it would run in Plone 3.

TODO
====
* Accessibility form and validators
* Integration tests
* Further testing   