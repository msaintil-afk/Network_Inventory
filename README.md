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


## Network Inventory API Documentation

## Device Locations

### GET /api/locations/
- Get all Device Locations

### POST /api/locations/
- Add Device Locations

### GET /api/locations/{location_id}/
- Get Device Location by ID

### DELETE /api/locations/{location_id}/
- Delete Device Location by ID

### PUT /api/locations/{location_id}/
- Update Device Location by ID

## Device Types

### GET /api/device-types/
- Get all Device Types

### POST /api/device-types/
- Add Device Type

### GET /api/device-types/{device-type_id}/
- Get Device Type by ID

### PUT /api/device-types/{device-type_id}/
- Update Device Type by ID

### DELETE /api/device-types/{device-type_id}/
- Delete Device Type by ID

## Device Vendors

### POST /api/vendors/
- Add Vendor

### GET /api/vendors/
- Get all Vendors

### GET /api/vendors/{vendor_id}/
- Get Vendor by ID

### PUT /api/vendors/{vendor_id}/
- Update Vendor by ID

### DELETE /api/vendors/{vendor_id}/
- Delete Vendor by ID

## Devices

### POST /api/devices/
- Add Device


### GET /api/devices/
- Get all Devices

### GET /api/devices/{device_id}/
- Get Device by ID

### PUT /api/devices/{device_id}/
- Update Device by ID

### DELETE /api/devices/{device_id}/
- Delete Device by ID

