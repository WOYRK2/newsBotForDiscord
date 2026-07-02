text = (
'''
██████╗░██╗░░░██╗██╗  ░██╗░░░░░░░██╗░█████╗░██╗░░░██╗██████╗░██╗░░██╗
██╔══██╗╚██╗░██╔╝╚═╝  ░██║░░██╗░░██║██╔══██╗╚██╗░██╔╝██╔══██╗██║░██╔╝
██████╦╝░╚████╔╝░░░░  ░╚██╗████╗██╔╝██║░░██║░╚████╔╝░██████╔╝█████═╝░
██╔══██╗░░╚██╔╝░░░░░  ░░████╔═████║░██║░░██║░░╚██╔╝░░██╔══██╗██╔═██╗░
██████╦╝░░░██║░░░██╗  ░░╚██╔╝░╚██╔╝░╚█████╔╝░░░██║░░░██║░░██║██║░╚██╗
╚═════╝░░░░╚═╝░░░╚═╝  ░░░╚═╝░░░╚═╝░░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝
'''
)
from os import environ
from disnake.ext import commands
import disnake
from dotenv import load_dotenv
import os
import platform
import argparse

load_dotenv('.env', override=True)

toke = environ.get('token')

parser = argparse.ArgumentParser()
parser.add_argument('--test', action='store_true', help='запустить откладчик')
args = parser.parse_args()

if args.test:
    bot = commands.Bot(command_prefix='$', sync_commands=True, sync_commands_debug=True, test_guilds=[1363905513141702746], activity=disnake.Game(name='v1.0'), status=disnake.Status.dnd)
else:
    bot = commands.Bot(command_prefix='$',test_guilds=[1363905513141702746], activity=disnake.Game(name='v1.0'), status=disnake.Status.dnd)

@bot.event
async def on_ready():
    if args.test:
        print(f'Загруженные коги: {list(bot.cogs.keys())}')
        print(f'Загруженные команды: {[cmd.name for cmd in bot.slash_commands]}')
        print('------------------------------------------')
        print('github - WOYRK2')
        print(f'Бот запущен!(test) пинг - {round(bot.latency * 1000)}')
        print('------------------------------------------')
    else:
        os.system('cls' if platform.system() == 'Windows' else 'clear')

        print(text)
        print('github - WOYRK2')
        print(f'Бот запущен! пинг - {round(bot.latency * 1000)}')
    

if __name__ == '__main__':
        bot.load_extensions('cogs')
        bot.run(toke)