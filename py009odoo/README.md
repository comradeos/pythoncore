# Simple Device Logger (Odoo Community)

Minimal Odoo Community project that loads device telemetry from an external API, stores it in Odoo, shows it in the UI, and exposes a JSON endpoint with saved logs.

## What is included

- Docker environment with Odoo 17, PostgreSQL 15, and a mock external API
- Odoo addon `simple_device`
- Model `device.log`
- UI with list and form views
- Button `Load from API`
- Public endpoint `GET /api/device_logs`
- `Makefile` for common Docker tasks

## Project structure

```text
.
├── addons/
│   └── simple_device/
├── mock_api/
├── docker-compose.yml
├── Makefile
└── README.md
```

## Quick start

### 1. Build containers

```bash
make build
```

### 2. Start services

```bash
make up
```

The first start automatically initializes the base Odoo database, so it can take a little longer than the next runs.

Services:

- Odoo: [http://localhost:8069](http://localhost:8069)
- Mock Device API: [http://localhost:8080/device/demo-1](http://localhost:8080/device/demo-1)

### 3. Sign in to Odoo

Open [http://localhost:8069](http://localhost:8069) and sign in with:

- Login: `admin`
- Password: `admin`

### 4. Install the addon

In Odoo:

1. Open `Apps`.
2. Remove the default `Apps` filter if needed.
3. Search for `Simple Device Logger`.
4. Click `Install`.

## Manual test plan

### Step 1. Verify the mock API

Open:

- [http://localhost:8080/device/demo-1](http://localhost:8080/device/demo-1)
- [http://localhost:8080/device/demo-2](http://localhost:8080/device/demo-2)

You should see JSON with `voltage` and `current`.

### Step 2. Create a device log in Odoo

In Odoo:

1. Open `Device Logger` -> `Device Logs`.
2. Create a new record.
3. Fill:
   - `Name`: `Test Device`
   - `Device ID`: `demo-1`
4. Save the record.

### Step 3. Load data from API

1. Open the created record.
2. Click `Load from API`.
3. Confirm that `Voltage` and `Current` are filled in.
4. Confirm that `State` becomes `Loaded`.

### Step 4. Verify the REST endpoint

Open:

- [http://localhost:8069/api/device_logs](http://localhost:8069/api/device_logs)

You should receive a JSON array with stored logs.

### Step 5. Negative check

1. Create a second record with `Device ID`: `fail-demo`.
2. Click `Load from API`.
3. Confirm that Odoo shows an error and the record state changes to `Error`.

## Make commands

```bash
make build
make up
make down
make clean
make logs
```

## Notes

- The addon is mounted from `./addons` into Odoo as an extra addons path.
- The Odoo container reaches the mock API at `http://device-api:8080`.
- The `odoo-init` service prepares the base database on the first startup so Odoo opens without the database manager flow.
- `make clean` removes containers, networks, and named volumes.
