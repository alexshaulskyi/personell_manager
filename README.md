# Personnel manager

A service which will allow to manage hotel maids and technicians.

## Disclaimer

This project is at very early stage of development. Main purpose of it is to learn to new features, especially in frontend.
So far, thanks to it I understood how AJAX works and basics of JQuery and in-place edit.
However, I will try to constantly update it. All of the released updates can be seen in an appropriate section.

## Description

Anyone can register a user and then create a property. By default user will be granted by 'Manager' title, which will allow
to have full control over property. After creating a property manager will be able to add rooms, cleaning types and employees.
Manager can assign roles to created user profiles. Depending on them, employees will be able to see and modify only specific information.
For example, staff member (maid) will only be able to see the room they are responsible for and modify only room status field, while administrators can see all rooms.
Depending on selected checkin date and frequency of created cleanings you can automatically assign cleaning to every occupied room.

## Released updates

**25.06.2020** Depending on job title, users can only see and modify specific information.
<br>
**28.06.2020** Fixed datepicker. Improved it's behavior. It is possible now to automatically set cleaning types to every room.
<br>
**14.07.2020** Improved protection from unauthorized access.

## Planned updates

* Improve protection from unauthorized access.
* Improve quality of automatical cleaning type distribution. (Proper cleaning type selection if multiple cleanings have same frequency)
* Monthly schedule for maids. Automaticall distribution of responsible maids depending on working schedule.
* Messenger notification upon room status change and change in working schedule.
* Style update.
* Adding functionality to manage technicians.

## Installation

Simply install requirements via pip:

```pip install -r requirements.txt```

and you will be able to run project locally.