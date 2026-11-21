class WiFiConnectableMixin:
    """Provee conectivudad a Internet."""
    def connect_to_wifi(self, network_name):
        print(f"[WiFi] Conectado exitosamente a la red: '{network_name}'")


class LoggerMixin:
    """Provee resgistro de eventos / auditoria."""
    def log_event(self, event_message):
        print(f"[LOG]: {event_message}")


class Appliance:
    def __init__(self, brand):
        self.brand = brand


class SmartRefigerator(Appliance, WiFiConnectableMixin, LoggerMixin):
    """
    Hereda de 3 clases a la vez:
    1. Appliance (es un electrodomestico)
    2. WiFiConnectableMixin (puede conectarse a WiFi)
    3. Loggermixn (puede registrar eventos)
    """
    def __init__(self, brand, temperature=4):
        super().__init__(brand)
        self.temperature = temperature
    
    def change_temperature(self, new_temp):
        self.temperature = new_temp
        self.log_event(f"Temperatura ajustada a {self.temperature}°C")



print("\n=== Prueba Ejercicio 3 (Herencia Múltiple) ===")
fridge = SmartRefigerator(brand="Samsung")
fridge.change_temperature(2)
fridge.connect_to_wifi("Casa_5G")
