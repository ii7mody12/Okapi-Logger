const botconfig = require("./botconfig.json");
const Discord = require('discord.js');

const bot = new Discord.Client({disableEveryone: true});

bot.on("ready", async () => {
  console.log('I am ready!');
});

bot.on("message", async message => {
  if(message.author.bot) return;
  if(message.channel.type === "dm") return;

  let prefix = botconfig.prefix;
  let messageArray = message.content.split(" ");
  let cmd = messageArray[0];
  let args = messageArray.slice(1);
//-------------------------
//---------botinfo---------
//-------------------------
  if(cmd === `${prefix}botinfo`){

    let bicon = bot.user.displayAvatarURL;
    let botembed = new Discord.RichEmbed()
    .setDescription("Bot Information")
    .setColor("#15f153")
    .setThumbnail(bicon)
    .addField("Bot Name", bot.user.username)
    .addField("Created On", bot.user.createdAt);

    return message.channel.send(botembed);
  }
  
});

// THIS  MUST  BE  THIS  WAY
bot.login(process.env.BOT_TOKEN);
