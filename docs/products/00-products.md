# DCC-EX Product Overview

The DCC-EX team has designed and released various different open source products aimed at making model trains accessible to more people.

This page briefly outlines each of our products, the experience level you need to be able to use them, and links to more information.

## Conductor Level ![Conductor Icon](/_static/images/levels/conductor.png){ .header-img }

These are our easy to use, get up and running quickly type products. You don't need to pick up a soldering iron or write any software, just plug them in and go!

Note that you may need to install some software on your computer to take advantage of some of these, but our documentation will walk you through that process.

![csb1](/_static/images/ex-csb1/csb1-small.png){ align=right}

### EX-CommandStation Booster 1 Express

![EX-CommandStation Logo](/_static/images/logos/product-logo-ex-commandstation-only-light.png){ .only-light width=400px }
![EX-CommandStation Logo](/_static/images/logos/product-logo-ex-commandstation-only-dark.png){ .only-dark width=400px }
![EX-CSB1 Logo](/_static/images/logos/product-logo-ex-csb1-only-light.png){ .only-light width=400px }
![EX-CSB1 Logo](/_static/images/logos/product-logo-ex-csb1-only-dark.png){ .only-dark width=400px }

A ready-to-run, all in one Command Station and Booster with built-in WiFi preloaded with our flagship train control and layout animation and automation software. For more information on this and how to purchase, head over to the [EX-CSB1 product page](/products/ex-commandstation/1-ex-csb1.md)

You can learn more about the software in the [EX-CommandStation documentation](/products/ex-commandstation/0-overview.md).

---

### EX-WebThrottle

![EX-WebThrottle Logo](/_static/images/logos/product-logo-ex-webthrottle-only-light.png){ .only-light width=400px }
![EX-WebThrottle Logo](/_static/images/logos/product-logo-ex-webthrottle-only-dark.png){ .only-dark width=400px }

This is the easiest way to validate you've connected your command station correctly to your track. Just load it up in your Chromium based web browser (Edge, Chrome, Opera) after connecting your command station to your computer and you can run your trains with it.

