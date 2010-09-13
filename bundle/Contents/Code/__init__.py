import htmlentitydefs
import re
from urlparse import urlparse

VIMCASTS_FEED_URL      = 'http://vimcasts.org/feeds/quicktime'
VIMCASTS_EP_THUMB      = 'http://vimcasts.org/images/posters/%s.png'
VIMCASTS_ICON          = 'icon-default.png'
VIMCASTS_ART           = 'art-default.png'

###############################################################################
def Start():
    Plugin.AddViewGroup("Details", viewMode="InfoList", mediaType="items")
    MediaContainer.title1 = L('vimcasts')
    MediaContainer.art    = R(VIMCASTS_ART)
    HTTP.CacheTime        = CACHE_1HOUR

@handler('/video/vimcasts', L('vimcasts'))
def VideoMenu():
    dir = MediaContainer(mediaType='video', viewGroup='Details')
    feed_items = XML.ElementFromURL(VIMCASTS_FEED_URL).xpath('//item')
    for item in feed_items:
        try:
            url = item.find('enclosure').get('url')
        except AttributeError:
            # Probably the feed has an entry without an enclosure
            pass
        else:
            # Example path: /videos/24/vimrc_on_the_fly.m4v
            path_parts  = urlparse(url).path.split('/')[1:]
            title       = F('episode', path_parts[1], item.find('title').text)
            date        = item.find('pubDate').text
            description = dehtmlize(item.find('description').text.strip())
            thumb       = VIMCASTS_EP_THUMB % path_parts[-1].split('.')[0]
            dir.Append(VideoItem(url, title=title, summary=description,
                                 subtitle=date[0:-15], thumb=thumb))
    return dir

##
# Removes HTML tags from a text string and converts character entities.
# Adapted from:
# http://effbot.org/zone/re-sub.htm#strip-html
#
# @param text The HTML source.
# @return The plain text.  If the HTML source contains non-ASCII
#     entities or character references, this is a Unicode string.
def dehtmlize(text):
    def convert_entities(m):
        text = m.group(0)
        if text[:2] == "&#":
            try:
                if text[:3] == "&#x":
                    return unichr(int(text[3:-1], 16))
                else:
                    return unichr(int(text[2:-1]))
            except ValueError:
                pass
        elif text[:1] == "&":
            entity = htmlentitydefs.entitydefs.get(text[1:-1])
            if entity:
                if entity[:2] == "&#":
                    try:
                        return unichr(int(entity[2:-1]))
                    except ValueError:
                        pass
                else:
                    return unicode(entity, "iso-8859-1")
        return text # leave as is
    return String.StripTags(re.sub("&#?\w+;", convert_entities, text))

