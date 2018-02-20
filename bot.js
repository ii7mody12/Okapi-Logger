const Discord = require('discord.js');
const bot = new Discord.Client();
￼ bot.on("ready", async () => {
￼   console.log(`${bot.user.username} is online!`);
￼   bot.user.setActivity("your commands", {type: "Following"});
￼   //bot.user.setGame("on SourceCade!");
￼ });
bot.on('message', message => {
    if (message.content === 'ping') {
    	message.reply('pong');
  	}
});

// THIS  MUST  BE  THIS  WAY
bot.login(process.env.BOT_TOKEN);
