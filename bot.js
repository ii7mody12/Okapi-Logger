var Discord = require('discord.io');

var bot = new Discord.Client({
    token: "NDE1MjY5NzczODg3NDA2MDgw.DW18-w.rWFfcZzfeqDIYalhhASvGzfFiss",
    autorun: true
});

bot.on('ready', function() {
    console.log('Logged in as %s - %s\n', bot.username, bot.id);
});

bot.on('message', function(user, userID, channelID, message, event) {
    if (message === "ding") {
        bot.sendMessage({
            to: channelID,
            message: "dong"
        });
    }
});
