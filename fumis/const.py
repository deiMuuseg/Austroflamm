"""Models for the Fumis WiRCU API."""


STATUS_OFF = "off"
STATUS_PRE_HEATING = "pre_heating"
STATUS_IGNITION = "ignition"
STATUS_COMBUSTION = "combustion"
STATUS_ECO = "eco"
STATUS_COOLING = "cooling"
STATUS_UNKNOWN = "unknown"

STATUS_MAPPING = {
    0: STATUS_OFF,
    10: STATUS_PRE_HEATING,
    20: STATUS_IGNITION,
    30: STATUS_COMBUSTION,
    40: STATUS_ECO,
    50: STATUS_COOLING,
}

STATE_OFF = "off"
STATE_ON = "on"
STATE_UNKNOWN = "unknown"

STATE_MAPPING = {
    1: STATE_OFF,
    2: STATE_ON,
}
