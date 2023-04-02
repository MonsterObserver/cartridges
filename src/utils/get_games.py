# get_games.py
#
# Copyright 2022-2023 kramo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

import json


def get_games(parent_widget, game_ids=None):
    games_dir = parent_widget.data_dir / "cartridges" / "games"
    games = {}

    if not games_dir.exists():
        return {}

    if game_ids:
        game_files = [games_dir / f"{game_id}.json" for game_id in game_ids]
    else:
        game_files = games_dir.iterdir()

    for game in game_files:
        data = json.loads(game.read_text())
        games[data["game_id"]] = data

    return games
