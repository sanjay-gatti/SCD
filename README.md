SCD (Slowly Changing Dimension)?

A Slowly Changing Dimension handles how dimension data changes over time in a data warehouse. It will also store the historic data wrt those chnages.

1. SCD Type 1 — Overwrite (No History)

  * Old value is replaced with new value.
  * No tracking of past changes.

2. SCD Type 2 — Full History

  * Keeps all historical versions.
  * Inserts a new row for every change.
  * Uses start/end dates and/or current flag.

3. SCD Type 3 — Limited History

  * Stores current + one previous value.
  * Adds extra columns like previous_department.
