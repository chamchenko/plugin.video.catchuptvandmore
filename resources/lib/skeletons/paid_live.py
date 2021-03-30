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
        'resolver': '/resources/lib/channels/fr/abfr:get_live_url',
        'label': 'RTL9',
        'thumb': 'channels/fr/rtl9.png',
        'fanart': 'channels/fr/rtl9_fanart.jpg',
        'm3u_group': 'Satellite/FAI',
        'enabled': True,
        'order': 1
    },
    'ab1': {
        'resolver': '/resources/lib/channels/fr/abfr:get_live_url',
        'label': 'AB 1',
        'thumb': 'channels/fr/ab1.png',
        'fanart': 'channels/fr/ab1_fanart.jpg',
        'm3u_group': 'Satellite/FAI',
        'enabled': True,
        'order': 2
    },
    'automoto-la-chaine': {
        'resolver': '/resources/lib/channels/fr/abfr:get_live_url',
        'label': 'AutoMoto',
        'thumb': 'channels/fr/automoto.png',
        'fanart': 'channels/fr/automoto_fanart.jpg',
        'm3u_group': 'Satellite/FAI',
        'enabled': True,
        'order': 3
    },
    'mangas': {
        'resolver': '/resources/lib/channels/fr/abfr:get_live_url',
        'label': 'Mangas',
        'thumb': 'channels/fr/mangas.png',
        'fanart': 'channels/fr/mangas_fanart.jpg',
        'm3u_group': 'Satellite/FAI',
        'enabled': True,
        'order': 4
    },
    'toute-l-histoire': {
        'resolver': '/resources/lib/channels/fr/abfr:get_live_url',
        'label': "Toute L'Histoire",
        'thumb': 'channels/fr/toutelhistoire.png',
        'fanart': 'channels/fr/toutelhistoire_fanart.jpg',
        'm3u_group': 'Satellite/FAI',
        'enabled': True,
        'order': 5
    },
    'science-et-vie': {
        'resolver': '/resources/lib/channels/fr/abfr:get_live_url',
        'label': 'Science & Vie',
        'thumb': 'channels/fr/scienceetvie.png',
        'fanart': 'channels/fr/scienceetvie_fanart.jpg',
        'm3u_group': 'Satellite/FAI',
        'enabled': True,
        'order': 6
    },
    'crime-district': {
        'resolver': '/resources/lib/channels/fr/abfr:get_live_url',
        'label': 'Crime District',
        'thumb': 'channels/fr/crimedistrict.png',
        'fanart': 'channels/fr/crimedistrict_fanart.jpg',
        'm3u_group': 'Satellite/FAI',
        'enabled': True,
        'order': 7
    },
    'animaux-tv': {
        'resolver': '/resources/lib/channels/fr/abfr:get_live_url',
        'label': 'Animaux',
        'thumb': 'channels/fr/animaux.png',
        'fanart': 'channels/fr/animaux_fanart.jpg',
        'm3u_group': 'Satellite/FAI',
        'enabled': True,
        'order': 8
    },
    'chasse-et-peche': {
        'resolver': '/resources/lib/channels/fr/abfr:get_live_url',
        'label': 'Chasse & Peche',
        'thumb': 'channels/fr/chasseetpeche.png',
        'fanart': 'channels/fr/chasseetpeche_fanart.jpg',
        'm3u_group': 'Satellite/FAI',
        'enabled': True,
        'order': 9
    },
    'trek': {
        'resolver': '/resources/lib/channels/fr/abfr:get_live_url',
        'label': 'Trek',
        'thumb': 'channels/fr/trek.png',
        'fanart': 'channels/fr/trek_fanart.jpg',
        'm3u_group': 'Satellite/FAI',
        'enabled': True,
        'order': 10
    },
    'action': {
        'resolver': '/resources/lib/channels/fr/abfr:get_live_url',
        'label': 'Action',
        'thumb': 'channels/fr/action.png',
        'fanart': 'channels/fr/action_fanart.jpg',
        'm3u_group': 'Satellite/FAI',
        'enabled': True,
        'order': 11
    },
    'golf-channel': {
        'resolver': '/resources/lib/channels/fr/abfr:get_live_url',
        'label': 'Golf Channel',
        'thumb': 'channels/fr/golfchannel.png',
        'fanart': 'channels/fr/golfchannel_fanart.jpg',
        'm3u_group': 'Satellite/FAI',
        'enabled': True,
        'order': 12
    }
}
