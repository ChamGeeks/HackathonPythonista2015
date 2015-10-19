#!/usr/bin/env python
# coding: utf-8

# This was created before the ChamonixHackathon2015 API was created to have a local copy of the data tables.
# It is no longer required now that the API is available but it could be used for disconnected operations or testing.

import sqlite3

in_filename = 'data_setup.sql'
out_filename = 'burgers_and_beers.db'

with open(in_filename) as in_file:
    conn = sqlite3.connect(out_filename)
    conn.executescript(in_file.read())
    conn.commit()
    conn.close()
