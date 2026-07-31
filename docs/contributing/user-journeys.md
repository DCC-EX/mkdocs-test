# User Personas and Journeys - Front Page Tiles

Use these Mermaid diagrams to help ensure the various user types can navigate successfully from the front page to get to the information they require.

## New to DCC-EX

These users don't really know what **DCC-EX** is, but saw it at their club, on a YouTube channel, at a show, or someone told them they should check it out.

```mermaid
graph LR
    A([Home]) --> B[DCC-EX introduction];
    B --> C[General product overview];
    C --> D[How they can get them];
    D --> E{DiY or RtR};
    E --> |RTR| F[Purchasing info];
    F --> G([See 'Ready-to-Run EX-CSB1'])
    E --> |DiY| H[DIY info];
    H --> I([See 'DIY Building an EX-CS'])
```

## Ready-to-Run EX-CSB1

These users just purchased their brand new shiny **EX-CSB1** and want to get up and running with it ASAP. They need to know how to connect it safely to their layout, how to connect a throttle (eg. **EX-WebThrottle**, Engine Driver), and how to power it.

```mermaid
graph LR
    A([Home]) --> B[Get Started or Run trains?];
    B --> C[EX-CSB1 setup, or user manual];
    C --> D[Use - Run Trains];
    D --> E[What's next to expand?];
```

## DIY - Building an EX-CommandStation

These users are just want to build a DIY EX-CommandStation.

```mermaid
graph LR
    A([Home]) --> B[Self Build];
    B --> C[Choose Options];
    C --> D[Purchase Parts];
    D --> E[Build];
    E --> F([See 'Getting it running'])
```

## DIY - Getting it running

These users want to enhance their **EX-CommandStation** or have just put together their DIY EX-CommandStation and want to get it up and running. They need to know how to upload the software and connect a throttle (e.g. **EX-WebThrottle**, Engine Driver, etc.).

```mermaid
graph LR
    A([Home]) --> B[Install the software];
    B --> C[Test];
    C --> |Needs changes| B;
    C --> D[Use - Run Trains];
    C --> E[Use - DCC Accessories];
    E --> F[What's next to expand?];
    D --> F;
```

## DC Users

These users want to run their existing DC trains. They may have a large collection that is too expensive or difficult to convert.

They have followed the steps above but now need to understand how to use the DC TrackManager modes.

They also need to know how to connect it to the layout and connect throttles as well as how to power it, but they also need to understand about isolation between the track outputs and potentially PWM sync issues.

```mermaid
graph LR
    A([Home]) --> B[Understanding <br/>DC PWM];
    B --> C[Understanding TrackManager];
    C --> D{Temp. or<br/>semi-<br/>permanent}
    D --> |Temporary changes| E[GUI and/or <br/>commands];
    D --> |Semi-permanent| F[EXRAIL commands];
    F --> G([See 'Getting it running'])

```

## Existing Users - Adding a Roster

These users already have an **EX-CSB1** or DIY stack up and running and want to extend to adding a Roster.

```mermaid
graph LR
    A([Home]) --> B[Explain Rosters in EXRAIL];
    B --> C[Install the software];
    C --> D[Test];
    D --> |Needs changes| C;
    D --> E[Use - Run Trains];
```

## Existing Users - Adding Accessories

These users already have an **EX-CSB1** or DIY stack up and running and want to extend to using accessories including turnouts/points, signals, sensors, turntables, and so forth. They need to know how to physically connect them (I2C) and enable them in software (myAutomation.h). This will move them from Conductor into early Tinkerer territory for I2C in particular.

```mermaid
graph LR
    A([Home]) --> B[Adding Accessories];
    B --> C[Understanding <br/>EXRAIL objects];
    C --> D[Editing <br/>myAutomation.h]
    D --> E([See 'Getting it running'])
```

## Existing Users - Looking to Automate/Animate

These users already have an **EX-CSB1** or DIY stack up and running and may or may not have accessories as well. They want to understand how to automate and/or animate running trains and/or their layout in general. This may be as simple as a shuttle running back and forth between two stations, or a complex display running trains, controlling various layout aspects (eg. lighting, cross gates), and automating shunting or routes across different tracks. This will definitely be out of Conductor territory but is all about **EXRAIL**, although guidance on what hardware is required to achieve these will be required.

```mermaid
graph LR
    A([Home]) --> B[EXRAIL introduction];
    B --> C[Accessory options];
    B --> D[EXRAIL cookbook];
    B --> E[EXRAIL reference];
    C --> F[Editing <br/>myAutomation.h]
    F --> G([See 'Getting it running'])
    D --> F;
    E --> F;
```

## Large Club Layout

These users are aware of **DCC-EX** and know enough to be able to start implementing it on a large club layout. They want to know about wiring, boosters, power districts, multiple wired and wireless throttles, and connecting accessories.

```mermaid
graph LR
    A([Home]) --> B[Large layout page];
    B --> C[Sample use cases?];
    B --> D[Accessories?];
    B --> E[EXRAIL animation<br/>/automation?];
    C --> F[Editing <br/>myAutomation.h]
    F --> G([See 'Getting it running'])
    D --> F;
    E --> F;
```

## Downloader

These users already know enough and just want a quick way to get the latest version of software.

```mermaid
graph LR
    A([Home]) --> B[Download page];
```