To access it, refer to the [EX-WebThrottle documentation](https://dcc-ex.com/legacy-docs/ex-webthrottle/index.html#ex-webthrottle).

---

### EX-Toolbox

![EX-Toolbox Logo](/_static/images/logos/product-logo-ex-toolbox-only-light.png){ .only-light width=400px }
![EX-Toolbox Logo](/_static/images/logos/product-logo-ex-toolbox-only-dark.png){ .only-dark width=400px }

For Android phone users, this is an extremely useful tool to help with configuring various aspects of your trains, command station, and accessories.

You can download it here [![app store](/_static/images/ex-toolbox/download.png)](https://play.google.com/store/apps/details?id=dcc_ex.ex_toolbox)

==TODO== ... Refer to the [EX-Toolbox documentation](https://dcc-ex.com/legacy-docs/ex-toolbox/index.html#ex-toolbox) for how to install and use it.

---

## Tinkerer level ![Tinkerer Icon](/_static/images/levels/tinkerer.png){ .header-img }

These products are more involved to get up and running, and aren't just plug in and go.

You will need to perform some assembly and configure and install some software to take advantage of these ones, but you won't need to solder anything.

![diy](/_static/images/mega/mega-small.png){ align=right}

### EX-CommandStation Recommended Self Build Option (DIY)

![EX-CommandStation Logo](/_static/images/logos/product-logo-ex-commandstation-only-light.png){ .only-light width=400px }
![EX-CommandStation Logo](/_static/images/logos/product-logo-ex-commandstation-only-dark.png){ .only-dark width=400px }
![CS DIY Logo](/_static/images/logos/product-logo-ex-cs-diy-only-light.png){ .only-light width=400px }
![CS DIY Logo](/_static/images/logos/product-logo-ex-cs-diy-only-dark.png){ .only-dark width=400px }

A supported DIY stack for EX-CommandStation using an Arduino Mega + EX-MotorShield8874 (or Arduino R3 Motor Shield) + EX-WiFiShield8266 (optional).

If you want to build it yourself, this is our recommended setup which simply requires some assembly and software installation with no advanced modifications required.

Refer to the [Easy build Arduino Mega page](/diy/20-mega-easy.md) for information on what to buy and how to assemble.

---

### EX-MotorShield8874

![EX-8874 Logo](/_static/images/logos/product-logo-ex-motorshield8874-only-light.png){ .only-light width=400px }
![EX-8874 Logo](/_static/images/logos/product-logo-ex-motorshield8874-only-dark.png){ .only-dark width=400px }

A dual channel, 5 amp (per channel) motor shield designed specifically for DCC-EX in an Arduino shield format.

Assembly is required to add this to an Arduino Mega along with software configuration.

Refer to the [EX-MotorShield8874 page](/products/ex-motorshield8874/ex-motorshield8874.md) for more information.

---

### EX-WiFiShield8266

![EX-8266 Logo](/_static/images/logos/product-logo-ex-wifishield8266-only-light.png){ .only-light width=400px }
![EX-8266 Logo](/_static/images/logos/product-logo-ex-wifishield8266-only-dark.png){ .only-dark width=400px }

A WiFi shield designed specifically for DCC-EX in an Arduino shield format.

Assembly is required to add this to an Arduino Mega along with software configuration.

Refer to the [EX-WiFiShield8266 page](/products/ex-wifishield8266/ex-wifishield8266.md) for more information.

---

## Engineer level ![Engineer Icon](/_static/images/levels/engineer.png){ .header-img }

These products are far more involved and complicated to get up and running.

This products go beyond simple assembly and you will need a good understanding of configuring software and hardware, including soldering components and making some modifications to existing hardware devices.

If you are new to DCC-EX and/or electronics in general, we do not recommend you try to tackle any of these products until you have become familiar with how our products work.

### EX-CommandStation Advanced Self Build (DIY)

![EX-CommandStation Logo](/_static/images/logos/product-logo-ex-commandstation-only-light.png){ .only-light width=400px }
![EX-CommandStation Logo](/_static/images/logos/product-logo-ex-commandstation-only-dark.png){ .only-dark width=400px }
![CS DIY Logo](/_static/images/logos/product-logo-ex-cs-diy-only-light.png){ .only-light width=400px }
![CS DIY Logo](/_static/images/logos/product-logo-ex-cs-diy-only-dark.png){ .only-dark width=400px }

A more complex DIY stack for EX-CommandStation using Espressif ESP32 or STMicroelectronics Nucleo microcontrollers. Some modifications may be required depending on the device chosen, and there are various nuances to be aware of when assembling and configuring these DIY options.

You will need to need to be careful when configuring and installing software on these devices also.

Refer to the [EX-CommandStation DIY Pages](/diy/1-diy.md) for information on what options are available and supported.

---

### EX-FastClock

![EX-FastClock Logo](/_static/images/logos/product-logo-ex-fastclock-only-light.png){ .only-light width=400px }
![EX-FastClock Logo](/_static/images/logos/product-logo-ex-fastclock-only-dark.png){ .only-dark width=400px }

An integrated fast clock for your layout.

While it's possible to get up and running with this fairly easily, there is still some software configuration and installation to be performed which makes this a little more complicated.

Refer to the [EX-FastClock documentation](/products/ex-fastclock/01-overview.md) for how to get up and running.

---

### EX-Turntable

![EX-Turntable Logo](/_static/images/logos/product-logo-ex-turntable-only-light.png){ .only-light width=400px }
![EX-Turntable Logo](/_static/images/logos/product-logo-ex-turntable-only-dark.png){ .only-dark width=400px }

An integrated turntable/traverser controller using a stepper motor.

The software and integration side of EX-Turntable is reasonably straight forward, however the mechanics of getting a turntable operational with a stepper motor and the required sensors to control the location of the turntable accurately is quite involved.

Refer to the [EX-Turntable documentation](/products/ex-turntable/ex-turntable.md) for what's required and how to get up and running.

---

### EX-DCCInspector

![EX-DCCInspector Logo](/_static/images/logos/product-logo-ex-dccinspector-only-light.png){ .only-light width=400px }
![EX-DCCInspector Logo](/_static/images/logos/product-logo-ex-dccinspector-only-dark.png){ .only-dark width=400px }

A diagnostic tool to inspect DCC packets.

This requires some assembly and soldering to get up and running, and you will need to understand various aspects of the DCC protocol to get the most out of it.

Refer to the [EX-DCCInspector documentation](https://dcc-ex.com/legacy-docs/ex-dccinspector/index.html#ex-dccinspector) for more information.

---

### EX-IOExpander

![EX-IOExpander Logo](/_static/images/logos/product-logo-ex-ioexpander-only-light.png){ .only-light width=400px }
![EX-IOExpander Logo](/_static/images/logos/product-logo-ex-ioexpander-only-dark.png){ .only-dark width=400px }

Driven by a shortage of I2C connected I/O expansion devices, EX-IOExpander allows you to use various Arduino devices to expand the I/O capabilities of your command station.

However, this does mean you will need to understand I2C connectivity and will likely need some more complex assembly and/or soldering to use this on your layout.

Refer to the [EX-IOExpander documentation](/products/ex-ioexpander/ex-ioexpander.md) for more information.
