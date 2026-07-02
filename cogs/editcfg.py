from os import environ, path
from disnake.ext import commands
import disnake
from dotenv import load_dotenv
from json import load, dump
from datetime import datetime
from time import time

class cfgedit(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.slash_command(name='cfg_addrole', description='Добавить роль для работы с новостями')
    async def addrole(self, inter: disnake.ApplicationCommandInteraction, role: disnake.Role = commands.Param(name='роль')):
        roleId = role.id
        userId = inter.author.id
        ownerId = inter.guild.owner_id
        userroleid = [role.id for role in inter.author.roles]
        
        with open('cfg.json', 'r', encoding='utf-8') as f:
            data = load(f)
            
            if data['isAuth'] == False:
                await inter.response.send_message(embed=(
                    disnake.Embed(
                        description='`[🟥] | Сервер не зарегистрирован`',
                        color=disnake.Color.red()
                    )
                ))
                return
            
            rolesData = data['TrustIdRole']
            isRole = any(role_id in rolesData for role_id in userroleid)
        
        if roleId in rolesData:
                await inter.response.send_message(embed=(
                    disnake.Embed(
                        description='`[🟥] | Роль уже есть в конфиге!`',
                        color=disnake.Color.red()
                    )
                ))
                return
        
        if not (isRole or ownerId == userId or inter.author.guild_permissions.administrator):
            await inter.response.send_message(embed=(
                disnake.Embed(
                    description='`[🟥] | У вас нет прав!`',
                    color=disnake.Color.red(),
                )
            ))
            return
        
        data['TrustIdRole'].append(roleId)
        
        with open('cfg.json', 'w', encoding='utf-8') as f:
            dump(data, f, indent=4, ensure_ascii=False)
            
            embed = (
                disnake.Embed(
                    title='**Добавление роли**',
                    description='`[🟩] | Роль успешно добавлена в конфиг`',
                    timestamp=datetime.now(),
                    color=disnake.Color.green()
                )
                .set_author(name=inter.author, icon_url=inter.author.avatar.url)
            )
            
            embed.add_field(
                name='**Роль**',
                value=f'<@&{roleId}>',
                inline=True,
            )
            
            embed.add_field(
                name='**Роль (на случай если не пинганулась роль)**',
                value=f'**`{role.name}`**',
                inline=True
            )
            
            embed.add_field(
                name='**Кто добавил**',
                value=f'<@{userId}>',
                inline=True,
            )
            
            embed.add_field(
                name='**Время добавления**',
                value=f'**<t:{int(time())}:F>**',
                inline=True,
            )
            
            await inter.response.send_message(embed=embed)
    
    @commands.slash_command(name='cfg_dellrole', description='Удаление роли из конфига')
    async def dellrole(self, inter: disnake.ApplicationCommandInteraction, role: disnake.Role = commands.Param(name='роль')):
        roleId = role.id
        userId = inter.author.id
        ownerId = inter.guild.owner_id
        userroleid = [role.id for role in inter.author.roles]
        
        with open('cfg.json', 'r', encoding='utf-8') as f:
            data = load(f)
            
            if data['isAuth'] == False:
                await inter.response.send_message(embed=(
                    disnake.Embed(
                        description='`[🟥] | Сервер не зарегистрирован`',
                        color=disnake.Color.red()
                    )
                ))
                return
            
            rolesData = data['TrustIdRole']
            isRole = any(role_id in rolesData for role_id in userroleid)
        
        if not roleId in rolesData:
                await inter.response.send_message(embed=(
                    disnake.Embed(
                        description='`[🟥] | Роли нет в конфиге!`',
                        color=disnake.Color.red()
                    )
                ))
                return
        
        if not (isRole or ownerId == userId or inter.author.guild_permissions.administrator):
            await inter.response.send_message(embed=(
                disnake.Embed(
                    description='`[🟥] | У вас нет прав!`',
                    color=disnake.Color.red(),
                )
            ))
            return
        
        data['TrustIdRole'].remove(roleId)
        
        with open('cfg.json', 'w', encoding='utf-8') as f:
            dump(data, f, indent=4, ensure_ascii=False)
            
            embed = (
                disnake.Embed(
                    title='**Удаление роли**',
                    description='`[🟩] | Роль успешно удалена из конфига`',
                    timestamp=datetime.now(),
                    color=disnake.Color.green()
                )
                .set_author(name=inter.author, icon_url=inter.author.avatar.url)
            )
            
            embed.add_field(
                name='**Роль**',
                value=f'<@&{roleId}>',
                inline=True,
            )
            
            embed.add_field(
                name='**Роль (на случай если не пинганулась роль)**',
                value=f'**`{role.name}`**',
                inline=True
            )
            
            embed.add_field(
                name='**Кто удалил**',
                value=f'<@{userId}>',
                inline=True,
            )
            
            embed.add_field(
                name='**Время удаления**',
                value=f'**<t:{int(time())}:F>**',
                inline=True,
            )
            
            await inter.response.send_message(embed=embed)
    
    @commands.slash_command(name='cfg_info')
    async def show(self, inter: disnake.ApplicationCommandInteraction):
        userId = inter.author.id
        ownerId = inter.guild.owner_id
        userroleid = [role.id for role in inter.author.roles]
        
        with open('cfg.json', 'r', encoding='utf-8') as f:
            data = load(f)
            
            if data['isAuth'] == False:
                await inter.response.send_message(embed=(
                    disnake.Embed(
                        description='`[🟥] | Сервер не зарегистрирован`',
                        color=disnake.Color.red()
                    )
                ))
                return
            
            rolesData = data['TrustIdRole']
            isRole = any(role_id in rolesData for role_id in userroleid)
        
        if not (isRole or ownerId == userId or inter.author.guild_permissions.administrator):
            await inter.response.send_message(embed=(
                disnake.Embed(
                    description='`[🟥] | У вас нет прав!`',
                    color=disnake.Color.red(),
                )
            ))
            return
        
        embed = (
            disnake.Embed(
                title='**Информация конфига**',
                description='```Ниже представлена вся информация конфига```',
                timestamp=datetime.now(),
                color=disnake.Color.green()
            )
            .set_author(name=inter.author.name, icon_url=inter.author.avatar.url)
        )
        
        ment = ''.join(f'<@&{roleidredact}> ,' for roleidredact in data['TrustIdRole'])
        
        embed.add_field(
            name='**Роли редакторов**',
            value=f'{ment}',
            inline=False
        )
        
        embed.add_field(
            name='**Регистрация сервера**',
            value='**`[🟩] Сервер зарегистрирован! (Ну типо че еще писать?)`**',
            inline=True
        )
        
        await inter.response.send_message(embed=embed)

    @commands.slash_command(name='cfg_reset', description='Сбрасывает конфиг полностью!')
    async def cfgreset(self, inter: disnake.ApplicationCommandInteraction):
        userId = inter.author.id
        ownerId = inter.guild.owner_id
        userroleid = [role.id for role in inter.author.roles]
        
        with open('cfg.json', 'r', encoding='utf-8') as f:
            data = load(f)
            
            if data['isAuth'] == False:
                await inter.response.send_message(embed=(
                    disnake.Embed(
                        description='`[🟥] | Сервер не зарегистрирован`',
                        color=disnake.Color.red()
                    )
                ))
                return
            
            rolesData = data['TrustIdRole']
            isRole = any(role_id in rolesData for role_id in userroleid)
        
        if not (ownerId == userId or inter.author.guild_permissions.administrator):
            await inter.response.send_message(embed=(
                disnake.Embed(
                    description='`[🟥] | У вас нет прав!`',
                    color=disnake.Color.red(),
                )
            ))
            return
        
        await inter.response.send_message(embed=(
            disnake.Embed(description='**`Внимание! Эта команда сбросит полностью конфиг до изначального варианта!`**', color=disnake.Color.dark_red()
                          )),ephemeral=True ,components=[
                              disnake.ui.Button(label='Сбросить', style=disnake.ButtonStyle.danger, custom_id='resetcfg'),
                              disnake.ui.Button(label='Не сбрасывать', style=disnake.ButtonStyle.green, custom_id='norestcfg')
                          ])
        
    @commands.Cog.listener('on_button_click')
    async def on_button_click(self, inter: disnake.MessageInteraction):
        await inter.response.defer()
        
        if inter.component.custom_id not in ['resetcfg', 'norestcfg']:
            return
        
        userId = inter.author.id
        ownerId = inter.guild.owner_id
        userroleid = [role.id for role in inter.author.roles]
        
        if inter.component.custom_id == 'resetcfg':
            
            with open('cfg.json', 'r', encoding='utf-8') as f:
                data = load(f)
                
                if data['isAuth'] == False:
                    await inter.edit_original_response(embed=(
                        disnake.Embed(
                            description='`[🟥] | Сервер не зарегистрирован`',
                            color=disnake.Color.red()
                        )
                    ), components=[])
                    return
                
                rolesData = data['TrustIdRole']
                isRole = any(role_id in rolesData for role_id in userroleid)
            
            if not (ownerId == userId or inter.author.guild_permissions.administrator):
                await inter.edit_original_response(embed=(
                    disnake.Embed(
                        description='`[🟥] | У вас нет прав!`',
                        color=disnake.Color.red(),
                    )
                ), components=[])
                return
            
            data['TrustIdRole'] = []
            data['isAuth'] = False
            
            with open('cfg.json', 'w', encoding='utf-8') as f:
                dump(data, f, indent=4, ensure_ascii=False)
                
                embed = (
                    disnake.Embed(
                        title='**Сброс бота**',
                        description='`[🟩] | Успешный сброс бота!`',
                        timestamp=datetime.now(),
                        color=disnake.Color.green()
                    )
                    .set_author(name=inter.author.name, icon_url=inter.author.avatar.url)
                )
                
                embed.add_field(
                    name='**Кто сбросил бота**',
                    value=f'<@{inter.author.id}>',
                    inline=False,
                )
                
                await inter.edit_original_response(embed=embed, components=[])
                
        elif inter.component.custom_id == 'norestcfg':
            with open('cfg.json', 'r', encoding='utf-8') as f:
                data = load(f)
                
                if data['isAuth'] == False:
                    await inter.response.edit_message(embed=(
                        disnake.Embed(
                            description='`[🟥] | Сервер не зарегистрирован`',
                            color=disnake.Color.red()
                        )
                    ), components=[])
                    return
                
                rolesData = data['TrustIdRole']
                isRole = any(role_id in rolesData for role_id in userroleid)
            
            if not (ownerId == userId or inter.author.guild_permissions.administrator):
                await inter.response.edit_message(embed=(
                    disnake.Embed(
                        description='`[🟥] | У вас нет прав!`',
                        color=disnake.Color.red(),
                    )
                ), components=[])
                return
            
            await inter.edit_original_response(components=[])
    
def setup(bot: commands.Bot):
    bot.add_cog(cfgedit(bot))