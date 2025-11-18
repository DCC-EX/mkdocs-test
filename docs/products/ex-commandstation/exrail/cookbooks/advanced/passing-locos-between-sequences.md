# Passing locos between sequences

Each of the methods below involves creating a new Exrail task that will run in parallel with the current task. The difference is in how the locoid information is passed to the new sequence.

## START(sequence_id)

Start a new task with no loco attached.

## SENDLOCO(loco_id,sequence_id)

Start a new task with the given loco id

## START_SEND(sequence_id)

Hands over the current loco to the new task. The current task is no longer connected to this loco.

## START_SHARED(sequence_id)

Shares the loco with the new task. For example the new task may flash the loco lights to a disco beat while the original task continues to drive the loco.
