const Discord = require('discord.js');
const bot = new Discord.Client();
￼ bot.on("ready", async () => {
￼   console.log(`${bot.user.username} is online!`);
￼   bot.user.setActivity("your commands", {type: "Following"});
￼   //bot.user.setGame("on SourceCade!");
￼ });
client.on('ready', () => {
    console.log('I am ready!');
});

client.on('message', message => {
    if (message.content === 'ping') {
    	message.reply('pong');
  	}
});

// THIS  MUST  BE  THIS  WAY
client.login(process.env.BOT_TOKEN);
