# Personnel manager

Service which will allow chief maid, technician officer or shift manager to effectively manage maids and technicians.

## Purpose

Improve my Django skills. Improve understanding of Front-end in general and JavaScript, JQuery in particular. Secondary, offer small hotels on a budget, product which will help them in eliminating daily routine tasks.

## Description

Anyone can register and then create a property. Users can only access and see their own property. After registration it is possible to add rooms, cleaning types and create employees accounts, which they will use to log in.

## Achieved goals

* CRUD operations related to rooms, employees and cleanings are performed via AJAX calls.
* Modification of rooms, employees and cleanings data is IN-PLACE edit based.

## Released updates:

**25.06.2020** Allowed modification of specific fields depending on user role (maids can only change room status, administrators can change status and checkin/checkout date)
**25.06.2020** Depending on user role only specific rooms are displayed (i.e. maid can only see rooms which she is responsible for)

## Planned updates:

Listed in descending priority order.

* ~~Allow modification of specific fields depending on user role (i.e. maid can only modify room status)~~ (released)
* ~~Display specific rooms depending on user role (i.e. maids only see rooms which they need to clean)~~ (released)
* Automate assigning cleaning to room depending on checkin and checkout date.
* Improve registration in order to eliminate redundant actions.
* Add working schedule.
* Automate assigning responsible maid to room depending on working schedule and difficulty of cleaning.
* Messenger notifications to maids if cleaning schedule was changed.
* Messenger notifications to administrators if rooms status was changed.
* Style improvement.
