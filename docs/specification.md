# Event Agency Management App – Specification

## Purpose

This app is for the team at an event agency who organise events for business clients. It keeps every event in one place so the team can see at a glance which events are being planned, confirmed, completed or cancelled.

## Entities

### Event

- id (integer, primary key)
- name (text, required, max 200)
- client\_name (text, required, max 200)
- event\_type (text, optional; one of: conference, product\_launch, corporate\_dinner, gala\_dinner, team\_building, workshop\_training, networking\_event, exhibition, trade\_show, corporate\_retreat, award\_ceremony, other)
- description (text, optional)
- start\_date (date, required)
- end\_date (date, required, not earlier than start\_date; same as start\_date for a one-day event)
- venue (text, optional; venue name and location)
- guest\_count (integer, optional, 0 or more)
- status (one of: planning, confirmed, completed, cancelled — default planning)
- notes (text, optional)
- created\_at (timestamp)

## Routes

| Method | Path | Does |
| --- | --- | --- |
| GET | / | List all events, soonest start\_date first, with a count per status; `?status=` shows only that status; each status has its own colour |
| GET | /event/new | Form to create an event |
| POST | /event | Create an event, redirect to / |
| GET | /event/\<id> | Show one event |
| POST | /event/\<id>/status | Change status, redirect back |

## Technical constraints

- Python 3.11+, Flask 3.x
- SQLite via the standard library `sqlite3` (no ORM this week)
- Jinja2 templates in `templates/`, one base template
- No authentication this week
- No JavaScript framework
- Plain CSS; the layout works on desktop and phone screens

## Out of scope

- Separate client records (the client is a text field on the event)
- Editing event details and deleting events (cancelled events stay with status cancelled)
- Search and column sorting
- Budgets, staff assignments, start and end times
- User accounts, notifications and reminders, import and export, activity history, an API
