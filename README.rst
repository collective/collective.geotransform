Introduction
============

.. image:: https://travis-ci.org/collective/collective.geotransform.svg?branch=master
    :target: https://travis-ci.org/github/collective/collective.geotransform

GEO stands for "Gracefully E-mail Obfuscation". This package implements the solution exposed in this post of List Apart web site authored by Roel Van Gils:

http://www.alistapart.com/articles/gracefulemailobfuscation/ 

collective.geotransform uses plone.transformchain to transform the response output from Zope before it reaches your browser. It searches for all "mailto:" occurences inside the response and transform them into encoded harmless links.
It also searches for plain email addresses (without links) inside the response and transform them into encrypted spans.
This codification is done via a simple base64 encoding, but enough to fool a spam robot.

This is the form of the encoded mailto link:

    <a rel="nofollow" href="geomailto:dmljdG9yLmZlcm5hbmRlejJAdXBjbmV0LmVz">Link text</a>

While this is the form of the encoded span for plain email address:

    <span class="geomailaddress">dmljdG9yLmZlcm5hbmRlejJAdXBjbmV0LmVz</span>

On the browser side, the encoded links and spans are decoded to their original form by using a Javascript that restores them to normal "mailto:" links and decrypted plain text emails.

Authenticated responses are NOT affected by this transform. Only anonymous responses are modified.

Compatibility
=============

The versions 2.x (build from the master-branch) are used in Plone 5.

For support of Plone 4 please use versions 1.x.

TODO
====
 
 * Accessibility form and validators
