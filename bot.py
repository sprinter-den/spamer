from aiogram.utils import executor
import asyncio
from loader import scheduler, dp
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify


async def on_startup(dispatcher):
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    scheduler.start()
    executor.start_polling(dp, on_startup=on_startup)
