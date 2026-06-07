``<l «loco» «reg» «speedByte» «functMap»>``

* **loco** = DCC Address of the decoder/loco. The short (1-127) or long (128-10293) address of the engine decoder (this has to be already programmed in the decoder)
* **reg** not used. We no longer use this but need something here for compatibility with legacy systems. Enter any single digit. > * **speedbyte**:** Speed in DCC speedstep format
    * reverse - ``2``-``127`` = speed ``1``-``126``, ``0`` = stop, ``1`` = Emergency Stop
    * forward - ``130``-``255`` = speed ``1``-``126``, ``128`` = stop, ``129`` = Emergency Stop
* **FunctMap** individual function states represented by the bits in a byte
