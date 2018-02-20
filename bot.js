const Discord = require('discord.js');
const client = new Discord.Client();
￼ client.on("ready", async () => {
￼   console.log(`${client.user.username} is online!`);
￼   bot.user.setActivity("your commands", {type: "Following"});
￼   //bot.user.setGame("on SourceCade!");
￼ });

client.on('message', message => {
    if (message.content === 'ping') {
    	message.reply('pong');
  	}
});

// THIS  MUST  BE  THIS  WAY
client.login(process.env.BOT_TOKEN);
