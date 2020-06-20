# Personnel manager.

Allows chief maid or front desk administrators to effectively manage maids.

Main purpose of this project is to improve my Django and JavaScript skills. It is my main project for the moment and I am trying to learn and release as many new features as possible.

## Description.

Service allows to register property and add rooms, employees and cleanings. Each room beside basic info like room number or category has it's status, responsible maid and checkin - checkout dates.

## Goals achieved:

* CRUD operations related to employees, rooms and cleanings are performed via AJAX calls.
* Employees, rooms and cleanings data modifications are IN-PLACE edit based.

## Updates released:

Are being added upon release so my progress can be easily tracked.

## Planned updates:

* Depending on user role allow modification of only specific fields. (i.e. maid can only modify room status)
* Display specific rooms depending on user role (i.e. administrator can see all rooms, but maids can only see rooms which they have to clean)
* Assign cleanings automatically depending on checkin and checkout dates.
* Improve registration process in order to eliminate redundant actions.
* Automate assigning responsible maids depending on working calendar and cleaning difficulty.
* Messenger notifications to maid if cleaning schedule was changed.
* Messenger notifications to front-desk administrators if room status was changed (i.e dirty -> clean)
* Minor style updates.
