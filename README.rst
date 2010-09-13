=============
Plex-Vimcasts
=============

A simple `Plex`_ plugin for `vimcasts.org`_, allowing you to view the
screencasts from the comfort of your media center.

Building From Source
====================

The `Plex-Vimcasts`_ plugin bundle is built from files in the ``bundle/`` and ``templates/`` directories. To build the bundle you'll need:

* Git_
* Ruby_ & Rake_ (Both are bundled with OS X)

With those tools installed, get a copy of the source and install the plugin::

    $ git clone git://github.com/ches/plex-vimcasts.git
    $ cd plex-vimcasts
    $ rake install

If you'd like to remove the plugin later, use::

    $ rake uninstall

Or, ``rake uninstall:hard`` to uninstall the plugin *and* it's preferences and data.

License
=======

Under the same terms as Plex, GPLv2.

Thanks
======

This, my first Plex plugin, is essentially a bunch of copy and paste!

- Basically a clone of David Leatherman's `Railscasts plugin`_.
- Rake build script cribbed from Rick Fletcher's `MLB plugin`_. Probably
  overkill for this simple plugin, but especially as a Rubyist it may prove a
  useful model for future plugins :-)

.. _Plex: http://plexapp.com/
.. _vimcasts.org: http://vimcasts.org/
.. _Git: http://code.google.com/p/git-osx-installer/downloads/list?can=3
.. _Ruby: http://www.ruby-lang.org/
.. _Rake: http://rake.rubyforge.org/
.. _Railscasts plugin: http://github.com/leathekd/plex_railscasts_plugin
.. _MLB plugin: http://github.com/rfletcher/plex-mlb

