# General EXRAIL Tips

Below are some tips and techniques you can implement to get the most out of **EXRAIL**.

!!! warning "AI does not understand EXRAIL"

    Do not waste your time asking ChatGPT, Copilot or Gemini to create EXRAIL scripts.   They do not understand EXRAIL and will get it wrong 100% of the time.

## Numbers and Leading Zeros

**Do not use leading zeros for any numbers!**
  
Any number with a leading zero will be treated as an octal number, so for example ``ALIAS(MY_ALIAS, 010)`` will assign the value of ``8`` to MY_ALIAS, not ``10``. This is a common mistake that can lead to very confusing behaviour if you don't know about it. Always use numbers without leading zeros, for example ``ALIAS(MY_ALIAS, 10)`` to assign the value of 10 to MY_ALIAS.

## Comments

Comments can be very helpful if you need to go back at a later time to make changes to your sequences, to help you remember what you did or why you did it.

You can add comments to myAutomation.h in two ways:

* If ``//`` occurs in the line, everything after that (including the slashes) is ignored.  i.e. a 'Comment'
* If a line starts with ``/*`` then everything, including all subsequent lines an including the '/*' is ignored until a ``*/`` is found.  i.e. a 'Comment'

## Aliases - User Friendly Names for any Ids

Use the ``ALIAS()`` command in your script to make IDs a bit more human friendly, and easier to refer to later. 

``ALIAS( name[, value] )`` Aliases assigns names to values. They can go anywhere in the script. If a value is not assigned, a unique ID will be assigned based on the alias "name" text.

This is a simple substitution that lets you have readable names for things in your script. For example, instead of having to remember the VPin a turnout/point is connected to, give the pin number an alias and refer to it by that name. You can use this to name routes, values, pin numbers, or anything you need.

```cpp
   //example
   ALIAS(COAL_YARD_TURNOUT,19)
   ALIAS(COAL_YARD_SIGNAL_3,27)

   ROUTE(1,"Coal yard exit")
      THROW(COAL_YARD_TURNOUT)
      GREEN(COAL_YARD_SIGNAL_3)
   
   // As above with auto generated IDs
   ALIAS(COAL_YARD_TURNOUT)
   ALIAS(COAL_YARD_SIGNAL_3)

   ROUTE(1,"Coal yard exit")
      THROW(COAL_YARD_TURNOUT)
      GREEN(COAL_YARD_SIGNAL_3)
```

Alias names:

* **Must not** be an existing EXRAIL command name or other reserved word.
* **Should be** reasonably short but descriptive.
* **Must start** with letters A-Z/a-z, 0-9 or underscore _ .
* **May then** also contain numbers.
* **Must not** contain spaces or special characters.
* **May** end with ``+`` or  ``-``. When used the alias must be followed by a number.

## Parameters with Arithmetic

Any parameter for an |EX-R| command that takes numbers can be replaced with an c++ arithmetic calculation, as long as that calculation can be resolved at compile/load time.  (e.g.  + - * /  >> << &  | ! ~ and even ?: )

This can be useful if you have a block of related IDs or VPINs and you don't wish to give each an ALIAS.

```cpp
   ALIAS(Platform, 600)
   ...
   IF(Platform)
   IF(Platform + 1)     // equivalent to IF(601)
   IF(Platform + 2)     // equivalent to IF(602)
```
