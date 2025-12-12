# I2C – An Introduction

## What is I2C?

If you want the nitty gritty of what I2C is, you can refer to the [Wikipedia article](https://en.wikipedia.org/wiki/I%C2%B2C), which covers more detail than we will here.

To keep it simple and in the context of DCC-EX, I2C is a bus that allows multiple accessories or peripherals to be connected to your Command Station, utilising two signal lines/connections and a common ground connection. While power can be provided by your Command Station, it is recommended to have your accessories powered separately.

Each I2C device must have a unique address in order to be detected and configured by the software.

You will typically see these addresses in hexadecimal format, for example ``0x40``.

## How does it help?

Model trains come alive when we add points (turnouts), signals, sensors, lights, sounds and more. DCC-EX comes ready-equipped with the capability to add many such devices. In the hands of users experienced in electronics, DCC-EX can support hundreds of such devices using a connection system called I2C “I Squared C” which is built-into your Command Station. While I2C is very powerful, it is not a consumer plug and play set up. If you have not used it before and are not experienced in electronics, you will need to teach yourself some new skills – which can be fun and which also creates its own challenges.

To help Conductors to get up the learning curve, we have 3 proven and essential building blocks that will get you there as smoothly as possible. We ask new users to closely follow all 3 of these, as otherwise our volunteer support teams get overwhelmed with support requests as the success of the DCC-EX venture grows.

The 3 I2C building blocks we very strongly request Conductors build for themselves are:

- Firstly, we have developed a set of tightly-specified components and configurations that we know work well in practice. Yes, you can often find cheaper individual components but these are a false economy as they are often poorly manufactured, meaning they may not work at all, causing frustration and a non-functioning model train layout. Please use these configurations initially, so that you can get used to the I2C system before becoming more adventurous.

- Secondly, there are new skills to learn and new terms to become familiar with if you are to be able to understand why your own set up is or is not working. You will hear terms like pullup resistors, logic voltage level, clock and data lines bandied about. Some of these you’ll need to understand well, others can wait. Self-education on I2C therefore is vital for Conductors to enjoy your deployment of I2C from the very beginning. We have curated a number of videos and guides that we know to be helpful. There is even a foundation set that we strongly urge new users to watch, so that you understand the basics of I2C.

- Third, even when using a configuration that is known to work, you will be using a number of cables to connect items and it is very common to have problems caused by inadvertently swapping cables, or simply poor connections, which can cause things not to work, or worse, be damaged. The use of a multimeter to confirm correct set up and to troubleshoot any issues arising is mission critical. Yes, we are strong on this point because it is such a vital tool for you to enjoy this aspect of your hobby and for our support teams to guide you through any problems you may encounter.

Using these 3 proven building blocks together, you will likely have a successful installation. If you choose to ignore these, you will probably find a multitude of unexpected and unknown issues and join the ranks of users that can’t get their accessories to work and don’t understand why.
