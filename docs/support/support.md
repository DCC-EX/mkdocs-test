# Help and Support

At some point you will likely need to get some help or support for our products, and the available methods are outlined on this page.

!!! note "If you purchased hardware from a reseller"

    For users of hardware products purchased from resellers, in the event of a hardware issue please contact the reseller in the first instance. Each reseller is responsible for supporting the hardware they sell.

Please note that the DCC-EX team are all volunteers and are distributed globally, so while we endeavour to help as much and as quickly as we can, all support is provided on a best-effort basis only, and there will be times where no team members are available.

This is why we strongly recommend Discord as the best source of support, because there is a global community of over 4,000 users, some of whom may be able to help before a DCC-EX team member is online.

## Information required for support queries

When requesting support for any of our products, there is some critical information you must provide in order for us to be able to help you. The more information you provide up front, the quicker we can help resolve the issue.

This is the information typically required:

- The product and version
- The exact hardware in use
- All error messages and error codes
- Serial console logs
- EX-Installer logs
- All configuration files for the software in use
- Detail any troubleshooting steps you have already performed
- If applicable/possible, clear (not blurry) and detailed photos of hardware connections typically help

_**Please! Do not take photos of your computer screen when sharing logs and error codes as they are always unreadable and do not help us help you.**_

Below we outline how to obtain each of these items, and it is easiest if you use EX-Installer's Device Monitor to connect to the serial console.

### Using EX-Installer Device Monitor

--8<-- "snippets/ex-installer/device-monitor.md"

### Product and version

The command `<s>` will show the current status of EX-CommandStation which includes the platform, motorshield definition, and software version. For convenience, the EX-Installer Device monitor highlights this information as shown in the screen shot.

![EX-CommandStation version](/_static/images/support/ex-commandstation-show-version.png){ width=50% }

### Exact hardware in use

For users of the EX-CSB1, we simply need to know which reseller you purchased from, and if it was supplied with an additional EX8874 motorshield and/or a display.

For DIY users, we need to know the brand and model of all devices in use.

It's not helpful to simply say "Mega with standard shield", but rather "Elegoo Mega with genuine Arduino R3 motorshield powered by a 15V DC power supply".

If you're using something a little out of the ordinary, a link to the purchase page will also help.

### All error messages and error codes



### Serial console logs

--8<-- "snippets/ex-installer/startup-logs.md"

Once you have saved the serial console logs, you can upload them in Discord using the "Upload a file" option when clicking the `+` button.

![Discord upload](/_static/images/discord/discord-upload.png){ width=25% }

### Configuration files

--8<-- "snippets/ex-installer/backup-config-files.md"

As per uploading your serial console logs above, you can use the "Upload a file" option with the `+` button in Discord.

![Discord upload](/_static/images/discord/discord-upload.png){ width=25% }

## Discord (Strongly recommended)

Our strongly recommended support option is the DCC-EX Discord server, where you can interact directly with the DCC-EX team as well as a global community of over 4,400 users. Issues are usually resolved quite quickly in comparison with the other options, and you can also interact with the community in real-time.

Please refer to our [Discord page](/support/discord.md) which outlines how to join our Discord server, interact with the community, and how to raise support tickets.

## GitHub

If you are an existing GitHub user, you can also get support via GitHub which is particularly useful for bug reports. While all the DCC-EX team members have GitHub accounts and can respond, this is typically not as quick as getting support via our recommended Discord server option.

Please refer to our [GitHub page](/support/github.md) on the various repositories you can raise issues in.

## TrainBoard

If you're a member of the TrainBoard forum, there is a [DCC++ Forum](https://www.trainboard.com/highball/index.php?forums/dcc.177/) you can post in for help. Yes, it is still called DCC++.

Note that this isn't the busiest forum and only a few of the DCC-EX team are members of TrainBoard, so resolution of issues may be slow. There are other members of the forum that may try to assist though.

## Email (NOT recommended)

While email support is available for those who have no other way to obtain support, there is only one team member with access to reply to your queries, and therefore _**this is a slow process and is not recommended.**_

If necessary, you can email us at <support@dcc-ex.com>.
