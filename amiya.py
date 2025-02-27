import os
import sys
import asyncio
import core.frozen

from typing import Coroutine
from core.plugins import PluginsLoader
from core import app, bot, init_task, BotResource


def run_amiya(*tasks: Coroutine):
    try:
        BotResource.download_bot_resource()

        sys.path += [
            os.path.dirname(sys.executable),
            os.path.abspath('resource/env/python-dlls'),
            os.path.abspath('resource/env/python-standard-lib.zip'),
        ]
        loader = PluginsLoader(bot)

        asyncio.run(loader.load_local_plugins())
        asyncio.run(
            asyncio.wait(
                [
                    *init_task,
                    *tasks,
                ]
            )
        )
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    run_amiya(bot.start(launch_browser=True), app.serve())
