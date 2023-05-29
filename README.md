# Network Inventory Project

The Network Inventory Project is a Dockerized Django-based web application that allows you to manage a network device inventory. It provides CRUD operations (Create, Read, Update, Delete) to interact with the inventory.

## Features

- Add new network devices to the inventory.
- View a list of all network devices in the inventory.
- Update information for existing network devices.
- Delete network devices from the inventory.

## Requirements

- Python 3.9 or higher
- Django 4.2.1
- PostgreSQL
- psycopg2
- gunicorn 20.1.0
- Docker
- DjangoRestFramework 3.14.0


## ERD Diagram

                                      +---------+           +--------------+
                                      | Location|           | Device_Type  |
                                      +---------+           +--------------+
                                      | location_id |<>---->| type_id      |
                                      | name      |           | name        |
                                      | address   |           +--------------+
                                      +----------+

                                            |
                                            |
                             +--------------+--------------+
                             |                             |
                             v                             v
                        +-------+                    +--------+
                        | Device|                    |  Vendor|
                        +-------+                    +--------+
                        | device_id |<-------------->| vendor_id|
                        | name     |                    | name   |
                        | model    |                    +--------+
                        | serial_no|
                        | location_id|
                        | type_id |
                        | software_version|
                        +---------+


Reference Network Inventory API documentation for API examples