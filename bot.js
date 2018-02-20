var Discord = require('discord.io');

var client = new Discord.Client({
    token: "NDE1MjY5NzczODg3NDA2MDgw.DW18-w.rWFfcZzfeqDIYalhhASvGzfFiss",
    autorun: true
});

client.on('ready', function() {
    console.log('Logged in as %s - %s\n', client.username, client.id);
});

client.setPresence({
	game.name: 'On ndeogj',
});

client.on('message', function(user, userID, channelID, message, event) {
    if (message === "bot.ping") {
      client.sendMessage({
          to: channelID,
          message: "pong"
      });
    }
});
