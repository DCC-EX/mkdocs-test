# DC Mode - PWM Frequency

The default PWM frequency is 131Hz.  Functions F29-F30-F31 are defined to enable other frequencies.

The functions will toggle the bits ON/OFF as shown in the table.

<!-- &nbsp; &nbsp; &nbsp; &nbsp; ![PWM Frequency](/_static/images/trackmanager/dc-pwm-frequency.png){: style="width: 50%"} -->

<style>
/* Target the table inside the main content area */
/* 1. Force the table container and table wrapper to allow shrinking */
.md-typeset table:not([class]),
.md-typeset .md-content__inner table {
    table-layout: fixed !important;
    width: auto !important; /* Forces the table to shrink wrap to cell widths instead of stretching to 100% */
    display: table !important;
}

/* 2. Target the first 4 narrow columns (F31, F30, F29, and index) */
.md-typeset table:not([class]) th:nth-child(-n+4),
.md-typeset table:not([class]) td:nth-child(-n+4) {
    width: 45px !important;
    max-width: 45px !important;
    min-width: 45px !important;
    padding: 4px !important;
    text-align: center !important;
}

/* 3. Target the microcontroller columns (Nucleo, ESP32, Mega) */
.md-typeset table:not([class]) th:nth-child(n+5),
.md-typeset table:not([class]) td:nth-child(n+5) {
    width: 90px !important;
    max-width: 90px !important;
    min-width: 90px !important;
    padding: 4px 8px !important;
}

.md-content th,
.md-content td {
    width: 12%; /* Adjust this percentage or use pixels (e.g., 60px) to make them tighter */
    padding: 4px 8px; /* Optional: reduce padding to squeeze text closer together */
}

.md-typeset__scrollwrap table {
    display: table !important;
    width: 100% !important;
    border-collapse: separate !important;
    border-spacing: 0 !important;
}

.md-typeset table td,  
.md-typeset table th {
    font-size: smaller !important;
    padding-top: 2px !important;
    padding-bottom: 2px !important;
    padding-left: 0px !important;
    padding-right: 0px !important;
    line-height: 110% !important;
    font-family: 'Roboto Condensed', sans-serif !important;
 }
</style>

| F31 | F30 | F29 |      | Nucleo-F4 | ESP32 | Mega |
| --: | --: | --: | ---: | --------: | ----: | ---: |
| 0 | 0 | 0 | 0 | 131 | 131 | 131 |
| 0 | 0 | 1 | 1 | 480 | 480 | 490 |
| 0 | 1 | 0 | 2 | 3600 | 3400 | 3400 |
| 0 | 1 | 1 | 3 | 16000 | 16000 | 3400 |
| 1 | 0 | 0 | 4 | 32000 | 32000 | 62500 |
| 1 | 0 | 1 | 5 | 32000 | 32000 | 62500 |
| 1 | 1 | 0 | 6 | 32000 | 32000 | 62500 |
| 1 | 1 | 1 | 7 | 62500 | 32000 | 62500 |

**NOTE:**

- The frequency does not change until a powerON command is sent.

- Tracks are assigned to timers.  Throttles are assigned to tracks.  
  Changing the frequency for one throttle will impact all tracks assigned to the same timer.  
  [more information](dc-track-sync.md/#timers-brake-pins)

- ==TODO==  How to effectively use DC mode when using multiple frequencies.  

--8<-- "snippets/abbr.md"
