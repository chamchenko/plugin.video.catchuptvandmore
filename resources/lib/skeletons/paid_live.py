# -*- coding: utf-8 -*-
# Copyright: (c) 2016, SylvainCecchetto
# GNU General Public License v2.0+ (see LICENSE.txt or https://www.gnu.org/licenses/gpl-2.0.txt)

# This file is part of Catch-up TV & More

from __future__ import unicode_literals
from codequick import Script, utils

# The following dictionaries describe
# the addon's tree architecture.
# * Key: item id
# * Value: item infos
#     - route (folder)/resolver (playable URL): Callback function to run once this item is selected
#     - thumb: Item thumb path relative to "media" folder
#     - fanart: Item fanart path relative to "media" folder

root = 'live_tv'

menu = {
    'rtl9': {
        'resolver': '/resources/lib/channels/paid/abfr:get_live_url',
        'label': 'RTL9',
        'thumb': 'channels/paid/rtl9.png',
        'fanart': 'channels/paid/rtl9_fanart.jpg',
        'm3u_group': 'Satellite/FAI',
        'enabled': True,
        'order': 1
    },
    'ab1': {
        'resolver': '/resources/lib/channels/paid/abfr:get_live_url',
        'label': 'AB 1',
        'thumb': 'channels/paid/ab1.png',
        'fanart': 'channels/paid/ab1_fanart.jpg',
        'm3u_group': 'Satellite/FAI',
        'enabled': True,
        'order': 2
    },
    'automoto-la-chaine': {
        'resolver': '/resources/lib/channels/paid/abfr:get_live_url',
        'label': 'AutoMoto',
        'thumb': 'channels/paid/automoto.png',
        'fanart': 'channels/paid/automoto_fanart.jpg',
        'm3u_group': 'Satellite/FAI',
        'enabled': True,
        'order': 3
    },
    'mangas': {
        'resolver': '/resources/lib/channels/paid/abfr:get_live_url',
        'label': 'Mangas',
        'thumb': 'channels/paid/mangas.png',
        'fanart': 'channels/paid/mangas_fanart.jpg',
        'm3u_group': 'Satellite/FAI',
        'enabled': True,
        'order': 4
    },
    'toute-l-histoire': {
        'resolver': '/resources/lib/channels/paid/abfr:get_live_url',
        'label': "Toute L'Histoire",
        'thumb': 'channels/paid/toutelhistoire.png',
        'fanart': 'channels/paid/toutelhistoire_fanart.jpg',
        'm3u_group': 'Satellite/FAI',
        'enabled': True,
        'order': 5
    },
    'science-et-vie': {
        'resolver': '/resources/lib/channels/paid/abfr:get_live_url',
        'label': 'Science & Vie',
        'thumb': 'channels/paid/scienceetvie.png',
        'fanart': 'channels/paid/scienceetvie_fanart.jpg',
        'm3u_group': 'Satellite/FAI',
        'enabled': True,
        'order': 6
    },
    'crime-district': {
        'resolver': '/resources/lib/channels/paid/abfr:get_live_url',
        'label': 'Crime District',
        'thumb': 'channels/paid/crimedistrict.png',
        'fanart': 'channels/paid/crimedistrict_fanart.jpg',
        'm3u_group': 'Satellite/FAI',
        'enabled': True,
        'order': 7
    },
    'animaux-tv': {
        'resolver': '/resources/lib/channels/paid/abfr:get_live_url',
        'label': 'Animaux',
        'thumb': 'channels/paid/animaux.png',
        'fanart': 'channels/paid/animaux_fanart.jpg',
        'm3u_group': 'Satellite/FAI',
        'enabled': True,
        'order': 8
    },
    'chasse-et-peche': {
        'resolver': '/resources/lib/channels/paid/abfr:get_live_url',
        'label': 'Chasse & Peche',
        'thumb': 'channels/paid/chasseetpeche.png',
        'fanart': 'channels/paid/chasseetpeche_fanart.jpg',
        'm3u_group': 'Satellite/FAI',
        'enabled': True,
        'order': 9
    },
    'trek': {
        'resolver': '/resources/lib/channels/paid/abfr:get_live_url',
        'label': 'Trek',
        'thumb': 'channels/paid/trek.png',
        'fanart': 'channels/paid/trek_fanart.jpg',
        'm3u_group': 'Satellite/FAI',
        'enabled': True,
        'order': 10
    },
    'action': {
        'resolver': '/resources/lib/channels/paid/abfr:get_live_url',
        'label': 'Action',
        'thumb': 'channels/paid/action.png',
        'fanart': 'channels/paid/action_fanart.jpg',
        'm3u_group': 'Satellite/FAI',
        'enabled': True,
        'order': 11
    },
    'golf-channel': {
        'resolver': '/resources/lib/channels/paid/abfr:get_live_url',
        'label': 'Golf Channel',
        'thumb': 'channels/paid/golfchannel.png',
        'fanart': 'channels/paid/golfchannel_fanart.jpg',
        'm3u_group': 'Satellite/FAI',
        'enabled': True,
        'order': 12
    }
}
