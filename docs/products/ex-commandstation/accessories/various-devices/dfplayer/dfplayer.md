# DFPlayer Sound player

The DFPlayer device van be used to play pre-recorded sounds from an onboard SD-card.

## Suggested uses

An example of a layout line side sound scenario of what can be achieved with two or more DFPlayers:

1. Background ambiance sound of a grand central station (repeat sound file on one DFPLayer)
2. Conductor shouts: “All aboard”
3. The Solari departure/arrival board comes to live (random play)
4. A station announcement, synchronized with a train arrival (triggered via an input sensor)
5. Station announcements (random play)
6. Car horns outside station (random play)
7. Someone shouting: “Taxi” (random play)
8. Only limited by your imagination

## Hardware connection

Because the DFPlayer is a Serial device, this can be inconvenient for command stations with limited serial pins available (eg CSB-1) so dcc-ex provides an additional HAL driver to access the device over I2C with a suitable UART breakout board.

Please see the relevant connection details:

- [DFPlayer Serial connection](./serial-dfplayer.md)
- [DFPlayer I2C connection](./i2c-dfplayer.md)

## Audio file storage and naming convention

The DFPlayer read audio files from a microSD flash card. If audio files are copied in the root directory, then the order of the copying determine which audio file will be the 1st.  So when a command is sent to the DFPlayer to play track 1, it will play the 1st audio file that was copied on the microSD card.

To control consistently which audio file is to be played, the DFPlayer needs a folder structure. Folders need to be named 01, 02, 03 . . . . 99, and the audio files in each folder need to be named 001.mp2, 002.mp3 up to 255.mp3. Audio files in MP3 format are preferred, but WAV format is also supported, but take up more space.

Audio files may be renamed from ‘my favourite song.mp3’ to ‘001My favourite song.mp3’ as per DFPlayer manual.

The (current) exception is an audio file that is to be played continuously with the DF_REPEATPLAY command, as there is no DFPlayer REPEAT command to play a specific audio file in a specific folder. Therefor it is recommended to store the audio file that needs to be played continuously in the root folder and name it ‘001.mp3’.


## Providing sound files

the DFPlayer has a strange behaviour when the audio files are stored in the root directory. It does not look at the file name for example 001.mp3 to play file 001.mp3, but will play the 1st file that has been copied on the microSD card when it receives the command to play file 1. To solve this issue, a directory structure must be in place.

The DFLayer implementation require a directory named 01 to 99, and should contain all the audio files named 001.mp3 to 255.mp3. The format `001<sound title>.mp3` is also supported.

Best practice is to compile an audio catalogue and store files in different folders, for example each folder is for a different category. It makes it easy to write EXRAIL scripts to control sound when each DFPLayer has the same sound catalogue on its microSD card. We have created an example sound catalogue, royalty free, full attribution document and open source to get you started.

Files in WAV format are also supported, but take up more space, audio files in MP3 format are recommended.

The EXRAIL cookbooks provide several worked example sound scenarios.

## Testing DFPlayer

There is a <y> command that is specifically designed for easy testing and control from the serial monitor. Every command is directed towards the previously defined vpin.

- `<y vpin PLAY track [volume]>` Plays given track number and specified (or default) volume
- `<y vpin REPEAT track [volume]>` Plays track repeatedly
- `<y vpin FOLDER folder>` Switches future play commands to a different folder
- `<y vpin STOP>` Stops playing
- `<y vpin VOL volume>` Changes default play volume (Does not affect currently playing track)
- `<y vpin EQ eq>` Changes sound equalisation
- `<y vpin RESET>` Resets the DFPlayer
