## DCC-EX Serial Command List

THIS IS A PLACEHOLDER FILE THAT WILL BE BUILT AT GITHUB DEPLOY TIME

It will look a bit like this:

### [`<#>`](?_8hash8)

Request number of simultaneously supported locos
Socket connected apps use this as a heartbeat.

UDP connected apps send this if they are unable to listen for multicast updates, the CS will send unicasts.

### [`<F «loco» DCCFREQ «freqValue»>`](?_▪F▪_▫loco▫_▪DCCFREQ▪_▫freqValue▫)

Set DC frequency for loco
