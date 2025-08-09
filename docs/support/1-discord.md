# The DCC-EX Discord Server

The DCC-EX team has a strong preference for providing support via the DCC-EX Discord server, and we have information on joining and using Discord on this page.

![DCC-EX Discord](/_static/images/discord/dcc-ex-discord.png){ align=right width=300px }

Discord is free to join, and provides these benefits over our other support methods:

- The DCC-EX team actively participate in Discord, so you can talk to the people who create the products
- There is a global community of over 4,000 DCC-EX users in Discord
- When people are online at the same time, you can have a live, interactive chat
- There is the opportunity for DCC-EX users to help other users, which happens frequently

In short, Discord gives you the best access to the broadest set of people who can help with DCC-EX; an entire, global community of users.

***Please ensure when you first join, you review the Server Guide which will help you get started with our Discord server.***

## Joining and Using Discord

1. Use the button below to navigate to your invitation to join our Discord server:

    [DCC-EX Discord server](https://discord.gg/y2sB4Fp){ .md-button }

2. Click ``Register on the sign-in page:

    ![Register](/_static/images/discord/discord-sign-in.png){ width=400px }

3. Fill in your details, click ``Continue``, and follow the instructions:

    ![Details](/_static/images/discord/discord-register.png){ width=400px }

4. Choose which channels you are interested in and if you're unsure, just select ``Get help to setup an EX-CommandStation``:

    ![Channels](/_static/images/discord/discord-customise.png){ width=600px }

## Sharing Code and Configuration Snippets

Quite often in interactions in Discord, you will need to share either some code you have entered or parts of configuration files as text in the channel. Just pasting raw code or configuration text in Discord doesn't render well in the screen, and often characters are interpreted as emojis or other random ASCII characters which confuse the issue.

Discord has a handy way of rendering code correctly so it appears correctly. To do this, you need to use the grave accent or backtick key  ++grave++ on your keyboard.

On English QWERTY keyboards, this typically coexists with the tilde ++tilde++ key and is located in the top left near the Escape ++esc++ key.

This may appear elsewhere on other international keyboards, but Googling "grave accent key" or "backtick key" for your keyboard type should provide guidance on where it is located.

To use this in Discord, simply surround your code or configuration snippets in three grave accents or backticks:

````console
```
// config.h entry for the EX8874
#define MOTORSHIELD EX8874_SHIELD
```
````

If you're sharing code, sometimes it can be helpful to specify the language, which in the case of DCC-EX is typically C++:

````console
```cpp
uint8_t dummy = 0;
```
````

## Discord Channels

We have organised the Discord server into various channels which help keep similar topics grouped together.

***Please try to post questions in the relevant channel, and please do not post the same question in multiple channels.***

If you can't see channels which seem relevant or of interest to you, you can customise which channels you can see:

- Click ``Channels & Roles`` under the DCC-EX server menu:

    ![Channels & Roles](/_static/images/discord/channels-roles.png){ width=200px }

- You can change your customisation options if you wish:

    ![Customise](/_static/images/discord/customise-channels.png){ width=400px }

- Or you can browse the channels and select which ones you'd like to see:

    ![Browse](/_static/images/discord/browse-channels.png){ width=400px }

Here are some examples of commonly used channels, and there are plenty more:

- ``#support-and-issues__ex-commandstation`` - Use this channel for general EX-CommandStation conversations and help
- ``#exrail`` - Use this channel for general EXRAIL conversations and help
- ``#tack-manager`` - Use this channel for general TrackManager conversations and help
- ``#accessories`` - Use this channel for topics such as PCA9685 servo controllers and servos, MCP23017 I/O expansion boards, and other accessories
- ``#sensors``
- ``signals``

Our other products typically have their own channel also:

- ``#ex-ioexpander`` - EX-IOExpander, not to be confused with other I/O expansion modules such as PCA9685 or MCP23017 devices, see ``#accessories``
- ``#ex-dccinspector``
- ``#ex-turntable``
- ``#ex-fastclock``

## Opening a Support Ticket

If you need help with a specific issue and the conversation in the general support channels haven't resolved the issue, you are welcome to open a support ticket in Discord to get help for your specific issue.

- From the ``Server Guide``, you can select the ``Open a Support Ticket`` option:

    ![Select Server Guide](/_static/images/discord/server-guide.png){ width=200px }

    ![Server Guide](/_static/images/discord/support-ticket.png){ width=400px }

- This takes you to the TicketTool app, and clicking the ``Create ticket`` icon will open a support ticket:

    ![Create ticket](/_static/images/discord/create-ticket.png){ width=300px }

- You will see the message ``Ticket Created`` with the channel name of your new ticket:

    ![New ticket](/_static/images/discord/new-ticket.png){ width=300px }

- Clicking on the ticket channel will take you to the ticket, and it should also appear in your channels list, and you can now share all relevant information, upload the required logs and configuration files, and share any troubleshooting steps you've already attempted:

    ![Use ticket](/_static/images/discord/use-ticket.png){ width=500px }

Once your ticket has been created, only the DCC-EX support team members and yourself will have access to the ticket, but other users can be invited if necessary.

In order to help the DCC-EX team give you the help you need, you will need to provide as much information as possible, as we cannot read minds, see your setup, access your hardware or configuration files, nor look over your shoulder to see what is going on.

![Discord Upload](/_static/images/discord/discord-upload.png){ align=right width=200px }

To upload files to the ticket, click the ``+`` sign in the message box and select ``Upload a File``.

Please provide this information at the time you open the support ticket:

- [ ] The product and version
- [ ] The exact hardware in use
- [ ] Upload serial/console logs
- [ ] Upload all configuration files for the software in use
- [ ] Detail any troubleshooting steps you have already performed

### Closing a Support Ticket

Once your issue is resolved, we encourage you to close your support ticket, as you can only have one open at a time, and a new and different issue should be in a different ticket.

You can either click the ``Close`` button (you may need to scroll all the way to the top of the ticket thread):

![Close Ticket](/_static/images/discord/close-ticket.png){ width=500px }

Or you can type ``/close`` in the message box and hit the ++enter++ key.
