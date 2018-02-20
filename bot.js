const Discord = require('discord.js');
const client = new Discord.Client();

client.on('ready', () => {
    console.log('I am ready!');
});

client.on('message', message => {
  if(message.author.bot) return;
  if(message.channel.type === "dm") return;
  
  if (message.content === 'ping') {
  	message.reply('pong');
	}
  if (message.content === 'info') {
  	message.reply('info');
	}
});

// THIS  MUST  BE  THIS  WAY
client.login(process.env.BOT_TOKEN);
