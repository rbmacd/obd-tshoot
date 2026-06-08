import obd

connection = obd.OBD("/dev/ttyUSB0")

# Active DTCs
dtcs = connection.query(obd.commands.GET_DTC)
print("Active DTCs:", dtcs.value)

# Pending DTCs (detected but not yet triggering CEL)
pending = connection.query(obd.commands.GET_CURRENT_DTC)
print("Pending DTCs:", pending.value)

# Freeze frame snapshot at time of fault
freeze_frame = {
    "engine_load":      connection.query(obd.commands.DTC_ENGINE_LOAD).value,
    "coolant_temp":     connection.query(obd.commands.DTC_COOLANT_TEMP).value,
    "short_fuel_trim":  connection.query(obd.commands.DTC_SHORT_FUEL_TRIM_1).value,
    "long_fuel_trim":   connection.query(obd.commands.DTC_LONG_FUEL_TRIM_1).value,
    "rpm":              connection.query(obd.commands.DTC_RPM).value,
}
print("Freeze frame:", freeze_frame)
