# Setup

Per default, SQLite has WAL (Write-Ahead Logging) mode disabled.
This is to preserve backwords compatibility but means that the database can handle a lot less concurrent database operations.

Simon Willison has written great tutorial on how to setup SQLite with WAL mode enabled:

<https://til.simonwillison.net/sqlite/enabling-wal-mode>
