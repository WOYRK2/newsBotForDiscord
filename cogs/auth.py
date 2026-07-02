from os import environ, path
from disnake.ext import commands
import disnake
from dotenv import load_dotenv
from json import load, dump
from datetime import datetime
from time import time

class Auth(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.slash_command(name='auth_news')
    async def auth(self, inter: disnake.ApplicationCommandInteraction, role: disnake.Role = commands.Param(name='роль', description='выберите роль для работы с новостями')):
        OwnerID = inter.guild.owner_id
        UserID = inter.author.id
        
        if not (OwnerID == UserID or inter.author.guild_permissions.administrator):
            await inter.response.send_message(embed=(
                disnake.Embed(
                    description='`[🟥] | У вас нет прав!`',
                    color=disnake.Color.red(),
                )
            ))
            return
        
        with open('cfg.json', 'r', encoding='utf-8') as f:
            isauth = load(f)
            data = isauth
            isauth = isauth['isAuth']
            
            if isauth == True:
                await inter.response.send_message(embed=(
                    disnake.Embed(
                        description='`[🟥] | Сервер уже зарегистрирован`',
                        color=disnake.Color.red()
                    )
                ))
                return
        
        roleId = role.id
        
        with open('cfg.json', 'w', encoding='utf-8') as f:
            data['TrustIdRole'].append(roleId)
            data['isAuth'] = True
            
            dump(data, f, ensure_ascii=False, indent=4)
            
            embed = (
                disnake.Embed(
                    color=disnake.Color.green(),
                    timestamp=datetime.now(),
                    title='**Регистрация**',
                    description='`[🟩] Бот успешно зарегистрирован!`'
                )
                .set_author(name=inter.author, icon_url=inter.author.avatar.url)
            )
            
            embed.add_field(
                name='Кто зарегистрировал',
                value=f'<@{UserID}>',
                inline=True
            )
            
            embed.add_field(
                name='Время регистрации',
                value=f'**<t:{int(time())}:F>**',
                inline=True
            )
            
            await inter.response.send_message(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Auth(bot))