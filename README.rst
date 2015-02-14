=============
Plex-Vimcasts
=============

A simple Plex_ plugin for vimcasts.org_, allowing you to view the
screencasts from the comfort of your media center.

Installation
============

The plugin is accepted in Plex's official channel directory—just browse the
Channel Directory section in the Plex Home Theater app and you can install it
from there.

Building From Source
====================

If you want to hack on the plugin, this should get you going. Pull requests
are welcome, I'll try to get enhancements upstreamed to Plex, but the plugin
submission process is not self-service and to be honest isn't very transparent,
so it may take some time.

The Plex-Vimcasts_ plugin bundle is built from files in the ``bundle/`` and
``templates/`` directories. To build the bundle you'll need:

- Git_
- Ruby_ & Rake_ (Both are bundled with OS X)

With those tools installed, get a copy of the source and install the plugin::

    $ git clone git://github.com/ches/plex-vimcasts.git
    $ cd plex-vimcasts
    $ rake install

If you'd like to remove the plugin later, use::

    $ rake uninstall

Or, ``rake uninstall:hard`` to uninstall the plugin *and* it's preferences and data.

If you wish to package your own double-clickable plugin installer, you'll need
two additional build dependencies:

- The `Plex App Maker`_
- The rb-appscript_ RubyGem (``gem install rb-appscript``)

Then, just run ``rake package`` and check the ``dist`` directory.

License
=======

Under the same terms as Plex, GPLv2.

Thanks
======

This, my first Plex plugin, began as a bunch of copy and paste! (Please Plex,
update the documentation for plugin developers one of these days...).

- Basically a clone of David Leatherman's `Railscasts plugin`_.
- Rake build script cribbed from Rick Fletcher's `MLB plugin`_. Probably
  overkill for this simple plugin, but it's a nice generalized example for other
  plugins to follow :-)

.. _Plex: http://plexapp.com/
.. _vimcasts.org: http://vimcasts.org/
.. _the downloads: http://github.com/ches/plex-vimcasts/downloads
.. _Git: http://code.google.com/p/git-osx-installer/downloads/list?can=3
.. _Ruby: http://www.ruby-lang.org/
.. _Rake: http://rake.rubyforge.org/
.. _Plex App Maker: http://forums.plexapp.com/index.php?/topic/10180-plex-app-maker/
.. _rb-appscript: http://appscript.sourceforge.net/rb-appscript/index.html
.. _Railscasts plugin: http://github.com/leathekd/plex_railscasts_plugin
.. _MLB plugin: http://github.com/rfletcher/plex-mlb

