#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Do you like Python ?
#
#                         .-=-.          .--.
#              __        .'     '.       /  " )
#      _     .'  '.     /   .-.   \     /  .-'\
#     ( \   / .-.  \   /   /   \   \   /  /    ^
#      \ `-` /   \  `-'   /     \   `-`  /
#       `-.-`     '.____.'       `.____.'
#
#

""" 
   Gotham Live Channel 
"""

import re, math, sys, traceback
from time import sleep
from datetime import datetime
from table_def import ChatLog
from ircbot import SingleServerIRCBot
from irclib import nm_to_n, nm_to_h, irc_lower, ip_numstr_to_quad, ip_quad_to_numstr

class GothamLive(SingleServerIRCBot):
    main=""
    spy_channel=""
    def __init__(self, channel, spy_channel, nickname, server, main):
        SingleServerIRCBot.__init__(self, [(s, 6667) for s in server], main, nickname, nickname)
        self.channel = channel
        self.main = main
        self.spy_channel = spy_channel 

#   General    
    def on_nicknameinuse(self, c, e):
        c.nick(c.get_nickname() + "_")

    def on_welcome(self, c, e):
        print "welcome"
        if c.server == self.main: 
            c.join(self.channel)
        else:
            c.join(self.spy_channel)

    def on_join(self, c, e):
        print "join"
        nick = nm_to_n(e.source())

#    Private message
    def on_privmsg(self, c, e):
        nick = nm_to_n(e.source())
        ch = self.channel
        said = e.arguments()[0]
        print "privmsg"

#    Listen on public message
    def on_pubmsg(self, c, e):
        try:
            chat = unicode(e.arguments()[0], "utf-8")
        except:
            chat = "### INVALID UTF-8 ###"
        nick = nm_to_n(e.source())
        ch = self.channel
        if c.server == self.main: 
            pass
        else: 
           print "live from co" 
           main_co = self.get_conn(self.main)
           main_co.privmsg(ch, chat)

    def get_conn(self,server_name):
        for key, value in self.conn.items():
            if key[0]==server_name:
                return value
        return None

def main():
    server=["irc.o-in.dwango.co.jp","irc.freenode.org"]
    channel = "#ktmt.github" 
    spy_channel = "#test_irc"
    nickname = "live_orakaro" 
    main = "irc.freenode.org"

    bot = GothamLive(channel, spy_channel, nickname, server, main)
    bot.start()

if __name__ == "__main__":
    main()
