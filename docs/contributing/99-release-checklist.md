# Release Checklist

Everything on this page supports the team being able to determine when these docs can be released.

This is a list of to do items that will allow us to release this new documentation, and move the existing to a separate "legacy-docs" URL for reference only.

## Content

- [ ] Conductor friendly getting started with RTR and officially supported Mega DIY stack only

    - [ ] General getting started page
    - [ ] General EX-CommandStation page
    - [ ] Clarity on what you need including **good and recommended** power supplies
    - [x] EXRAIL under EX-CS
    - [x] TrackManager under EX-CS - no waveform/DC PWM details, they can be a reference later, just focus on config and use
    - [ ] EX-CSB1 RTR information - must be complete
    - [ ] Mega DIY stack page - Mega + EX8874/Arduino R3 + WiFiShield8266 only (no hardware mods, plug n play only)

- [ ] ESP32 and Nucleo DIY to refer to legacy docs to start

- [ ] Product pages for EX-Installer, EX-CommandStation (includes EXRAIL and TrackManager), EX-CSB1, EX-Motorshield8874, and EX-WiFiShield8266
- [ ] Better how to get help and support info

    - [ ] How to use Discord, code snippets, upload files, raise a ticket
    - [ ] What are the logs/file required, how to get them

- [ ] EX-CommandStation troubleshooting steps

    - [ ] USB issues - drivers, cables, ports, permissions, other programs open
    - [ ] WiFi/serial interfering
    - [ ] WiFi issues
    - [ ] EX-Installer common issues
    - [ ] Not seeing roster/routes/turnouts in throttles/JMRI

- [ ] I2C more accessible information

    - [ ] Wiring/pullups/distance in layman's terms
    - [ ] Default device addresses and how to disable
    - [ ] Troubleshooting steps

- [ ] Purchasing information for hardware
- [ ] EXRAIL command reference from doxyGen
- [ ] User journeys to guide users through the site

    - [ ] Brand new users no knowledge
    - [ ] Running trains?
    - [ ] Accessories?
    - [ ] Animation/automation?

## Release QA Items

- [ ] Proof-reading all pages but not by original author
- [ ] Address all TODO markers

## Menu and Page Structure

- [ ] All hardware pages should "next" onto the EX-Installer EX-CommandStation configuration instructions, maybe nav plugin extension, maybe JS
- [ ] Relocate Self Build from a top level nav bar item

## Styling

- [ ] Revisit navigation menu bar colouring
- [ ] Table separator colours are almost invisible

## Team Info

- [x] Ensure MkDocs contributor guide covers all customisations

    - [x] How to use our logos
    - [x] Grid cards
    - [x] CSS/JS customisations
    - [x] Custom plugins
    - [x] Custom footer
    - [x] How we use Material extensions
    - [x] Icons/emojis
    - [x] Snippets

- [ ] About Us page - combine with contributing or separate?
