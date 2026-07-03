from os import environ, path
from disnake.ext import commands
import disnake
from dotenv import load_dotenv
from json import load, dump
from datetime import datetime
from time import time

class sendnews(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

#Упом рольки/без цвета
    class sendmodal_mentetion(disnake.ui.Modal):
        def __init__(self, channel: disnake.TextChannel, image, linknews, bot: commands.Bot, role: disnake.Role):
            self.channel = channel
            self.image = image
            self.bot = bot
            self.linknews = linknews
            self.role = role

            components = [
                disnake.ui.TextInput(
                    label='Заголовок',
                    placeholder='Напишите заголовок',
                    custom_id='labelnews',
                    style=disnake.TextInputStyle.short
                ),
                disnake.ui.TextInput(
                    label='Содержимое новости',
                    placeholder='Введите содержимое новости',
                    custom_id='infonews',
                    style=disnake.TextInputStyle.paragraph,
                )
            ]
            super().__init__(
                title=f'Создание новости(упом - {self.role})',
                components=components,
                custom_id='createnews_ment'
            )
        
        async def callback(self, inter: disnake.ModalInteraction):
            await inter.response.defer()

            label = inter.text_values['labelnews']
            info = inter.text_values['infonews']

            if self.linknews:
                embed = (
                    disnake.Embed(
                        title=f'{str(label)}',
                        description=f'{str(info)}',
                        timestamp=datetime.now(),
                        color=disnake.Color.green()
                    )
                    .set_footer(text=f'Редактор новости: {inter.author.name}')
                    .set_author(name=inter.guild.me.display_name, icon_url=self.bot.user.display_avatar.url)\
                    .set_image(url=self.linknews)
                )

                await self.channel.send(content=self.role.mention)
                await self.channel.send(embed=embed)
                return
            
            elif self.image:
                embed = (
                    disnake.Embed(
                        title=f'{str(label)}',
                        description=f'{str(info)}',
                        timestamp=datetime.now(),
                        color=disnake.Color.green()
                    )
                    .set_footer(text=f'Редактор новости: {inter.author.name}')
                    .set_author(name=inter.guild.me.display_name, icon_url=self.bot.user.display_avatar.url)
                    .set_image(url=self.image.url)
                )

                await self.channel.send(content=self.role.mention)
                await self.channel.send(embed=embed)
                return
            
            embed = (
                disnake.Embed(
                    title=f'{str(label)}',
                    description=f'{str(info)}',
                    timestamp=datetime.now(),
                    color=disnake.Color.green()
                )
                .set_footer(text=f'Редактор новости: {inter.author.name}')
                .set_author(name=inter.guild.me.display_name, icon_url=self.bot.user.display_avatar.url)
            )
                
            await self.channel.send(content=self.role.mention)
            await self.channel.send(embed=embed)
            return
            
#Упом рольки/с выбором цвета
    class sendmodal_mentetioncolor(disnake.ui.Modal):
        def __init__(self, channel: disnake.TextChannel, image, linknews, bot: commands.Bot, role: disnake.Role, color: disnake.Color):
            self.channel = channel
            self.image = image
            self.bot = bot
            self.linknews = linknews
            self.role = role
            self.color = color

            components = [
                disnake.ui.TextInput(
                    label='Заголовок',
                    placeholder='Напишите заголовок',
                    custom_id='labelnews',
                    style=disnake.TextInputStyle.short
                ),
                disnake.ui.TextInput(
                    label='Содержимое новости',
                    placeholder='Введите содержимое новости',
                    custom_id='infonews',
                    style=disnake.TextInputStyle.paragraph,
                )
            ]
            super().__init__(
                title=f'Создание новости(упом - {self.role})',
                components=components,
                custom_id='createnews_ment_color'
            )
        
        async def callback(self, inter: disnake.ModalInteraction):
            await inter.response.defer()
            label = inter.text_values['labelnews']
            info = inter.text_values['infonews']

            if self.linknews:
                embed = (
                    disnake.Embed(
                        title=f'{str(label)}',
                        description=f'{str(info)}',
                        timestamp=datetime.now(),
                        color=self.color
                    )
                    .set_footer(text=f'Редактор новости: {inter.author.name}')
                    .set_author(name=inter.guild.me.display_name, icon_url=self.bot.user.display_avatar.url)
                    .set_image(url=self.linknews)
                )

                await self.channel.send(content=self.role.mention)
                await self.channel.send(embed=embed)
                return
            
            elif self.image:
                embed = (
                    disnake.Embed(
                        title=f'{str(label)}',
                        description=f'{str(info)}',
                        timestamp=datetime.now(),
                        color=self.color
                    )
                    .set_footer(text=f'Редактор новости: {inter.author.name}')
                    .set_author(name=inter.guild.me.display_name, icon_url=self.bot.user.display_avatar.url)
                    .set_image(url=self.image.url)
                )

                await self.channel.send(content=self.role.mention)
                await self.channel.send(embed=embed)
                return
            
            embed = (
                disnake.Embed(
                    title=f'{str(label)}',
                    description=f'{str(info)}',
                    timestamp=datetime.now(),
                    color=self.color
                )
                .set_footer(text=f'Редактор новости: {inter.author.name}')
                .set_author(name=inter.guild.me.display_name, icon_url=self.bot.user.display_avatar.url)
            )
                
            await self.channel.send(content=self.role.mention)
            await self.channel.send(embed=embed)

#неУпом рольки/без цвета
    class sendmodal_nomentetion(disnake.ui.Modal):
        def __init__(self, channel: disnake.TextChannel, image, linknews, bot: commands.Bot):
            self.channel = channel
            self.image = image
            self.bot = bot
            self.linknews = linknews

            components = [
                disnake.ui.TextInput(
                    label='Заголовок',
                    placeholder='Напишите заголовок',
                    custom_id='labelnews',
                    style=disnake.TextInputStyle.short
                ),
                disnake.ui.TextInput(
                    label='Содержимое новости',
                    placeholder='Введите содержимое новости',
                    custom_id='infonews',
                    style=disnake.TextInputStyle.paragraph,
                )
            ]
            super().__init__(
                title=f'Создание новости(без упома)',
                components=components,
                custom_id='createnews_noment'
            )
        
        async def callback(self, inter: disnake.ModalInteraction):
            await inter.response.defer()
            label = inter.text_values['labelnews']
            info = inter.text_values['infonews']

            if self.linknews:
                embed = (
                    disnake.Embed(
                        title=f'{str(label)}',
                        description=f'{str(info)}',
                        timestamp=datetime.now(),
                        color=disnake.Color.green()
                    )
                    .set_footer(text=f'Редактор новости: {inter.author.name}')
                    .set_author(name=inter.guild.me.display_name, icon_url=self.bot.user.display_avatar.url)\
                    .set_image(url=self.linknews)
                )

                await self.channel.send(embed=embed)
                return
            
            elif self.image:
                embed = (
                    disnake.Embed(
                        title=f'{str(label)}',
                        description=f'{str(info)}',
                        timestamp=datetime.now(),
                        color=disnake.Color.green()
                    )
                    .set_footer(text=f'Редактор новости: {inter.author.name}')
                    .set_author(name=inter.guild.me.display_name, icon_url=self.bot.user.display_avatar.url)
                    .set_image(url=self.image.url)
                )

                await self.channel.send(embed=embed)
                return
            
            embed = (
                disnake.Embed(
                    title=f'{str(label)}',
                    description=f'{str(info)}',
                    timestamp=datetime.now(),
                    color=disnake.Color.green()
                )
                .set_footer(text=f'Редактор новости: {inter.author.name}')
                .set_author(name=inter.guild.me.display_name, icon_url=self.bot.user.display_avatar.url)
            )
                
            await self.channel.send(embed=embed)
            return
            
#неУпом рольки/с выбором цвета
    class sendmodal_nomentetioncolor(disnake.ui.Modal):
        def __init__(self, channel: disnake.TextChannel, image, linknews, bot: commands.Bot, color: disnake.Color):
            self.channel = channel
            self.image = image
            self.bot = bot
            self.linknews = linknews
            self.color = color

            components = [
                disnake.ui.TextInput(
                    label='Заголовок',
                    placeholder='Напишите заголовок',
                    custom_id='labelnews',
                    style=disnake.TextInputStyle.short
                ),
                disnake.ui.TextInput(
                    label='Содержимое новости',
                    placeholder='Введите содержимое новости',
                    custom_id='infonews',
                    style=disnake.TextInputStyle.paragraph,
                )
            ]
            super().__init__(
                title=f'Создание новости(без упома)',
                components=components,
                custom_id='createnews_noment_color'
            )
        
        async def callback(self, inter: disnake.ModalInteraction):
            await inter.response.defer()
            label = inter.text_values['labelnews']
            info = inter.text_values['infonews']

            if self.linknews:
                embed = (
                    disnake.Embed(
                        title=f'{str(label)}',
                        description=f'{str(info)}',
                        timestamp=datetime.now(),
                        color=self.color
                    )
                    .set_footer(text=f'Редактор новости: {inter.author.name}')
                    .set_author(name=inter.guild.me.display_name, icon_url=self.bot.user.display_avatar.url)
                    .set_image(url=self.linknews)
                )

                await self.channel.send(embed=embed)
                return
            
            elif self.image:
                embed = (
                    disnake.Embed(
                        title=f'{str(label)}',
                        description=f'{str(info)}',
                        timestamp=datetime.now(),
                        color=self.color
                    )
                    .set_footer(text=f'Редактор новости: {inter.author.name}')
                    .set_author(name=inter.guild.me.display_name, icon_url=self.bot.user.display_avatar.url)
                    .set_image(url=self.image.url)
                )
                
                await self.channel.send(embed=embed)
                return
            
            embed = (
                disnake.Embed(
                    title=f'{str(label)}',
                    description=f'{str(info)}',
                    timestamp=datetime.now(),
                    color=self.color
                )
                .set_footer(text=f'Редактор новости: {inter.author.name}')
                .set_author(name=inter.guild.me.display_name, icon_url=self.bot.user.display_avatar.url)
            )
                
            await self.channel.send(embed=embed)

    @commands.slash_command(name='send_news', description='Отправка новости')
    async def news_ment(self, inter: disnake.ApplicationCommandInteraction, 
                        channel: disnake.TextChannel = commands.Param(name='канал'), 
                        role: disnake.Role = commands.Param(name='роль', default=None), 
                        linknews: str = commands.Param(name='ссылка', description='ссылка на картинку', default=None),
                        image: disnake.Attachment = commands.Param(name='картинка', default=None),
                        color: str = commands.Param(name='цвет', description='Введите цвет', default=None)):
        
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
        
        parsed_col = None
        if color:
            try:
                parsed_col = disnake.Color(int(color.strip('#'), 16))
            except ValueError:
                await inter.response.send_message(embed=(
                    disnake.Embed(
                        description='[🟥] | Неверный HEX формат'
                    )
                ))
                return
        
        if role and parsed_col:
            modal = self.sendmodal_mentetioncolor(
                channel=channel,
                image=image,
                linknews=linknews,
                bot=self.bot,
                role=role,
                color=parsed_col
            )
        elif role and not parsed_col:
            modal = self.sendmodal_mentetion(
                channel=channel,
                image=image,
                linknews=linknews,
                bot=self.bot,
                role=role
            )
        elif not role and parsed_col:
            modal = self.sendmodal_nomentetioncolor(
                channel=channel,
                image=image,
                linknews=linknews,
                bot=self.bot,
                color=parsed_col
            )
        else:
            modal = self.sendmodal_nomentetion(
                channel=channel,
                image=image,
                linknews=linknews,
                bot=self.bot
            )

        await inter.response.send_modal(modal=modal)

def setup(bot: commands.Bot):
    bot.add_cog(sendnews(bot))